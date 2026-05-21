import bluetooth
import time
# 반드시 보드에 ble_simple_peripheral.py 파일이 있어야 합니다.
from ble_simple_peripheral import BLESimplePeripheral

# gpio lib
from machine import Pin

# 블루투스 설정
ble = bluetooth.BLE()

ble.active(False)	
time.sleep_ms(100)

#sp = BLESimplePeripheral(ble, name="ESP32_BLE")
sp = BLESimplePeripheral(ble, name="52oioi")

#. gpio 설정
led= Pin(12, Pin.OUT)
led.value(0)

# 1. 하드웨어 설정 (버튼)
button_pin = Pin(14, Pin.IN, Pin.PULL_UP)



print("블루투스 연결 대기 중...")

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

# 버튼의 이전 상태를 저장하기 위한 변수
last_state = button_pin.value()


while True:
    if sp.is_connected():
        sp.on_write(on_rx)

        current_state = button_pin.value()
        if current_state != last_state:
            current_state = button_pin.value()
            print(current_state)
            if current_state != last_state:
                if current_state == 1:
                    print("Button Pressed!")
                    sp.send("Button Pressed!\n")
                    time.sleep_ms(500)
                else:
                    print("Button Released!")
                    sp.send("Button Released!\n")
                    time.sleep_ms(500)
                last_state = current_state

    time.sleep_ms(100)
