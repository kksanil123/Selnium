import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import time


class Signin(unittest.TestCase):
    driver = None
    s = None
    result = None

    @classmethod
    def setUpClass(cls):
        cls.s = Service(executable_path=r'D:\chromedriver_win32\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.delete_all_cookies()

    @classmethod
    def setUp(self):
        self.driver.get("https://www.zee5.com/")
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        if self.result == False:
            self.skipTest(self, f"Login failed.. {self.result}")
        else:
            time.sleep(3)
            self.driver.find_element(By.XPATH, '(//button[text()= "Open Menu"])[1]').click()
            self.driver.find_element(By.XPATH, '//div[text()= "Logout"]').click()

    def test_sigin_email(self):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.loginBtn.noSelect')))
        self.driver.find_element(By.CSS_SELECTOR, 'a.loginBtn.noSelect').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "userName"]').send_keys("crmtest@yopmail.com")
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "password"]').send_keys("123456787")
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, '(//span[text() = "Login"])[2]')))
        self.driver.find_element(By.XPATH, '(//span[text() = "Login"])[2]').click()
        time.sleep(2)
        if (self.driver.find_element(By.XPATH, '(//button[text()= "Open Menu"])[1]')).is_displayed():
            pass
        else:
            self.driver.save_screenshot(r'C:\Users\karla\PycharmProjects\Selnium\Zee5\Screenshots\email_sign_err.png')
            self.result = False
            return self.result

    def test_sigin_mobile(self):
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'a.loginBtn.noSelect').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "userName"]').send_keys("9848941133")
        self.driver.find_element(By.XPATH, '(//span[text() = "Login"])[2]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Enter Password"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "inputPassword"]').send_keys("1234567")
        self.driver.find_element(By.XPATH, '//div[text() = "PROCEED"]').click()
        time.sleep(2)
        if (self.driver.find_element(By.XPATH, '(//button[text()= "Open Menu"])[1]')).is_displayed():
            pass
        else:
            self.driver.save_screenshot(r'C:\Users\karla\PycharmProjects\Selnium\Zee5\Screenshots\mobile_sign_err.png')
            self.result = False
            return self.result

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

# if __name__ == "__main__":
#     unittest.main()
# else:
# print(f"This module is running with __name__ : {__name__}")
