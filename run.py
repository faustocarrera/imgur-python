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
@click.option('--username', default=None, help='imgur username')
@click.pass_context
def account_base(ctx, username):
    "Get account base"
    imgur = ctx.obj['IMGUR']
    if username is None:
        username = ctx.obj['CONFIG']['account_username']
    print(imgur.account_base(username))


@cli.command('block_status')
@click.option('--username', default=None, help='imgur username')
@click.pass_context
def block_status(ctx, username):
    "Check if the <username> blocked you"
    imgur = ctx.obj['IMGUR']
    if username is None:
        username = ctx.obj['CONFIG']['account_username']
    print(imgur.block_status(username))


@cli.command('blocks')
@click.pass_context
def blocks(ctx):
    "Blocked accounts"
    imgur = ctx.obj['IMGUR']
    print(imgur.blocks())


@cli.command('block')
@click.option('--username', default=None, help='imgur username')
@click.pass_context
def block(ctx, username):
    "Block a user"
    if username is None:
        print('Username is required')
        return

    if username == ctx.obj['CONFIG']['account_username']:
        print('You can not block yourself')
        return

    imgur = ctx.obj['IMGUR']
    print(imgur.block(username))


@cli.command('unblock')
@click.option('--username', default=None, help='imgur username')
@click.pass_context
def unblock(ctx, username):
    "Block a user"
    if username is None:
        print('Username is required')
        return

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
@click.option('--username', default=None, help='imgur username')
@click.pass_context
def submissions(ctx, username):
    "Block a user"
    if username is None:
        print('Username is required')
        return

    imgur = ctx.obj['IMGUR']
    print(imgur.submissions(username))

# Image


@cli.command('images')
@click.option('--username', default=None, help='imgur username')
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
