from machine import Pin, PWM, ADC
import time

#led = Pin(18, Pin.OUT)

pwm = PWM(Pin(18), freq=50)

SENSOR_PIN = 34
adc = ADC(SENSOR_PIN)
# adc = ADC(PIN(SENSOR_PIN))

# 선택사항: 12비트 해상도 설정 (기본값; 16비트는 65535)
adc.atten(ADC.ATTN_11DB) # 0~3.3V 전체 범위
adc.width(ADC.WIDTH_12BIT)

while True:
    raw_value = adc.read()
    duty = int((raw_value/4095)*1023)

#    voltage = (raw_value / 4095) * 1023  # 전압으로 변환
#    angle = (raw_value / 4095) * 300 # 대략적인 각도 계산 (0~300°; 포트에 따라 조정)

    pwm.duty(duty)

#    print(f"원시값: {raw_value}, 전압: {voltage:.2f}V, 각도: {angle:.1f}°")
    time.sleep(0.01)

#while True:
#    for dutyratio in range(1,1024,10):
#        pwm.duty(dutyratio)
#        time.sleep(0.01)
#    for dutyratio in range(1023,1,-10):
#        pwm.duty(dutyratio)
#        time.sleep(0.01)

