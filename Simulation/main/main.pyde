from arm import arm
from joint import joint

b1 = arm(50)
b2 = arm(50)
b3 = arm(100)
b4 = arm(200)
j1 = joint(b1,b2)
j2 = joint(b2,b3)
j3 = joint(b3,b4)

def setup():
    size(512, 512, P3D)
    #print(b1.lenght)
    
i = 0

def draw():
    global i
    background(220)
    lights()
    #translate(100, 100, 0)
    translate (200, 200, 0)
    rotateY(radians(i))
    b1.pos(0,0,0,0,0)
    j1.rot(20)
    j2.rot(90)
    j3.rot(-20)
    #rotateX(radians(i))
    #b1.update()
    #b2.update()
    i=i+1
    

    
