import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 17
ECHO = 18
LED = 4

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

#GPIO.output(TRIG, False)
#time.sleep(0.1)
GPIO.output(LED, GPIO.LOW)
GPIO.output(TRIG, True)
time.sleep(1)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False:
    start = time.time()
    #print ("GPIO input = ",start)
    #GPIO.output(LED, GPIO.HIGH)

while GPIO.input(ECHO) == True:
    end = time.time()
    #print ('GPIO output = ',end)
    #GPIO.output(LED, GPIO.HIGH)

sig_time = end-start


#CM:
#distance = sig_time / 0.000058

#inches:
distance = sig_time / 0.000148

print('Distance: {} inches'.format(distance))

if distance <= 8:
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(3)
else:
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(1)


GPIO.cleanup()
