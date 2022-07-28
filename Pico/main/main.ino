#include <Servo.h>
#define S0 5
#define S1 4
#define S2 2
#define S3 3
#define FLAG 6

char recchr;
String mes, buf;
float x, y, z;
float ik0, ik1;

//Arm parameters
float l1 = 85;
float l2 = 65;
float dtt = 10000;
float off = 60;

Servo flag;
Servo s[4];
int initial_joints[] = {120, 90, 90, 90};

const float pi = 3.14159267;

float degres(float radins) {
  return radins / 2 / pi * 360;
}

void ik2dof(float x, float y) {
  if (x == 0) x = 0.01;
  float a2 = acos(+(pow(x, 2) + pow(y, 2) - pow(l1, 2) - pow(l2, 2)) / (2 * l1 * l2));
  float a1 = atan(y / x) - atan(l2 * sin(a2) / (l1 + l2 * cos(a2)));
  ik0 = degres(a1);
  ik1 = degres(a2);
}

void manarie(float x, float y, float z) {
  if (y == 0) y = 0.01;
  float a0 =  degres(atan(z / y));
  float l = sqrt(pow(y, 2) + pow(z, 2));
  ik2dof(x, l);
  //ik2dof(x, y);
  float a1 = ik0;
  float a2 = ik1;
  float a3 = 90 - a1 - a2;
  /*
    a0 = max(a0, -dtt);
    a0 = min(a0, dtt);
    a1 = max(a1, -dtt);
    a1 = min(a1, dtt);
    a2 = max(a2, -dtt);
    a2 = min(a2, dtt);
    a3 = max(a3, -dtt);
    a3 = min(a3, dtt);
  */
  Serial.print(a1);
  Serial.print(" ");
  Serial.print(a2);
  Serial.print(" ");
  Serial.print(a3);
  if(!(isnan(a0) || isnan(a1) || isnan(a2) || isnan(a3))){
  s[0].write(a0 + off);
  s[1].write(a1 + off);
  s[2].write(a2 + off);
  s[3].write(a3 + off);
  }
  delay(100);
}

void setup() {
  Serial.begin(115200);
  flag.attach(FLAG);
  s[0].attach(S0);
  s[1].attach(S3);
  s[2].attach(S2);
  s[3].attach(S1);

  flag.write(80);
  for (int i = 0; i < 4; i++)
    //s[i].write(initial_joints[i]);
    s[i].writeMicroseconds(1500);
  //delay(10000000);
  delay(100);
  //testServo();

}

bool gcode(String mes)
{
  String param = "";
  bool moveArm = false;
  //float x, y, z;
  for (int i = 0; i < mes.length(); i++)
  {

    param += mes[i];
    if (mes[i] == ' ' || mes[i] == '\n')
    {
      param.remove(param.length() - 1);
      if (param == "G1")
        moveArm = true;
      else if (param[0] == 'X')
      {
        param.remove(0, 1);
        x = param.toFloat();
      }
      else if (param[0] == 'Y')
      {
        param.remove(0, 1);
        y = param.toFloat();
      }
      else if (param[0] == 'Z')
      {
        param.remove(0, 1);
        z = param.toFloat();
      }

      param = "";
    }
  }
  return moveArm;
}
void testServo()
{
  for (int i = 0; i < 4; i++) {
    s[i].write(initial_joints[i] - 20);
    delay(2000);
    s[i].write(initial_joints[i] + 20);
    delay(5000);
  }
}
float i = 0;


void loop() {

  
  if (Serial.available()) {
    recchr = Serial.read();
    buf = buf + recchr;
    if (recchr == '\n')
    {
      mes = buf;
      buf = "";
      if (gcode(mes))
      {
        Serial.println("ok");
        manarie(x, y, z);
      }

    }

  }
   //manarie(100, 80, 20);
   //i=i+1;
   //delay(100);
   //if(i==100) i=0;

}
