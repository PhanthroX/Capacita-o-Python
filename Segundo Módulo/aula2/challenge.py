from navigation import chrome_browser, PageObjects
from file_manipulation import le_dados_challenge
from selenium.webdriver.common.by import By
import time

def challenge(arquivo):
    site_challenge = "https://rpachallenge.com"
    driver = chrome_browser(site_challenge)
    #arquivo = "./assets/challenge.xlsx"

    PageObjects.inicia_challenge(driver)

    for i in range(10):
        row = le_dados_challenge(arquivo, i)
        PageObjects.executa_challenge(driver, row)

    time.sleep(2)

    resultado = driver.find_element(By.CLASS_NAME,"message2")
    resultado = resultado.text

    return resultado
