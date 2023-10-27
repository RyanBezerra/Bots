# Bots

# AutoTibia

O AutoTibia é um projeto que desenvolvi de forma amadora, com o propósito exclusivo de ser executado em meu próprio computador e sob minha supervisão. Cada linha de código foi elaborada com a intenção específica de atender às minhas necessidades, sem a pretensão de ser dinâmica ou portável para outros sistemas. Decidi compartilhá-lo no GitHub para que outros entusiastas e desenvolvedores amadores, assim como eu, possam ter acesso a um modelo atualizado, a partir do qual podem trabalhar e aprimorar suas próprias soluções. Acredito que disponibilizar esse projeto pode contribuir para a comunidade de pessoas que compartilham do mesmo interesse e também estão explorando o desenvolvimento de automações para suas atividades.

## Funcionalidades

- Verifica se o jogador está em uma batalha.
- Realiza ações para derrotar monstros.
- Coleta itens (loot) após derrotar monstros.
- Navega para uma posição específica no mapa.
- Verifica a posição atual do jogador no mapa.
- Verifica o status de vida e mana do personagem.
- Comer comida.
- Executa um loop principal para repetir as ações.
- Carregar informações de um arquivo JSON para facilitar a automação de novas hunts.
- Automatiza o processo de matar monstros e coletar itens.
- Interação com elementos na tela por meio do movimento do cursor e cliques.
- Implementa um fluxo de controle baseado em verificações e condições.
- Hunts setadas: Dawnport, SwampTroll(Venore), Salamander Cave(Venore), Winter Wolf Hunt(Sul de Svargrond)

## Em desenvolvimento

- [ ] Verificar se a criatura está em combate
- [X] Caso a vida COLOR_LIFE_FULL seja False, usar curas até COLOR_LIFE_FULL ser True
- [ ] Setar rotações das spells de ataque de acordo com as hunts setadas



# Extrator de Vídeos da Web usando Selenium e Beautiful Soup

Este projeto demonstra como automatizar a extração de vídeos de uma página web específica usando as bibliotecas Selenium e Beautiful Soup em Python. O código é projetado para baixar vídeos da página 'https://br.ifunny.co/top-memes/day', mas pode ser adaptado para outras finalidades.

## Pré-requisitos

Antes de usar este código, certifique-se de que você tenha as seguintes bibliotecas instaladas em seu ambiente Python:

- [Selenium](https://pypi.org/project/selenium/): Para automatizar a interação com o navegador.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Para analisar o HTML da página.
- [Requests](https://pypi.org/project/requests/): Para baixar o conteúdo da web.
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/): O WebDriver específico do navegador que corresponde à versão do Microsoft Edge que você está usando.

Você também deve ter o Microsoft Edge instalado em seu sistema.

## Como Usar

1. Certifique-se de ter todos os pré-requisitos instalados e o Microsoft Edge WebDriver configurado.

2. Clone este repositório para o seu sistema.

3. Execute o script Python `extract_videos.py` para iniciar a extração dos vídeos. O código abrirá o navegador, acessará a página desejada e baixará os vídeos para um diretório local chamado 'videos'.

4. Após a execução do script, os vídeos estarão disponíveis no diretório 'videos'.

## Estrutura do Projeto

- `extract_videos.py`: O script principal que automatiza a extração dos vídeos.
- `videos/`: O diretório onde os vídeos extraídos são salvos.
- `div_cy00_13az.html`: O arquivo HTML temporário baixado da página.

## Notas

- Certifique-se de que o caminho para o executável do Microsoft Edge WebDriver esteja definido corretamente no script.

- Lembre-se de respeitar os termos de uso e direitos autorais ao extrair e usar o conteúdo da web.

Este é um exemplo básico de como automatizar a extração de conteúdo da web usando Python. Você pode personalizar e expandir este código para atender às suas necessidades específicas.
