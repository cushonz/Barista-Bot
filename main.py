import RPi.GPIO as GPIO
import sys
from pump import pump

GPIO.setwarnings(False)

pumps = {
	"orange" : 16,
	"lime" : 21,
	"blue": 19,
	"strawberry" : 20,
}

order = sys.argv[1:];
pc = pump(14,pumps)
pc.pump_init()

pc.order_drink(order)
