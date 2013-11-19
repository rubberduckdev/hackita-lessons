#! /usr/bin/env python2.7
# encoding: utf-8

'''
Hackita lessons
'''

from bottle import route, default_app, run

@route('/')
def get():
    return "Hello from bottle! :-)"

application = default_app()