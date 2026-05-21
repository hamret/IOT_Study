import bluetooth
import time
# 반드시 보드에 ble_simple_peripheral.py 파일이 있어야 합니다.
from ble_simple_peripheral import BLESimplePeripheral
from machine import Pin

led_B = Pin(33, Pin.OUT)
led_G = Pin(12, Pin.OUT)

# 블루투스 설정
ble = bluetooth.BLE()
#sp = BLESimplePeripheral(ble, name="ESP32_BLE")
sp = BLESimplePeripheral(ble, name="52oioi")

def on_rx(data):
    msg = data.decode('utf-8').strip()
    print("수신 메시지:", msg)

    if msg == "Blue on":
        led_B.value(1)
        sp.send("Blue 전등을 켰습니다.\n")
    elif msg == "Blue off":
        led_B.value(0)
        sp.send("Blue 전등을 껐습니다.\n")
    if msg == "Green on":
        led_G.value(1)
        sp.send("Green 전등을 켰습니다.\n")
    elif msg == "Green off":
        led_G.value(0)
        sp.send("Green 전등을 껐습니다.\n")
    else:
        # 응답 보내기(명령어가 아닐때)
        sp.send("응답: " + msg + "\n")

print("블루투스 연결 대기 중...")

while True:
    if sp.is_connected():
        sp.on_write(on_rx)
    time.sleep_ms(100)
