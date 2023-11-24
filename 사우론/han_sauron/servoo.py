import RPi.GPIO as GPIO
from time import sleep
import random

servoPin = 32 # 서보모터 핀 설정, pwm 사용
Detect = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)
pin7 = GPIO.PWM(servoPin, 50)
pin7.start(0)

def angleToDutyConvert(angle):  # 서보모터 pwm 제어
    dutyCycle = angle / 18 + 2.0
    if dutyCycle>22:
        dutyCycle=22
    if dutyCycle<0:
        dutyCycle=0
    GPIO.output(servoPin, GPIO.HIGH)
    pin7.ChangeDutyCycle(dutyCycle)
    sleep(0.15)
    GPIO.output(servoPin, GPIO.LOW)
    sleep(0.15)


def detect_target():#타겟 감지 확인
    global Detect
    if Detect == 0:
        if random.random() < 0.02:  # 2% 확률로 감지 발생
            Detect=1
        else:
            Detect=0
    return Detect

def detect_coord():#감지된 타겟 좌표 확인
     global Detect
     global coordinate
     if random.random() < 1:  # 100% 확률로 감지 발생
            coordinate= random.randint(40, 60)# 40~60의 랜덤 x좌표 생성
     return coordinate
    
# 고속 우회전
def right(degrees):
    global save_degree
    global coordinate
    save_degree=save_degree+(coordinate-50)# 감지된 각도와 x좌표를 기반으로 수정된 각도 생성
    print("targets in: ", save_degree)
    print("x coordinate:", coordinate)
    angleToDutyConvert(save_degree + 20)# 수정된 각도 반환, 각도 조절

    return save_degree

# 고속 좌회전
def left(degrees):
    global save_degree
    global coordinate
    save_degree=save_degree-(50-coordinate)# 감지된 각도와 x좌표를 기반으로 수정된 각도 생성
    print("targets in: ", save_degree)
    print("x coordinate:", coordinate)
    angleToDutyConvert(save_degree - 20)# 수정된 각도 반환, 각도 조절

    return save_degree

# 동물 추적
def track_target(target_coord):
    if target_coord >= 55:  # 좌표가 오른쪽일 경우
        print("turn left")
        left(target_coord)
    if target_coord <= 45:  # 좌표가 왼쪽일 경우
        print("turn right")
        right(target_coord)
    else:
        print("detect!")
        print("targets in: ", save_degree)
        print("x coordinate:", coordinate)
        return 0

# 평소 회전
def sweep():
    global Detect
    global save_degree
    if Detect != 0:  # 감지가 됐을 경우
        coord = detect_coord()
        track_target(coord)
        return
    else:
        for pos in range(0, 180, +10):
            print(pos)
            angleToDutyConvert(pos)
            Detect = detect_target()
            save_degree = pos

            if Detect != 0:  # 감지되면 순찰 탈출
                break

        for pos in range(save_degree + 10, 0, -10):
            print(pos)
            angleToDutyConvert(pos)
            Detect = detect_target()
            save_degree = pos

            if Detect != 0:  # 감지되면 순찰 탈출
                break

# 메인 루프
while True:
    sweep()