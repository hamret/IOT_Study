# from machine import Pin
# import time

# button_pin = Pin(18, Pin.IN, Pin.PULL_UP)
# led= Pin(4, Pin.OUT)

# while True:
#     if button_pin.value() == 0:
#         print("Button Pressed!")
#         led.value(1)
#     else:
#         print("Button OFF!")
#         led.value(0)
#     time.sleep(0.2) 


from machine import Pin, PWM
from time import sleep_ms
servo = PWM(Pin(32), freq=50)

def set_angle(angle):
    angle = max(0, min(180, angle))

    min_us = 500
    max_us = 2500
    pulse_us = min_us + (angle / 180) * (max_us - min_us)
    servo.duty_ns(int(pulse_us * 1000))

while True:
    # 0도에서 180도까지 이동
    for angle in range(0, 181, 5):
        set_angle(angle)
        sleep_ms(50)

    # 180도에서 0도까지 이동
    for angle in range(180, -1, -5):
        set_angle(angle)
        sleep_ms(50)
