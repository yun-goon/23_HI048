// 모터 테스트 아두이노

#define Pin2 2
#define PWMA 9
#define AIN2 8
#define AIN1 7
#define STBY 6

int Speed = 200; //
volatile int counter = 0;
int long prevTime, curTime;

void setup() {
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


void loop() {
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

