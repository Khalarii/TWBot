from village import *
import datetime

class Util():
	def __init__(self,world_id):
		self.world_id = world_id

	def sleep_for_minutes(self,minutes):
		from time import sleep
		counter = minutes
		while counter > 0:
			self.print_with_time_stamp("Sleeping for {} more minutes".format(counter))
			counter -= 1
			sleep(60)
		self.print_with_time_stamp("Continuing activity")
		return

	def print_with_time_stamp(self,text):
		print("W{} {} {}".format(self.world_id, datetime.datetime.now(), text))
		return

	def get_points_for_village(self,x,y):
		all_villages = open("./villages/{}/village.txt".format(self.world_id), "r").read().split()
		for village in all_villages:
			v_info = village.split(",")
			if v_info[2] == x and v_info[3] == y:
				return [v_info[5], v_info[1]]
		return ["-1", ""]

	def is_barbarian(self, name):
		return name == "Aldeia+de+b%C3%A1rbaros" or name == "Aldeia-bonus"

	def can_attack(self, my_points, target_points, target_name):
		return target_points > 0 and target_points < 800 and self.is_barbarian(target_name)

	def get_villages_to_farm(self, my_points, coordinates):
		villages = []

		for coordinate in coordinates:
			x = coordinate.split("|")[0]
			y = coordinate.split("|")[1]
			info = self.get_points_for_village(x,y)
			points = int(info[0])
			name = info[1]
			if self.can_attack(my_points, points, name): villages.append(Village(x,y,points))
		return villages

	def get_random_float(self,start,end):
		import random
		return random.uniform(start,end)
