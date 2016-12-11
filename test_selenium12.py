#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import choice
import time
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
    General(driver)
    Information(driver)
    Prices(driver)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"table.dataTable")))
    Table = driver.find_element_by_css_selector("table.dataTable")
    added_item = Table.find_element_by_xpath('//a[contains(text(),"Duck Admiral")]')
    assert added_item



def General(driver): # Заполним все поля на вкладке General
    driver.find_element_by_xpath('//a[contains(@href,"catalog")]').click()
    driver.find_element_by_xpath('//a[contains(@href, "edit_product")]').click()
    driver.find_element_by_css_selector('input[value="1"]').click()
    # Вводим имя
    Name = driver.find_element_by_css_selector('input[name="name[en]"]')
    Name.send_keys('Duck Admiral')
    # Вводим код продукта
    Code = driver.find_element_by_css_selector('input[name="code"]')
    Code.send_keys('12345')
    # Выбираем категорию
    driver.find_element_by_css_selector('input[name="categories[]"]').click() # cняли галочку с общей категории
    Category = driver.find_element_by_css_selector('input[data-name="Rubber Ducks"]')
    Category.click()
    time.sleep(5)
    # Выбор по полу выбираем случайно
    Gender = driver.find_elements_by_css_selector('input[name="product_groups[]"]')
    Gender = choice(Gender)
    Gender.click()
    # Случайно задаем количество от 1 до 99
    Quantity = driver.find_element_by_css_selector('input[name="quantity"]')
    Quantity.clear()
    number= choice(range(1,100))
    Quantity.send_keys(number)
    # Ставим Sold Out
    Sold_out = driver.find_element_by_css_selector('select[name="sold_out_status_id"]')
    Sold_out.click()
    Sold_out.send_keys(Keys.ARROW_DOWN)
    Sold_out.send_keys(Keys.ARROW_DOWN)
    Sold_out.send_keys(Keys.RETURN)
    # Добавляем картинку
    File_upload = File_upload = driver.find_element_by_css_selector('input[type="file"]')
    File_upload.send_keys('D:\\selenium\\learning\\Selenium-1-\\picture.jpg')
    # В даты запишем даты с какого он активен, и до какого он активен
    Date_fields = driver.find_elements_by_xpath('//input[contains(@name,"date_valid")]')
    Date_fields[0].send_keys('09'+'12'+'2016')
    Date_fields[1].send_keys('25'+'12'+'2016')

def Information(driver):
    driver.find_element_by_xpath('//a[contains(@href,"information")]').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="text"]')))
    # Выбираем производителя
    Manufacturer = driver.find_element_by_css_selector('select[name="manufacturer_id"]')
    Manufacturer.click()
    Manufacturer.send_keys(Keys.ARROW_DOWN)
    Manufacturer.send_keys(Keys.ENTER)
    # Пишем ключевые слова
    Keywords = driver.find_element_by_css_selector('input[name="keywords"]')
    Keywords.send_keys('Duck, Admiral, Rubber Duck, Bath, NAVY')
    # Небольшое описание
    Short_description = driver.find_element_by_css_selector('input[name="short_description[en]"]')
    Short_description.send_keys('This is rubber duck admiral.')
    # Пишем развернутое описание
    Description = driver.find_element_by_css_selector('div.trumbowyg-editor')
    Description.send_keys('This is rubber duck admiral.' + Keys.ENTER + 'He is awesome addition to your colletion' + Keys.ENTER + 'Product was not tested on animals')
    # Название продукта
    Head_title=driver.find_element_by_css_selector('input[name="head_title[en]"]')
    Head_title.send_keys('Rubber Duck Admiral')
    # Мета теги наверное ??
    Meta_description = driver.find_element_by_css_selector('input[name="meta_description[en]"]')
    Meta_description.send_keys("I don't know what this is")

def Prices(driver):
    driver.find_element_by_xpath('//a[contains(@href,"prices")]').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="purchase_price"]')))
    #
    Purchase_price = driver.find_element_by_css_selector('input[name="purchase_price"]')
    Purchase_price.clear()
    Purchase_price.send_keys('15')
    #
    Currency_select= driver.find_element_by_css_selector('select[name="purchase_price_currency_code"]')
    Currency_select.click()
    Currency_select.send_keys(Keys.ARROW_DOWN)
    Currency_select.send_keys(Keys.ENTER)
    #
    Price = driver.find_element_by_css_selector('input[name="prices[USD]"]')
    Price.clear()
    Price.send_keys('45')
    Price_with_tax = driver.find_element_by_css_selector('input[name="gross_prices[USD]"]')
    Price_with_tax.clear()
    Price_with_tax.send_keys('55')
    driver.find_element_by_css_selector('button[name="save"]').click()
