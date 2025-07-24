import time
import undetected_chromedriver as uc
from undetected_chromedriver import By
from selenium.webdriver.common.keys import Keys

options = uc.ChromeOptions()

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

options.add_experimental_option("prefs", prefs)

driver = uc.Chrome(options=options)

driver.get("https://www.google.com")

driver.find_element(By.ID, "APjFqb").send_keys("test")

driver.find_element(By.ID, "APjFqb").send_keys(Keys.ENTER)

time.sleep(5)