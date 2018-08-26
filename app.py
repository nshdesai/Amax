from flask import Flask, render_template, request
from questgen import keywords

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        inpt = request.values.get('demo-message')
        subm = keywords.get_keywords(inpt)
        return render_template('create.html', sub=subm)
    else:
        return render_template('create.html', sub=False)

@app.route('/results')
def results():
	return render_template('results.html')

if __name__ == "__main__":
    app.run(ssl_context='adhoc')

