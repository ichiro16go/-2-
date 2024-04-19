import pyxel

pyxel.init(200, 200)

ballx = pyxel.rndi(0,200)
bally = pyxel.rndi(0,200)
angle = pyxel.rndi(30,150)
vx = pyxel.cos(angle)  
vy = pyxel.sin(angle) 
col1 = pyxel.rndi(0,14)
col2 = pyxel.rndi(0,14) 
padx = 100
gear = 1
score=0

def direction_controller(ball, velocity):
    if ball >= 200 or ball <= 0:
        velocity *= -1 
    return velocity

def gear_change(gear,bally):
    if  bally <= 0:
        gear *=1.2
    return gear

def soundController(ballx,bally,padx):
    if bally>=200:
        if ballx>=padx-20 and ballx<=padx+20:
            pyxel.play(0,0)
        else:
            pyxel.play(0,3)

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
    soundController(ballx,bally,padx)
    padx = pyxel.mouse_x


def draw():
    global ballx, bally, padx ,score,col1
    
    result = "score:"+str(score)
    pyxel.cls(7)
    pyxel.text(0,10,result,1)
    pyxel.circ(ballx, bally, 10, col1)
    pyxel.rect(padx - 20, 195, 40, 5,col1)

pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.run(update, draw)

#03:32