import pyxel

pyxel.init(200, 200)

a = 0
b = 0
c = 0

def update():
    global a, b
    if a >= 200:
        a = 0
    if pyxel.btnp(pyxel.KEY_SPACE):
        switch()
    if c%4==1:
        a+=1
        b+=1
    elif c%4==2:
        a+=1
        b-=1
    elif c%4==3:
        a-=1
        b-=1
    else:
        a-=1
        b+=1


def switch():
    global c
    # b をトグル
    c += 1

def draw():
    global a,b
    pyxel.cls(7)
    pyxel.circ(a,b,10,0)


pyxel.run(update,draw)

#03:45