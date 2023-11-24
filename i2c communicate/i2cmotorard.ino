#include <Wire.h>
#include <Servo.h>
#define Pin2 2
#define PWMA 9
#define AIN2 8
#define AIN1 7
#define STBY 6

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int Angle = 0;



volatile int counter = 0;
int long prevTime, curTime;


int LED = 7;
int ledState = 0;
int Speed = ledState;
const int Address = 0x50; 

void setup()
{
  Serial.begin(9600);
  Wire.begin(Address);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(sendData);
  myservo.attach(4);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  pinMode(Pin2, INPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(STBY, OUTPUT);
  digitalWrite(STBY, HIGH);
  attachInterrupt(0,interruptFunction,CHANGE);

analogWrite(PWMA, Speed);
digitalWrite(AIN1, HIGH);
digitalWrite(AIN2, LOW);

prevTime = millis(); 
}

void receiveEvent(int bytes) {
  ledState = Wire.read();
  Serial.print("Receive Data : ");
  Serial.println(ledState);
}

void loop()
{
  curTime = millis();
  int del = curTime - prevTime;

while(del >= 3000){
  Serial.print("tinme = ");
  Serial.print(del);
  Serial.print("counter = ");
  Serial.println(counter);
  prevTime = curTime;
  counter = 0;
  del = 0;
}
  
}
void interruptFunction(){
  counter++;
}
void sendData(){
  
    Wire.write(ledState);
}