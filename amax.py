from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/create')
def create():
	return render_template('create.html')

@app.route('/results')
def results():
	return render_template('results.html')

if __name__ == "__main__":
    app.run()

