from machine import Pin
from time import sleep_ms


red_led = Pin(17, Pin.OUT)
green_led = Pin(12, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

led_state = 0
last_button_state = 0

while True:
    current_button_state = button.value()

    if current_button_state == 1 and last_button_state == 0:
        if led_state == 0:
            led_state = 1
        else:
            led_state = 0

        red_led.value(led_state)
        green_led.value(led_state)

        sleep_ms(200)

    last_button_state = current_button_state

    sleep_ms(20)
