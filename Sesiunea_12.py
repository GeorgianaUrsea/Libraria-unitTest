import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class alerte(unittest.TestCase):
    JS_ALERT_LOC=(By.CSS_SELECTOR,'[onclick="jsAlert()"]')
    RESULT_LOC = (By.CSS_SELECTOR,'[style="color:green"]')
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get('https://the-internet.herokuapp.com/javascript_alerts')
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
    def tearDown(self):
        print('eliberam driverul')
        self.chrome.quit()
    def test_JsAlert(self):
        self.chrome.find_element(*self.JS_ALERT_LOC).click()
        time.sleep(3)
        self.chrome.switch_to.alert.accept()            #sa clickam pe butonul de accept trebuie folosit switch_to
        time.sleep(3)
        msg = self.chrome.find_element(*self.RESULT_LOC).text
        assert 'You successfully clicked an alert' in msg