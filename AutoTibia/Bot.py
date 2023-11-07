import pyautogui
import keyboard
import Screenshots
import json
import cv2
import numpy as np
import threading
import tkinter as tk

#REGION_BATTLE = (1190,440,176,65)
REGION_MAP_BATTLE = (1198,25,108,111)
REGION_LOOT = (690,270,150,131)
#POSITION_MANA_FULL = (777,33) #FULL
POSITION_MANA_FULL = (978,33) #HALF
COLOR_MANA = (0, 57, 126)
POSITION_LIFE = (366, 35)
COLOR_LIFE_FULL = (0, 174, 0)
COLOR_LIFE_GREEN = (100, 145, 4)
COLOR_LIFE_YELLOW = (199, 151, 9)

# Direções perto do personagem
DIRECTION1 = (723,295)
DIRECTION2 = (768,295)
DIRECTION3 = (818,296)
DIRECTION4 = (818,343)
DIRECTION5 = (814,386)
DIRECTION6 = (772,389)
DIRECTION7 = (723,385)
DIRECTION8 = (723,344)

#{"path": "SvargrondWinterWolfs/flag_4.png", "wait": 10}, {"path": "SvargrondWinterWolfs/flag_5.png", "wait": 20}, {"path": "SvargrondWinterWolfs/flag_6.png", "wait": 15},
def check_battle():
	return pyautogui.locateOnScreen('C:/Users/Ryan/Desktop/AutoTibia/PNG/Region_Battle.png')
	#print(pyautogui.locateOnScreen('C:/Users/Ryan/Desktop/AutoTibia/PNG/Region_Battle.png'))

def kill_monster(combo):
	if combo == 0:
		while check_battle() == None:
			pyautogui.press('space')
			pyautogui.sleep(1)
			print('procurando outros monstros')
			pyautogui.sleep(1)
	elif combo == 1:
		while check_battle() == None:
			pyautogui.press('space')
			pyautogui.sleep(1)
			pyautogui.press('F10')
			pyautogui.sleep(1)
			print('procurando outros monstros')
			pyautogui.sleep(1)

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

def go_to_flag(path, wait, elevation, direction):
    flag = pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE)
    if flag:
        if elevation == 0:
            # Apenas anda
            x, y = pyautogui.center(flag)
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')
            pyautogui.sleep(wait)
        elif elevation == 1:
            # Usa a corda
            x, y = pyautogui.center(flag)
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')
            pyautogui.sleep(wait)
            pyautogui.press('1')
            pyautogui.sleep(1)
            pyautogui.moveTo(770, 342)
            pyautogui.click(button='left')
        elif elevation == 2:
            # Usa a pá
            x, y = pyautogui.center(flag)
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')
            pyautogui.sleep(wait)
            if direction == 1:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION1)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION1)
                pyautogui.click(button='left')
            elif direction == 2:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION2)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION2)
                pyautogui.click(button='left')
            elif direction == 3:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION3)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION3)
                pyautogui.click(button='left')
            elif direction == 4:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION4)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION4)
                pyautogui.click(button='left')
            elif direction == 5:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION5)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION5)
                pyautogui.click(button='left')
            elif direction == 6:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION6)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION6)
                pyautogui.click(button='left')
            elif direction == 7:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION7)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION7)
                pyautogui.click(button='left')
            elif direction == 8:
                pyautogui.sleep(1)
                pyautogui.press('2')
                pyautogui.sleep(1)
                pyautogui.moveTo(DIRECTION8)
                pyautogui.click(button='left')
                pyautogui.moveTo(DIRECTION8)
                pyautogui.click(button='left')

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

def check_life():
    while True:
        if not (pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_FULL) or pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_GREEN)):
            pyautogui.press('F1')
            print('Enchendo vida...')
            pyautogui.sleep(1)

def check_mana():
    while True:
        while not pyautogui.pixelMatchesColor(POSITION_MANA_FULL[0], POSITION_MANA_FULL[1], COLOR_MANA):
            pyautogui.press('F2')
            print('Enchendo mana...')
            pyautogui.sleep(1)

def run():
    life_thread = threading.Thread(target=check_life)
    mana_thread = threading.Thread(target=check_mana)
    life_thread.daemon = True
    mana_thread.daemon = True
    life_thread.start()
    mana_thread.start()

    while True:
        with open(f'{Screenshots.FOLDER_NAME}/infos.json', 'r') as file:
            data = json.loads(file.read())
        for item in data:
            kill_monster(item ['combo'])
            pyautogui.sleep(1)
            get_loot()
            go_to_flag(item['path'], item['wait'], item ['elevation'], item ['direction'])
            if check_player_position():
                kill_monster(item ['combo'])
                pyautogui.sleep(1)
                get_loot()
                go_to_flag(item['path'], item['wait'], item ['elevation'], item ['direction'])
            eat_food()

#pyautogui.displayMousePosition()
#keyboard.wait('h')
run()