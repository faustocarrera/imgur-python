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
        # start the party
        self.auth = Authorize(self.config, self.api_url)
        self.account = Account(self.config, self.api_url)
        self.comment = Comment(self.config, self.api_url)
        self.album = Album(self.config, self.api_url)

    # Authorization

    def authorize(self):
        "Generate authorization url"
        return self.auth.get_url()

    def access_token(self):
        "Generate new access token using the refresh token"
        return self.auth.generate_access_token()

    # Account

    def account_base(self, username):
        "Request standard user information"
        return self.account.base(username)

    def block_status(self, username):
        "Determine if the user making the request has blocked a username"
        return self.account.block_status(username)

    def blocks(self):
        "List all accounts being blocked"
        return self.account.blocks()

    def block(self, username):
        "Block a user"
        return self.account.block(username)

    def unblock(self, username):
        "Unblock a user"
        return self.account.unblock(username)

    def favorites(self, page=0, sort='newest'):
        "User favorites"
        return self.account.favorites(page, sort)

    def submissions(self, username, page=0):
        "User submissions to the gallery"
        return self.account.submissions(username, page)

    def avatars(self):
        "Get the list of available avatars for the logged user"
        return self.account.avatars()

    def avatar(self):
        "Get the current account's avatar URL and avatar name"
        return self.account.avatar()

    def settings(self, settings_data=None):
        "Get the current account's avatar URL and avatar name"
        if settings_data is None:
            return self.account.settings()
        else:
            return self.account.save(settings_data)

    # Comment

    def comments(self, username, page=0, sort='newest'):
        "Return the comments the user has created"
        return self.comment.comments(username, page, sort)

    def comment_get(self, comment_id):
        "Get information about a specific comment"
        return self.comment.comment(comment_id)

    def comment_post(self, image_id, comment, parent_id=None):
        "Creates a new comment or reply a comment, returns the ID of the comment"
        data = {
            'image_id': image_id,
            'comment': comment
        }
        if parent_id is not None:
            data['parent_id'] = parent_id
        return self.comment.post(data)

    def comment_delete(self, comment_id):
        "Delete a comment by the given id"
        return self.comment.delete(comment_id)

    def comment_vote(self, comment_id, vote):
        "Vote on a comment"
        return self.comment.vote(comment_id, vote)

    def comment_report(self, comment_id, reason):
        "Report a comment for being inappropriate"
        return self.comment.report(comment_id, reason)

    # Album

    def albums(self, username, page=0):
        "Get all the albums associated with the account"
        return self.album.albums(username, page)

    def album_get(self, album_id):
        "Get additional information about an album"
        return self.album.album(album_id)

    def album_images(self, album_id):
        "Get information about an image in an album"
        return self.album.images(album_id)

    def album_create(self, images, title, description, privacy='hidden'):
        "Create a new album"
        payload = {}
        payload['title'] = title
        payload['description'] = description
        payload['privacy'] = privacy
        if len(images):
            payload['ids[]'] = images
            payload['cover'] = images[0]
        return self.album.create(payload)

    def album_update(self, album_id, images, title, description, privacy='hidden'):
        "Update the information of an album"
        payload = {}
        payload['title'] = title
        payload['description'] = description
        payload['privacy'] = privacy
        if len(images):
            payload['ids[]'] = images
            payload['cover'] = images[0]
        return self.album.update(album_id, payload)

    def album_delete(self, delete_hash):
        "Delete an album with a given deletehash"
        return self.album.delete(delete_hash)

    # Image

    def images(self, username, page):
        "Get account images"
        if username == self.config['account_username']:
            username = 'me'
        image = Image(self.config, self.api_url)
        return image.images(username, page)
