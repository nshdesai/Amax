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
    set_api_key()
    if data:
        return indicoio.keywords(data, threshold=0.15)


def get_summary(data):
    set_api_key()
    if data:
        return indicoio.summarization(data)


def set_api_key():
    api_key = os.environ["INDICO_API_KEY"]
    indicoio.config.api_key = api_key
