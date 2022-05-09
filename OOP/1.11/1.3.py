import RPi.GPIO as GPIO  # Only works on Raspberry Pi
import time 


class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

led_1 = Led(36)
led_2 = Led(38)
led_3 = Led(31)
led_4 = Led(33)

while True:
    time.sleep(1)
    led_1.on()
    led_2.on()
    led_3.off()
    led_4.off()
    time.sleep(1)
    led_1.off()
    led_2.off()
    led_3.on()
    led_4.on()