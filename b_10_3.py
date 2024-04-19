import pyxel

# 最初はボール1個で、ボールを10個受け取るとボールが2個に増えてスピードがゆっくりに戻り、さらに10個受け取るとボールが3個に増えてまたスピードがゆっくりに戻り、と繰り返すようにしなさい。

pyxel.init(200, 200)

ballx = [pyxel.rndi(0,200)]
bally = [pyxel.rndi(0,200)]
angle = [pyxel.rndi(30,150)]
vx = [pyxel.cos(angle[0])]  
vy = [pyxel.sin(angle[0])]
color= [pyxel.rndi(0,15)]
padx = 100
gear = 1
ballsum=1
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
    global score
    if bally>=200:
        if ballx>=padx-20 and ballx<=padx+20:
            score += 1000 
    
def createNewBall(score):
    global ballx,bally,angle,vx,vy,color,ballsum
    if score>1000*ballsum :
        ballsum +=1
        ballx.append(pyxel.rndi(0,200))
        bally.append(pyxel.rndi(0,200))
        angle.append(pyxel.rndi(30,150))
        vx.append(pyxel.cos(angle[ballsum-1]))
        vy.append(pyxel.sin(angle[ballsum-1]))
        color.append(pyxel.rndi(0,15))
        
        
def display(ballsum,score):
    result = "score:"+str(score)
    pyxel.cls(7)
    pyxel.text(0,10,result,1)
    for i in range(ballsum-1):
        pyxel.circ(ballx[i],bally[i],10,color[i])
    pyxel.rect(padx-20,195,40,5,1)

def update():
    global ballx, bally, vx, vy, padx,score
    for i in range (ballsum):
        ballx[i] += vx[i]
        bally[i] += vy[i]
        vx[i] = direction_controller(ballx[i], vx[i])
        vy[i] = direction_controller(bally[i], vy[i])*gear_change(gear,bally[i])
        soundController(ballx[i],bally[i],padx)
        countScore(ballx[i],bally[i],padx)
        gear_change(gear,bally[i])
    padx = pyxel.mouse_x
    createNewBall(score)

def draw():
    global ballx, bally, padx ,score,col
    display(ballsum,score)

pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.run(update, draw)

#11:27