#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:

Author: ndesai
"""

import os

import indicoio


def get_keywords(data):
    """Returns all keywords in an article along with a confidence score """
    set_api_key('api_key.txt')
    if data:
        return indicoio.keywords(data)


def set_api_key(api_file):
    api_key = os.environ["INDICO_API_KEY"]
    indicoio.config.api_key = api_key
