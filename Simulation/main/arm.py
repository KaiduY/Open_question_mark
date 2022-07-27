class arm:
    
    def __init__(self, lenght = 10):
        self.lenght = lenght
        self.surface = 10
        self.xyzab = (0,0,0,0,0)

        
    def pos(self, x, y, z, a, b):
        self.xyzab = (x,y,z,a,b)
        pushMatrix()
        translate(x, y, z)
        rotateX(radians(a))
        rotateY(radians(b))
        box(self.surface, self.lenght, self.surface)
        popMatrix()
    
    def getOrigin(self):
        return self.xyzab
    
    def getLenght(self):
        return self.lenght
    
    def getSurface(self):
        return self.surface
    
