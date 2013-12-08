#! /usr/bin/env python
# encoding: utf-8

"""
Created on Nov 23, 2013

@author: Yuval Langer
"""


from bottle import post, get, request, template


def multiplication_list(n):
    """ Number -> [[Number]] """
    return [[
        row_i * col_i
        for col_i in range(1, n + 1)
    ] for row_i in range(1, n + 1)]


@get("/multiplication_list")
def multiplication_list_get():
    return """
    <form action="/multiplication_list" method="post">
        <input name="number" type="number">
        <input value="Submit" type="submit">
    </form>
    """


@post("/multiplication_list")
def multiplication_list_post():
    num = request.forms.get("number")
    multlist = multiplication_list_dict(int(num))
    return template("""
    <table border=1>
    % for row in multiplication_list:
      <tr>
      % for num in row:
        <td>{{str(num)}}</td>
      % end
      </tr>
    % end
    </table>
    """, multiplication_list=multlist)


def asserts():
    assert multiplication_list(1) == [[1]]
    assert multiplication_list(2) == [[1, 2], [2, 4]]
    assert multiplication_list(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

asserts()