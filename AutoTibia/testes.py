import tkinter as tk

# Defina as variáveis de entrada globalmente
entrada_email = None
entrada_senha = None

def fazer_autologin():
    # Limpa todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Atualiza o título da janela principal
    root.title("AutoLogin")

    # Adiciona campos de entrada para email e senha
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    global entrada_email
    global entrada_senha

    label_email = tk.Label(frame, text="Email:")
    label_email.grid(row=0, column=0, pady=5)
    entrada_email = tk.Entry(frame)
    entrada_email.grid(row=0, column=1, pady=5)

    label_senha = tk.Label(frame, text="Senha:")
    label_senha.grid(row=1, column=0, pady=5)
    entrada_senha = tk.Entry(frame, show="*")  # O argumento "show" esconde os caracteres digitados
    entrada_senha.grid(row=1, column=1, pady=5)

    # Adiciona o botão "Login"
    botao_login = tk.Button(frame, text="Login", command=realizar_login)
    botao_login.grid(row=2, columnspan=2, pady=10)

    # Adiciona o botão "Voltar"
    botao_voltar = tk.Button(root, text="Voltar", command=voltar_para_menu)
    botao_voltar.pack(pady=10)

def voltar_para_menu():
    # Limpa todos os widgets da janela atual
    for widget in root.winfo_children():
        widget.destroy()

    # Atualiza o título da janela principal
    root.title("Menu Principal")

    # Adiciona novamente o botão "AutoLogin"
    botao_autologin = tk.Button(root, text="AutoLogin", command=fazer_autologin)
    botao_autologin.pack(pady=20)

def realizar_login():
    # Função para lidar com a lógica de login
    email = entrada_email.get()
    senha = entrada_senha.get()
    print(f"Email: {email}, Senha: {senha}")

# Configuração da janela principal
root = tk.Tk()
root.title("Menu Principal")

# Criando o botão AutoLogin
botao_autologin = tk.Button(root, text="AutoLogin", command=fazer_autologin)
botao_autologin.pack(pady=20)

# Iniciando o loop principal
root.mainloop()
