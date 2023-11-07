import pyautogui
import keyboard
from pynput.keyboard import Listener
from pynput import keyboard
import json
import os

#FOLDER_NAME = 'LagunaBloodCrabs'
FOLDER_NAME = 'SvargrondWinterWolfs'

#'SvargrondWinterWolfs'

def create_folder():
	if not os.path.isdir(FOLDER_NAME):
		os.mkdir(FOLDER_NAME)


class Rec:
	def __init__(self):
		create_folder()
		self.count = 0
		self.coordinates = []

	def photo(self):
		x, y = pyautogui.position()
		photo = pyautogui.screenshot(region = (x - 3, y - 3, 6, 6))
		path = f'{FOLDER_NAME}/flag_{self.count}.png'
		photo.save(path)
		self.count = self.count + 1
		infos = {
			"path": path,
			"wait": 15,
			"elevation": 0,
			"direction": 0,
			"combo": 0
		}
		self.coordinates.append(infos)

	def key_code(self, key):
		if key == keyboard.Key.esc:
			with open(f'{FOLDER_NAME}/infos.json', 'w') as file:
				file.write(json.dumps(self.coordinates))
			return False
		if key == keyboard.Key.home:
			self.photo()

	def start(self):
		with Listener(on_press = self.key_code) as listener:
			listener.join()

#record = Rec()
#record.start()