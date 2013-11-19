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

if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)