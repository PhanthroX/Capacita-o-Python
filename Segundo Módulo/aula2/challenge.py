from navigation import chrome_browser, PageObjects
from file_manipulation import le_dados_challenge
from selenium.webdriver.common.by import By
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from logging import basicConfig
from logging import critical, error, warning, info, debug
import logging 
import logging.config
import pyscreenshot as ps
import time
import pymsteams


logging.config.fileConfig('./logs/logging.conf')
logger = logging.getLogger('root')

# Configuração básica de log da própria linguagem. Passa-se os parâmetros necessários para cada ocasião.

# basicConfig(
#     level=INFO,
#     filename='./logs/log_sicredi.log',
#     filemode='a',
#     format='%(levelname)s:%(asctime)s:%(message)s'
# )

def challenge(arquivo):
    site_challenge = "https://rpachallenge.com"
    driver = chrome_browser(site_challenge)
    #arquivo = "./assets/challenge.xlsx"

    PageObjects.inicia_challenge(driver)
    info(f'Arquivo {arquivo} criado com sucesso. Iniciando Challenge')

    for i in range(10):
        row = le_dados_challenge(arquivo, i)
        PageObjects.executa_challenge(driver, row)

    time.sleep(2)

    resultado = driver.find_element(By.CLASS_NAME,"message2")
    resultado = resultado.text

    return resultado

# Configuração para rodar apenas este arquivo sem precisar chamar uma função.
if __name__ == '__main__':
    challenge('./assets/challenge.xlsx')
