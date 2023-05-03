import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

print("Name :", __name__)


class SearchEngines(unittest.TestCase):
    def test_chrome(self):
        s = Service(executable_path=r'D:\chromedriver_win32\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.facebook.com")
        print(driver.title)
        driver.close()

    def test_firefox(self):
        s = webdriver.firefox.service.Service(executable_path=r'D:\geckodriver-v0.30.0-win64\geckodriver.exe')
        driver = webdriver.Firefox(service=s)
        driver.get("https://www.gmail.com")
        print(driver.title)
        driver.close()


if __name__ == "__main__":
    print("Hi from if condition.")
else:
    print("Hi from else condition.")
    #unittest.main()
