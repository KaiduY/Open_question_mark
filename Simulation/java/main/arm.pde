class arm{
  float lenght = 10, surface=10;
  float xyzab[] = {0,0,0,0,0};
  arm(float lenght)
  {
    this.lenght = lenght;
  }
  
  void pos(float x, float y, float z, float a, float b){
    xyzab[0]=x;
    xyzab[1]=y;
    xyzab[2]=z;
    xyzab[3]=a;
    xyzab[4]=b;
    pushMatrix();
    translate(x,y,z);
    rotateX(radians(a));
    rotateY(radians(b));
    box(surface, lenght, surface);
    popMatrix();
  }
  
  float getOriginX(){
    return xyzab[0];
  }
  
  float getOriginY(){
    return xyzab[1];
  }
  
  float getOriginZ(){
    return xyzab[2];
  }
  
  float getOriginA(){
    return xyzab[3];
  }
  
  float getOriginB(){
    return xyzab[4];
  }
  
  float getLenght(){
    return lenght;
  }
  
  float getSurface(){
    return surface;
  }
  
}
