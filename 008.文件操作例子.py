#!/bin/python3

# -*- coding: utf-8 -*-

# write file
file = open('d:/test.txt', 'wb')
data = b'hello'
file.write(data)
file.close()

# read file
file = open('d:/test.txt', 'rb')
data = file.read()
file.close()
print(data)
