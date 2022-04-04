class drink:

	def countFlav(self):
		for x in self.ing:
			if (self.ing[x] == True):
				self.flav += 1
	
	
	def __init__(self, orange,blue,straw,lime):
	
		self.ing = {
		'Orange': orange,
		'Blue': blue,
		'Strawberry':straw,
		'Lime':lime,
		}
		
		self.flav = 0
		self.countFlav()
		
	
	
