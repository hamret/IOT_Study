from machine import Pin
import time

# 핀 설정
button_pin = Pin(12, Pin.IN, Pin.PULL_UP)
button_pin1 = Pin(17, Pin.IN, Pin.PULL_UP)
led1 = Pin(33, Pin.OUT)
led2 = Pin(19, Pin.OUT)

last_press_time = 0

def button_handler(pin):
    global last_press_time
    current_time = time.ticks_ms()

    # 200ms 디바운싱 처리
    if time.ticks_diff(current_time, last_press_time) > 200:
        if pin.value() == 0:  # 버튼이 눌렸을 때
            target_led = led1 if pin == button_pin else led2

            print(f"Button {pin} Pressed!")
            target_led.value(1)      # 해당 LED 켜기

            time.sleep_ms(1000)      # 1초 대기

            target_led.value(0)      # 해당 LED 끄기
            print("LED OFF")

        last_press_time = time.ticks_ms()

# 인터럽트 설정 (두 버튼 모두 동일한 핸들러 사용)
button_pin.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button_pin1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# 메인 루프
while True:
    time.sleep(1)
