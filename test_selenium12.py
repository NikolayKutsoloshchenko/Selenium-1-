#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    request.addfinalizer(driver.quit)
    return driver

def test_add_items(driver):
    driver.find_element_by_xpath('//a[contains(@href,"catalog")]').click()
    driver.find_element_by_xpath('//a[contains(@href, "edit_product")]').click()
    driver.find_element_by_xpath('//input [contais(text(),"Enabled")]').click()
    Name = driver.find_element_by_css('input[name="name[en]"]')
    Name.send_keys('Duck Admiral')
