import pyxel

pyxel.init(200, 200)

ballx = [pyxel.rndi(0,200),pyxel.rndi(0,200),pyxel.rndi(0,200)]
bally = [pyxel.rndi(0,200),pyxel.rndi(0,200),pyxel.rndi(0,200)]
angle = [pyxel.rndi(30,150),pyxel.rndi(30,150),pyxel.rndi(30,150)]
vx = [pyxel.cos(angle[0]),pyxel.sin(angle[1]),pyxel.sin(angle[2])]  
vy = [pyxel.sin(angle[0]),pyxel.sin(angle[1]),pyxel.sin(angle[2])]
col =[0,0,0] 
padx = 100
life=0

def colorSelector():
    global col
    for i in range(3):
        col[i]=pyxel.rndi(0,14)
    while col[0]!=col[1]:
        col[1]=pyxel.rndi(0,14)
    while col[0]!=col[2] and col[1]!=col[2]:
        col[2]=pyxel.rndi(0,14)
        
def direction_controller(ball, velocity):
    if ball >= 200 or ball <= 0:
        velocity *= -1 
    return velocity


def soundController(ballx,bally,padx):
    if bally>=200:
        if ballx>=padx-20 and ballx<=padx+20:
            pyxel.play(0,0)
        else:
            pyxel.play(0,3)

def countScore(ballx,bally,padx):
    global life
    if bally>=200:
        if ballx<=padx-20 or ballx>=padx+20:
            life += 1
    
def gameover():
    global life
    result = "life:"+str(10-life)
    if life>=10:
        pyxel.cls(7)
        pyxel.text(100,100,"GameOver",1)
    else:
        pyxel.cls(7)
        pyxel.text(0,10,result,1)
        pyxel.circ(ballx[0], bally[0], 10, col[0])
        pyxel.circ(ballx[1], bally[1], 10, col[1])
        pyxel.circ(ballx[2], bally[2], 10, col[2])
        pyxel.rect(padx - 20, 195, 40, 5,0)

def update():
    global ballx, bally, vx, vy, padx,life,living
    countScore(ballx[0],bally[0],padx)
    countScore(ballx[1],bally[1],padx)
    countScore(ballx[2],bally[2],padx)
    for i in range(3):    
        ballx[i] += vx[i]
        bally[i] += vy[i]
        vx[i] = direction_controller(ballx[i], vx[i])
        vy[i] = direction_controller(bally[i], vy[i])
        soundController(ballx[i],bally[i],padx)
    padx = pyxel.mouse_x


def draw():
    global ballx, bally, padx ,life, col,living
    gameover()

pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.run(update, draw)

#11:27