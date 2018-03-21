#!/bin/python3

# -*- coding: utf-8 -*-

import urllib.request

url = "https://github.com/"
resp = urllib.request.urlopen(url)
print(resp.status, resp.reason)

data = resp.read()
print(data)
