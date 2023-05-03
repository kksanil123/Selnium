from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

s = Service(executable_path=r'D:\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=s)


driver.implicitly_wait(5)

# driver.get('http://only-testing-blog.blogspot.com/2014/01/textbox.html')
# driver.maximize_window()
#
#
# e1 = driver.find_element(By.ID, 'text1')
# e1.send_keys('anil')
# print(e1.is_enabled())
# print(e1.is_displayed())
# print(e1.is_selected())
#
# e2 = driver.find_element(By.ID, 'text2')
# print(e2.is_enabled())
# print(e2.is_displayed())
# print(e2.is_selected())
#
# e3 = driver.find_element(By.ID, 'check1')
# e3.click()
# print(e3.is_enabled())
# print(e3.is_displayed())
# print(e3.is_selected())
#
# e4 = driver.find_element(By.ID, 'check2')
# e4.click()
# print(e4.is_enabled())
# print(e4.is_displayed())
# print(e4.is_selected())
#
# e5 = driver.find_element(By.ID, 'radio1')
# e5.click()
#
# e6 = driver.find_element(By.NAME, 'img')
# e6.send_keys(r'E:\bird.png')
#
# e7 = driver.find_element(By.ID, 'Carlist')
#
# sel = Select(e7)
# print(len(sel.options))
# sel.select_by_visible_text('Audi')
#
# e8 = driver.find_element(By.XPATH, '//select[@name="FromLB"]')
#
# sel = Select(e8)
# print(len(sel.options))
# sel.select_by_index(10)
#
# e9 = driver.find_element(By.XPATH, '//input[@value="Show Me Alert"]')
# e9.click()
# alert = driver.switch_to.alert
# alert.dismiss()
#
# e10 = driver.find_element(By.XPATH, '//button[text()="Show Me Confirmation"]')
# e10.click()
# alert = driver.switch_to.alert
# alert.dismiss()
#
# e11 = driver.find_element(By.XPATH, '//button[text()="Show Me Prompt"]')
# e11.click()
# alert = driver.switch_to.alert
# print(alert.text)
# alert.send_keys('Anil')
# alert.accept()

'''--------------------------------------------------------------'''

driver.get('https://jqueryui.com/')
driver.maximize_window()

driver.find_element(By.LINK_TEXT, 'Draggable').click()
act = ActionChains(driver)
frame_id = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame_id)
el1 = driver.find_element(By.XPATH, '//p[text()="Drag me around"]')
print(el1.location)
print(el1.size)
act.drag_and_drop_by_offset(el1, 250, 250).perform()
act.reset_actions()

driver.switch_to.default_content()

driver.find_element(By.LINK_TEXT, 'Droppable').click()
act = ActionChains(driver)
frame_id = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame_id)
src = driver.find_element(By.XPATH, '//p[text()="Drag me to my target"]')
print(src.location)
print(src.size)
target = driver.find_element(By.XPATH, '//p[text()="Drop here"]')
act.click_and_hold(src).move_to_element(target).release().perform()
act.reset_actions()



driver.switch_to.default_content()

driver.find_element(By.LINK_TEXT, 'Resizable').click()
act = ActionChains(driver)
frame_id = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame_id)
# src = driver.find_element(By.XPATH, '//h3[text()="Resizable"]')
src1 = driver.find_element(By.XPATH, '//div[@class="ui-resizable-handle ui-resizable-e"]')
print(src1.location)
print(src1.size)
act.click_and_hold(src1).move_by_offset(250, 0).release().perform()
src2 = driver.find_element(By.XPATH, '//div[@class="ui-resizable-handle ui-resizable-s"]')
print(src2.location)
print(src2.size)
act.click_and_hold(src2).move_by_offset(0, 100).release().perform()
act.reset_actions()

driver.switch_to.default_content()

driver.find_element(By.LINK_TEXT, 'Sortable').click()
act = ActionChains(driver)
frame_id = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame_id)
e_list = driver.find_elements(By.XPATH, '//li[@class="ui-state-default ui-sortable-handle"]')

for i in e_list.copy():
    act.click_and_hold(i).move_by_offset(0, 70).release().perform()

act.reset_actions()

driver.switch_to.default_content()
act = ActionChains(driver)
tab = driver.find_element(By.LINK_TEXT, 'Tabs')
for i in range(4):
    act.key_down(Keys.CONTROL).click(tab).key_up(Keys.CONTROL).perform()
    act.reset_actions()

tabs = driver.window_handles
print(tabs)
for tab in tabs:
    driver.switch_to.window(tab)
    time.sleep(2)
    driver.close()

time.sleep(5)
print('driver closing')
driver.close()
