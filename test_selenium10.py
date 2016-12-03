#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_duck_attributes():
    driver = webdriver.Chrome()
    driver.get('http://localhost/litecart/en/')
    duck = driver.find_element_by_css_selector('div#box-campaigns a.link')
    duck_name = duck.find_element_by_css_selector('div.name').get_attribute('textContent')
    assert duck_name == 'Yellow Duck'

    duck_price = duck.find_element_by_css_selector('s.regular-price')
    duck_price_old = duck_price.get_attribute('textContent')
    duck_price_old_color = duck_price.value_of_css_property("color")
    duck_price_old_font = duck_price.value_of_css_property("text-decoration")
    assert duck_price_old == '$20'
    assert duck_price_old_color == 'rgba(119, 119, 119, 1)'
    assert duck_price_old_font == 'line-through'

    duck_price = duck.find_element_by_css_selector('strong.campaign-price')
    duck_price_new = duck_price.get_attribute('textContent')
    duck_price_new_color = duck_price.value_of_css_property("color")
    duck_price_new_font = duck_price.value_of_css_property("font-weight")
    assert duck_price_new == '$18'
    assert duck_price_new_color == 'rgba(204, 0, 0, 1)'
    assert duck_price_new_font == 'bold'

    duck.click()
    duck_name_after_click = driver.find_element_by_css_selector('h1.title').get_attribute('textContent')
    assert duck_name == duck_name_after_click

    duck_price = driver.find_element_by_css_selector('strong.campaign-price')
    assert duck_price_new == duck_price.get_attribute('textContent')
    assert duck_price_new_color == duck_price.value_of_css_property("color")
    assert duck_price_new_font == duck_price.value_of_css_property("font-weight")

    duck_price = driver.find_element_by_css_selector('s.regular-price')
    assert duck_price_old == duck_price.get_attribute('textContent')
    assert duck_price_old_font == duck_price.value_of_css_property("text-decoration")
    assert duck_price_old_color == duck_price.value_of_css_property("color") # Тест валится потому что на странице товара другой цвет
