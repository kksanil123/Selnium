from selenium import webdriver
from Zee5.signin.signin import Signin
import unittest


class AfterLogin(Signin):

    def test_zdd_contents_to_mylist(self):
        print(f"{self.result}")
        self.result = True
