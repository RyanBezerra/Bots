from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-logging')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('w3c', True)

driver.maximize_window()

driver.get('https://blaze-4.com/pt/')

sleep(5)
print('Atualizando site...')
driver.refresh()

print('iniciando login...')
driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div[2]/div/div/div[1]/a').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@id="auth-modal"]/div/form/div[1]/div/input').send_keys('Bot01@gmail.com')
sleep(3)
driver.find_element(By.XPATH,'//*[@id="auth-modal"]/div/form/div[2]/div/input').send_keys('Senha123')
sleep(3)
driver.find_element(By.XPATH,'//*[@id="auth-modal"]/div/form/div[4]/button').click()
sleep(3)

print('Acessando crash...')
driver.get('https://blaze-4.com/pt/games/crash')
sleep(3)

print('Configurando crash...')
driver.find_element(By.XPATH,'//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[2]/div[1]/input').send_keys('2')
sleep(3)

numeros_antigos = set()

while True:
    try:
        # Encontre a div com a classe "entries"
        div_element = driver.find_element(By.CLASS_NAME, 'entries')

        # Encontre todos os elementos <span> dentro da div
        spans = div_element.find_elements(By.XPATH, './/span')

        # Extraia os textos dos spans, converta em números float
        numeros_novos = [float(span.text.replace('X', '').replace(',', '.')) for span in spans[:2] if span.text]

        sleep(1)

        # Verifique se há diferença entre os conjuntos de números novos e antigos
        if numeros_novos != numeros_antigos:
            # Imprima os novos números
            print(' '.join(map(str, numeros_novos)))

            # Atualize os números antigos
            numeros_antigos = numeros_novos

            # Verifique se os dois primeiros números são menores que 2
            if all(num < 2 for num in numeros_novos):
                print("Aposte, o método foi detectado")

    except Exception as e:
        print(f"Erro: {e}")