import pyxel

pyxel.init(200, 200)

ballx = 100
bally = 100
vx = 0.5  # cos 60 degree
vy = 0.866  # sin 60 degree
padx = 100
gear = 1

def direction_controller(ball, velocity):
    if ball >= 200 or ball <= 0:
        velocity *= -1 
    return velocity

def gear_change(gear,bally):
    if  bally <= 0:
        gear *=2
    return gear

def update():
    global ballx, bally, vx, vy, padx,gear

    ballx += vx
    bally += vy 

    vx = direction_controller(ballx, vx)
    vy = direction_controller(bally, vy)* gear_change(gear,bally)

    padx = pyxel.mouse_x

def draw():
    global ballx, bally, padx
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx - 20, 195, 40, 5, 14)

pyxel.run(update, draw)
