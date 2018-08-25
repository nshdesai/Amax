#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:

Author: ndesai
"""

import indicoio
import os

def get_keywords(data):
    """Returns all keywords in an article along with a confidence score """
    indicoio.config.api_key = os.environ["INDICO_API_KEY"]
    return indico.keywords(data)
