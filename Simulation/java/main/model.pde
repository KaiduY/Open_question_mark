class model{
  arm b1 = null;
  arm b2 = null;
  arm b3 = null;
  arm b4 = null;
  joint j1 = null;
  joint j2 = null;
  joint j3 = null;
  float start[] = {0,0,0};
  float startj[] = {0,0,0,0};
  float mv[] = {0,0,0,0,0};

  model(float normal_lenght)
  {
    b1 = new arm(normal_lenght);
    b2 = new arm(normal_lenght);
    b3 = new arm(normal_lenght);
    b4 = new arm(normal_lenght);
    j1 = new joint(b1, b2);
    j2 = new joint(b2, b3);
    j3 = new joint(b3, b4);
  }
  
    void setStartingPossition(float x, float y, float z):
        start[0] = x;
        start[1] = y;
        start[2] = z;
    
    void setStartingPossitionJoints(float s0, float s1, float s2, float s3):
        startj[0] = s0;
        startj[1] = s1;
        startj[2] = s2;
        startj[3] = s3;
        init()
        
    void moveM(self, s0, s1, s2, s3):
        self.mv = (s0, s1, s2, s3)
        self.update()
        
    void init(self):
        x,y,z = self.start
        s0, s1, s2, s3 = self.startj
        translate(x,y,z)
        rotateY(s0)
        self.b1.pos(0,0,0,0,0)
        self.j1.rot(s1)
        self.j2.rot(s2)
        self.j3.rot(s3)
        
    void update(self):
        x,y,z = self.start
        s0, s1, s2, s3 = self.mv
        translate(x,y,z)
        rotateY(s0)
        self.b1.pos(0,0,0,0,0)
        self.j1.rot(s1)
        self.j2.rot(s2)
        self.j3.rot(s3)
        
    void fwkinematics(self):
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
    
    void ik2dof(self, x, y):
        l1 = 80//#self.
        l2 = 80
        try:
            a2 = acos((x**2+y**2-l1**2-l2**2)/(2*l1*l2))
            a1 = atan(y/x) - atan(l2*sin(a2)/(l1+l2*cos(a2)))
            return (degrees(a1), degrees(a2))
        catch:
            print('Cannot reach that posssition sorry!')
            return (0,0)
            
        
    
    void manarie(self,x,y,z):
        dt = 90
        if y==0: y=0.001
        a0 = atan(z/y)
        l = sqrt(y**2 + z**2) 
        a1, a2 = self.ik2dof(x,l)
        a3 = 90-a1-a2
        a0 = max(a0, -dt)
        a0 = min(a0, dt)
        a1 = max(a1, -dt)
        a1 = min(a1, dt)
        a2 = max(a2, -dt)
        a2 = min(a2, dt)
        a3 = max(a3, -dt)
        a3 = min(a3, dt)
        self.moveM(a0,a1,a2,a3)
  

  
}
