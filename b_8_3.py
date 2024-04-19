import pyxel

pyxel.init(200, 200)

ballx = 100
bally = 100
vx = 0.5  # cos 60 degree
vy = 0.866  # sin 60 degree
padx = 100
gear = 1
score=0

def direction_controller(ball, velocity):
    if ball >= 200 or ball <= 0:
        velocity *= -1 
    return velocity

def gear_change(gear,bally):
    if  bally <= 0:
        gear *=2
    return gear

def countScore(ballx,bally,padx):
    if bally>=200:
        if ballx>=padx-20 and ballx<=padx+20:
            return 1000

def update():
    global ballx, bally, vx, vy, padx,gear,score
    ballx += vx
    bally += vy
    if bally>=200:
        if ballx>=padx-20 and ballx<=padx+20:
            score +=1000
    vx = direction_controller(ballx, vx)
    vy = direction_controller(bally, vy)* gear_change(gear,bally)
    padx = pyxel.mouse_x

def draw():
    global ballx, bally, padx ,score
    pyxel.cls(7)
    pyxel.text(0,0,str(score),1)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx - 20, 195, 40, 5, 14)

pyxel.run(update, draw)
