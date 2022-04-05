from pump import pump

pumps = {
	"orange" : 16,
	"lime" : 21,
	"blue": 19,
	"strawberry" : 20,
}

pc = pump(15,pumps)

pc.order_drink("strawberry lime")