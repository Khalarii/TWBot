from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from village import *
from time import sleep
from player_village import *

class Bot:
	def __init__(self, world, first_village):
		self.baseLC = 1
		self.base_spears = 4
		self.base_swords = 4
		self.current_village = first_village
		self.meeting_place_URL = "https://br{}.tribalwars.com.br/game.php?village={}&screen=place"
		self.secondary_meeting_place_URL = "https://br{}.tribalwars.com.br/game.php?screen=place&village={}"
		self.u = Util(world)
		self.browser = webdriver.Firefox(executable_path="./geckodriver")
		self.browser.implicitly_wait(30)
		self.world = world

	def captcha_visible(self):
		captcha_visible = False
		try:
			self.browser.implicitly_wait(1)
			captcha = self.browser.find_element_by_id("bot_check")
			captcha_visible = True
		except:
			captcha_visible = False
		finally:
			self.browser.implicitly_wait(10)
		return captcha_visible

	def stop_if_captcha(self):
		if self.captcha_visible():
			self.u.print_with_time_stamp("Captcha identified")
			while self.captcha_visible():
				sleep(1)
		return

	def run(self):
		self.browser.get("https://tribalwars.com.br")
		return

	def move_to_and_click_on_by_id(self,id):
		item_to_click = self.browser.find_element_by_id(id)
		ActionChains(self.browser).move_to_element(item_to_click).perform()
		item_to_click.click()
		return

	def move_to_and_click_on_by_name(self, name):
		item_to_click = self.browser.find_element_by_name(name)
		ActionChains(self.browser).move_to_element(item_to_click).perform()
		item_to_click.click()
		return		

	def move_to_and_click_on_by_class(self,class_name):
		item_to_click = self.browser.find_element_by_class_name(class_name)
		ActionChains(self.browser).move_to_element(item_to_click).perform()
		item_to_click.click()
		return

	def login(self, username, password):
		self.move_to_and_click_on_by_id("user")
		self.browser.find_element_by_id("user").clear()
		self.browser.find_element_by_id("user").send_keys(username)
		self.move_to_and_click_on_by_id("password")
		self.browser.find_element_by_id("password").clear()
		self.browser.find_element_by_id("password").send_keys(password)
		self.move_to_and_click_on_by_id("remember-me")
		self.move_to_and_click_on_by_class("btn-login")
		self.u.print_with_time_stamp("Logged in")
		sleep(self.u.get_random_float(2,3))
		self.u.print_with_time_stamp("Going to world {}".format(self.world))
		self.browser.get("https://tribalwars.com.br/page/play/br{}".format(self.world))
		sleep(self.u.get_random_float(2,3))
		return

	def end_session(self):
		self.u.print_with_time_stamp("Finishing session")
		self.browser.close()
		return

	def go_to_meeting_place(self):
		if self.browser.current_url == "https://www.tribalwars.com.br/?session_expired=1":
			self.browser.get("https://tribalwars.com.br/page/play/br{}".format(self.world))
			sleep(self.u.get_random_float(1,2))
		self.stop_if_captcha()
		self.u.print_with_time_stamp("Directing to villages overview")
		self.browser.get("https://br{}.tribalwars.com.br/game.php?village={}&screen=overview_villages".format(self.world, self.current_village.village_id))
		sleep(self.u.get_random_float(1,2))
		self.u.print_with_time_stamp("Directing to overview")
		self.browser.get("https://br{}.tribalwars.com.br/game.php?village={}&screen=overview".format(self.world, self.current_village.village_id))
		sleep(self.u.get_random_float(1,2))
		self.stop_if_captcha()
		self.u.print_with_time_stamp("Directing to meeting place")
		self.browser.get(self.meeting_place_URL.format(self.world, self.current_village.village_id))
		sleep(self.u.get_random_float(1,2))
		return

	def go_to_main_village(self):
		self.stop_if_captcha()
		self.u.print_with_time_stamp("Directing to main village screen")
		self.move_to_and_click_on_by_id("ds_body")
		self.browser.find_element_by_id("ds_body").send_keys("v")
		sleep(self.u.get_random_float(2,3))
		return

	def get_available_units(self, unit_type):
		available_units = "(0)"

		if unit_type == "lc":
			available_units = str(self.browser.find_element_by_id("units_entry_all_light").text)
		elif unit_type == "spear":
			available_units = str(self.browser.find_element_by_id("units_entry_all_spear").text)
		elif unit_type == "sword":
			available_units = str(self.browser.find_element_by_id("units_entry_all_sword").text)
		elif unit_type == "scout":
			available_units = str(self.browser.find_element_by_id("units_entry_all_spy").text)

		return int(available_units[1:available_units.index(")")])

	def send_attack(self, village, unit_type):
		self.stop_if_captcha()

		attack_units = 0

		if unit_type == "lc":
			attack_units = self.baseLC * village.get_unit_multiplier()
		elif unit_type == "spear":
			attack_units = self.base_spears * village.get_unit_multiplier()

		try:

			if unit_type == "spear":
				if self.get_available_units("sword") > self.base_swords * village.get_unit_multiplier():
					self.move_to_and_click_on_by_id("unit_input_sword")
					self.browser.find_element_by_id("unit_input_sword").send_keys(str(self.base_swords * village.get_unit_multiplier()))
					sleep(self.u.get_random_float(0.2,0.5))
				self.move_to_and_click_on_by_id("unit_input_spear")
				self.browser.find_element_by_id("unit_input_spear").send_keys(str(attack_units))
				sleep(self.u.get_random_float(0.2,0.5))
			elif unit_type == "lc":
				self.move_to_and_click_on_by_id("unit_input_light")
				self.browser.find_element_by_id("unit_input_light").send_keys(str(attack_units))
				sleep(self.u.get_random_float(0.5,1))
				
			self.move_to_and_click_on_by_name("input")
			self.browser.find_element_by_name("input").send_keys(village.get_coords())
			sleep(self.u.get_random_float(1,2))
			self.move_to_and_click_on_by_id("target_attack")
			self.u.print_with_time_stamp("Sent {} {} to attack {}({})".format(attack_units, unit_type, village.get_coords(), village.get_points()))
			sleep(self.u.get_random_float(2,3))
			self.move_to_and_click_on_by_id("troop_confirm_go")
			self.u.print_with_time_stamp("Confirmed attack")
			sleep(self.u.get_random_float(2,3))
		except:
			self.go_to_meeting_place()
		return

	def enough_units(self, village, unit_type):
		attack_units = 0

		if unit_type == "lc":
			attack_units = self.baseLC * village.get_unit_multiplier()
		elif unit_type == "spear":
			attack_units = self.base_spears * village.get_unit_multiplier()

		return attack_units > 0 and attack_units <= self.get_available_units(unit_type)

	def not_in_meeting_place(self, current_url):
		return current_url != self.meeting_place_URL.format(self.world, self.current_village.village_id) and current_url != self.secondary_meeting_place_URL.format(self.world, self.current_village.village_id)

	def farm_villages(self, player_village):
		self.current_village = player_village
		loop_started = datetime.datetime.now()

		while True:
			self.stop_if_captcha()

			if (datetime.datetime.now() - player_village.first_village_run_at) > datetime.timedelta(minutes=30):
				self.u.print_with_time_stamp("30 minute first village timeout")
				self.u.print_with_time_stamp("Resetting index")
				player_village.current_index = 0
				player_village.first_village_run_at = datetime.datetime.now()
			elif player_village.current_index == len(self.current_village.villages_to_farm):
				player_village.current_index = 0

			village = self.current_village.villages_to_farm[player_village.current_index]

			sleep(self.u.get_random_float(1,2))

			if self.not_in_meeting_place(self.browser.current_url):
				self.go_to_meeting_place()

			while not self.enough_units(village, player_village.unit_type):
				if (datetime.datetime.now() - loop_started) > datetime.timedelta(minutes=5):
					self.u.print_with_time_stamp("5 minute loop timeout")
					self.u.print_with_time_stamp("Going to next village")
					return
				else:
					self.u.print_with_time_stamp("Not enough units to attack")
					self.u.sleep_for_minutes(1)


			self.send_attack(village, player_village.unit_type)
			player_village.current_index+=1
		return