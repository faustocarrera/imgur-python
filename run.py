#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
imgur entry point
"""

from os import path
import json
import webbrowser
import click
from imgur import Imgur


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
        print('You can not block yourself')
        return

    imgur = ctx.obj['IMGUR']
    print(imgur.block(username))


@cli.command('unblock')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def unblock(ctx, username):
    "Unblock a user"
    if username == ctx.obj['CONFIG']['account_username']:
        print('You can not unblock yourself')
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


@cli.command('comments')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def comments(ctx, username):
    "Account comments"
    imgur = ctx.obj['IMGUR']
    print(imgur.comments(username))


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

# Album


@cli.command('albums')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def albums(ctx, username):
    "Account albums"
    imgur = ctx.obj['IMGUR']
    print(imgur.albums(username))


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
    images = []
    title = 'Album title'
    description = 'Album description'
    privacy = 'hidden'
    print(imgur.album_create(images, title, description, privacy))


@cli.command('album_update')
@click.option('--album_id', default=None, help='Album ID', required=True)
@click.pass_context
def album_update(ctx,  album_id):
    "Update the information of an album"
    imgur = ctx.obj['IMGUR']
    images = ['g38lQAb', 'flF3tuE', 'DZhTxTf', 'qmjQAHV']
    title = 'Album edited title'
    description = 'Album edited description'
    privacy = 'hidden'
    print(imgur.album_update(album_id, images, title, description, privacy))


@cli.command('album_delete')
@click.option('--delete_hash', default=None, help='Album delete hash', required=True)
@click.pass_context
def album_delete(ctx, delete_hash):
    "Delete an album with a given deletehash."
    imgur = ctx.obj['IMGUR']
    print(imgur.album_delete(delete_hash))


# Image


@cli.command('images')
@click.option('--username', default=None, help='imgur username', required=True)
@click.pass_context
def images(ctx, username):
    "Check if the <username> blocked you"
    imgur = ctx.obj['IMGUR']
    if username is None:
        username = ctx.obj['CONFIG']['account_username']
    print(imgur.images(username, 0))


def get_config():
    "Get imgur configuration"
    dir_path = path.dirname(path.realpath(__file__))
    config_json = path.join(dir_path, 'config/config.json')
    with open(config_json) as json_file:
        return json.loads(json_file.read())


if __name__ == '__main__':
    cli(obj={})
