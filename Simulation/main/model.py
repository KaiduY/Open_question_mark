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
        
    def moveM(self, s0, s1, s2, s3):
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
        
    def fwkinematics(self):
        l1 = self.b1.getLenght()
        l2 = self.b2.getLenght()
        l3 = self.b3.getLenght()
        l4 = self.b4.getLenght()
        s0, s1, s2, s3 = self.mv
        
        rx = l2 * cos(radians(s1)) + l3 * cos(radians(s2)) + l4 * cos(radians(s3))
        y = l1 + l2 * sin(radians(s1)) + l3 * sin(radians(s2)) + l4 * sin(radians(s3))
        z = rx * sin(radians(s0))
        x = rx * cos(radians(s0))
        print(x,y,z)
    
    def ik2dof(self, x, y):
        l1 = 80#self.
        l2 = 80
        try:
            a2 = acos((x**2+y**2-l1**2-l2**2)/(2*l1*l2))
            a1 = atan(y/x) - atan(l2*sin(a2)/(l1+l2*cos(a2)))
            return (degrees(a1), degrees(a2))
        except:
            print('Cannot reach that posssition sorry!')
            return (0,0)
            
        
    
    def manarie(self,x,y,z):
        #z=80
        if y==0: y=0.001
        a0 = atan(z/y)
        l = sqrt(y**2 + z**2) 
        a1, a2 = self.ik2dof(x,l)
        a3 = 90-a1-a2
        self.moveM(a0,a1,a2,a3)
        
        #print(x,y,z)
        
        
        
        
        
