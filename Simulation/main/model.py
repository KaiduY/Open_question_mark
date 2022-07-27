from arm import arm
from joint import joint

class model:
    
    def __init__(self, normal_lenght):
        self.b1 = arm(normal_lenght)
        self.b2 = arm(normal_lenght)
        self.b3 = arm(normal_lenght)
        self.b4 = arm(normal_lenght)
        self.j1 = joint(self.b1, self.b2)
        self.j2 = joint(self.b2, self.b3)
        self.j3 = joint(self.b3, self.b4)
        self.start = (0,0,0,0)
        self.mv = (0,0,0,0,0)
    
    def setStartingPossition(self, x, y, z, a=0):
        self.start = (x, y, z, a)
        
    def move(self, s0, s1, s2, s3):
        self.mv = (s0, s1, s2, s3)
        
    def update():
        x,y,z,_ = self.start
        translate(x,y,z)
        
        
        
