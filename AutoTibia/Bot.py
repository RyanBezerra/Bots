import pyautogui
import keyboard
import Screenshots
import json
import cv2
import numpy as np

REGION_BATTLE = (1190,440,176,65)
REGION_MAP_BATTLE = (1198,25,108,111)
REGION_LOOT = (690,270,150,131)
POSITION_MANA_FULL = (777,33)
COLOR_MANA = (0, 57, 126)
POSITION_LIFE = (366, 35)
COLOR_LIFE_FULL = (0, 174, 0)
COLOR_LIFE_GREEN = (100, 145, 4)
COLOR_LIFE_YELLOW = (199, 151, 9)
#{"path": "SvargrondWinterWolfs/flag_4.png", "wait": 10}, {"path": "SvargrondWinterWolfs/flag_5.png", "wait": 20}, {"path": "SvargrondWinterWolfs/flag_6.png", "wait": 15},
def check_battle():
	return pyautogui.locateOnScreen('C:/Users/Ryan/Desktop/AutoTibia/PNG/Region_Battle.png', region = REGION_BATTLE)
	#print(pyautogui.locateOnScreen('C:/Users/Ryan/Desktop/AutoTibia/PNG/Region_Battle.png'))


#check_battle() 

def kill_monster():
	contador = 0
	while check_battle() == None:
		pyautogui.press('space')
#		while check_battle() != None:
		pyautogui.sleep(2)
#			print('esperando os monstros morrerem')
		print('procurando outros monstros')
		pyautogui.sleep(2)

#kill_monster()

def get_loot():

	for _ in range(8):
		pyautogui.moveTo(723,295)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		pyautogui.moveTo(768,295)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		pyautogui.moveTo(818,296)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		pyautogui.moveTo(818,343)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		pyautogui.moveTo(814,386)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		pyautogui.moveTo(772,389)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		pyautogui.moveTo(723,385)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		pyautogui.moveTo(723,344)
		pyautogui.click(button = "right")
		pyautogui.sleep(0.1)
		return

#get_loot()

def go_to_flag(path, wait):
	flag = pyautogui.locateOnScreen(path, confidence = 0.8, region = REGION_MAP_BATTLE)
	if flag:
		x, y = pyautogui.center(flag)
		pyautogui.moveTo(x, y)
		pyautogui.click()
		pyautogui.sleep(wait)

def check_player_position():
	return pyautogui.locateOnScreen('C:/Users/Ryan/Desktop/AutoTibia/PNG/Player_On_Map.png', confidence = 0.8, region = REGION_MAP_BATTLE)

def check_status(name, delay, x, y, rgb, button_name):
	print(f'checando {name}...')
	pyautogui.sleep(delay)
	if pyautogui.pixelMatchesColor(x, y, rgb):
		pyautogui.press(button_name)

def eat_food():
	pyautogui.press('F3')
	print('comendo comida...')

#pyautogui.displayMousePosition()

def run():
	while True:
		with open(f'{Screenshots.FOLDER_NAME}/infos.json', 'r') as file:
			data = json.loads(file.read())
		for item in data:
			kill_monster()
			pyautogui.sleep(1)
			get_loot()
			go_to_flag(item['path'], item['wait'])
			if check_player_position():
				kill_monster()
				pyautogui.sleep(1)
				get_loot()
				go_to_flag(item['path'], item['wait'])
			eat_food()
			check_status('mana', 1, *POSITION_MANA_FULL, COLOR_MANA, 'F4')
			check_status('life', 2, *POSITION_MANA_FULL, COLOR_LIFE_GREEN, 'F4')
			while pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_FULL) is False:
				pyautogui.press('F4')
				pyautogui.sleep(1)

#keyboard.wait('h')
run()

