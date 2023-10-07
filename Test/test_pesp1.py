import time
from selene import browser, by, be, have
from selene._managed import config
from selene.support.shared.jquery_style import s, ss

def test_search():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    # Вибір категорії Жіноче взуття
    s('#menu>ul>li').click()
    # Фільтр Категорія
    s('.d-flex>div').click()
    # Вибір Босоніжки
    s('.cp-filter-items>a:nth-of-type(9)').click()
    # Фільтр Колір
    s('.cp-filter-group:nth-of-type(3)').click()
    # Вибір кольору чорний
    s('.cp-filter-items.cp-filter-cap .cp-label-item:nth-of-type(11)').click()
    s('.cp-filter-button.active').click()
    # Вибір категорії Розмір
    s('.cp-filter-group:nth-of-type(4)').click()
    # Вибір розміру 39
    s('.cp-filter-items.cp-check-row .cp-label-item:nth-of-type(3)').click()
    s('.cp-filter-button.active').click()
    # Перевірка
    ss('.col8-xl-8.col8-md-6.col8-sm-6.col8-xs-6.cp-selected-filters-box').should(have.texts('чорний'))
    time.sleep(5)

def test_search_button():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    s('.search').click()
    # Введення в пошук  назву бренда 'tamaris'
    s('.box>input').type('tamaris').press_enter()
    time.sleep(1)
    # Перевірка наявності двох елементів пошуку
    page_text = browser.driver.page_source.count('Жіночі босоніжки TAMARIS білий')
    print('Повторюється:', page_text, 'рази')

def test_registration():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    s('.login').click()
    s('.register').click()
    s('[name="lastname"]').type('Зоріна')
    s('[name="firstname"]').type('Олена')
    s('[name="firstname2"]').type('Миколаївна')
    s('#birthday').type('25121983')
    s('#passwd').type('a0822a10f2')
    s('#confirm').type('a0822a10f2')
    s('.carat').click()
    s('//*[@id="form"]/div[2]/div[2]/div/div/ul/li[22]').click()
    s('#noroftown').type('Харків')
    s('#norofindx').type('61003')
    s('#addr').type('майдан Павлівський, 10')
    s('[name="agree"]').click()
    s('.register-button').click()
    # browser.all('.col-md-12>div').should(have.texts('запис'))
    time.sleep(5)

def test_authorization():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    s('.login').click()
    s('[placeholder="ЛОГІН"]').type('zorinae83@gmail.com')
    s('[placeholder="ПАРОЛЬ"]').type('a0822a10f2')
    s('.button').click()
    ss('.col-md-12>div').should(have.texts('Мій обліковий запис'))
    time.sleep(5)
    # Додавання товару в Обране після реєстрації
    # Вибір категорії Жіноче взуття
    s('#menu>ul>li').click()
    # Вибір взуття
    s('.rowProducts.row8>div:nth-of-type(6)').click()
    # Додавання до обраного
    s('.pi-heart-text').click()
    # Перевірка
    ss('.alert>div').should(have.texts('ТОВАР ДОДАНО В ОБРНЕ!'))
    time.sleep(5)

def test_list_of_desired_products():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    # Вибір категорії Жіноче взуття
    s('#menu>ul>li').click()
    # Вибір взуття
    s('.rowProducts.row8>div:nth-of-type(6)').click()
    # Додавання до обраного
    s('.pi-heart-text').click()
    # Перевірка
    ss('.alert>div').should(have.texts('ТОВАР ДОДАНО В ОБРНЕ!'))
    time.sleep(5)

def test_adding():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    s('#menu>ul>li>a').click()
    s('.rowProducts.row8>div:nth-of-type(4)').click()
    s('.pi-size-list>div:nth-of-type(4)').click()
    s('.pi-cart').click()
    time.sleep(2)
    # редагування кількості
    s('.fa.fa-plus-square').click()
    s('[href="https://respect-shoes.com.ua/cart"]').click()
    time.sleep(2)
    # перевірка наявності товару в кошику в кількості 2
    ss('.total>div:nth-of-type(1)').should(have.texts('2'))
    time.sleep(2)
    # видалення товару з кошика
    s('[style="display:block;"]').click()
    # перевірка пустого кошика
    ss('.col-md-12 .account').should(have.texts('Ваш кошик порожній!'))
    #browser.all('.container .row .col-md-12 .account').should(have.texts('Ваш'))
    time.sleep(2)





