import RPi.GPIO as GPIO
import time
import drink

GPIO.setmode(GPIO.BCM)

orange = 16
lime = 21
blue = 19
strawberry = 20

flavor = [16,19,20,21]

pump_time = 15 #seconds

#Populate Drinks
# Drink = drink.drink(orange,blue,strawberry,lime);
josh = drink.drink(False,True,True,False)
zach = drink.drink(True,False,False,False)
	
def all_off():
	GPIO.output(orange,GPIO.HIGH)
	GPIO.output(lime,GPIO.HIGH)
	GPIO.output(blue,GPIO.HIGH)
	GPIO.output(strawberry,GPIO.HIGH)

def pump_setup(): #sets up GPIO and turns all pumps off

	GPIO.setup(orange,GPIO.OUT)
	GPIO.setup(strawberry,GPIO.OUT)
	GPIO.setup(lime,GPIO.OUT)
	GPIO.setup(blue,GPIO.OUT)

	all_off()

def make_drink(name):
	act_time = int(pump_time/name.flav)	
	if name.ing['Orange'] == True:
		GPIO.output(orange,GPIO.LOW)
	if name.ing['Blue'] == True:
		GPIO.output(blue,GPIO.LOW)
	if name.ing['Strawberry'] == True:
		GPIO.output(strawberry,GPIO.LOW)
	if name.ing['Lime'] == True:
		GPIO.output(lime,GPIO.LOW)
	print(time)
	time.sleep(act_time)
	all_off()
	
	
		
		
		
pump_setup()		
make_drink(josh)
print(val)
	
	
