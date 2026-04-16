from machine import Pin, ADC
from time import sleep

msensor = ADC(Pin(35))
msensor.atten(ADC.ATTN_11DB)
led = Pin(18, Pin.OUT)

EMPTY = 500
FULL = 4000

while True:
    val = msensor.read()
    print(val)

    if val < EMPTY:
        led.value(0)
    elif EMPTY <= val and val < FULL:
        led.value(not led.value())
    else:
        led.value(1)

    sleep(0.5)
