#! /usr/bin/env python
# encoding: utf-8

"""
Created on Nov 24, 2013

@author: Yuval Langer
"""


from bottle import get, post, template, request


def html_list(text, is_ordered):
    """ text -> boolean -> html list """
    if type(text) == type(""):
        text = text.decode("utf-8")
    assert type(text) == type(u"")
    s = ""
    line_list = text.split(u"\n")
    start = u"<ul><li>"
    fill = u"</li>\n<li>"
    end = u"</ul>\n"
    if is_ordered == True:
        start = u"<ol><li>"
        end = u"</ol>\n"
    s += start + fill.join(line_list) + end
    return s


@get("/html_list")
def html_list_get():
    """ html list get """
    return """
        <form action="/html_list" method="post">
            <textarea name="text"></textarea>
            <input name="ordered" type="checkbox"> Ordered
            <input type="submit">
        </form>
    """


@post("/html_list")
def html_list_post():
    """ html list post """
    text = request.forms.get("text")
    ordered = request.forms.get("ordered")
    print str(ordered)
    html_list(text, ordered=='ordered')
    return html_list(text, ordered=='on')

'''

def asserts():
    print "asserts"
    assert False

asserts()
'''
