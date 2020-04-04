#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
imgur entry point
"""

from os import path
import json
import click
from imgur_python import Imgur


@click.group(chain=False, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    "Script for the imgur API client testing"
    if ctx.invoked_subcommand is None:
        print('Use run.py --help to display options')
    else:
        ctx.ensure_object(dict)
        ctx.obj['CONFIG'] = get_config()
        ctx.obj['IMGUR'] = Imgur(get_config())

# Version


@cli.command('version')
@click.pass_context
def version(ctx):
    "Library version"
    imgur = ctx.obj['IMGUR']
    print(imgur.version())

# Auth


@cli.command('authorize')
@click.pass_context
def authorize(ctx):
    "Generate authorization link"
    imgur = ctx.obj['IMGUR']
    print(imgur.authorize())


@cli.command('access_token')
@click.pass_context
def access_token(ctx):
    "Generate access token"
    imgur = ctx.obj['IMGUR']
    print(imgur.access_token())

# Account


@cli.command('account_base')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def account_base(ctx, username):
    "Get account base"
    imgur = ctx.obj['IMGUR']
    print(imgur.account_base(username))


@cli.command('block_status')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def block_status(ctx, username):
    "Check if the <username> blocked you"
    imgur = ctx.obj['IMGUR']
    print(imgur.block_status(username))


@cli.command('blocks')
@click.pass_context
def blocks(ctx):
    "Blocked accounts"
    imgur = ctx.obj['IMGUR']
    print(imgur.blocks())


@cli.command('block')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def block(ctx, username):
    "Block a user"
    if username == ctx.obj['CONFIG']['account_username']:
        print('You cannot block yourself')
        return

    imgur = ctx.obj['IMGUR']
    print(imgur.block(username))


@cli.command('unblock')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def unblock(ctx, username):
    "Unblock a user"
    if username == ctx.obj['CONFIG']['account_username']:
        print('You cannot unblock yourself')
        return

    imgur = ctx.obj['IMGUR']
    print(imgur.unblock(username))


@cli.command('favorites')
@click.pass_context
def favorites(ctx):
    "Users favorited images"
    imgur = ctx.obj['IMGUR']
    print(imgur.favorites(0, 'oldest'))


@cli.command('submissions')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def submissions(ctx, username):
    "User submissions"
    imgur = ctx.obj['IMGUR']
    print(imgur.submissions(username))


@cli.command('avatars')
@click.pass_context
def avatars(ctx):
    "Available avatars"
    imgur = ctx.obj['IMGUR']
    print(imgur.avatars())


@cli.command('avatar')
@click.pass_context
def avatar(ctx):
    "Account avatar"
    imgur = ctx.obj['IMGUR']
    print(imgur.avatar())


@cli.command('settings')
@click.pass_context
def settings(ctx):
    "Account settings"
    imgur = ctx.obj['IMGUR']
    print(imgur.settings())


@cli.command('gallery_profile')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def gallery_profile(ctx, username):
    "Gallery profile"
    imgur = ctx.obj['IMGUR']
    print(imgur.gallery_profile(username))


@cli.command('follow_tag')
@click.option('--tag', default=None, help='imgur tag', required=True)
@click.pass_context
def follow_tag(ctx, tag):
    "Follow tag"
    imgur = ctx.obj['IMGUR']
    print(imgur.follow_tag(tag))


@cli.command('unfollow_tag')
@click.option('--tag', default=None, help='imgur tag', required=True)
@click.pass_context
def unfollow_tag(ctx, tag):
    "Unfollow tag"
    imgur = ctx.obj['IMGUR']
    print(imgur.unfollow_tag(tag))


@cli.command('notifications')
@click.pass_context
def notifications(ctx):
    "Unfollow tag"
    imgur = ctx.obj['IMGUR']
    print(imgur.notifications())

# Comments


@cli.command('comments')
@click.pass_context
def comments(ctx):
    "Account comments"
    imgur = ctx.obj['IMGUR']
    print(imgur.comments())


@cli.command('comment')
@click.option('--comment_id', default=None, help='Comment ID', required=True)
@click.pass_context
def comment(ctx, comment_id):
    "Information about a comment"
    # 1804022011
    imgur = ctx.obj['IMGUR']
    print(imgur.comment_get(comment_id))


@cli.command('comment_post')
@click.pass_context
def comment_post(ctx):
    "Post a comment"
    imgur = ctx.obj['IMGUR']
    print(imgur.comment_post('TneZVzU', 'this is a reply to the comment'))


@cli.command('comment_delete')
@click.pass_context
def comment_delete(ctx):
    "Delete a comment"
    imgur = ctx.obj['IMGUR']
    print(imgur.comment_delete(1809979027))


@cli.command('comment_ids')
@click.pass_context
def comment_ids(ctx):
    "Account comments"
    imgur = ctx.obj['IMGUR']
    print(imgur.comment_ids())


@cli.command('comment_replies')
@click.option('--comment_id', default=None, help='Comment ID', required=True)
@click.pass_context
def comment_replies(ctx, comment_id):
    "Account comments"
    imgur = ctx.obj['IMGUR']
    print(imgur.comment_replies(comment_id))

# Album


@cli.command('albums')
@click.pass_context
def albums(ctx):
    "Account albums"
    imgur = ctx.obj['IMGUR']
    print(imgur.albums())


@cli.command('album_get')
@click.option('--album_id', default=None, help='Album ID', required=True)
@click.pass_context
def album_get(ctx, album_id):
    "Details about an album"
    imgur = ctx.obj['IMGUR']
    print(imgur.album_get(album_id))


@cli.command('album_images')
@click.option('--album_id', default=None, help='Album ID', required=True)
@click.pass_context
def album_images(ctx, album_id):
    "Album images"
    imgur = ctx.obj['IMGUR']
    print(imgur.album_images(album_id))


@cli.command('album_create')
@click.pass_context
def album_create(ctx):
    "Create a new album"
    imgur = ctx.obj['IMGUR']
    images_list = []
    title = 'Album title'
    description = 'Album description'
    privacy = 'hidden'
    print(imgur.album_create(images_list, title, description, privacy))


@cli.command('album_update')
@click.option('--album_id', default=None, help='Album ID', required=True)
@click.pass_context
def album_update(ctx, album_id):
    "Update the information of an album"
    imgur = ctx.obj['IMGUR']
    images_list = ['g38lQAb', 'flF3tuE', 'DZhTxTf', 'qmjQAHV']
    title = 'Album edited title'
    description = 'Album edited description'
    privacy = 'hidden'
    print(imgur.album_update(album_id, images_list, title, description, privacy))


@cli.command('album_delete')
@click.option('--delete_hash', default=None, help='Album delete hash', required=True)
@click.pass_context
def album_delete(ctx, delete_hash):
    "Delete an album with a given deletehash."
    imgur = ctx.obj['IMGUR']
    print(imgur.album_delete(delete_hash))


@cli.command('album_add')
@click.option('--album_id', default=None, help='Album ID', required=True)
@click.pass_context
def album_add(ctx, album_id):
    "Adds the marked images to an album"
    imgur = ctx.obj['IMGUR']
    images_list = ['g38lQAb', 'flF3tuE', 'DZhTxTf', 'qmjQAHV']
    print(imgur.album_add(album_id, images_list))


@cli.command('album_remove')
@click.option('--delete_hash', default=None, help='Album ID', required=True)
@click.pass_context
def album_remove(ctx, delete_hash):
    "Remove the marked images from an album"
    imgur = ctx.obj['IMGUR']
    images_list = ['g38lQAb', 'flF3tuE']
    print(imgur.album_remove(delete_hash, images_list))


@cli.command('album_ids')
@click.pass_context
def album_ids(ctx):
    "Album ids"
    imgur = ctx.obj['IMGUR']
    print(imgur.album_ids())


@cli.command('album_fav')
@click.option('--album_id', default=None, help='Album ID', required=True)
@click.pass_context
def album_fav(ctx, album_id):
    "Mark an album as favorite"
    imgur = ctx.obj['IMGUR']
    print(imgur.album_fav(album_id))

# Image


@cli.command('images')
@click.pass_context
def images(ctx):
    "Get account images"
    imgur = ctx.obj['IMGUR']
    print(imgur.images())


@cli.command('image')
@click.option('--image_id', default=None, help='image id', required=True)
@click.pass_context
def image(ctx, image_id):
    "Get information about an image"
    imgur = ctx.obj['IMGUR']
    print(imgur.image_get(image_id))


@cli.command('image_upload')
@click.pass_context
def image_upload(ctx):
    "Upload a new image or video"
    imgur = ctx.obj['IMGUR']
    # files
    image_path = path.realpath('./files/untitled.png')
    ## video = path.realpath('./files/0kYG5Y6.mp4')
    ## url = 'https://i.imgur.com/SqLVq0w.jpg'
    # image data
    title = 'Untitled'
    description = 'Image description'
    album = None
    disable_audio = 0
    print(imgur.image_upload(image_path, title, description, album, disable_audio))


@cli.command('image_update')
@click.option('--image_id', default=None, help='image id', required=True)
@click.pass_context
def image_update(ctx, image_id):
    "Updates the title or description of an image"
    imgur = ctx.obj['IMGUR']
    # image data
    title = 'Image updated title'
    description = 'Image updated description'
    print(imgur.image_update(image_id, title, description))


@cli.command('image_delete')
@click.option('--image_id', default=None, help='image id', required=True)
@click.pass_context
def image_delete(ctx, image_id):
    "Deletes an image"
    imgur = ctx.obj['IMGUR']
    print(imgur.image_delete(image_id))


@cli.command('image_ids')
@click.pass_context
def image_ids(ctx):
    "Returns an array of Image IDs"
    imgur = ctx.obj['IMGUR']
    print(imgur.image_ids())


@cli.command('image_fav')
@click.option('--image_id', default=None, help='image id', required=True)
@click.pass_context
def image_fav(ctx, image_id):
    "Favorite an image with the given ID"
    imgur = ctx.obj['IMGUR']
    print(imgur.image_fav(image_id))

# Gallery


@cli.command('gallery_tags')
@click.pass_context
def gallery_tags(ctx):
    "Gets a list of default tags"
    imgur = ctx.obj['IMGUR']
    print(imgur.gallery_tags())


@cli.command('gallery_tag')
@click.option('--tag_name', default=None, help='tag name', required=True)
@click.pass_context
def gallery_tag(ctx, tag_name):
    "Gets metadata about a tag"
    imgur = ctx.obj['IMGUR']
    print(imgur.gallery_tag(tag_name))


@cli.command('gallery_image')
@click.pass_context
def gallery_image(ctx):
    "Share an Album or Image to the Gallery"
    imgur = ctx.obj['IMGUR']
    image_id = '6ZYihph'
    title = 'It was a joke'
    mature = 0
    tags = 'joke,funny,penguins,midly_interesting'
    print(imgur.gallery_image(image_id, title, mature, tags))


@cli.command('gallery_album')
@click.pass_context
def gallery_album(ctx):
    "Share an Album or Image to the Gallery"
    imgur = ctx.obj['IMGUR']
    album_id = 'zbF0LnN'
    title = 'I need a home with this swimming pool'
    mature = 0
    tags = 'midly_interesting,pool,swimmingpool,home'
    print(imgur.gallery_album(album_id, title, mature, tags))


@cli.command('gallery_remove')
@click.option('--gallery_id', default=None, help='gallery id', required=True)
@click.pass_context
def gallery_remove(ctx, gallery_id):
    "Remove an image from the public gallery"
    imgur = ctx.obj['IMGUR']
    print(imgur.gallery_remove(gallery_id))

# Config


def get_config():
    "Get imgur configuration"
    dir_path = path.dirname(path.realpath(__file__))
    config_json = path.join(dir_path, 'config/config.json')
    with open(config_json) as json_file:
        return json.loads(json_file.read())


if __name__ == '__main__':
    cli(obj={})
