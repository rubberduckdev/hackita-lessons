'''
Hackita lessons
'''

from bottle import route, default_app, run

@route('/<somesuch>')
def hello(somesuch):
    return "Hello from bottle! :-)" + "<br /> " + somesuch

application = default_app()

if __name__ == '__main__':
    run(
        host='localhost',
        port=8080,
        reloader=True,
    )
