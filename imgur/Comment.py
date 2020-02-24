#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comment handler
"""

import requests
from .ImgurBase import ImgurBase


class Comment(ImgurBase):

    def __init__(self, config, api_url):
        self.config = config
        self.api_url = api_url

    def comments(self, username, page=0, sort='newest'):
        "Return the comments the user has created"
        url = '{0}/3/account/{1}/comments/{2}/{3}'.format(
            self.api_url,
            username,
            sort,
            page
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def comment(self, comment_id):
        "Get information about a specific comment"
        url = '{0}/3/comment/{1}/replies'.format(self.api_url, comment_id)
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def comment_post(self, payload):
        "Creates a new comment or reply a comment, returns the ID of the comment"
        url = '{0}/3/comment'.format(self.api_url)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def comment_delete(self, comment_id):
        "Delete a comment by the given id"
        url = '{0}/3/comment/{1}'.format(self.api_url, comment_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.delete(url, headers=headers)
        return self.response(request, url)

    def comment_vote(self, comment_id, vote):
        "Vote on a comment"
        url = '{0}/3/comment/{1}/vote/{1}'.format(
            self.api_url, comment_id, vote)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers)
        return self.response(request, url)

    def comment_report(self, comment_id, reason):
        "Report a comment for being inappropriate"
        url = '{0}/3/comment/{1}/report'.format(self.api_url, comment_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        payload = {
            'reason': reason
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)
