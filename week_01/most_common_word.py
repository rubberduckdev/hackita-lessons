#!/usr/bin/env python
# encoding: utf-8

from collections import Counter

from bottle import post, get, request, SimpleTemplate


def most_common_word(s):
    """ text -> most common word """
    return max(Counter(s.split()))


@get("/most_common_word")
def most_common_word_get():
    return """
        <form action="/most_common_word" method="post">
        Enter ze texts: <input name="text" type="text">
        <input value="Submit" type="button">
        </form>
    """

post_template = SimpleTemplate(
    """Ze most common word out of: <br />
<pre>{{text}}</pre> and the most common word: {{most_common_word}}""",
)


@post("/most_common_word")
def most_common_word_post():
    text = request.forms.get("text")
    return post_template.render(
        text=text,
        most_common_word=most_common_word(text),
    )
