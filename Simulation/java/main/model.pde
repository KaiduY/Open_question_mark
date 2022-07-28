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
  float ik0 = 0;
  float ik1 = 0;

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
  
    void setStartingPossition(float x, float y, float z){
        start[0] = x;
        start[1] = y;
        start[2] = z;
    }
    
    void setStartingPossitionJoints(float s0, float s1, float s2, float s3){
        startj[0] = s0;
        startj[1] = s1;
        startj[2] = s2;
        startj[3] = s3;
        init();
    }
        
    void moveM(float s0, float s1, float s2, float s3){
        mv[0] = s0;
        mv[1] = s1;
        mv[2] = s2;
        mv[3] = s3;
        update();
    }
        
    void init(){
        float x = start[0];
        float y = start[1];
        float z = start[2];
        
        float s0 = startj[0];
        float s1 = startj[1];
        float s2 = startj[2];
        float s3 = startj[3];
        
        translate(x,y,z);
        rotateY(s0);
        b1.pos(0,0,0,0,0);
        j1.rot(s1);
        j2.rot(s2);
        j3.rot(s3);
    }
        
    void update(){
        float x = start[0];
        float y = start[1];
        float z = start[2];
        float s0 = mv[0];
        float s1 = mv[1];
        float s2 = mv[2];
        float s3 = mv[3];
        translate(x,y,z);
        rotateY(s0);
        b1.pos(0,0,0,0,0);
        j1.rot(s1);
        j2.rot(s2);
        j3.rot(s3);
    }
        
    void fwkinematics(){
        float l1 = b1.getLenght();
        float l2 = b2.getLenght();
        float l3 = b3.getLenght();
        float l4 = b4.getLenght();
        float s0 = mv[0];
        float s1 = mv[1];
        float s2 = mv[2];
        float s3 = mv[3];
        
        float rx = l2 * cos(radians(s1)) + l3 * cos(radians(s2)) + l4 * cos(radians(s3));
        float y = l1 + l2 * sin(radians(s1)) + l3 * sin(radians(s2)) + l4 * sin(radians(s3));
        float z = rx * sin(radians(s0));
        float x = rx * cos(radians(s0));
        //print(x,y,z)
    }
    
    void ik2dof(float x, float y){
        float l1 = 80;//#self.
        float l2 = 80;
        try{
            float a2 = acos((pow(x,2)+pow(y,2)-pow(l1,2)-pow(l2,2))/(2*l1*l2));
            float a1 = atan(y/x) - atan(l2*sin(a2)/(l1+l2*cos(a2)));
            ik0 = degrees(a1);
            ik1 = degrees(a2);
        }
        catch (Exception e){
            print("Cannot reach that posssition sorry!");
        }
            
    }
            
        
    
    void manarie(float x,float y,float z){
        float dt = 90;
        y = y==0 ? 0.01 : y;
        float a0 = atan(z/y);
        float l = sqrt(pow(y,2) + pow(z,2));
        ik2dof(x,l);
        float a1 = ik0;
        float a2 = ik1;
        float a3 = 90-a1-a2;
        a0 = max(a0, -dt);
        a0 = min(a0, dt);
        a1 = max(a1, -dt);
        a1 = min(a1, dt);
        a2 = max(a2, -dt);
        a2 = min(a2, dt);
        a3 = max(a3, -dt);
        a3 = min(a3, dt);
        moveM(a0,a1,a2,a3);
    }

  
}
