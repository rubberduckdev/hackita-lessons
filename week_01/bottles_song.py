# encoding: utf-8

""" Handling the bottle song """

from bottle import post, get, request


def bottles(bottles_max):
    """ number -> [song line] """
    def bottles_(bottles_num):
        if bottles_num <= 0:
            return [
                "No more bottles of beer on the wall, no more bottles of beer.",
                "Go to the store and buy some more, {bottlesmax} bottles of beer on the wall.".format(bottlesmax=bottles_max),
             ]
        else:
            return [
                "{bottlenum} bottles of beer on the wall, {bottlenum} bottles of beer.".format(bottlenum=bottles_num),
                "Take one down, pass it around, {bottlenum} bottles of beer on the wall...".format(bottlenum=bottles_num - 1),
            ] + bottles_(bottles_num - 1)
    return bottles_(bottles_max)


@get('/bottles')
def bottle_get():
    return """
        <form action="/bottles" method="post">
            Number of bottles: <input name="n" type="number" />
            <input value="Break some bottles" type="submit" />
        </form>
    """


@post('/bottles')
def bottle_post():
    return bottle_get() + '<br />'.join(
        bottles(int(request.forms.get('n')))
    )


def asserts():
    assert bottles(2) == [
        "2 bottles of beer on the wall, 2 bottles of beer.",
        "Take one down, pass it around, 1 bottles of beer on the wall...",
        "1 bottles of beer on the wall, 1 bottles of beer.",
        "Take one down, pass it around, 0 bottles of beer on the wall...",
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, 2 bottles of beer on the wall.",
    ]
    assert bottles(1) == [
        "1 bottles of beer on the wall, 1 bottles of beer.",
        "Take one down, pass it around, 0 bottles of beer on the wall...",
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, 1 bottles of beer on the wall.",
    ]
    assert bottles(0) == [
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, 0 bottles of beer on the wall.",
    ]
    '''assert bottle_get() == """<form action="/bottles" method="post">
    Number of bottles: <input name="n" type="number" />
    <input value="Break some bottles" type="submit" />
</form>"""'''

asserts()
