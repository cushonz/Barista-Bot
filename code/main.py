import RPi.GPIO as GPIO
import sys
from pump import pump

GPIO.setwarnings(False)

pumps = {
	"dragon" : 16,
	"watermelon" : 21,
	"sour": 19,
	"apple" : 20,
}

order = sys.argv[1:];
pc = pump(14,pumps)
pc.pump_init()

pc.order_drink(order)
