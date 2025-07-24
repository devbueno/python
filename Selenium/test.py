from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string



options = uc.ChromeOptions()

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

options.add_experimental_option("prefs", prefs)

driver = uc.Chrome(options=options)

rand_init = random.uniform(2, 5)

us = ""
pw = ""
codigo = ""

code1, code2, code3, code4, code5, code6 = codigo



def random_pair():
    # Create a pool of characters: lowercase letters, uppercase letters, and digits
    pool = string.ascii_letters + string.digits
    
    # Select two random characters from the pool
    return ''.join(random.choices(pool, k=2))






# Navigate to YouTube
driver.get('hidden')
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".mr-2 > .ml-2").click()
time.sleep(rand_init)
driver.find_element(By.ID, "user_login").send_keys(us)
time.sleep(rand_init)
driver.find_element(By.ID, "user_password").send_keys(pw)
time.sleep(rand_init)
driver.find_element(By.ID, "user_password").send_keys(Keys.ENTER)
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".inpu_attempt").send_keys(code2)
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".inputttempt").send_keys(code3)
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".ittempt").send_keys(code4)
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".inputtempt").send_keys(code5)
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".intt").send_keys(code6)
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".xs(3)").click()
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".ive").click()
time.sleep(rand_init)
driver.find_element(By.ID, "q").click()
time.sleep(rand_init)
driver.find_element(By.ID, "q").send_keys(" ")
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".10").click()
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".en").click()
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".mpan").click()
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".den").click()
time.sleep(rand_init)
driver.find_element(By.CSS_SELECTOR, ".").click()
time.sleep(rand_init)


while True:
    driver.find_element(By.ID, "q").send_keys(random_pair())
    time.sleep(rand_init)
    driver.find_element(By.ID, "q").send_keys(Keys.ENTER)
    




