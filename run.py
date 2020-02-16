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


@click.group(chain=True, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    "Script for the imgur API client testing"
    if ctx.invoked_subcommand is None:
        print('Use run.py --help to display options')
    else:
        ctx.ensure_object(dict)
        ctx.obj['IMGUR'] = Imgur(get_config())


@cli.command('authorize')
@click.pass_context
def authorize(ctx):
    "Generate authorization link"
    imgur = ctx.obj['IMGUR']
    webbrowser.open(imgur.authorize())


@cli.command('access_token')
@click.pass_context
def access_token(ctx):
    "Generate access token"
    imgur = ctx.obj['IMGUR']
    print(imgur.access_token())


def get_config():
    "Get imgur configuration"
    dir_path = path.dirname(path.realpath(__file__))
    config_json = path.join(dir_path, 'config/config.json')
    with open(config_json) as json_file:
        return json.loads(json_file.read())


if __name__ == '__main__':
    cli(obj={})
