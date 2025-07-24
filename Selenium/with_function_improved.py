import time
import random
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string


def random_pair():
    # Create a pool of characters: lowercase letters, uppercase letters, and digits
    pool = string.ascii_letters + string.digits
    
    # Select two random characters from the pool
    return ''.join(random.choices(pool, k=2))


def pageLoop():
    