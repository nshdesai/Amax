from flask import Flask, render_template, request
from questgen import keywords

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        user_input = request.values.get('demo-message')
        keywords_dict = keywords.get_keywords(user_input)
        formatted_paragraph = highlight_paragraph(user_input, keywords_dict)
        return render_template('create.html', sub=formatted_paragraph)
    else:
        return render_template('create.html', sub=False)

def highlight_paragraph(body, keywords):
    # eliminate subsets first
    keywords_keys = list(keywords.keys())
    keys_to_remove = []
    num_keys = len(keywords_keys)

    for i in range(num_keys):
        for j in range(i+1, num_keys):
            if keywords_keys[i] in keywords_keys[j]:
                keys_to_remove += keywords_keys[i]
                break

    for k in keywords_keys:
        if k in keys_to_remove:
            del keywords[k]

    for word in keywords:
        body = body.replace(word, "<span style = \"background-color:green\">" + word + "</span>")

    return body

@app.route('/results')
def results():
	return render_template('results.html')

if __name__ == "__main__":
    app.run(ssl_context='adhoc')

