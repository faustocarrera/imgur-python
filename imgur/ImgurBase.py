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
        # response['headers'] = request.headers
        if request.status_code == 200:
            response['response'] = request.json()
        else:
            response['response'] = request
        return response
