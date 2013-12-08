#! /usr/bin/env python
# encoding: utf-8

"""
Created on Nov 23, 2013

@author: Yuval Langer
"""


from collections import Counter

from bottle import request, post, get, template


def letter_count_dict(text):
    assert type(text) == type(u"")
    letter_to_count = {}
    for letter in text:
        letter_to_count.setdefault(letter, 0)
        letter_to_count[letter] += 1
    return letter_to_count


def letter_count_counter(text):
    assert type(text) == type(u"")
    letter_to_count = Counter(text)
    return letter_to_count


@get("/letter_count")
def letter_count_get():
    """ letter count get """
    return u"""
        <form action="/letter_count" method="post">
            our text: <input name="text" type="text">
            <input value="Submit" type="submit">
        </form>
    """


@post("/letter_count")
def letter_count_post():
    """ letter count post """

    text = request.forms.get("text")
    text = text.decode("utf-8")
    letter_to_count = letter_count_counter(
        request.forms.get("text").decode("utf-8")
    )
    return template("""% for k, v in letter_to_count.items():
        {{k}}: {{v}}<br />
        % end
    """, letter_to_count=letter_to_count)


def asserts():
    assert letter_count_dict(u"abc") == {u"a": 1, u"b": 1, u"c": 1}
    assert letter_count_dict(u"אבג") == {u"א": 1, u"ב": 1, u"ג": 1}
    print "asserts PASS: letter_count"

asserts()
