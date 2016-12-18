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

def test_java_script_error(driver):
    open_duck_page(driver)
    lenth= len(driver.find_elements_by_xpath('//tr/td[3]/a[contains(@href,"product_id")]'))
    for number in range(lenth):
        ducks = driver.find_elements_by_xpath('//tr/td[3]/a[contains(@href,"product_id")]')
        ducks[number].click()
        print('Logs for duck number ', number, ':')
        for line in driver.get_log('browser'):
            print(line)
        open_duck_page(driver)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"product_id")]')))


def open_duck_page(driver):
    driver.find_element_by_xpath("//a[contains(@href,'catalog')]").click()
    link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"category_id=1")]')))
    link.click()
    link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"category_id=2")]')))
    link.click()
