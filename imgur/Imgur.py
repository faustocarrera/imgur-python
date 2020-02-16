#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imgur entry point
"""

import json
import requests
from .Authorize import Authorize

class Imgur():
    
    def __init__(self, config):
        self.config = config
        self.api_url = 'https://api.imgur.com/'
        
    def authorize(self):
        "Generate authorization url"
        auth = Authorize(self.config, self.api_url)
        return auth.get_url()
    
    def access_token(self):
        "Generate new access token using the refresh token"
        auth = Authorize(self.config, self.api_url)
        return auth.generate_access_token()