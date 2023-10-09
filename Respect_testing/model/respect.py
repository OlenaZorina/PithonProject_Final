import time
from selene import have, command
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser

class Respect:

    def __init__(self):
        self.filters = ss('.col8-xl-8.col8-md-6.col8-sm-6.col8-xs-6.cp-selected-filters-box')
        self.authoriz = ss('.col-md-12>div')
        self.desired = ss('.alert>div')
        self.number = ss('.total>div:nth-of-type(1)')
        self.check_remove = ss('.col-md-12 .account')

    def open(self):
        browser.open('https://respect-shoes.com.ua')
        browser.driver.maximize_window()
        return self

    def search_category(self):
        # Вибір категорії Жіноче взуття
        s('#menu>ul>li').click()
        # Фільтр Категорія
        s('.d-flex>div').click()
        # Вибір Босоніжки
        s('.cp-filter-items>a:nth-of-type(9)').click()
        return self

    def search_color(self):
        # Фільтр Колір
        s('.cp-filter-group:nth-of-type(3)').click()
        # Вибір кольору чорний
        s('.cp-filter-items.cp-filter-cap .cp-label-item:nth-of-type(11)').click()
        s('.cp-filter-button.active').click()
        return self

    def search_size(self):
        # Вибір категорії Розмір
        s('.cp-filter-group:nth-of-type(4)').click()
        # Вибір розміру 39
        s('.cp-filter-items.cp-check-row .cp-label-item:nth-of-type(5)').click()
        s('.cp-filter-button.active').click()
        return self

    def search(self):
        self.search_category()
        self.search_color()
        self.search_size()

    def should_be_search(self, text: str):
        self.filters.should(have.texts(text))
        time.sleep(5)
        return self

    def search_button(self, name: str):
        # Натиснути значок Пошук
        s('.search').click()
        # Введення в пошук  назву бренда 'tamaris'
        s('.box>input').type(name).press_enter()
        time.sleep(5)
        return self

    def should_be_search_button(self, name: str):
        # Перевірка наявності двох елементів пошуку
        page_text = browser.driver.page_source.count(name)
        print('Повторюється:', page_text, 'рази')
        return self

    def registration_open(self):
        s('.login').click()
        s('.register').click()
        return self

    def registration_name(self, lastname: str, firstname: str, firstname2: str):
        s('[name="lastname"]').type(lastname)
        s('[name="firstname"]').type(firstname)
        s('[name="firstname2"]').type(firstname2)
        return self

    def registration_birthday(self, day: str):
        s('#birthday').type(day)
        return self

    def registration_passwd(self, passwd: str, confirm: str):
        s('#passwd').type(passwd)
        s('#confirm').type(confirm)
        s('.carat').click()
        s('//*[@id="form"]/div[2]/div[2]/div/div/ul/li[22]').click()
        return self

    def registration_address(self, city: str, indx: str, addr: str):
        s('#noroftown').type(city)
        s('#norofindx').type(indx)
        s('#addr').type(addr)
        s('[name="agree"]').click()
        s('.register-button').click()
        return self

    def authorization(self, login: str, passwd: str):
        s('.login').click()
        s('[placeholder="ЛОГІН"]').type(login)
        s('[placeholder="ПАРОЛЬ"]').type(passwd)
        s('.button').click()
        return self

    def should_be_authorization(self, text: str):
        self.authoriz.should(have.texts(text))
        time.sleep(3)
        return self

    def desired_products(self):
        s('#menu>ul>li').click()
        s('.rowProducts.row8>div:nth-of-type(6)').click()
        s('.pi-heart-text').click()
        time.sleep(2)
        return self

    def should_be_desired(self, text: str):
        self.desired.should(have.texts(text))
        return self

    def adding_to_cart(self):
        s('#menu>ul>li>a').click()
        s('.rowProducts.row8>div:nth-of-type(4)').click()
        s('.pi-size-list>div:nth-of-type(4)').click()
        s('.pi-cart').click()
        time.sleep(2)
        return self

    def edit(self):
        # редагування кількості
        s('.fa.fa-plus-square').click()
        s('[href="https://respect-shoes.com.ua/cart"]').click()
        time.sleep(2)
        return self

    def should_be_edit(self, num: str ):
        # перевірка наявності товару в кошику в кількості 2
        self.number.should(have.texts(num))
        time.sleep(2)
        return self

    def remove(self):
        # видалення товару з кошика
        s('[style="display:block;"]').click()
        time.sleep(2)
        return self

    def should_be_remove(self, text1: str):
        # перевірка пустого кошика
        self.check_remove.should(have.texts(text1))
        return self

