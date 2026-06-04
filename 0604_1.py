import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
from machine import Pin, PWM
from time import sleep_ms, sleep

ble = bluetooth.BLE()
sp = BLESimplePeripheral(ble, name="52oioi")

servo = PWM(Pin(32), freq=50)
button_pin = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(4, Pin.OUT)

def set_angle(angle):
    angle = max(0, min(180, angle))
    min_us = 500
    max_us = 2500
    pulse_us = min_us + (angle / 180) * (max_us - min_us)
    servo.duty_ns(int(pulse_us * 1000))

def open_door():
    print("문이 열립니다")
    led.value(1)
    set_angle(170)

    if sp.is_connected():
        sp.send("문이 열렸습니다.\n")

    sleep(5)

    print("문이 닫힙니다.")
    set_angle(0)
    led.value(0)

    if sp.is_connected():
        sp.send("문이 닫혔습니다.\n")

    sleep(0.5)

def on_rx(data):
    msg = data.decode('utf-8').strip()
    print("수신 메시지:", msg)

    if msg == "open":
        open_door()
    else:
        sp.send("응답: " + msg + "\n")

set_angle(0)
led.value(0)
print("블루투스 연결 대기 중...")

while True:
    if sp.is_connected():
        sp.on_write(on_rx)

    if button_pin.value() == 1:
        open_door()

    sleep_ms(50)
