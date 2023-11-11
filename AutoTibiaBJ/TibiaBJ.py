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
#options.add_argument('--headless')
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

driver.get('https://tibiablackjack.com/')

sleep(5)
print('Atualizando site...')
driver.refresh()

print('Clicando no botão de que estou ciente...')

WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/footer/div/div[4]/div/div/button'))
    )                                           

driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/footer/div/div[4]/div/div/button').click()
sleep(3)

print('iniciando login...')
driver.find_element(By.XPATH,'//*[@id="root"]/nav/section[2]/div[2]/div/button').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/footer/div/div[4]/div/div/div[2]/form/div[1]/input').send_keys('Seuemail@gmail')
sleep(3)
print('Faça o captcha dentro de 15 segundos')
driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/footer/div/div[4]/div/div/div[2]/form/div[2]/input').send_keys('suasenha')
sleep(15)
driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/footer/div/div[4]/div/div/div[2]/form/button[2]').click()
sleep(3)

print('Acessando crash...')
driver.get('https://tibiablackjack.com/crash')

numeros_antigos = []

while True:
    try:
        # Encontre a div com a classe "sc-czUNiH haisVB"
        div_element = driver.find_element(By.CLASS_NAME, 'sc-czUNiH')

        # Encontre todos os elementos <span> dentro da div
        spans = div_element.find_elements(By.XPATH, './/span')

        # Extraia os textos dos spans, converta em números float
        numeros_novos = [float(span.text.replace('x', '')) for span in spans[:4] if span.text]

        # Verifique se os novos números são diferentes dos antigos
        if numeros_novos != numeros_antigos:
            # Imprima os novos números
            print(' '.join(map(str, numeros_novos)))

            # Atualize os números antigos
            numeros_antigos = numeros_novos

            # Verifique se quatro primeiros números são menores que 2
            if all(num < 2 for num in numeros_novos):
                print("Aposte, o método foi detectado")
                sleep(5)
                driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div/div/section/div/div[2]/section/div[2]/button').click()

    except Exception as e:
        print(f"Erro: {e}")


#driver.quit()
