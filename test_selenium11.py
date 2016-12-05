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
    driver.get('http://localhost/litecart/en/')
    request.addfinalizer(driver.quit)
    return  driver

def test_login(driver):
    driver.find_element_by_xpath('//a[contains(text(),"New customers click here")]').click()
    City= driver.find_element_by_xpath('//input [@name="city"]')
    City.send_keys('Random City') # Почему то у города нет атрибута required, хотя он обязателен
    Required_elements= driver.find_elements_by_css_selector('input[required="required"]') # получили все обязательные поля
    for element in Required_elements:
        name = element.get_attribute('name')
        if name == 'firstname':
            element.send_keys('Nikolay')
        elif name == 'lastname':
            element.send_keys('Kutsoloshchenko')
        elif name == 'address1':
            element.send_keys('Random name str.')
        elif name == 'postcode':
            element.send_keys('12345')
        elif name =='email':
            element.send_keys('asdfukmail+test5@gmail.com')
        elif name =='phone':
            text = element.get_attribute('placeholder') + '123456789'
            element.send_keys(text)
        elif name == 'password':
            element.send_keys('Qwert12345')
        elif name == 'confirmed_password':
            element.send_keys('Qwert12345')
    driver.find_element_by_css_selector('button[type ="submit"]').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"Logout")]')))
    driver.find_element_by_xpath('//a[contains(text(),"Logout")]').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="email"]')))
    email_field = driver.find_element_by_css_selector('input[name="email"]')
    email_field.send_keys('asdfukmail+test@gmail.com')
    password_field = driver.find_element_by_css_selector('input[name="password"]')
    password_field.send_keys('Qwert12345')
    driver.find_element_by_css_selector('button[name="login"]').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"Logout")]')))
    driver.find_element_by_xpath('//a[contains(text(),"Logout")]').click()