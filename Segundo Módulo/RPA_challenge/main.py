from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Atribuição de variáveis
site = "https://rpachallenge.com/"

arquivo = "Segundo Módulo\RPA_challenge\challenge.xlsx"

df_registros = pd.read_excel(arquivo)

print(df_registros.head())

# Configurar Navegação
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# Importação do Chrome test e Chrome Driver. Por se tratar de um arquivo muito grande não foi possível adicionar o arquivo aqui.
chrome_options.binary_location = "Segundo Módulo/RPA_challenge/chrome-win64/chrome-win64/chrome.exe"
chrome_driver_path = "Segundo Módulo/RPA_challenge/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options, service=service_options)
driver.get(site)

print("Inicializando...")
botao = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
botao.click()

for i, r in df_registros.iterrows():
    first_name = r["First Name"]
    last_name = r["Last Name "]
    company = r["Company Name"]
    role = r["Role in Company"]
    email = r["Email"]
    phone = r["Phone Number"]
    address = r["Address"]

#    print(first_name)

#    print("Preenchendo cargo...")

    textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelRole']")
    textbox.clear()
    textbox.send_keys(role)

#    print("Preenchendo nome...")

    textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelFirstName']")
    textbox.clear()
    textbox.send_keys(first_name)

#    print("Preenchendo sobrenome...")

    textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelLastName']")
    textbox.clear()
    textbox.send_keys(last_name)

#    print("Preenchendo empresa...")

    textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelCompanyName']")
    textbox.clear()
    textbox.send_keys(company)

#    print("Preenchendo email...")

    textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelEmail']")
    textbox.clear()
    textbox.send_keys(email)

#    print("Preenchendo endereço...")

    textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelAddress']")
    textbox.clear()
    textbox.send_keys(address)

#   print("Preenchendo telefone...")

    textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelPhone']")
    textbox.clear()
    textbox.send_keys(phone)

#    print("Enviando...")
    botao = driver.find_element(By.XPATH, "//input[@type='submit']")
    botao.click()

time.sleep(5)

print("Processo finalizado...")

driver.close()
