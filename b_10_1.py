import pyxel

pyxel.init(200, 200)

ballx = [pyxel.rndi(0,200),pyxel.rndi(0,200),pyxel.rndi(0,200)]
bally = [pyxel.rndi(0,200),pyxel.rndi(0,200),pyxel.rndi(0,200)]
angle = [pyxel.rndi(30,150),pyxel.rndi(30,150),pyxel.rndi(30,150)]
vx = [pyxel.cos(angle[0]),pyxel.sin(angle[1]),pyxel.sin(angle[2])]  
vy = [pyxel.sin(angle[0]),pyxel.sin(angle[1]),pyxel.sin(angle[2])]
col =[0,0,0] 
padx = 100
# gear = 1
score=0

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

# def gear_change(gear,bally):
#     if  bally <= 0:
#         gear *=1.2
#     return gear

def soundController(ballx,bally,padx):
    if bally>=200:
        if ballx>=padx-20 and ballx<=padx+20:
            pyxel.play(0,0)
        else:
            pyxel.play(0,3)

def countScore(ballx,bally,padx):
    global score
    if bally>=200:
        if ballx>=padx-20 and ballx<=padx+20:
            score += 1000 
    

def update():
    global ballx, bally, vx, vy, padx,score
    
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
    global ballx, bally, padx ,score,col
    
    result = "score:"+str(score)
    pyxel.cls(7)
    pyxel.text(0,10,result,1)
    pyxel.circ(ballx[0], bally[0], 10, col[0])
    pyxel.circ(ballx[1], bally[1], 10, col[0])
    pyxel.circ(ballx[2], bally[2], 10, col[0])
    pyxel.rect(padx - 20, 195, 40, 5,col[1])

pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.run(update, draw)

#11:27