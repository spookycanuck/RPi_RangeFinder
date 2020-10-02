import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 17
ECHO = 18
LED = 4
BLUE = 21

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.5)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #inches:
    distance = sig_time / 0.000148

    print('Distance: {} inches'.format(distance))

    return distance

while True:
    distance = get_distance()
    if distance <= 8:
        GPIO.output(LED,GPIO.HIGH)
	GPIO.output(BLUE,GPIO.LOW)
    else:
        GPIO.output(BLUE,GPIO.HIGH)
	GPIO.output(LED,GPIO.LOW)

GPIO.cleanup()
