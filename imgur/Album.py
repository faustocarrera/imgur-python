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

    def album(self, album_id):
        "Get additional information about an album"
        url = '{0}/3/album/{1}'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def images(self, album_id):
        "Get information about an image in an album"
        url = '{0}/3/album/{1}/images'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def create(self, payload):
        "Create a new album"
        url = '{0}/3/album'.format(self.api_url)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def update(self, album_id, payload):
        "Update the information of an album"
        url = '{0}/3/album/{1}'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.put(url, headers=headers, data=payload)
        return self.response(request, url)

    def delete(self, delete_hash):
        "Delete an album with a given deletehash"
        url = '{0}/3/album/{1}'.format(self.api_url, delete_hash)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.delete(url, headers=headers)
        return self.response(request, url)

    def add(self, album_id, payload):
        "Adds the marked images to an album"
        url = '{0}/3/album/{1}/add'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def remove(self, delete_hash, payload):
        "Remove the marked images from an album"
        url = '{0}/3/album/{1}/remove_images'.format(self.api_url, delete_hash)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)
