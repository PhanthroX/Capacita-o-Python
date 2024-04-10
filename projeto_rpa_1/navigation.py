from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def chrome_browser(site):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.binary_location = r"C:\Users\matheus_mariano\Documents\Ultima Aula\projeto_rpa_1\chrome-win64\\chrome.exe"
    chrome_driver_path = r"C:\Users\matheus_mariano\Documents\Ultima Aula\projeto_rpa_1\\chromedriver.exe"
    service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(options=chrome_options, service=service_options)

    driver.get(site)

    return driver


class Waits:
    def clickable(driver, by_type, selector):
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, selector)))

    def visible(driver, by_type, selector):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by_type, selector)))

    def url(driver, url):
        return WebDriverWait(driver, 10).until(EC.url_to_be(url))
