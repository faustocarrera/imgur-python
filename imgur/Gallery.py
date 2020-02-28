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

    def image(self, image_id, payload):
        "Share an Album or Image to the Gallery"
        url = '{0}/3/gallery/image/{1}'.format(self.api_url, image_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def album(self, album_id, payload):
        "Share an Album or Image to the Gallery"
        url = '{0}/3/gallery/album/{1}'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def remove(self, gallery_id):
        "Remove an image from the public gallery"
        url = '{0}/3/gallery/{1}'.format(self.api_url, gallery_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.delete(url, headers=headers)
        return self.response(request, url)
