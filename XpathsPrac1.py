from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
try:
    s = Service('D:\chromedriver_win32\chromedriver.exe')

    driver = webdriver.Chrome(service=s)

    driver.get("https:\\www.expedia.com")

    driver.maximize_window()

    driver.delete_all_cookies()

    driver.find_element(By.XPATH, '//span[text()="Flights"]').click()

    driver.find_element(By.XPATH, '//button[@aria-label= "Leaving from"]').click()

    driver.find_element(By.ID, "location-field-leg1-origin").send_keys('hyd')

    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@aria-label='Search for “hyd”']").click()

    driver.find_element(By.XPATH, '//button[@aria-label= "Going to"]').click()

    driver.delete_all_cookies()

    driver.find_element(By.ID, "location-field-leg1-destination").send_keys('usa')

    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@aria-label='Search for “usa”']").click()

    driver.find_element(By.XPATH, '//button[text()= "Search"]').click()


finally:
    driver.close()
    pass
