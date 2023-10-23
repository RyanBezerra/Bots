from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import os

# Inicializa o WebDriver do Microsoft Edge
driver = webdriver.Edge(executable_path='C:\\Users\\Ryan\\Desktop\\AutoEdge\\msedgedriver.exe')

# URL da página que contém a div desejada
url = 'https://br.ifunny.co/top-memes/day'

# Abre a página da web
driver.get(url)

# Use espera explícita para aguardar a presença da div
wait = WebDriverWait(driver, 10)  # Aguarda até 10 segundos
div_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.CY00._13AZ')))

# Obtenha o HTML interno da div
div_html = div_element.get_attribute('innerHTML')

# Salve o HTML em um arquivo
with open('div_cy00_13az.html', 'w', encoding='utf-8') as file:
    file.write(div_html)

print('HTML da div salvo com sucesso em "div_cy00_13az.html"')

# Fecha o navegador
driver.quit()

# Abra o arquivo HTML que você baixou anteriormente
with open('div_cy00_13az.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Analise o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontre todas as divs com a classe "_0ZvA"
divs_0ZvA = soup.find_all('div', class_='_0ZvA')

# Crie um diretório para salvar os vídeos
os.makedirs('videos', exist_ok=True)

# Percorra as divs e extraia os links do atributo "data-src"
for div in divs_0ZvA:
    # Encontre todos os elementos com o atributo "data-src"
    elements_with_data_src = div.find_all(attrs={"data-src": True})

    for element in elements_with_data_src:
        data_src = element['data-src']

        if data_src and data_src.endswith('.mp4'):
            # Nomeie o arquivo com base no último segmento do URL
            filename = os.path.join('videos', os.path.basename(data_src))

            # Baixe o vídeo
            response = requests.get(data_src)

            if response.status_code == 200:
                with open(filename, 'wb') as video_file:
                    video_file.write(response.content)
                print('Vídeo baixado:', filename)
            else:
                print('Falha ao baixar o vídeo:', data_src)
                
# Função para excluir o arquivo HTML baixado
def excluir_arquivo_html():
    if os.path.exists('div_cy00_13az.html'):
        os.remove('div_cy00_13az.html')
        print('Arquivo HTML excluído com sucesso.')
    else:
        print('O arquivo HTML não foi encontrado.')

# Chame a função para excluir o arquivo HTML
excluir_arquivo_html()