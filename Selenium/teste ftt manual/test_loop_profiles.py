from selenium import webdriver
from selenium.webdriver.common.by import By
from undetected_chromedriver.v2 import Chrome, ChromeOptions

# Initialize undetected Chrome WebDriver
options = ChromeOptions()
driver = Chrome(options=options)

# Load the webpage
driver.get("your_website_url_here")

# Find all the parent div elements containing the profile information

profile_divs = driver.find_elements(By.CSS_SELECTOR, '.w-ful0.focus\\:\\:mb-2')

# Loop through each profile div and extract the desired information
for profile_div in profile_divs:
    # Extracting information from each profile div
    name = profile_div.find_element(By.CSS_SELECTOR, '.text-t-red-500').text
    Prof-ag_and_role = profile_div.find_element(By.CSS_SELECTOR, '.texgray-300').text
    location = profile_div.find_element(By.CSS_SELECTOR, '.trun300').text

    # Printing the extracted information for demonstration
    print("Name:", name)
    print("Location:", location)
    print("\n")  # Just for formatting

# Close the WebDriver
driver.quit()
