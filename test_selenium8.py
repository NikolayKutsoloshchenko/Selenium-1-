#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_stickers(driver):
    driver.get('http://localhost/litecart/en/')
    # найдем все товары в вкладке Most Popular и сохраним их в переменную
    most_popular = driver.find_elements_by_css_selector('div#box-most-popular li')
    for element in most_popular: #для каждого элемента проверяем что количество стикеров - 1
        sticker = element.find_elements_by_xpath('.//div [contains(@class, "sticker")]')
        assert len(sticker) == 1

    campaings = driver.find_elements_by_css_selector('div#box-campaigns li') #команды из раздела campaings
    for element in campaings:
        sticker = element.find_elements_by_xpath('.//div [contains(@class, "sticker")]')
        assert len(sticker) == 1

    latest_products = driver.find_elements_by_css_selector('div#box-latest-products li')
    for element in latest_products:
        sticker = element.find_elements_by_xpath('.//div [contains(@class, "sticker")]')
        assert len(sticker) == 1

    # Проверили что у всех товаров есть стикеры