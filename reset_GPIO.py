import RPi.GPIO as GPIO

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

GPIO.cleanup()
