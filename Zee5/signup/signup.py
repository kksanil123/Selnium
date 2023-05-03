import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class SignUp(unittest.TestCase):
    driver = None
    s = None

    @classmethod
    def setUpClass(cls):
        cls.s = Service(executable_path=r'D:\chromedriver_win32\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.get("https://www.zee5.com/")
        cls.driver.maximize_window()

    @unittest.skip("skipping this test, bcoz email signup is not enabled...")
    def test_email_signup(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, 'a.loginBtn.noSelect').click()
        self.driver.find_element(By.XPATH, '// span[text() = "Register"]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

# if __name__ == "__main__":
#     unittest.main()
# else:
#     print(f"This module is running with __name__ : {__name__}")
