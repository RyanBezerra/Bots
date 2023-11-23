import pyautogui
import keyboard
from pynput.keyboard import Listener
from pynput import keyboard
import json
import cv2
import numpy as np
import threading
import tkinter as tk
from tkinter import ttk
import TKinterModernThemes as TKMT
import ctypes
import pygetwindow as gw
import os

#REGION_BATTLE = (1190,440,176,65)
REGION_MAP_BATTLE = (1198,25,108,111)
REGION_CONDITIONS = (717,58,108,17)
REGION_LOOT = (690,270,150,131)
#POSITION_MANA_FULL = (777,33) #FULL
POSITION_MANA_FULL = (978,33) #HALF
COLOR_MANA = (0, 57, 126)
POSITION_LIFE = (366, 35)
COLOR_LIFE_FULL = (0, 174, 0)
COLOR_LIFE_GREEN = (100, 145, 4)
COLOR_LIFE_YELLOW = (183, 139, 8)
COLOR_LIFE_RED = (174, 44, 44)
x1, y1 = (1213, 456)
expected_color = (254, 0, 0)
CENTRO_MAPA = (1252, 82)
CRIAR_MARCADOR = (1184, 93)
CONFIRMAR_MARCADOR = (737, 457)


# Direções perto do personagem
DIRECTION1 = (723,295)
DIRECTION2 = (768,295)
DIRECTION3 = (818,296)
DIRECTION4 = (818,343)
DIRECTION5 = (814,386)
DIRECTION6 = (772,389)
DIRECTION7 = (723,385)
DIRECTION8 = (723,344)

MARCADORES = [
    (563, 405), (584, 405), (605, 405), (626, 405), (647, 405),
    (668, 405), (689, 405), (710, 405), (731, 405), (752, 405)
]

#FOLDER_NAME = 'Crawler'

# Lista de opções para a combo box
opcoes_folders = [
    'LagunaBloodCrabs',
    'SvargrondWinterWolf',
    'Dawnport',
    'SalamanderCave',
    'VenoreSwampTroll',
    'Feyrist',
    'Putrid',
    'PiratCave',
    'Crawler'
]

def selecionar_folder():
    global FOLDER_NAME
    selected_folder = combo_var.get()
    FOLDER_NAME = selected_folder
    print(FOLDER_NAME)
    # Faça o que precisar com o nome da pasta selecionada


def create_folder():
    if not os.path.isdir(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)


class Rec:
    def __init__(self):
        create_folder()
        self.count = 0
        self.current_marcador_index = 0
        self.coordinates = []

    def setarhunt(self, marcador):
        pyautogui.moveTo(CENTRO_MAPA)
        pyautogui.click(button="right")
        pyautogui.sleep(1)
        pyautogui.moveTo(CRIAR_MARCADOR)
        pyautogui.click(button="left")
        pyautogui.sleep(1)
        pyautogui.moveTo(marcador)
        pyautogui.click(button="left")
        pyautogui.sleep(1)
        pyautogui.moveTo(CONFIRMAR_MARCADOR)
        pyautogui.click(button="left")
        pyautogui.sleep(1)
        pyautogui.moveTo(CENTRO_MAPA)

    def photo(self):
        self.current_marcador_index = (self.current_marcador_index + 1) % len(MARCADORES)
        x, y = pyautogui.position()
        photo = pyautogui.screenshot(region = (x - 4, y - 4, 9, 9))
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
            self.setarhunt(MARCADORES[self.current_marcador_index])
            pyautogui.sleep(1)
            self.photo()
            print('Feito!')

    def start(self):
        with Listener(on_press = self.key_code) as listener:
            listener.join()


def iniciar():
    email = entry_email.get()
    senha = entry_senha.get()

    if not email or not senha:
        print("Erro: Preencha ambos os campos de e-mail e senha.")
        return

    POSITION_EMAIL = (705, 346)
    POSITION_PASSWORD = (704, 377)
    POSITION_LOGIN = (763, 460)
    POSITION_Abertura_Italiana = (677, 254)
    POSITION_Defesa_eslava = (681, 316)
    POSITION_Defesa_Siciliana = (677, 391)
    POSITION_INICIAR = (962, 584)

    pyautogui.sleep(1)
    pyautogui.moveTo(POSITION_EMAIL)
    pyautogui.click(button='left')
    pyautogui.sleep(1)
    pyautogui.write(email)
    pyautogui.sleep(1)

    pyautogui.moveTo(POSITION_PASSWORD)
    pyautogui.click(button='left')
    pyautogui.sleep(1)
    pyautogui.write(senha)
    pyautogui.sleep(1)

    pyautogui.moveTo(POSITION_LOGIN)
    pyautogui.click(button='left')
    pyautogui.sleep(3)

    if aba_retratil.index(tk.CURRENT) == 0:
        pyautogui.moveTo(POSITION_Defesa_Siciliana)
    elif aba_retratil.index(tk.CURRENT) == 1:
        pyautogui.moveTo(POSITION_Abertura_Italiana)
    elif aba_retratil.index(tk.CURRENT) == 2:
        pyautogui.moveTo(POSITION_Defesa_eslava)

    pyautogui.click(button='left')
    pyautogui.sleep(1)

    pyautogui.moveTo(POSITION_INICIAR)
    pyautogui.click(button='left')
    pyautogui.sleep(1)


def salvar():
    email = entry_email.get()
    senha = entry_senha.get()

    if not email or not senha:
        print("Erro: Preencha ambos os campos de e-mail e senha.")
        return

    dados = {"email": email, "senha": senha}

    with open("configs.json", "w") as arquivo:
        json.dump(dados, arquivo)

    print("Salvo: As credenciais foram salvas com sucesso!")


def carregar():
    try:
        with open("configs.json", "r") as arquivo:
            dados = json.load(arquivo)

        entry_email.delete(0, tk.END)
        entry_senha.delete(0, tk.END)

        entry_email.insert(0, dados["email"])
        entry_senha.insert(0, dados["senha"])

        print("Carregado: As credenciais foram carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado: O arquivo 'configs.json' não foi encontrado.")


def opacidade():

    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x00080000
    LWA_ALPHA = 0x00000002

    OPACITY = 1# 0 -- 255
    WINDOW_TITLE = "Tibia"
    target_window = gw.getWindowsWithTitle(WINDOW_TITLE)[0]

    if target_window is not None:
        target_hwnd = target_window._hWnd

        ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)
        ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)

        ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, OPACITY, LWA_ALPHA)

        print("Opacidade da janela modificada.")
    else:
        print("Janela não encontrada.")


def check_battle():
	return pyautogui.locateOnScreen('C:/Users/Ryan/Desktop/AutoTibia/PNG/Region_Battle.png')


def check_target_pixel():
     return pyautogui.pixelMatchesColor(x1, y1, expected_color)


def kill_monster(combo):
    if combo == 0:
        while check_battle() == None:
            pyautogui.press('space')
            pyautogui.press('F5')
            pyautogui.press('F6')
            pyautogui.press('F7')
            pyautogui.press('F8')
            pyautogui.sleep(1)
            while check_target_pixel() is True:
                print('Matando...')
                pyautogui.press('F5')
                pyautogui.press('F6')
                pyautogui.press('F7')
                pyautogui.press('F8')
                pyautogui.sleep(1)
            print('Procurando outros monstros')
    elif combo == 1:
        while check_battle() == None:
            pyautogui.press('space')
            pyautogui.sleep(1)
            while check_target_pixel() is True:
                print('Matando...')
                pyautogui.sleep(1)
            print('Procurando outros monstros')


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


def go_to_flag(path, wait, elevation, direction):
    flag = pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE)
    if flag:
        if elevation == 0:
            # Apenas anda
            x, y = pyautogui.center(flag)
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')
            while pyautogui.locateOnScreen(path, region=(1252 - 4,82 - 4,9,9)) == None:
                print('Esperando')
                pyautogui.sleep(1)
                antigo = pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE)
                pyautogui.sleep(1)
                if antigo == pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE):
                    break


        elif elevation == 1:
            # Usa a corda
            x, y = pyautogui.center(flag)
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')
            while pyautogui.locateOnScreen(path, region=(1252 - 4,82 - 4,9,9)) == None:
                print('Esperando')
                pyautogui.sleep(1)
                antigo = pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE)
                pyautogui.sleep(1)
                if antigo == pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE):
                    break
            if direction == 1:
                pyautogui.sleep(1)
                pyautogui.press('1')
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
        elif elevation == 2:
            # Usa a pá
            x, y = pyautogui.center(flag)
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')
            while pyautogui.locateOnScreen(path, region=(1252 - 4,82 - 4,9,9)) == None:
                print('Esperando')
                pyautogui.sleep(1)
                antigo = pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE)
                pyautogui.sleep(1)
                if antigo == pyautogui.locateOnScreen(path, confidence=0.8, region=REGION_MAP_BATTLE):
                    break
            if direction == 1:
                pyautogui.sleep(1)
                pyautogui.press('1')
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


def check_conditions():
    while haste_var.get():
        try:
            # Localiza a posição da imagem na tela
            Haste = pyautogui.locateOnScreen('C:\\Users\\Ryan\\Desktop\\AutoTibia\\PNG\\Haste.png', confidence=0.8, region=REGION_CONDITIONS)

            # Se a imagem não for encontrada, faça alguma coisa
            if Haste is None:
                pyautogui.press('F12')

        except Exception as e:
            print(f"Erro: {e}")

        pyautogui.sleep(1)


def check_life():
    while ligado:
        if (pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_GREEN)):
            pyautogui.press('F4')
            print('Enchendo vida...')
        if (pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_YELLOW) or pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_RED)):
            pyautogui.press('F1')
            pyautogui.press('F4')
            print('Enchendo vida com pot...')


def check_mana():
    while ligado:
        if not pyautogui.pixelMatchesColor(POSITION_MANA_FULL[0], POSITION_MANA_FULL[1], COLOR_MANA):
            if not (pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_YELLOW) or pyautogui.pixelMatchesColor(366, 35, COLOR_LIFE_RED)):
                pyautogui.press('F2')
                print('Enchendo mana...')


def run():
    while ligado:
        with open(f'{FOLDER_NAME}/infos.json', 'r') as file:
            data = json.loads(file.read())
        for item in data:
            if ligado == False:
                    break
            kill_monster(item ['combo'])
            pyautogui.sleep(1)
            if ligado == False:
                    break
            get_loot()
            if ligado == False:
                    break
            go_to_flag(item['path'], item['wait'], item ['elevation'], item ['direction'])
            if check_player_position():
                if ligado == False:
                    break
                kill_monster(item ['combo'])
                if ligado == False:
                    break
                pyautogui.sleep(1)
                get_loot()
                if ligado == False:
                    break
                go_to_flag(item['path'], item['wait'], item ['elevation'], item ['direction'])
                if ligado == False:
                    break
            eat_food()
            if ligado == False:
                break


def ligar():
    global ligado
    ligado = True
    print("O Bot está ativado.")
    thread_check_conditions = threading.Thread(target=check_conditions)
    life_thread = threading.Thread(target=check_life)
    mana_thread = threading.Thread(target=check_mana)
    run_thread = threading.Thread(target=run)
    thread_check_conditions.daemon = True
    life_thread.daemon = True
    mana_thread.daemon = True
    run_thread.daemon = True
    thread_check_conditions.start()
    life_thread.start()
    mana_thread.start()
    run_thread.start()

    if haste_var.get():
        print("O haste está ativado.")
    else:
        print("O haste está desativado.")


def desligar():
    global ligado
    ligado = False
    print("O Bot está desativado.")


# Criar janela
janela = tk.Tk()
janela.title("Menu")

# Adicionar captura e manter no topo
janela.grab_set()
janela.attributes("-topmost", True)

# Criar o widget para a area de login automatico
label_email = tk.Label(janela, text="Email:")
label_senha = tk.Label(janela, text="Senha:")
entry_email = tk.Entry(janela)
entry_senha = tk.Entry(janela, show="*")
botao_iniciar = tk.Button(janela, text="Login", command=iniciar)

label_email.grid(row=0, column=0, sticky=tk.E)
label_senha.grid(row=1, column=0, sticky=tk.E)
entry_email.grid(row=0, column=1)
entry_senha.grid(row=1, column=1)
botao_iniciar.grid(row=1, column=2, pady=10, padx=5)

# Criar widgets
botao_stop = tk.Button(janela, text="Desligar", command=desligar)
botao_run = tk.Button(janela, text="Ligar", command=ligar)
botao_opacidade = tk.Button(janela, text="Opacidade", command=opacidade)
botao_salvar = tk.Button(janela, text="Salvar", command=salvar)
botao_carregar = tk.Button(janela, text="Carregar", command=carregar)

# Criar o widget Notebook para as abas retráteis
aba_retratil = ttk.Notebook(janela)

# Adicionar frames para cada aba
frame_siciliana = tk.Frame(aba_retratil)
frame_italiana = tk.Frame(aba_retratil)
frame_eslava = tk.Frame(aba_retratil)

# Variável para armazenar a escolha da combo box
combo_var = tk.StringVar(janela)
combo_var.set(opcoes_folders[0])

# Variável de controle para a check box
haste_var = tk.BooleanVar()

# Adicionar abas ao Notebook
aba_retratil.add(frame_siciliana, text="Defesa Siciliana")
aba_retratil.add(frame_italiana, text="Abertura Italiana")
aba_retratil.add(frame_eslava, text="Defesa Eslava")

# Criar a combo box
combo_box = tk.OptionMenu(janela, combo_var, *opcoes_folders)
combo_box.grid(row=3, column=1, pady=10, padx=5)

# Botão para confirmar a seleção
botao_confirmar = tk.Button(janela, text="Confirmar", command=selecionar_folder)
botao_confirmar.grid(row=3, column=2, pady=10, padx=5)

# Criar a check box
check_box = tk.Checkbutton(janela, text="Haste", variable=haste_var)
check_box.grid(row=4, column=1, pady=10, padx=5)

aba_retratil.grid(row=2, column=0, columnspan=3, pady=10, padx=5)

botao_stop.grid(row=5, column=5, pady=10, padx=5)
botao_run.grid(row=5, column=4, pady=10, padx=5)
botao_opacidade.grid(row=5, column=2, pady=10, padx=5)
botao_salvar.grid(row=5, column=1, pady=10, padx=5)
botao_carregar.grid(row=5, column=0, pady=10, padx=5)

# Iniciar o loop de eventos
#record = Rec()
#record.start()
#print (pyautogui.pixel(366, 35))
janela.mainloop()

#run()
#print(pyautogui.locateOnScreen('C:/Users/Ryan/Desktop/AutoTibia/PNG/Region_Battle.png'))
#pyautogui.displayMousePosition()
#keyboard.wait('h')

