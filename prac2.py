from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# ser = Service(executable_path=r'D:\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome()

driver.get('https://facebook.com')

driver.close()
