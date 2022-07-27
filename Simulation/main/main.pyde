from model import model
import sys

model = model(50)

def setup():
    global model
    size(512, 512, P3D)
    model.setStartingPossition(200, 300, 0)
    model.setStartingPossitionJoints(30, 20, 20, 20)
    #print(b1.lenght)
    
i = 0

def draw():
    global i
    background(220)
    lights()
    #model.moveM(i,20,20,20)
    model.manarie(10,100,i)
    model.fwkinematics()
    i=i+0.1
    #print(i)
    i=min(i, 200)

    

    
