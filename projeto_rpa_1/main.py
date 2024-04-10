from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import keyring
import navigation
import pandas as pd
import preencher
# import logging

# logging.config.fileConfig('./logs/logging.conf')
# logger = logging.getLogger('root')

login = "jane007"
password = keyring.get_password('LoginRPA', 'ChaveSecretaPython')

# Abre navegador
driver = navigation.chrome_browser('https://rpaexercise.aisingapore.org/login')

# Localizar o elemento de entrada de texto pelo XPath
usuario = driver.find_element(By.XPATH, '//*[@id="outlined-search"]')

# Preencher o valor desejado no elemento de entrada de texto
usuario.send_keys(login)

# Localizar o elemento de entrada de texto pelo XPath
usuario = driver.find_element(By.XPATH, '//*[@id="password"]')

# Preencher o valor desejado no elemento de entrada de texto
usuario.send_keys(password)

# Clica em logar
botao = driver.find_element(By.XPATH, '//*[@id="login"]')
botao.click()

df = pd.read_csv(".\\datatable.csv", delimiter=",")
print(df.head())

for i, r in df.iterrows():
    
    time.sleep(5)

    # Aguarda botão e clica pra startar o preenchimento
    new_job = driver.find_element(By.XPATH, '//*[@id="newJobPosting"]/span[1]')
    new_job.click()
    
    preencher.preenche_job(driver=driver, row=r, i=i, caminhoScreenchot=".\\assets\\images\\print")
    # print(r['jobTitle'])
    
# time.sleep(60)