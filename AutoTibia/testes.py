# Atribuindo números às opções de nomes de pasta
opcoes_nomes = {1: 'LagunaBloodCrabs', 2: 'SvargrondWinterWolfs', 3: 'Dawnport', 4: 'SalamanderCave', 5: 'VenoreSwampTroll'}

# Variável global para armazenar o nome da pasta escolhido
FOLDER_NAME = None

# Função que pergunta ao usuário e atribui um novo nome à variável FOLDER_NAME
def escolher_novo_folder_name():
    global FOLDER_NAME  # Indicando que estamos utilizando a variável global

    # Se FOLDER_NAME já estiver definido, perguntar se o usuário deseja mantê-lo ou escolher outro
    if FOLDER_NAME:
        manter_atual = input(f"O nome da pasta atual é '{FOLDER_NAME}'. Deseja mantê-lo? (S/N): ")
        if manter_atual.lower() == 's':
            return

    # Exibindo opções de nomes de pasta
    print("Escolha o número correspondente ao novo nome da pasta:")
    for num, nome in opcoes_nomes.items():
        print(f"{num} - '{nome}'")

    # Obtendo a escolha do usuário
    opcao = input("Digite o número correspondente ao novo nome desejado: ")
    
    # Mapeando a escolha do usuário para o nome da pasta
    novo_folder_name = opcoes_nomes.get(int(opcao), None)
    
    # Verificando se o nome da pasta é válido
    if novo_folder_name:
        # Atribuindo o novo nome à variável FOLDER_NAME
        FOLDER_NAME = novo_folder_name
        print(f"Novo nome da pasta atribuído: '{FOLDER_NAME}'")

        # Salvando o nome da pasta no arquivo para manter entre execuções
        with open("config.txt", "w") as config_file:
            config_file.write(FOLDER_NAME)
    else:
        print("Opção inválida.")

# Tenta ler o nome da pasta salvo no arquivo para manter entre execuções
try:
    with open("config.txt", "r") as config_file:
        FOLDER_NAME = config_file.read()
        print(f"Nome da pasta obtido do arquivo: '{FOLDER_NAME}'")
except FileNotFoundError:
    pass

# Chamando a função para escolher e atribuir um novo nome à variável FOLDER_NAME
#escolher_novo_folder_name()

print(FOLDER_NAME)
