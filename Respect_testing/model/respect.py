import time
from selene import have, command
from selene.support import by
from selene.support.shared import browser
class Respect:
    def __init__(self):
        self.filters = browser.all('.col8-xl-8.col8-md-6.col8-sm-6.col8-xs-6.cp-selected-filters-box')
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

