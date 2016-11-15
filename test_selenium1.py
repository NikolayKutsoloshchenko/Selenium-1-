#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_open():
  driver = webdriver.Chrome()
  driver.get('https://www.python.org/')
  WebDriverWait(driver,10).until(EC.title_is('Welcome to Python.org'))
  driver.quit()
