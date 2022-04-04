import RPi.GPIO as GPIO
import time
import drink

GPIO.setmode(GPIO.BCM)



pump_time = 15 #seconds

#Populate Drinks
# Drink = drink.drink(orange,blue,strawberry,lime)

#Flavor Bank
#flavor = GPIO
#------------------
orange = 16
lime = 21
blue = 19
strawberry = 20
#------------------

#|Drinks|________________________________
josh = drink.drink(False,True,True,False)
zach = drink.drink(True,False,False,False)
tolby = drink.drink(False,True,False,True)
#________________________________________
	
def kill_all():	#Turns all pumps to HIGH to turn relays off

	GPIO.output(orange,GPIO.HIGH)
	GPIO.output(lime,GPIO.HIGH)
	GPIO.output(blue,GPIO.HIGH)
	GPIO.output(strawberry,GPIO.HIGH)

def pump_init(): #sets up GPIO and turns all pumps off

	#Sets up all pump GPIO
	GPIO.setup(orange,GPIO.OUT)
	GPIO.setup(strawberry,GPIO.OUT)
	GPIO.setup(lime,GPIO.OUT)
	GPIO.setup(blue,GPIO.OUT)

	#turns all motors to the off position to ensure syrup doesn't spray everywhere

	kill_all()

def make_drink(name): # Takes drink object and creates drink

	act_time = int(pump_time/name.flav)	
	for flavor in name.ingredient:  #Loop through dictionary,
		if name.ingredient[flavor]: #For every flavor
			GPIO.output(flavor,GPIO.LOW) #set LOW if true
		else :
			GPIO.output(flavor,GPIO.HIGH) #otherwise the pump will be set to HIGH
	
	#pump for target time
	time.sleep(act_time)

	#power off all pumps
	kill_all()

def make_drink(name,sweeten): # Overloaded version of make_drink, takes int for sweetener pump_time

	act_time = int(sweeten)	
	for flavor in name.ingredient:  #Loop through dictionary,
		if name.ingredient[flavor]: #For every flavor
			GPIO.output(flavor,GPIO.LOW) #set LOW if true
		else :
			GPIO.output(flavor,GPIO.HIGH) #otherwise the pump will be set to HIGH
	
	#pump for target time
	time.sleep(sweeten)

	#power off all pumps
	kill_all()
	
		
		
# Testing	
pump_init()		

	
