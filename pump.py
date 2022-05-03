import time
import drink
import RPi.GPIO as GPIO

class pump:	

	def __init__(self,pump_time,pfDict): # give a pump duration and a dictionary
		self.pump_time = pump_time #seconds
		self.pumps = pfDict


	def kill_all(self):	#Turns all pumps to HIGH to turn relays off
		for pump in self.pumps:
			GPIO.output(self.pumps[pump],GPIO.HIGH)

	def pump_init(self): #sets up GPIO and turns all pumps off
		#Sets up all pump GPIO
		GPIO.setmode(GPIO.BCM)
		for pump in self.pumps:
			GPIO.setup(self.pumps[pump],GPIO.OUT)
		#turns all motors to the off position to ensure syrup doesn't spray everywhere
		self.kill_all()
		
	def make_drink(self,name): # Takes drink object and creates drink

		act_time = int(self.pump_time/name.flav)	
		for flavor in name.ingredient:  #Loop through dictionary,
			if name.ingredient[flavor]: #For every flavor
				GPIO.output(flavor,GPIO.LOW) #set LOW if true
			else :
				GPIO.output(flavor,GPIO.HIGH) #otherwise the pump will be set to HIGH
		
		#pump for target time
		time.sleep(act_time)

		#power off all pumps
		self.kill_all()

	def make_drink(self,name,sweeten): # Overloaded version of make_drink, takes int for sweetener pump_time

		act_time = int(sweeten)	
		for flavor in name.ingredient:  #Loop through dictionary,
			if name.ingredient[flavor]: #For every flavor
				GPIO.output(flavor,GPIO.LOW) #set LOW if true
			else :
				GPIO.output(flavor,GPIO.HIGH) #otherwise the pump will be set to HIGH
		
		#pump for target time
		time.sleep(sweeten)
		#power off all pumps
		self.kill_all()

	def order_drink(self,flavors):
		flavs = flavors.split(" ")
		calc_time = int(self.pump_time/len(flavs))
		for vals in self.pumps:
			for f in flavs:
				if f == vals:
					GPIO.output(self.pumps[vals],GPIO.LOW)
		time.sleep(calc_time)
		self.kill_all()
				
		
	def lemonade(self,flavors):
		flavs = flavors.split(" ")
		lemon_time = 160
		calc_time = int(self.pump_time/len(flavs))
		
		GPIO.output(16,GPIO.LOW)
		time.sleep(lemon_time)
		for vals in self.pumps:
			for f in flavs:
				if f == vals:
					GPIO.output(self.pumps[vals], GPIO.LOW)
		time.sleep(calc_time)
		self.kill_all()
