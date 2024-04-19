import pyxel

pyxel.init(200,200)
pyxel.cls(7)
for i in range(11):
    for j in range(11):
        bigI=i*20
        bigJ=j*20
        pyxel.line(bigI,0,bigJ,200,0)
pyxel.show()

#00:51