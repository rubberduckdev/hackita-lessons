'''
Hackita lessons
'''

from bottle import route, default_app, run

@route('/<somesuch>')
def hello(somesuch):
    return "Hello from bottle! :-)" + "<br /> " + somesuch

def bottles(n):
    return [
        sentence
        for i in range(n, -1, -1)
        for sentence in [
            '{bottlenum} bottles of beer on the wall, {bottlenum} bottles of beer.'.format(bottlenum=n),
            'Take one down, pass it around, {bottlenum} bottles of beer on the wall...'.format(bottlenum=n-1),
        ]
    ] + [
        "No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.",
    ]

@route('/bottles/<n:int>')
def bottle_bottles(n):
    return '<br />'.join(bottles(n))
    

application = default_app()

if __name__ == '__main__':
    run(
        host='localhost',
        port=8080,
        reloader=True,
    )
