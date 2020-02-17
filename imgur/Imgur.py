#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imgur entry point
"""

from .Account import Account
from .Album import Album
from .Authorize import Authorize
from .Comment import Comment
from .Gallery import Gallery
from .Image import Image


class Imgur():

    def __init__(self, config):
        self.config = config
        self.api_url = 'https://api.imgur.com'

    # Authorization

    def authorize(self):
        "Generate authorization url"
        auth = Authorize(self.config, self.api_url)
        return auth.get_url()

    def access_token(self):
        "Generate new access token using the refresh token"
        auth = Authorize(self.config, self.api_url)
        return auth.generate_access_token()

    # Account

    def account_base(self, username):
        "Request standard user information"
        account = Account(self.config, self.api_url)
        return account.base(username)

    def block_status(self, username):
        "Determine if the user making the request has blocked a username"
        account = Account(self.config, self.api_url)
        return account.block_status(username)

    def blocks(self):
        "List all accounts being blocked"
        account = Account(self.config, self.api_url)
        return account.blocks()

    def block(self, username):
        "Block a user"
        account = Account(self.config, self.api_url)
        return account.block(username)

    def unblock(self, username):
        "Unblock a user"
        account = Account(self.config, self.api_url)
        return account.unblock(username)

    # Images

    def images(self, username, page):
        "Get account images"
        if username == self.config['account_username']:
            username = 'me'
        images = Image(self.config, self.api_url)
        return images.images(username, page)
