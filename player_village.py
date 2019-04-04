class PlayerVillage:
	def __init__(self, world_id, village_id, my_coordinates, coordinates_to_farm):
		from util import *
		u = Util(world_id)
		self.points = 0
		for coordinates in my_coordinates:
			self.points += int(u.get_points_for_village(coordinates[0], coordinates[1])[0])
		self.village_id = village_id
		self.villages_to_farm = u.get_villages_to_farm(self.points, coordinates_to_farm)