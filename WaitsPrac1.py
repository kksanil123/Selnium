from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

try:
    s= Service(r'D:\chromedriver_win32\chromedriver.exe')

    driver = webdriver.Chrome(service= s)

    driver.get("https:\\www.expedia.com")

    driver.maximize_window()

    driver.delete_all_cookies()

    driver.find_element(By.XPATH, '//span[text()="Flights"]').click()

    driver.find_element(By.XPATH, '//button[@aria-label= "Leaving from"]').click()

    driver.find_element(By.ID,"location-field-leg1-origin").send_keys('hyd')

    #time.sleep(2)

    hold = WebDriverWait(driver, 8)

    hold.until(ec.presence_of_element_located((By.XPATH, '//button[contains(@aria-label,"Rajiv")]')))

    driver.find_element(By.XPATH, "//button[contains(@aria-label,'Rajiv')]").click()

    driver.find_element(By.XPATH, '//button[@aria-label= "Going to"]').click()

    driver.find_element(By.ID, "location-field-leg1-destination").send_keys('usa')

    time.sleep(2)

    hold.until(ec.presence_of_element_located((By.XPATH, "//button[contains(@aria-label,'New York')]")))

    driver.find_element(By.XPATH, "//button[contains(@aria-label,'New York')]").click()

    driver.find_element(By.XPATH, '//button[text()= "Search"]').click()

    #print(driver.find_element(By.XPATH,'//button[@aria-label= "Leaving from"]').is_displayed())

    print(__name__)

finally:
    print("Driver closing")
    driver.close()
    pass
