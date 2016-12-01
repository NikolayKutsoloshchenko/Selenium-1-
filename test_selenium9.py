#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    request.addfinalizer(driver.quit)
    return driver

def zones(elements):
    element_name = []
    for element in elements:
        element_name.append(element.get_attribute('Value'))
    assert element_name == sorted(element_name)



def test_countries(driver):
    driver.find_element_by_xpath('//a[contains(@href,"countries")]').click()
    list_of_countries= driver.find_elements_by_css_selector('tr.row')
    countries_names = []
    countries_names_with_zones = []
    for element in list_of_countries:
        element_name=element.find_element_by_css_selector('a')
        countries_names.append(element_name.get_attribute('textContent'))
    assert countries_names == sorted(countries_names)
    for element in list_of_countries:
        zones = element.find_element_by_xpath('.//td[6]')
        if zones.get_attribute('textContent') is not '0':
            zones_names = []
            element.find_element_by_css_selector('a').click()
            zone_name=driver.find_elements_by_xpath('//input [contains(@name,"name")]')
            for zone in zone_name:
                zones_names.append(zone.get_attribute('textContennt'))
            assert zones_names == sorted(zones_names)
            list_of_countries = driver.find_elements_by_css_selector('tr.row')
