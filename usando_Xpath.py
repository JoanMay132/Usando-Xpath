from lib2to3.pgen2 import driver
import unittest
from black import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase): # Clase
 
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Descargas\chromedriver_win32\chromedriver.exe") # Inicializa el navegador
    
    def test_buscar_por_xpath(self): 
        driver= self.driver 
        driver.get("https://www.google.com")   # Abre el navegador en la URL
        time.sleep(3)
        buscar_por_xpath=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input") # Busca el elemento por Xpath
        time.sleep(3)   
        buscar_por_xpath.send_keys("selenium",Keys.ARROW_DOWN) # Envía la palabra "selenium" y presiona la tecla "flecha hacia abajo"
        time.sleep(3) 
    
    def tearDown(self): # Cierra el navegador
        self.driver.close() 

if __name__=='__main__': # Inicializa el test
    unittest.main() # Ejecuta el test

# XPATH estructura de direcciones (carpetas, objetos, etc...) 'XML'
# Existen dos tipos
# Xpath relativo y absoluto

# Relativo es el chido