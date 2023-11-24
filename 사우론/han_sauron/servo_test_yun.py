import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
servo_pin = 32

# GPIO 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

# PWM 객체 생성
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz 주파수

# 서보 모터 최소 및 최대 각도 설정 (도단위)
min_angle = 0
max_angle = 180

# 서보 모터 각도 부드럽게 변경 함수
def set_smooth_angle(target_angle):
    current_angle = min_angle
    angle_step = 10  # 부드럽게 움직이는 각도 단위
    
    while current_angle != target_angle:
        pwm.ChangeDutyCycle(current_angle / 18 + 2)
        time.sleep(0.02)  # 움직임 간격
        if target_angle > current_angle:
            current_angle += angle_step
            if current_angle > target_angle:
                current_angle = target_angle
        else:
            current_angle -= angle_step
            if current_angle < target_angle:
                current_angle = target_angle

try:
    pwm.start(0)  # PWM 시작

    while True:
        set_smooth_angle(min_angle)
        time.sleep(1)
        set_smooth_angle(max_angle)
        time.sleep(1)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
