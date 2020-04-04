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
from .FileCheck import FileCheck


class Imgur():
    "Imgur classes entry point"

    __version__ = '0.2.1'

    def __init__(self, config):
        # config
        self.config = config
        self.api_url = 'https://api.imgur.com'
        # start the party
        self.auth = Authorize(self.config, self.api_url)
        self.account = Account(self.config, self.api_url)
        self.comment = Comment(self.config, self.api_url)
        self.album = Album(self.config, self.api_url)
        self.image = Image(self.config, self.api_url)
        self.gallery = Gallery(self.config, self.api_url)

    # Version

    def version(self):
        "API client version"
        return 'Imgur API client {0}'.format(self.__version__)

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

    def gallery_profile(self, username):
        "Returns the totals for the gallery profile"
        return self.account.gallery_profile(username)

    def follow_tag(self, tag):
        "Follows the <tag> specified for the currently logged in user"
        return self.account.follow_tag(tag)

    def unfollow_tag(self, tag):
        "Unfollows the <tag> specified for the currently logged in user"
        return self.account.unfollow_tag(tag)
    
    def notifications(self, new=False):
        "Returns all of the reply notifications for the user"
        return self.account.notifications(new)

    # Comment

    def comments(self, page=0, sort='newest'):
        "Return the comments the user has created"
        return self.comment.comments(page, sort)

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

    def comment_ids(self, page=0, sort='newest'):
        "Return an array of all of the comment IDs"
        return self.comment.ids(page, sort)

    def comment_replies(self, comment_id):
        "Returns all of the reply notifications for the user"
        return self.comment.replies(comment_id)

    # Album

    def albums(self, page=0):
        "Get all the albums associated with the account"
        return self.album.albums(page)

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

    def album_add(self, album_id, images):
        "Adds the marked images to an album"
        payload = {
            'ids[]': images
        }
        return self.album.add(album_id, payload)

    def album_remove(self, delete_hash, images):
        "Remove the marked images from an album"
        payload = {
            'ids[]': images
        }
        return self.album.remove(delete_hash, payload)
    
    def album_ids(self, page=0):
        "Return an array of all of the album IDs"
        return self.album.ids(page)
    
    def album_fav(self, album_id):
        "Favorite an album with a given ID"
        return self.album.fav(album_id)

    # Image

    def images(self, page=0):
        "Get account images"
        return self.image.images(page)

    def image_get(self, image_id):
        "Get information about an image"
        return self.image.image(image_id)

    def image_upload(self, filename, title, description, album=None, disable_audio=1):
        "Upload a new image or video"
        files = None
        payload = {
            'title': title,
            'description': description
        }
        # album
        if album is not None:
            payload['album'] = album
        # file, video or url
        if filename.startswith('http'):
            payload['type'] = 'url'
            payload['image'] = filename
        else:
            file_check = FileCheck()
            file_info = file_check.check(filename)
            if file_info is not None:
                payload['type'] = 'file'
                if file_info['file_type'] == 'image':
                    files = {
                        'image': open(filename, 'rb')
                    }

                elif file_info['file_type'] == 'video':
                    files = {
                        'video': open(filename, 'rb')
                    }
                    payload['disable_audio'] = disable_audio

            else:
                return 'Error: this is not an accepted file format'
        return self.image.upload(payload, files)

    def image_update(self, image_id, title=None, description=None):
        "Updates the title or description of an image"
        payload = {}
        if title is not None:
            payload['title'] = title
        if description is not None:
            payload['description'] = description
        return self.image.update(image_id, payload)

    def image_delete(self, image_id):
        "Deletes an image"
        return self.image.delete(image_id)
    
    def image_ids(self, page=0):
        "Returns an array of Image IDs that are associated with the account"
        return self.image.ids(page)
    
    def image_fav(self, image_id):
        "Favorite an image with the given ID"
        return self.image.fav(image_id)

    # Gallery

    def gallery_tags(self):
        "Gets a list of default tags"
        return self.gallery.tags()

    def gallery_tag(self, tag_name):
        "Gets metadata about a tag"
        return self.gallery.tag(tag_name)

    def gallery_image(self, image_id, title, mature, tags):
        "Share an Album or Image to the Gallery"
        payload = {
            'title': title,
            'mature': mature,
            'tags': tags,
            'terms': 1
        }
        return self.gallery.image(image_id, payload)

    def gallery_album(self, album_id, title, mature, tags):
        "Share an Album or Image to the Gallery"
        payload = {
            'title': title,
            'mature': mature,
            'tags': tags,
            'terms': 1
        }
        return self.gallery.album(album_id, payload)

    def gallery_remove(self, gallery_id):
        "Remove an image from the public gallery"
        return self.gallery.remove(gallery_id)
