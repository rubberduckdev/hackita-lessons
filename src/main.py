'''
Hackita lessons
'''

from bottle import route, default_app, run, get, post, request
import itertools

@route('/<somesuch>')
def hello(somesuch):
    return "Hello from bottle! :-)" + "<br /> " + somesuch

def bottles(n):
    return itertools.chain((
        sentence
        for i in range(n, 0, -1)
        for sentence in (
            '{bottlenum} bottles of beer on the wall, {bottlenum} bottles of beer.'.format(bottlenum=i),
            'Take one down, pass it around, {bottlenum} bottles of beer on the wall...'.format(bottlenum=i-1),
            '<br />',
        )),
        [
         "No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.",
        ])

def bottles_html(n):
    return '<br />'.join(bottles(n))

@get('/bottles')
@get('/bottles/')
def bottle_get():
    return '''
    <br /><br />
        <form action="/bottles" method="post">
            Number of bottles: <input name="n" type="number" />
            <input value="Break some bottles" type="submit" />
        </form>
    '''
    
@get('/bottles/<n:int>')
def bottle_n(n):
    return bottles_html(n)

@post('/bottles')
def bottle_bottles():
    return bottles_html(int(request.forms.get('n'))) + bottle_get()
    

application = default_app()

if __name__ == '__main__':
    run(
        host='localhost',
        port=8080,
        reloader=True,
    )
