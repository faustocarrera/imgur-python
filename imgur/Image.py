#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Image handler
"""

import requests
from .ImgurBase import ImgurBase


class Image(ImgurBase):
    "Class to handle images in the imgur account"

    def __init__(self, config, api_url):
        self.config = config
        self.api_url = api_url

    def images(self, username, page):
        "Get account images"
        url = '{0}/3/account/{1}/images/{2}'.format(
            self.api_url,
            username,
            page
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)
