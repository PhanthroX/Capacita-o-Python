from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from logging import basicConfig
from logging import critical, error, warning, info, debug
from selenium.webdriver.support.ui import Select
import pyscreenshot as ps
import time

def preenche_job(driver:webdriver.Chrome, row, i, caminhoScreenchot):
    
    textbox = driver.find_element(By.XPATH, "//*[@id='jobTitle']") 
    textbox.clear()
    textbox.send_keys(row[1])

    textbox = driver.find_element(By.XPATH, "//*[@id='jobDescription'][1]")
    textbox.clear()
    textbox.send_keys(row[2])

    select_element = driver.find_element(By.XPATH, "//*[@id='hiringDepartment'][1]")
    select = Select(select_element)
    select.select_by_value(row[3])
    
    select_element = driver.find_element(By.XPATH, "//*[@id='educationLevel'][1]")
    select = Select(select_element)
    select.select_by_value(row[4])
    
    textbox = driver.find_element(By.XPATH, "//*[@id='postingStartDate'][1]")
    textbox.clear()
    textbox.send_keys(row[5])
    
    textbox = driver.find_element(By.XPATH, "//*[@id='postingEndDate'][1]")
    textbox.clear()
    textbox.send_keys(row[6])
    
    if row[7] == "No":
        remote = driver.find_element(By.XPATH, "//*[@id='remote']/label[2]/span[1]/span[1]/input[1]")
        remote.click()
    else:
        remote = driver.find_element(By.XPATH, "//*[@id='remote']/label[1]/span[1]/span[1]/input[1]")
        remote.click()
        
    if str(row[8]).find('Full-time') != -1:
        remote = driver.find_element(By.XPATH, "//*[@id='jobTypeFullTime']")
        remote.click() 
        
    if str(row[8]).find('Permanent') != -1:
        remote = driver.find_element(By.XPATH, "//*[@id='jobTypePermanent']")
        remote.click()

    if str(row[8]).find('Part-time') != -1:
        remote = driver.find_element(By.XPATH, "//*[@id='jobTypePartTime']")
        remote.click()
    
    if str(row[8]).find('Temp') != -1:
        remote = driver.find_element(By.XPATH, "//*[@id='jobTypeTemp'][1]")
        remote.click()        
    
    botaoSub = driver.find_element(By.XPATH, "//*[@id='submit']/span[1]")
    botaoSub.click()
    
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    screenshot = ps.grab()
    screenshot.save(f'{caminhoScreenchot}{str(i)}.png')