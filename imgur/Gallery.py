#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gallery handler
"""

import requests
from .ImgurBase import ImgurBase


class Gallery(ImgurBase):
    "Class to handle the gallery publications"

    def __init__(self, config, api_url):
        self.config = config
        self.api_url = api_url

    def tags(self):
        "Gets a list of default tags"
        url = '{0}/3/tags'.format(self.api_url)
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def tag(self, tag_name):
        "Gets metadata about a tag"
        url = '{0}/3/gallery/tag_info/{1}'.format(self.api_url, tag_name)
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)
