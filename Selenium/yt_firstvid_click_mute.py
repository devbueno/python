from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new Chrome driver instance
driver = webdriver.Chrome()

# Navigate to YouTube
driver.get('https://www.youtube.com')

# Find the search bar and enter a search query
search_bar = driver.find_element(By.NAME, 'search_query')
search_bar.send_keys('Music')
search_bar.submit()

# Wait for the first video to load and click on it
video = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-video-renderer')))
video.click()

# Wait for the video to load and mute it
mute_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.ytp-mute-button')))
mute_button.click()
time.sleep(50)