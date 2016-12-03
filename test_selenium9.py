#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    for number in range(len(list_of_countries)):
        countries = driver.find_elements_by_css_selector('tr.row')
        zones = countries[number].find_element_by_xpath('.//td[6]')
        if zones.get_attribute('textContent') is not '0':
            zones_names = []
            countries[number].find_element_by_css_selector('a').click()
            zone_name=driver.find_elements_by_xpath('//tbody/input [contains(@name,"name")]')
            for zone in zone_name:
                zones_names.append(zone.get_attribute('value'))
            assert zones_names == sorted(zones_names)
            driver.find_element_by_xpath('//a[contains(@href,"countries")]').click()

def test_zones_canada(driver):
    driver.find_element_by_xpath('//a[contains(@href,"geo_zones")]').click()
    driver.find_element_by_xpath('//a[contains(text(),"Canada")]').click()
    selected_zones = driver.find_elements_by_xpath('//select[contains(@name,"zone_code")]/option[@selected]')
    zones = []
    for zone in selected_zones:
        zones.append(zone.get_attribute('textContent'))
    assert zones == sorted(zones)

def test_zones_usa(driver):
    driver.find_element_by_xpath('//a[contains(@href,"geo_zones")]').click()
    driver.find_element_by_xpath('//a[contains(text(),"America")]').click()
    selected_zones = driver.find_elements_by_xpath('//select[contains(@name,"zone_code")]/option[@selected]')
    zones = []
    for zone in selected_zones:
        zones.append(zone.get_attribute('textContent'))
    assert zones == sorted(zones)