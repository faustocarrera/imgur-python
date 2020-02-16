#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate authorization link
"""


class Authorize():
    "Class to authorize account with the app"

    def __init__(self, config):
        self.config = config

    def get_url(self):
        "generate authorization url"
        url = 'https://api.imgur.com/oauth2/authorize?client_id={0}&response_type=token'
        return url.format(self.config['client_id'])
