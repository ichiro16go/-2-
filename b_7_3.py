import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)
x=[0]
y=[0]
count=0

def update():
    global count
    if pyxel.btnp(pyxel.KEY_SPACE):
        count+=1

def draw():
    global x,y,count
    pyxel.cls(7)
    if pyxel.btn(pyxel.KEY_SPACE):
        pyxel.line(0,0,pyxel.mouse_x,pyxel.mouse_y,0)
        for i in range(count):
            pyxel.line(0,0,x[i],y[i],0)
    elif pyxel.btnr(pyxel.KEY_SPACE):
        x.append(pyxel.mouse_x)
        y.append(pyxel.mouse_y)
    else:
        for i in range(count+1):
            pyxel.line(0,0,x[i],y[i],0)
        
pyxel.run(update,draw)

#05:02