# encoding: utf-8

"""
Created on Nov 23, 2013

@author: Yuval Langer
"""


from bottle import request, post, get


@get('/hello')
def hello():
    return '''Hello World! <br />
        <form action="/hello" method="post">
            Name: <input name="name" type="text" />
            <input value="Say Hello to bottle" type="submit" />
        </form>
    '''


@post('/hello')
def hello_name():
    return template("Hello, {{name}}!", name=request.forms.get('name'))
