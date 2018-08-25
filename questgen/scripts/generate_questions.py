from questgen.article import Article

import json


def generate_trivia(text, output="output/sample_out.json"):
    """Generates trivia questions from wikipedia articles. If no
    titles are supplied, pulls from these sample articles:
    """
    if len(text) == 0:
        raise Exception('No text was provided')

    # Retrieve the trivia sentences
    questions = []
    article = Article(text)
    questions += article.generate_trivia_sentences()

    # Output to JSON
    output_file = output.open()
    json.dump(questions, output_file, sort_keys=True, indent=4)


if __name__ == '__main__':
    generate_trivia()
