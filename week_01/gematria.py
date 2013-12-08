# encoding: utf-8

"""
Created on Nov 23, 2013

@author: Yuval Langer
"""

from bottle import request, get, post


gematria_letter_to_number = {
    u'א': 1,
    u'ב': 2,
    u'ג': 3,
    u'ד': 4,
    u'ה': 5,
    u'ו': 6,
    u'ז': 7,
    u'ח': 8,
    u'ט': 9,
    u'י': 10,
    u'כ': 20,
    u'ך': 20,
    u'ל': 30,
    u'מ': 40,
    u'ם': 40,
    u'נ': 50,
    u'ן': 50,
    u'ס': 60,
    u'ע': 70,
    u'פ': 80,
    u'ף': 80,
    u'צ': 90,
    u'ץ': 90,
    u'ק': 100,
    u'ר': 200,
    u'ש': 300,
    u'ת': 400,
}


def gematria(word):
    """ String -> Number """
    return sum([gematria_letter_to_number.get(letter, 0) for letter in word])


@get('/gematria')
def gematria_get():
    return """
        <form action="/gematria" method="post">
        Please enter a word you'd like to get its gematric value:
        <input name="word" type="text">
        <input value="Gematrify" type="submit">
        </form>
    """


@post('/gematria')
def gematria_post():
    word = request.forms.get('word').decode('utf-8')
    return u"The value of {word} is: {value}".format(
        word=word,
        value=gematria(word),
    )


def asserts():
    assert gematria(u"אגב") == 6

asserts()
