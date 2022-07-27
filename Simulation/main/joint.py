class joint:
    def __init__(self, arm1, arm2, type='x'):
        """
        arm1 = father/fixed
        arm2 = child/moveble
        """
        self.arm1 = arm1
        self.arm2 = arm2
        self.type = type
        
    def rot(self, ang):
        if self.type == 'x':
            x, y, z, a, b = self.arm1.getOrigin()
            l1 = self.arm1.getLenght()
            l2 = self.arm2.getLenght()
            z2 = z - l1/2*sin(radians(a)) - l2/2*sin(radians(a+ang))
            y2 = y - l1/2*cos(radians(a)) - l2/2*cos(radians(a+ang))
            
            #y2 = y-l1/2- l2/2#x + l1/2*sin(radians(a)) + l2/2*sin(radians(a+ang))
            #pushMatrix()
            #rotateY(radians(b))
            self.arm2.pos(x,y2,z2,a+ang,0)
            #popMatrix()
            
        """This type does not work yet
        elif self.type == 'y':
            x, y, z, a, b = self.arm1.getOrigin()
            l1 = self.arm1.getLenght()
            l2 = self.arm2.getLenght()
            s = self.arm1.getSurface()
            z2 = z #- s/2*sin(radians(b)) - s/2*sin(radians(b+ang))
            x2 = x #- s/2*sin(radians(b)) - s/2*sin(radians(b+ang))
            y2 = y - l1/2 - l2/2
            #y2 = y-l1/2- l2/2#x + l1/2*sin(radians(a)) + l2/2*sin(radians(a+ang))
            self.arm2.pos(x2,y2,z2,a,b+ang)
        """
            
