from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')

#driver = webdriver.Firefox(executable_path='D:\geckodriver-v0.30.0-win64\geckodriver.exe')

driver.get("http://demo.guru99.com/")

print(driver.title)

print(driver.current_window_handle)

driver.close()