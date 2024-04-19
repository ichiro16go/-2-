import pyxel

pyxel.init(200,200)
pyxel.cls(7)
for i in range(10):
    for j in range(10):
        k=i+j
        x=i*20
        y=j*20
        if k<5:
            pyxel.circ(10+x,10+y,10,1)
        elif 5<=k<9:
            pyxel.circ(10+x,10+y,10,2)
        elif 9<=k<14:
            pyxel.circ(10+x,10+y,10,3)
        else:
            pyxel.circ(10+x,10+y,10,4)
            
pyxel.show()

#01:02