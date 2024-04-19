import pyxel


pyxel.init(200, 200)
pyxel.mouse(True)
x=0
y=0
def update():
    global x,y
    

def draw():
    global x,y
    pyxel.cls(7)
    if pyxel.btn(pyxel.KEY_SPACE):
        pyxel.line(0,0,pyxel.mouse_x,pyxel.mouse_y,0)
    elif pyxel.btnr(pyxel.KEY_SPACE):
        x=pyxel.mouse_x
        y=pyxel.mouse_y
    else:
        pyxel.line(0,0,x,y,0)
pyxel.run(update,draw)

#10:02