from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

try:
    s= Service('D:\chromedriver_win32\chromedriver.exe')

    driver = webdriver.Chrome(service= s)

    driver.get("https:\\www.flipkart.com")

    driver.maximize_window()

    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@class= "_2KpZ6l _2doB4z"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//img[@class= "_396cs4 _3exPp9"]').click()

    time.sleep(2)

    print("clicked something")

    li = driver.find_elements(By.XPATH, '//div[@class= "_1KOcBL"]/section')

    print(len(li))
    s = '//div[@class= "_1KOcBL"]/'
    for x,y in enumerate(li):
        print(x+1, y.text,'-->>>', y.get_attribute("class"))
        cxpath1 = s + f'section[{x + 1}]/div'
        li2 = driver.find_elements(By.XPATH, cxpath1)
        if(y.get_attribute("class")== '_167Mu3 _2hbLCH'):
            if len(li2)==2:
                print("Already opened: ", y.text, cxpath1)
            else:
                cxpath2 = s + f'section{[x + 1]}/div[1]/div[1]'
                driver.find_element(By.XPATH, cxpath2).click()
                print("List enhanced after clicking: ", y.text)
                time.sleep(2)

        else:
            print('Going to Next filter----------')
            pass


finally:
    driver.close()
    pass

