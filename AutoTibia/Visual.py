import TKinterModernThemes as TKMT
from tkinter import ttk
import tkinter as tk

class App(TKMT.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("AutoTibia", theme, mode, usecommandlineargs, usethemeconfigfile)

        self.button_frame = self.addLabelFrame("Menu")  # colocado na linha 1, coluna 0

        self.button_state = True  # Variável para controlar o estado do botão
        self.toggle_button = ttk.Button(self.button_frame.master, text="Off")
        self.toggle_button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.toggle_button['command'] = self.toggle_button_state  # Configura a função a ser chamada quando o botão é clicado

        self.login_frame = self.addLabelFrame("Opção de login automático")

        # Opções da caixa de opções
        opcoes = ["Defesa eslava", "Defesa Siciliana", "Abertura Italiana"]

        # Crie a caixa de opções (combobox) dentro do frame "Opção de login automático"
        self.opcao_var = tk.StringVar(value=opcoes[0])  # Valor inicial da caixa de opções

        self.opcao_combobox = ttk.Combobox(self.login_frame.master, values=opcoes, textvariable=self.opcao_var, state="readonly")
        self.opcao_combobox.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.debugPrint()
        self.run()

    def toggle_button_state(self):
        # Função para alternar o estado do botão (ligado/desligado)
        if self.button_state:
            self.toggle_button.config(text="On")
        else:
            self.toggle_button.config(text="Off")
        self.button_state = not self.button_state

if __name__ == "__main__": 
    App("park", "dark")


#Opção de login automático -

#Escolhe o char (caixa de seleção)

#Opacidade definida pelo usuário (barra deslizante 1 a 255)

#Botão aplicar