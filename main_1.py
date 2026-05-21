import bluetooth
import time
# 반드시 보드에 ble_simple_peripheral.py 파일이 있어야 합니다.
from ble_simple_peripheral import BLESimplePeripheral

# gpio lib
from machine import Pin

# 블루투스 설정
ble = bluetooth.BLE()
#sp = BLESimplePeripheral(ble, name="ESP32_BLE")
sp = BLESimplePeripheral(ble, name="52oioi")

#. gpio 설정
led= Pin(2, Pin.OUT)
led.value(0)

def on_rx(data):
    # 스마트폰에서 esp32 보드로 데이터 수신 시 실행
    msg = data.decode('utf-8').strip()
    print("수신 메시지:", msg)
    # 응답 보내기
    #sp.send("응답: " + msg + "\n")
    if msg == 'on':
        led.value(1)
        print('LED 켜짐')
    elif msg == 'off':
        led.value(0)

print("블루투스 연결 대기 중...")

while True:
    if sp.is_connected():
        sp.on_write(on_rx)
    time.sleep_ms(100)
