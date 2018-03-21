#!/bin/python3

# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse

url = "http://www.example.com/?a=1&b=2"

# GET request
resp = urllib.request.urlopen(url)
data = resp.read()
print(data)


# POST request
data = urllib.parse.urlencode({"x": 1, "y": 2})
data2 = data.encode('utf-8')

resp = urllib.request.urlopen(url, data2)
data = resp.read()
print(data)

# get response headers
resp = urllib.request.urlopen(url)
print(resp.getheaders())
