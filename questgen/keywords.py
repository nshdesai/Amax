#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:

Author: ndesai
"""

import indicoio


def get_keywords(data):
    """Returns all keywords in an article along with a confidence score """
    set_api_key('api_key.txt')
    return indicoio.keywords(data)


def set_api_key(api_file):
    api_file = open(api_file, 'r')
    api_key = api_file.read().strip()
    indicoio.config.api_key = api_key
