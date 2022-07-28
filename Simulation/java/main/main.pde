import processing.serial.*;

model model = new model(50);
Serial ser = new Serial(this, Serial.list()[0], 115200);

PFont f;

String typing = "";

float x=50,  y=50, z=50;
float speed = 5;

void setup(){
    size(512, 512, P3D);
    model.setStartingPossition(100, 150, 0);
    model.setStartingPossitionJoints(30, 20, 20, 20);
    f = createFont("Arial", 16);
}

float i = 0;

void sendM(String mes)
{
  ser.write(mes+'\n');
  String conf = ser.readStringUntil('\n');
  println(mes);
  //String ok ="ok\n";
  //if(conf[0] == 'o') print("1");
  if(conf == null || conf.substring(0,2).equals("ok")==false){
    //sendM(mes);
    print("The message was not received!");
  }
}

long start = millis();
void draw(){
    background(220);
    textFont(f);
    //fill(0);
    text(typing, 100, 100);
    lights();
    scale(2);
    model.manarie(x,y,z);
    if(millis()-start > 100)
    {
      sendM("G1 X"+str(int(x))+" Y"+str(int(y)) + " Z"+str(int(z))+"\n");
      start = millis();
    }
    //#model.moveM(i,20,20,20);
    //model.manarie(50,100,i);
    //#model.fwkinematics();
    //i=i+0.1;
    //#print(i);
    //i=min(i, 200);
}
void getMouse()
{
  z = map(mouseX, 0, 512, 140, 0);
  y = map(mouseY, 0, 512, 140, 0);
  println(mouseY);
}
void keyPressed() {

  if (key == '\n' ) {
    sendM(typing);
    typing = ""; 
  } else {
    typing = typing + key; 
  }
}

void mouseWheel(MouseEvent event) {
  float e = event.getCount();
  x+= e*speed*(-1);
}

void mouseMoved() {
  getMouse();

}
