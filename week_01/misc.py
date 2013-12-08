# encoding: utf-8

"""
Created on Nov 23, 2013

@author: Yuval Langer
"""


import textwrap



assert dedentstrip((lambda: ""))() == ""

assert dedentstrip(lambda: """
    <form action="/bottles" method="post">
        Number of bottles: <input name="n" type="number" />
        <input value="Break some bottles" type="submit" />
    </form>
    """)() == """<form action="/bottles" method="post">
    Number of bottles: <input name="n" type="number" />
    <input value="Break some bottles" type="submit" />
</form>"""
