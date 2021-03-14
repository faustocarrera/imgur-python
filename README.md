imgur-python
============

A Python client for the Imgur API.

The original imgurpython project is no longer supported, so, I decided to create my own python client for the [Imgur API](https://apidocs.imgur_client.com/?version=latest).

__Disclaimer:__ This is a work in progress. In this first version, I'm not gonna implement all the API calls, only the necessary ones to interact with imgur and be able to create albums, upload images and share them on the site.

For more information, check the [API client documentation](https://imgur-python.readthedocs.io/en/latest/)

## Requirements

* Python 3.5
* [requests](https://2.python-requests.org/en/master/)
* [fleep](https://github.com/floyernick/fleep-py)

## Links

* [imgur API documentation](https://apidocs.imgur.com/?version=latest#intro)
* [API client documentation](https://imgur-python.readthedocs.io/en/latest/)

## Install

```
$ python setup.py install
```

with pip

```
$ pip install imgur-python
```

## How to publish something and share it with the community?

* upload a bunch of images
* add them to an album
* share it

```
from os import path
from imgur_python import Imgur

imgur_client = Imgur({'client_id': 'cf8c57ca8......'})
image = imgur_client.image_upload(path.realpath('./image.png'), 'Untitled', 'My first image upload')
image_id = image['response']['data']['id']
album =  imgur_client.album_create([image_id], 'My first album', 'Something funny', 'public')
album_id = album['response']['data']['id']
response = imgur_client.gallery_album(album_id, 'This is going down on the sub', 0, 'funny,midly_interesting')
print(response)
```

## Roadmap

__Gallery__

* Gallery Album
* Gallery Image
* Album / Image Reporting
* Album / Image Votes
* Album / Image Voting
* Album / Image Comments
* Album / Image Comment
* Album / Image Comment Creation