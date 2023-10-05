import time
from selene import have, command
from selene.support import by
from selene.support.shared import browser
class Respect:
    def __init__(self):
        self.filters = browser.all('.col8-xl-8.col8-md-6.col8-sm-6.col8-xs-6.cp-selected-filters-box')
        self.authoriz = browser.all('.col-md-12>div')
        self.desired1 = browser.all('.alert>div')
        self.desired2 = browser.all('.product')
        self.number = browser.all('.fancybox-inner')
        self.remove = browser.all('.col-md-12 .account')
    def open(self):
        browser.open('https://respect-shoes.com.ua')
        browser.driver.maximize_window()
        return self
    def search_category(self):
        # Вибір категорії Жіноче взуття
        browser.element('#menu>ul>li').click()
        # Фільтр Категорія
        browser.element('.d-flex>div').click()
        # Вибір Туфлі
        browser.element('.cp-filter-items>a:nth-of-type(2)').click()
        return self
    def search_color(self):
        # Фільтр Колір
        browser.element('.cp-filter-group:nth-of-type(3)').click()
        # Вибір кольору чорний
        browser.element('.cp-filter-items.cp-filter-cap .cp-label-item:nth-of-type(6)').click()
        browser.element('.cp-filter-button.active').click()
        return self
    def search_size(self):
        # Вибір категорії Розмір
        browser.element('.cp-filter-group:nth-of-type(4)').click()
        # Вибір розміру 39
        browser.element('.cp-filter-items.cp-check-row .cp-label-item:nth-of-type(4)').click()
        browser.element('.cp-filter-button.active').click()
        return self
    def search(self):
        self.search_category()
        self.search_color()
        self.search_size()
    def should_be_search(self, text: str):
        self.filters.should(have.texts(text))
        time.sleep(10)
        return self
    def search_button(self, name: str):
        # Натиснути значок Пошук
        browser.element('.search').click()
        # Введення в пошук Туфлі
        browser.element('.box>input').type(name).press_enter()
        time.sleep(5)
        return self
    def registration_open(self):
        browser.element('.login').click()
        browser.element('.register').click()
    def registration_name(self, lastname: str, firstname: str, firstname2: str):
        self.registration_open()
        browser.element('[name="lastname"]').type(lastname)
        browser.element('[name="firstname"]').type(firstname)
        browser.element('[name="firstname2"]').type(firstname2)
        return self
        #time.sleep(5)
    def registration_birthday(self, day: str):
        self.registration_open()
        browser.element('#birthday').type(day)
        return self

    def registration_passwd(self, passwd: str, confirm: str):
        self.registration_open()
        browser.element('#passwd').type(passwd)
        browser.element('#confirm').type(confirm)
        browser.element('.carat').click()
        browser.element('//*[@id="form"]/div[2]/div[2]/div/div/ul/li[22]').click()
        return self

    def registration_address(self, city: str, indx: str, addr: str):
        self.registration_open()
        browser.element('#noroftown').type(city)
        browser.element('#norofindx').type(indx)
        browser.element('#addr').type(addr)
        browser.element('[name="agree"]').click()
        browser.element('.register-button').click()
        return self

    def registration(self):
        self.registration_open()
        self.registration_name()
        self.registration_birthday()
        self.registration_passwd()
        self.registration_address()

    def authorization(self, login: str, passwd: str):
        browser.element('.login').click()
        browser.element('[placeholder="ЛОГІН"]').type(login)
        browser.element('[placeholder="ПАРОЛЬ"]').type(passwd)
        browser.element('.button').click()
        return  self
    def should_be_authorization(self, text: str):
        self.authoriz.should(have.texts(text))
        time.sleep(5)
        return self
    def desired_products(self):
        browser.element('#menu>ul>li').click()
        browser.element('.rowProducts.row8>div:nth-of-type(6)').click()
        browser.element('.pi-heart-text').click()
        #browser.element('.fancybox-item.fancybox-close').click()
        time.sleep(2)
        return self
    def should_be_desired1(self, text: str):
        self.desired1.should(have.texts(text))
        return self
    def should_be_desired2(self, number: str):
        self.desired2.should(have.texts(number))
        return self
    def adding_to_cart(self):
        browser.element('.fancybox-item.fancybox-close').click()
        browser.element('#menu>ul>li>a').click()
        browser.element('.rowProducts.row8>div:nth-of-type(3)').click()
        browser.element('.pi-size-list>div:nth-of-type(4)').click()
        browser.element('.pi-cart').click()
        return self
    def edit(self):
        self.adding_to_cart()
        # редагування кількості
        browser.element('.fa.fa-plus-square').click()
        browser.element('[href="https://respect-shoes.com.ua/cart"]').click()
        return self
    def should_be_edit(self, num: str ):
        # перевірка наявності товару в кошику в кількості 2
        self.number.should(have.texts(num))
        return self
    def remove(self):
        # видалення товару з кошика
        browser.element('[style="display:block;"]').click()
        return self
    def should_be_remove(self, text: str):
        # перевірка пустого кошика
        self.remove.should(have.texts(text))
        return self
