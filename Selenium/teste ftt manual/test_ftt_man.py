from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
import time
import pandas
import random
import string
import re
import csv

##################### Driver Init #############################
options = uc.ChromeOptions()

prefs = {
    "credentials_enable_service": False,
    "profile.password_manprof_agr_enabled": False
}

options.add_experimental_option("prefs", prefs)

driver = uc.Chrome(options=options)
################################################################

brazil = "Brazil"
csv_path = 'C:/files/data.csv'
campos_csv = ['nome', 'local', 'link']


################################################################

def random_pair():
    # Create a pool of characters: lowercase letters, uppercase letters, and digits 
    pool = string.ascii_letters + string.digits
    
    # Select two random characters from the pool 
    return ''.join(random.choices(pool, k=2))

def is_valid_pattern(string):
    pattern = r'^\d{2,3}F$'  # Two or three digits followed by 'F'
    return bool(re.match(pattern, string))

################################################################


driver.get('hidden')

time.sleep(30)


###################

    # time.sleep(random.uniform(2,5))
    # driver.find_element(By.ID, "q").clear() # limpa o campo de pesquisa
    # time.sleep(random.uniform(2,5))
    # driver.find_element(By.CSS_SELECTOR, ".pl.click() # click search bar when inside group 
    # time.sleep(random.uniform(2,5))
    # driver.find_element(By.ID, "q").send_keys(random_pair()) # envia um par de letras para o campo de pesquisa 
    # time.sleep(random.uniform(2,5))
    # driver.find_element(By.ID, "q").send_keys(Keys.ENTER)   # envia um ENTER para o campo de ID Q 
    # time.sleep(random.uniform(2,5))

#####



while(True):
    driver.find_element(By.CSS_SELECTOR, "hidden").click() # click search bar when inside group
    time.sleep(random.uniform(2,5))
    driver.find_element(By.ID, "q").send_keys(random_pair()) # envia um par de letras para o campo de pesquisa 
    time.sleep(random.uniform(2,5))
    driver.find_element(By.ID, "q").clear() # limpa o campo de pesquisa 
    time.sleep(random.uniform(2,5))
    driver.find_element(By.ID, "q").send_keys(Keys.ENTER)   # envia um ENTER para o campo de ID Q 
    time.sleep(random.uniform(2,5))

    while(True):
        try:
            time.sleep(random.uniform(2,5))
            profile_divs = driver.find_elements(By.CSS_SELECTOR, '')
            for profile_div in profile_divs:
                name = profile_div.find_element(By.CSS_SELECTOR, '').text
                prof_ag_and_role = profile_div.find_element(By.CSS_SELECTOR, '').text
                prof_ag2 = prof_ag_and_role.split()[0]
                location = profile_div.find_element(By.CSS_SELECTOR, '').text
                link_element = profile_div.find_element(By.CSS_SELECTOR, 'a')
                link = link_element.get_attribute('href')

                if is_valid_pattern(prof_ag2) and brazil in location:
                    profile_list = [{'nome': name, 'location:': location, 'link': link }]
                    lista_lida = []

                    # Ler os dados existentes no csv
                    with open (csv_path, 'r', newline='') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            lista_lida.append(row)

                    # Identificação da ultima linha populada
                    ultima_linha_populada = len(lista_lida)
                
                    # coloca os novos dados no csv a partir da primeira linha depois da última populada
                    with open(csv_path, 'a', newline='') as csvfile:
                        escreve_csv_obj = csv.DictWriter(csvfile, fieldnames=campos_csv)
                        for i, row in enumerate(profile_list):
                            if i >= ultima_linha_populada:
                                escreve_csv_obj.writerow(row)
            driver.find_element(By.XPATH, "").click() # next pprof_ag
        except NoSuchElementException:
            time.sleep(random.uniform(2,5))
            break



if is_valid_pattern(profag2) and brazil in location:
    print("success")
else:
    print("not")

driver.execute_script("return window.find(arguments[0])", "Switch") # find string and select pprof_ag 



