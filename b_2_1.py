import pyxel

pyxel.init(200,200)
pyxel.cls(7)
for i in range(10):
    xalin = i*10
    pyxel.line(xalin,0,100+xalin,200,0)
pyxel.show() 

#00:42