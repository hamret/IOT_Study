from machine import Pin, PWM, ADC
import time

SENSOR_PIN = 34
SERVO_PIN = 12

servo = PWM(Pin(SERVO_PIN), freq=50)

adc = ADC(Pin(SENSOR_PIN))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

def set_angle(angle):
    angle = max(0, min(180, angle))
    min_us = 500
    max_us = 2500
    pulse_us = min_us + (angle / 180) * (max_us - min_us)
    servo.duty_ns(int(pulse_us * 1000))

while True:
    raw_value = adc.read()
    target_angle = (raw_value / 4095) * 180
    set_angle(target_angle)

    print(f"Sensor: {raw_value}, Servo Angle: {target_angle:.1f}°")

    time.sleep(0.02)
