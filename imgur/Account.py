#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Account handler
"""

import requests
from .ImgurBase import ImgurBase


class Account(ImgurBase):

    def __init__(self, config, api_url):
        self.config = config
        self.api_url = api_url

    def base(self, username):
        "Request standard user information"
        url = '{0}/3/account/{1}'.format(
            self.api_url,
            username
        )
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def block_status(self, username):
        "Determine if the user making the request has blocked a username"
        url = '{0}/account/v1/{1}/block'.format(
            self.api_url,
            username
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def blocks(self):
        "List all accounts being blocked"
        url = '{0}/3/account/me/block'.format(self.api_url)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def block(self, username):
        "Block a user"
        url = '{0}/account/v1/{1}/block'.format(self.api_url, username)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers)
        return self.response(request, url)

    def unblock(self, username):
        "Ublock a user"
        url = '{0}/account/v1/{1}/block'.format(self.api_url, username)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.delete(url, headers=headers)
        return self.response(request, url)
