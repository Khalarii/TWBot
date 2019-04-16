from util import *
class PlayerVillage:
	def __init__(self, world_id, village_id, my_coordinates, coordinates_to_farm):
		u = Util(world_id)
		self.points = 0
		for coordinates in my_coordinates:
			self.points += int(u.get_points_for_village(coordinates[0], coordinates[1])[0])
		self.village_id = village_id
		self.villages_to_farm = u.get_villages_to_farm(self.points, coordinates_to_farm)
		self.first_run = True
		self.first_village_run_at = datetime.datetime.now()
		self.unit_type = "lc"
		self.current_index = 0