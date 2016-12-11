#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time
from random import choice

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    request.addfinalizer(driver.quit)
    return driver

def test_new_window(driver):
    driver.find_element_by_xpath("//a[contains(@href,'countries')]").click()
    countries = driver.find_elements_by_xpath('//a[contains(@href,"edit_country")]')
    choice(countries).click()
    time.sleep(5)
    main_window = driver.current_window_handle
    main_title = driver.title
    links = driver.find_elements_by_css_selector('i[class="fa fa-external-link"]')
    lenth = len(links)
    Wait = WebDriverWait(driver,10)
    for number in range(lenth):
        links = driver.find_elements_by_css_selector('i[class="fa fa-external-link"]')
        links[number].click()
        Wait.until(EC.new_window_is_opened)
        assert len(driver.window_handles) == 2
        for window in driver.window_handles:
            if window != main_window:
                new_window = window
                break
        driver.switch_to_window(new_window)
        assert driver.title != main_title
        driver.close()
        driver.switch_to_window(main_window)
