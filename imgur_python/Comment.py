#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comment handler
"""

import requests
from .ImgurBase import ImgurBase


class Comment(ImgurBase):
    "Class to handle the comments of the imgur account"

    def __init__(self, config, api_url):
        self.config = config
        self.api_url = api_url

    def comments(self, page=0, sort='newest'):
        "Return the comments the user has created"
        url = '{0}/3/account/{1}/comments/{2}/{3}'.format(
            self.api_url,
            self.config['account_username'],
            sort,
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

    def comment(self, comment_id):
        "Get information about a specific comment"
        url = '{0}/3/comment/{1}'.format(self.api_url, comment_id)
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def post(self, payload):
        "Creates a new comment or reply a comment, returns the ID of the comment"
        url = '{0}/3/comment'.format(self.api_url)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers, data=payload)
        return self.response(request, url)

    def delete(self, comment_id):
        "Delete a comment by the given id"
        url = '{0}/3/comment/{1}'.format(self.api_url, comment_id)
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.delete(url, headers=headers)
        return self.response(request, url)

    def vote(self, comment_id, vote):
        "Vote on a comment"
        url = '{0}/3/comment/{1}/vote/{1}'.format(
            self.api_url,
            comment_id,
            vote
        )
        headers = {
            'authorization': 'Bearer {0}'.format(self.config['access_token'])
        }
        request = requests.post(url, headers=headers)
        return self.response(request, url)

    def report(self, comment_id, reason):
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

    def ids(self, page, sort):
        "Return an array of all of the comment IDs"
        url = '{0}/3/account/{1}/comments/ids/{2}/{3}'.format(
            self.api_url,
            self.config['account_username'],
            sort,
            page
        )
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        response = self.response(request, url)
        # the total number of comments
        response['response']['total'] = self.count()
        return response

    def replies(self, comment_id):
        "Get the comment with all of the replies for the comment"
        url = '{0}/3/comment/{1}/replies'.format(
            self.api_url,
            comment_id
        )
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.response(request, url)

    def count(self):
        "Return a count of all of the comments associated with the account"
        url = '{0}/3/account/{1}/comments/count'.format(
            self.api_url,
            self.config['account_username']
        )
        headers = {
            'authorization': 'Client-ID {0}'.format(self.config['client_id'])
        }
        request = requests.get(url, headers=headers)
        return self.data(request)
