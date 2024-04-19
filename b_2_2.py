import pyxel

pyxel.init(200,200)
pyxel.cls(7)
for i in range (21):
    j = i*10
    pyxel.line(j,0,0,200-j,0)
pyxel.show()
#00:31