from village import *

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
		import datetime
		print("W{} {} {}".format(self.world_id, datetime.datetime.now(), text))
		return

	def get_points_for_village(self,x,y):
		all_villages = open("./villages/{}/village.txt".format(self.world_id), "r").read().split()
		for village in all_villages:
			v_info = village.split(",")
			if v_info[2] == x and v_info[3] == y:
				return [v_info[5], v_info[1]]
		return ["-1", ""]

	def get_villages_to_farm(self, my_points, coordinates):
		villages = []

		#if self.world == "93": my_points = int(self.get_points_for_village("441", "352")[0])
		#elif self.world == "94": my_points = int(self.get_points_for_village("390", "475")[0])

		#if self.world == "93": coordinates = "437|349 438|349 443|351 438|353 444|355 442|355 442|356 443|356 439|356 437|356 436|351 435|351 435|354 433|353 433|351 434|350 431|354 430|351 429|355 428|353 443|346 444|346 442|357 444|357 445|357 438|358 440|359 442|359 443|359 437|360 439|360 444|360 445|360 441|361 437|362 440|362 437|363 438|363 438|364 440|364 441|364 445|364 443|365 442|365 451|351 452|350 452|349 454|355 448|346 451|346 450|344 450|342 448|359 448|358 452|357 454|359 454|360 453|360 451|360 450|360 451|362 451|363 450|363 447|363 454|365 428|358 430|358 431|358 428|361 430|361 435|360 436|361 436|364 430|366 433|366 435|367 428|369 430|370 432|371 433|371 434|372 437|369 439|369 441|369 445|370 439|370 437|370 438|372 440|372 450|366 451|366 451|368 446|368 454|373 455|358 457|357 458|358 462|358 457|360 458|360 458|361 457|361 457|362 463|361 457|364 455|350 456|351 456|352 455|353 456|356 458|355 460|356 462|349 462|351 457|342 459|340 461|342 462|343 462|339 462|345 462|346".split()
		#elif self.world == "94": coordinates = "389|471 393|472 394|472 386|473 392|476 390|477 388|477 388|479 390|479 378|476 383|478 386|481 394|481 388|482 387|485 386|486 394|487 388|469 386|465 391|464 391|463 394|463 395|471 395|476 397|474 398|478 398|477 398|473 400|472 400|477 402|473 396|481 396|482 395|483 397|483 398|483 398|484 395|486 401|488 403|486 402|485 403|484 377|481 379|482 384|487 382|487 381|485 380|466 383|466 385|465 383|463 397|466 400|467 402|467 398|465 400|465 403|464 402|464 401|463 398|464 398|462 395|462 404|472 404|475 408|472 409|472 409|471 409|475 410|474 409|476 409|478 410|477 404|485 405|486 406|483 408|480 408|481 410|483 412|484 412|486 411|487 409|487 404|463 406|467 406|470 410|467 409|465 409|462".split()

		for coordinate in coordinates:
			x = coordinate.split("|")[0]
			y = coordinate.split("|")[1]
			info = self.get_points_for_village(x,y)
			points = int(info[0])
			name = info[1]
			if points > 0 and points < 300 and ((my_points/points < 20) or (name == "Aldeia+de+b%C3%A1rbaros" or name == "Aldeia-bonus")): villages.append(Village(x,y,points))
		return villages

	def get_random_float(self,start,end):
		import random
		return random.uniform(start,end)
