#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Album handler
"""

import requests


class Album():
    "Class to handle the albums in the imgur account"

    def __init__(self, config):
        self.config = config

    def create(self, ids, title, description, privacy):
        "Create an album"
        url = 'https://api.imgur.com/3/album'
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        payload = {
            'ids[]': ids,
            'title': title,
            'description': description,
            'privacy': privacy,
            'cover': ids[0]
        }
        response = requests.post(
            url,
            headers=headers,
            data=payload
        )
        return {
            'status': response.status_code,
            'response': response.json()
        }
