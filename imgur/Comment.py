#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comment handler
"""

import requests
from .ImgurBase import ImgurBase


class Comment(ImgurBase):

    def __init__(self, config, api_url):
        self.config = config
        self.api_url = api_url

    def comments(self, username, page=0, sort='newest'):
        "Return the comments the user has created"
        url = '{0}/3/account/{1}/comments/{2}/{3}'.format(
            self.api_url,
            username,
            sort,
            page
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)
