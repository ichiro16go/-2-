import pyxel

pyxel.init(200, 200)

a = 0
b = True

def update():
    global a, b
    a += 1
    if a >= 200:
        a = 0
    if a == 0:
        b = not b

def draw():
    global a, b
    pyxel.cls(7)
    if b:
        pyxel.circ(a, a, 10, 0)
    else:
        pyxel.circ(200 - a, 200 - a, 10, 0)

pyxel.run(update, draw)

#03:12