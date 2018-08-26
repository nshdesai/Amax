#! usr/bib/env python
# -*- coding utf-8 -*-

from highlight import highlight_paragraph
from questgen import keywords
from questgen.scripts import generate_questions

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        user_input = request.values.get('demo-message')
        keywords_dict = keywords.get_keywords(user_input)

        if keywords_dict is None:
            return render_template('create.html', sub=False)

        formatted_paragraph = highlight_paragraph(user_input, keywords_dict)
        questions = generate_questions(user_input)

        return render_template('create.html', sub=formatted_paragraph,
                               questions=questions)
    else:
        return render_template('create.html', sub=False)


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
