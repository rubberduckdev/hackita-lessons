#! /usr/bin/env python
# encoding: utf-8

from bottle import cgi # get, post, request, cgi

def html_table(table_list):
    html_table_string = "<table>"
    for line in table_list:
        html_table_string += "<tr>"
        for item in line:
            html_table_string += "<td>" + cgi.escape(item) + "</td>"
        html_table_string += "</tr>"
    html_table_string += "</table>"
    return html_table_string

@get("/html_table")
def html_table_get():
    return "Ain't nobody here but us chickens."