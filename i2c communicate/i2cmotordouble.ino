#include <Wire.h>
#include <Servo.h>

#define Pin2 2
#define Pin3 3
#define PWMA 9
#define AIN2 8
#define AIN1 7
#define STBY 6

#define PWMB 10
#define BIN2 11
#define BIN1 12


int Duration = 3;
int pos = 0;
int Angle = 0;

volatile int counter0 = 0;
volatile int counter1 = 0;
int long prevTime, curTime;

int ledState = 0;
volatile int SpeedA = 200, SpeedB = 200;
const int Address = 0x50; 

void setup()
{
  Serial.begin(9600);
  Wire.begin(Address);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(sendData);
  
  pinMode(Pin2, INPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(Pin3, INPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(STBY, OUTPUT);

  attachInterrupt(digitalPinToInterrupt(Pin2), interruptFunction0, CHANGE);
  attachInterrupt(digitalPinToInterrupt(Pin3), interruptFunction1, CHANGE);
  
  digitalWrite(AIN1,HIGH);
  digitalWrite(AIN2,LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2,HIGH);
  digitalWrite(STBY, HIGH); // Set STBY pin to HIGH to enable the motor driver

  prevTime = millis(); 
}

void receiveEvent(int bytes) {
  ledState = Wire.read();
  Serial.print("Receive Data : ");
  Serial.println(ledState);
}

void loop()
{
   SpeedA = ledState;
   SpeedB = ledState;
   delay(Duration);
   Serial.print("counter0 = ");
   Serial.print(counter0);
   Serial.print("counter1 = ");
   Serial.print(counter1);
   int del = counter0 - counter1;

   if(del >= 0){SpeedA = SpeedA*0.99;}
   else{SpeedA = SpeedA * 1.01;} 

   Serial.print("del = ");
   Serial.print(del);
   Serial.print("SpeedA = ");
   Serial.print(SpeedA);
   Serial.print("SpeedB = ");
   Serial.println(SpeedB);

   analogWrite(PWMA, SpeedA);
   analogWrite(PWMB, SpeedB);
 
   counter0 = 0;
   counter1 = 0;
}

void interruptFunction0()
{
   counter0++;
}

void interruptFunction1()
{
   counter1++;
}

void sendData(){
    Wire.write(ledState);
}