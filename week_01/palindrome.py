# encoding: utf-8

"""
Created on Nov 23, 2013

@author: Yuval Langer
"""

from bottle import get, post, request, template


def palindrome(s):
    """
    gets a string
    returns the string's palindrome
    """
    if type(s) == type(""):
        s = s.decode("utf-8")

    def palindrome_(s):
        if len(s) == 0:
            return u""
        else:
            return palindrome_(s[1:]) + s[0]

    return palindrome_(s)

assert palindrome(u'abc') == u'cba'
assert palindrome('abc') == 'cba'


@get('/palindrome')
def palindrome_get():
    return """
    <form method="post">
        <input name="word" type="text">
        <input value="Submit" type="button">
    </form>
    """


@post('/palindrome')
def palindrome_post():
    word = request.forms.get('word')
    return template(
        u"""Word: {{word}}<br />
Palindrome: {{palindrome}}""",
        word=word,
        palindrome=palindrome(word),
    )
