import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)
x=[0,0]
y=[0,0]
count=0

def update():
    global x,y,count
    if pyxel.btnp(pyxel.KEY_SPACE):
        count+=1
        if count%2==1:
            x[0]=pyxel.mouse_x
            y[0]=pyxel.mouse_y
            print(x[0],y[0])
        elif (count%2==0)and(count>0):
            x[1]=pyxel.mouse_x
            y[1]=pyxel.mouse_y
            print(x[1],y[1])
        else:
            pyxel.cls(7)
        
        
def draw():
    global x, y, count
    pyxel.cls(7)
    if count%2==1:
        pyxel.line(x[0],y[0],pyxel.mouse_x,pyxel.mouse_y,0)
    else:
        pyxel.line(x[0],y[0],x[1],y[1],0)
        
pyxel.run(update,draw)

#07:37