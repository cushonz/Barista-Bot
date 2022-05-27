class drink:

	def countFlav(self):
		for x in self.ing:
			if (self.ing[x] == True):
				self.flav += 1
	
	
	def __init__(self, orange,blue,straw,lime):
	
	#orange = 16
	#lime = 21
	#blue = 19
	#strawberry = 20
		self.ing = {
		16:orange,
		19: blue,
		20:straw,
		21:lime,
		}
		
		self.flav = 0
		self.countFlav()
		
	
	
