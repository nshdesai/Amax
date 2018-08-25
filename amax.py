from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        subm = request.values.get('demo-message')
        return render_template('create.html', sub=subm)
    else:
        return render_template('create.html', sub=False)

@app.route('/results')
def results():
	return render_template('results.html')

if __name__ == "__main__":
    app.run(port=80)

