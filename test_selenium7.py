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

def test_clicking_appearence(driver):
  # Кликнем Appearence
  driver.find_element_by_xpath("//a[contains(@href, 'appearance')]").click()
  assert driver.find_element_by_css_selector('h1')
  # Кликнем Logotype
  driver.find_element_by_xpath("//a[contains(@href, 'logotype')]").click()
  assert driver.find_element_by_css_selector('h1')
  # Клиенем Template (Отдельно от Appearence)
  driver.find_element_by_xpath("//a[contains(@href, 'template')]").click()
  assert driver.find_element_by_css_selector('h1') # ищем заголовок

def test_clicking_catalog(driver):
  # Кликаем Catalog
  driver.find_element_by_xpath("//a[contains(@href,'catalog')]").click()
  assert driver.title #Почему то он просто My Store а не Сatalog | My Store
  # Кликаем каждый елемент списка Каталог
  Elements = driver.find_elements_by_css_selector('ul.docs li')
  print(Elements)
  for Number in range(len(Elements)):
      current_element = driver.find_elements_by_css_selector('ul.docs li')[Number]
      current_element.click()
      assert driver.find_element_by_css_selector('h1')

def test_clicking_all(driver):
    # Кликаем все елементы на странице, один за одним
    all_elements = driver.find_elements_by_css_selector('ul#box-apps-menu li#app-')
    number_of_elements= len(all_elements)
    for number in range(number_of_elements):
        element = driver.find_elements_by_css_selector('ul#box-apps-menu li#app-')[number].click()
        assert driver.find_element_by_css_selector('h1')
        context_menu = driver.find_elements_by_css_selector('ul.docs li') #ищем кнопки подменю
        if len(context_menu) > 0:                                 # если есть елементы - проходим по списку и кликаем их
            for context_number in range(len(context_menu)):
                current_element = driver.find_elements_by_css_selector('ul.docs li')[context_number].click()
                assert driver.find_element_by_css_selector('h1')