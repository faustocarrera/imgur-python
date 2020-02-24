#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Album handler
"""

import requests
from .ImgurBase import ImgurBase


class Album(ImgurBase):
    "Class to handle the albums in the imgur account"

    def __init__(self, config, api_url):
        self.config = config
        self.api_url = api_url

    def albums(self, username, page):
        "Get all the albums associated with the account"
        url = '{0}/3/account/{1}/albums/{2}'.format(
            self.api_url,
            username,
            page
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def album_get(self, album_id):
        "Get additional information about an album"
        url = '{0}/3/album/{1}'.format(
            self.api_url,
            album_id
        )
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def album_images(self, album_id):
        "Get information about an image in an album"
        url = '{0}/3/album/{1}/images'.format(
            self.api_url,
            album_id
        )
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)
