from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
import time

PATH = "C:\WebDriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://google.com/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
time.sleep(5)
print(driver.title)
driver.quit()
  