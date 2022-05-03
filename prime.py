import RPi.GPIO as GPIO

orange = 16
lime = 21
blue = 19
strawberry = 20

def all_off():
	GPIO.output(orange,GPIO.HIGH)
	GPIO.output(lime,GPIO.HIGH)
	GPIO.output(blue,GPIO.HIGH)
	GPIO.output(strawberry,GPIO.HIGH)
	
def all_on(x):
	GPIO.output(orange,GPIO.LOW)
	GPIO.output(lime,GPIO.LOW)
	GPIO.output(blue,GPIO.LOW)
	GPIO.output(strawberry,GPIO.LOW)
	time.sleep(x)
	all_off()

def pump_setup(): #sets up GPIO and turns all pumps off
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(orange,GPIO.OUT)
	GPIO.setup(strawberry,GPIO.OUT)
	GPIO.setup(lime,GPIO.OUT)
	GPIO.setup(blue,GPIO.OUT)

	all_off()
	
pump_setup()
all_on(3)

