#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Image handler
"""

import requests


class Image():
    "Class to handle images in the imgur account"

    def __init__(self, config):
        self.config = config

    def post_image(self, image, name, description):
        "Post new image"
        url = 'https://api.imgur.com/3/image'
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        payload = {
            'type': 'file',
            'name': name,
            'title': 'Year progress',
            'description': description
        }
        files = {
            'image': open(image, 'rb')
        }
        response = requests.post(
            url,
            headers=headers,
            data=payload,
            files=files
        )
        return {
            'status': response.status_code,
            'response': response.json()
        }

    def list_images(self):
        "List images from the account"
        images = []
        url = 'https://api.imgur.com/3/account/{0}/images/0'.format(
            self.config['account_username']
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            data = result['data']
            for image in data:
                images.append(image['name'])
        return images
