#!/usr/bin/env python
# encoding: utf-8

'''
Hackita lessons
'''

from bottle import route, default_app, run, template

import hello
import gematria
import bottles_song
import palindrome
import most_common_word
import multiplication_list
import letter_count
import palindrome
import most_common_word
import html_list
#import html_table
import linkify
'''
import html_anchor
import the_world_s_countries_and_us
'''


@route('/')
def index():
    return template(
        u"""
<ul>
% for route, text in route_text_list:
  <li><a href="{{route}}">{{text}}</a></li>
% end
</ul>""",
        [("/bottles", "bottles"),
         ("/gematria", "gematria"),
         ("/multiplication_list", "multiplication list"),
         ("/palindrome", "palindrome"),
         ("/most_common_word", "most common word"),
         ("/html_list", "html list"),
         ("/html_table", "html table"),
         ("/linkify", "linkify"),
         ("/html_anchor", "html anchor"),
         ("/the_world_s_countries_and_us", "the world's countries and us"),
        ],
    )


application = default_app()

if __name__ == '__main__':
    run(
        host='localhost',
        port=8081,
        reloader=True,
        debug=True,
    )
o