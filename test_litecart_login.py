#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login():
    driver=webdriver.Chrome()
    driver.get('http://192.168.204.132/litecart/admin')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    driver.quit()

def test_remember_me_button():
    driver = webdriver.Chrome()
    driver.get('http://192.168.204.132/litecart/admin')
    remember_me=driver.find_element_by_name('remember_me')
    remember_me.click()
    remember_me.click()
    driver.quit()