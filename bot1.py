import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
en = 11

gpio.setup(3, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(29, gpio.OUT)
gpio.setup(en, gpio.OUT)

gpio.setup(3, gpio.LOW)
gpio.setup(5, gpio.LOW)
gpio.setup(7, gpio.LOW)
gpio.setup(29, gpio.LOW)

p=gpio.PWM(en,1000)
p.start(11)
gpio.output(3, gpio.HIGH)
gpio.output(5, gpio.HIGH)
gpio.output(7, gpio.HIGH)
gpio.output(29, gpio.HIGH)
time.sleep(3)
gpio.cleanup()
print("DONE")