import pyxel

pyxel.init(200,200)
pyxel.cls(7)
for i in range(10):
    for j in range(10):
        k=(i+j)%2
        x=i*20
        y=j*20
        if k==0:
            pyxel.circ(10+x,10+y,10,1)
        else:
            pyxel.circ(10+x,10+y,10,2)
            
pyxel.show()

#02:12