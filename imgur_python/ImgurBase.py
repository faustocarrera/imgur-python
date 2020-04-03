#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class
"""


class ImgurBase():
    "Basic methods"

    @staticmethod
    def response(request, url):
        "Compose response"
        response = {}
        response['url'] = url
        response['status'] = request.status_code
        if request.status_code == 200:
            response['response'] = request.json()
        else:
            response['response'] = request
        return response

    @staticmethod
    def data(request):
        "Just return the data"
        if request.status_code == 200:
            response = request.json()
            return response['data']
        else:
            return null
