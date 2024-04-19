import pyxel

pyxel.init(200,200)

ballx = 0
bally = 0
direction = True
vx = 0.5  # cos 60 degree
vy = 0.866 # sin 60 degree
padx = 100

def update():
    global ballx, bally, vx, vy, padx, direction
    if direction==True:
        ballx += vx
    else:
        ballx -=vx 
    bally += vy   
    padx = pyxel.mouse_x
    if bally >= 200:
        ballx = 100
        bally = 0
        
    if ballx >= 200 :
        direction = False
    elif ballx <= 0:
        direction = True
        
def draw():
    global ballx, bally, vx, vy, padx
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)

pyxel.run(update, draw)

#10:09