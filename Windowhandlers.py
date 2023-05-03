import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service(executable_path=r'D:\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service = s)

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.CSS_SELECTOR,'button[class = "btn btn-info"]').click()

tab = print(driver.window_handles)

time.sleep(3)

driver.switch_to_window(driver.window_handles[1])

print(driver.title)

driver.find_element(By.CSS_SELECTOR,'a:contains("Charity supporting the Ukrainian army")').click()

tab = print(driver.window_handles)

driver.switch_to_window(tab[2])

print(driver.title)

time.sleep(3)

driver.close()
