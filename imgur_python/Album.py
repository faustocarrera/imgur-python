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

    def albums(self, page):
        "Get all the albums associated with the account"
        url = '{0}/3/account/{1}/albums/{2}'.format(
            self.api_url,
            self.config['account_username'],
            page
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        response = self.response(request, url)
        # the total number of comments
        response['response']['total'] = self.count()
        return response

    def album(self, album_id):
        "Get additional information about an album"
        url = '{0}/3/album/{1}'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def images(self, album_id):
        "Get information about an image in an album"
        url = '{0}/3/album/{1}/images'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
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

    def ids(self, page):
        "Return an array of all of the album IDs"
        url = '{0}/3/account/{1}/albums/ids/{2}'.format(
            self.api_url,
            self.config['account_username'],
            page
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        response = self.response(request, url)
        # the total number of comments
        response['response']['total'] = self.count()
        return response

    def fav(self, album_id):
        "Favorite an album with a given ID"
        url = '{0}/3/album/{1}/favorite'.format(self.api_url, album_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers)
        return self.response(request, url)

    def count(self):
        "Return the total number of albums associated with the account"
        url = '{0}/3/account/{1}/albums/count'.format(
            self.api_url,
            self.config['account_username']
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.data(request)
