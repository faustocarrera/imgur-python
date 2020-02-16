#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
imgur entry point
"""

from os import path
import json
import click
import webbrowser
from imgur import Authorize
from imgur import Images
from imgur import Albums


@click.group(chain=True, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('I was invoked without subcommand')


@cli.command('authorize')
def authorize():
    "Authorization"
    auth = Authorize(get_config())
    webbrowser.open(auth.get_url())


@cli.command('post')
def post():
    "Post image to imgur"
    config = get_config()
    image = realpath('./images/untitled.png')
    images = Images(config)
    albums = Albums(config)
    image_response = images.post_image(image, 'untitled.png', 'this is a test')
    if image_response['status'] == 200:
        # create album and add the image
        ids = []
        image_data = image_response['response']['data']
        ids.append(image_data['id'])
        # create album and add image
        album_response = albums.create(
            ids, 'this is a test', 'this is a test', 'hidden')
        print(image_data)
        print(album_response)


def get_config():
    "Get imgur configuration"
    dir_path = path.dirname(path.realpath(__file__))
    config_json = path.join(dir_path, 'config/config.json')
    with open(config_json) as json_file:
        return json.loads(json_file.read())


if __name__ == '__main__':
    cli()
