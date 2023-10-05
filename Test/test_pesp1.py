import time
from selene import browser, by, be, have
from selene._managed import config
from selene.support.shared.jquery_style import s, ss


def test_open():
    browser.open('https://www.ecosia.org/')
    browser.driver.maximize_window()
    browser.element(by.name('q')).type("respect ua").press_enter()
    browser.all(by.css('.result')).first.click()
    time.sleep(5)

def test_search1():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    # Вибір категорії Жіноче взуття
    browser.element('#menu>ul>li').click()
    # Фільтр Категорія
    browser.element('.d-flex>div').click()
    # Вибір Туфлі
    browser.element('.cp-filter-items>a:nth-of-type(2)').click()
    # Фільтр Колір
    browser.element('.cp-filter-group:nth-of-type(3)').click()
    # Вибір кольору чорний
    browser.element('.cp-filter-items.cp-filter-cap .cp-label-item:nth-of-type(6)').click()
    browser.element('.cp-filter-button.active').click()
    # Вибір категорії Розмір
    browser.element('.cp-filter-group:nth-of-type(4)').click()
    # Вибір розміру 39
    browser.element('.cp-filter-items.cp-check-row .cp-label-item:nth-of-type(4)').click()
    browser.element('.cp-filter-button.active').click()
    # Перевірка
    browser.all('.col8-xl-8.col8-md-6.col8-sm-6.col8-xs-6.cp-selected-filters-box').should(have.texts('чорний'))
    time.sleep(5)

def test_search_button():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    browser.element('.search').click()
    # Введення в пошук Туфлі
    browser.element('.box>input').type('Босоніжки').press_enter()
    # browser.all('.categoryBox')
    time.sleep(5)

def test_registration():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    browser.element('.login').click()
    browser.element('.register').click()
    browser.element('[name="lastname"]').type('Зоріна')
    browser.element('[name="firstname"]').type('Олена')
    browser.element('[name="firstname2"]').type('Миколаївна')
    browser.element('#birthday').type('25121983')
    browser.element('#passwd').type('a0822a10f2')
    browser.element('#confirm').type('a0822a10f2')
    browser.element('.carat').click()
    browser.element('//*[@id="form"]/div[2]/div[2]/div/div/ul/li[22]').click()
    browser.element('#noroftown').type('Харків')
    browser.element('#norofindx').type('61003')
    browser.element('#addr').type('майдан Павлівський, 10')
    browser.element('[name="agree"]').click()
    browser.element('.register-button').click()
    # browser.all('.col-md-12>div').should(have.texts('запис'))
    time.sleep(5)

def test_authorization():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    browser.element('.login').click()
    browser.element('[placeholder="ЛОГІН"]').type('zorinae83@gmail.com')
    browser.element('[placeholder="ПАРОЛЬ"]').type('a0822a10f2')
    browser.element('.button').click()
    browser.all('.col-md-12>div').should(have.texts('Мій'))
    time.sleep(5)

    # Додавання товару в Обране після реєстрації
    # Вибір категорії Жіноче взуття
    browser.element('#menu>ul>li').click()
    # Вибір взуття
    browser.element('.rowProducts.row8>div:nth-of-type(6)').click()
    # Додавання до обраного
    browser.element('.pi-heart-text').click()
    # Перевірка
    browser.all('.alert>div').should(have.texts('ТОВАР ДОДАНО В ОБРНЕ!'))
    browser.all('.product').should(have.texts('3,790 грн'))
    time.sleep(5)

def test_list_of_desired_products():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    # Вибір категорії Жіноче взуття
    browser.element('#menu>ul>li').click()
    # Вибір взуття
    browser.element('.rowProducts.row8>div:nth-of-type(6)').click()
    # Додавання до обраного
    browser.element('.pi-heart-text').click()
    # Перевірка
    browser.all('.alert>div').should(have.texts('ТОВАР ДОДАНО В ОБРНЕ!'))
    browser.all('.product').should(have.texts('3,790 грн'))
    time.sleep(5)


def test_adding():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    browser.element('#menu>ul>li>a').click()
    browser.element('.rowProducts.row8>div:nth-of-type(3)').click()
    browser.element('.pi-size-list>div:nth-of-type(4)').click()
    browser.element('.pi-cart').click()
    # редагування кількості
    browser.element('.fa.fa-plus-square').click()
    # перевірка наявності товару в кошику в кількості 2
    browser.all('.fancybox-inner').should(have.texts('2'))
    time.sleep(5)
    # видалення товару з кошика
    browser.element('.cart-products-remove>a').click()
    browser.element('.empty').click()
    # перевірка пустого кошика
    browser.all('.col-md-12 .account').should(have.texts('Ваш кошик порожній!'))


# варіант 2
def test_adding1():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    browser.element('#menu>ul>li>a').click()
    browser.element('.rowProducts.row8>div:nth-of-type(3)').click()
    browser.element('.pi-size-list>div:nth-of-type(4)').click()
    browser.element('.pi-cart').click()
    # редагування кількості
    browser.element('.fa.fa-plus-square').click()
    # перевірка наявності товару в кошику в кількості 2
    browser.all('.fancybox-inner').should(have.texts('2'))
    browser.element('[href="https://respect-shoes.com.ua/cart"]').click()
    time.sleep(5)
    # видалення товару з кошика
    browser.element('[style="display:block;"]').click()
    # перевірка пустого кошика
    browser.all('.col-md-12 .account').should(have.texts('Ваш кошик порожній!'))




