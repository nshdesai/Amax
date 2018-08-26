#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:

Author: ndesai
"""


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
        colour = '#{:02d}{:02d}{:02d}'.format(0, int(255 * keywords[word]), 0)
        body = body.replace(word, "<span style = \"background-color:" + colour + "\">" + word + "</span>")
    return body


def main():
    return 0


if __name__ == '__main__':
    main()
