from questgen.article import Article

import json


def generate_trivia(text):
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
    return json.dumps(questions, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    generate_trivia()
