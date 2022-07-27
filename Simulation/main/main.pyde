from model import model

model = model(50)

def setup():
    global model
    size(512, 512, P3D)
    model.setStartingPossition(100, 100, 0)
    model.setStartingPossitionJoints(30, 20, 20, 20)
    #print(b1.lenght)
    
i = 0

def draw():
    global i
    background(220)
    lights()

    

    
