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
    for word in keywords:
        body = body.replace(word, "<span style = \"color:green\">" + word + "<\\span>")

    return body

@app.route('/results')
def results():
	return render_template('results.html')

if __name__ == "__main__":
    app.run(ssl_context='adhoc')

