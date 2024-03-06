import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    #Constante de Locatori
    USER_LOC = (By.ID,"username")
    PASS_LOC = (By.ID,"password")
    SUBMIT_LOC = (By.TAG_NAME,"button")
    ERROR_LOC = (By.CLASS_NAME,"error")
    #Constante de Valori
    USER_CORRECT = "tomsmith"
    PASS_CORRECT = "SuperSecretPassword!"
    WRONG_USER = "billybutcher"
    WRONG_PASS = "SmallSecretPassword!"

    #Metoda setup
    def setUp(self):
        #Crearea Drive-ului
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.maximize_window()
        #Folosim un wait implicit de maxim 5 secunde
        self.chrome.implicitly_wait(5.5)
    #Metoda teardown
    def tearDown(self):
        self.chrome.quit()
    #Metodele de Test
    def test_invalid_password(self):
        self.chrome.find_element(*self.USER_LOC).send_keys(*self.USER_CORRECT)
        #self.chrome.find_element(By.CSS_SELECTOR,"id='username'")
        self.chrome.find_element(*self.PASS_LOC).send_keys(*self.WRONG_PASS)
        self.chrome.find_element(*self.SUBMIT_LOC).click()
        time.sleep(1)
        #Folosim instructiunea Assert sa verificam aparitia erorii de Login
        msg = self.chrome.find_element(*self.ERROR_LOC).get_attribute("id")
        #print(msg)
        assert msg == "flash"
    #@unittest.skip
    def test_invalid_user(self):
        # Trebuie sa gasim campul username si sa-i trimitem un user incorect
        # Trebuie sa gasim campul password si sa-i dam o parola corecta
        # Trebuie sa gasim butonul de login si sa-l clickam
        # Trebuie sa construim assert-ul ca sa confirmam ca obitnem rezultatul dorit
        self.chrome.find_element(*self.USER_LOC).send_keys(*self.WRONG_USER)
        time.sleep(2)
        self.chrome.find_element(*self.PASS_LOC).send_keys(*self.PASS_CORRECT)
        time.sleep(2)
        self.chrome.find_element(*self.SUBMIT_LOC).click()
        time.sleep(2)
        msg = self.chrome.find_element(*self.ERROR_LOC).text
        assert "Your username is invalid!" in msg
        # Construiti un nou assert in care sa verificati egalitatea intre mesaj si "Your username is invalid!"


