from navigation import chrome_browser, PageObjects
from file_manipulation import cria_csv, escreve_csv
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from logging import basicConfig
from logging import critical, error, warning, info, debug
import logging 
import logging.config
import pyscreenshot as ps

logging.config.fileConfig('./logs/logging.conf')
logger = logging.getLogger('root')

# Configuração básica de log da própria linguagem. Passa-se os parâmetros necessários para cada ocasião.

# basicConfig(
#     level=INFO,
#     filename='./logs/log_sicredi.log',
#     filemode='a',
#     format='%(levelname)s:%(asctime)s:%(message)s'
# )

def fake_data():
    site_data = "https://www.fakenamegenerator.com/gen-random-br-br.php"
    file_path = './assets/new_challenge.csv'

    driver = chrome_browser(site_data)

    cria_csv(file_path)
    info(f'Arquivo {file_path} criado com sucesso.')

    for i in range(10):
        row = (PageObjects.executa_fake_data(driver))
        logging.info(row)
        screenshot = ps.grab()
        screenshot.save(f'./logs/screenshots/{i}.png')
        escreve_csv(file_path, row)

# Configuração para rodar apenas este arquivo sem precisar chamar uma função.
if __name__ == '__main__':
    fake_data()
