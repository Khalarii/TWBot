from bot import *
my_coordinates = [ [ "390", "475" ] ]
villages = [ PlayerVillage("94", "13443", my_coordinates, "389|471 393|472 394|472 386|473 392|476 390|477 388|477 388|479 390|479 378|476 383|478 386|481 394|481 388|482 387|485 386|486 394|487 388|469 386|465 391|464 391|463 394|463 395|471 395|476 397|474 398|478 398|477 398|473 400|472 400|477 402|473 396|481 396|482 395|483 397|483 398|483 398|484 395|486 401|488 403|486 402|485 403|484 377|481 379|482 384|487 382|487 381|485 380|466 383|466 385|465 383|463 397|466 400|467 402|467 398|465 400|465 403|464 402|464 401|463 398|464 398|462 395|462 404|472 404|475 408|472 409|472 409|475 410|474 409|476 409|478 410|477 404|485 405|486 406|483 408|480 408|481 410|483 412|484 412|486 411|487 409|487 404|463 406|467 406|470 410|467 409|465 409|462".split())]
world_94 = World("94", villages)
bot = Bot(world_94)
bot.run()
bot.login("Kimgss", "^8@Ku*N6P8WJm7a2*yet")
bot.go_to_meeting_place()

while (True):
	#first_village_run_at = datetime.datetime.now()
	for village in world_94.village_list:
		bot.farm_villages(village, "lc", datetime.datetime.now(), False)
	#bot.u.sleep_for_minutes(40 - int((datetime.datetime.now() - first_village_run_at).total_seconds() // 60))