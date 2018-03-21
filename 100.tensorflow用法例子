#!/bin/python3

# -*- coding: utf-8 -*-

import tensorflow as tf

a = tf.constant(2)
sess = tf.Session()
print(sess.run(a))


x = tf.Variable([1, 2])
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(x))
