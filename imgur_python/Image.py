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

    def images(self, page):
        "Get account images"
        url = '{0}/3/account/me/images/{1}'.format(
            self.api_url,
            page
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def image(self, image_id):
        "Get information about an image"
        url = '{0}/3/image/{1}'.format(self.api_url, image_id)
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def upload(self, payload, files=None):
        "Upload a new image or video"
        url = '{0}/3/upload'.format(self.api_url)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        if files is not None:
            request = requests.post(
                url,
                headers=headers,
                data=payload,
                files=files
            )
        else:
            request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def update(self, image_id, payload):
        "Updates the title or description of an image"
        url = '{0}/3/image/{1}'.format(self.api_url, image_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def delete(self, image_id):
        "Deletes an image"
        url = '{0}/3/image/{1}'.format(self.api_url, image_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.delete(url, headers=headers)
        return self.response(request, url)
