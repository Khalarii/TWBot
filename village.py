class Village:
	def __init__(self,x,y,points):
		self.x = x
		self.y = y
		self.points = points

	def get_coords(self):
		return "{}|{}".format(self.x,self.y)

	def get_points(self):
		return self.points

	def get_unit_multiplier(self):
		multiplier = -1
		if self.points < 500:
			multiplier = 30
		if self.points < 300:
			multiplier = 20
		return multiplier