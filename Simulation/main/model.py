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
        self.start = (0,0,0)
        self.startj = (0,0,0,0)
        self.mv = (0,0,0,0,0)
    
    def setStartingPossition(self, x, y, z):
        self.start = (x, y, z)
    
    def setStartingPossitionJoints(self, s0, s1, s2, s3):
        self.startj = (s0, s1, s2, s3)
        self._init()
        
    def move(self, s0, s1, s2, s3):
        self.mv = (s0, s1, s2, s3)
        self.update()
        
    def _init(self):
        x,y,z = self.start
        s0, s1, s2, s3 = self.startj
        translate(x,y,z)
        rotateY(s0)
        self.b1.pos(0,0,0,0,0)
        self.j1.rot(s1)
        self.j2.rot(s2)
        self.j3.rot(s3)
        
    def update(self):
        x,y,z = self.start
        s0, s1, s2, s3 = self.mv
        translate(x,y,z)
        rotateY(s0)
        self.b1.pos(0,0,0,0,0)
        self.j1.rot(s1)
        self.j2.rot(s2)
        self.j3.rot(s3)
        
        
        
