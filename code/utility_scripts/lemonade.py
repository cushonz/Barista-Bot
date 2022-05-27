import RPi.GPIO as GPIO
from pump import pump

GPIO.setwarnings(False)

pumps = {
	"orange" : 16,
	"lime" : 21,
	"blue": 19,
	"strawberry" : 20,
}

pc = pump(15,pumps)
pc.pump_init()
order = input("flavors: ")
pc.lemonade(order)
