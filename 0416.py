from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
led = Pin(25,Pin.OUT)

THRESHOLD=2900

while True:
    pot_value = pot.read()
    print(pot_value)

    if pot_value > THRESHOLD:
        led.value(0)
    else:
        led.value(1)

    sleep(0.5)
