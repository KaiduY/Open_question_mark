
class joint{
  arm arm1 = null;
  arm arm2 = null;
  joint(arm arm1, arm arm2)
  {
    this.arm1 = arm1;
    this.arm2 = arm2;
  }
  
  void rot(float ang){
    float x = arm1.getOriginX();
    float y = arm1.getOriginY();
    float z = arm1.getOriginZ();
    float a = arm1.getOriginA();
    float b = arm1.getOriginB();
    float l1 = arm1.getLenght();
    float l2 = arm2.getLenght();
    float z2 = z - l1/2*sin(radians(a)) - l2/2*sin(radians(a+ang));
    float y2 = y - l1/2*cos(radians(a)) - l2/2*cos(radians(a+ang));
    arm2.pos(x,y2,z2,a+ang,0);
  }
  

  
}
