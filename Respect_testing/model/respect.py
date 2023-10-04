import time

from selene import have, command
from selene.support import by
from selene.support.shared import browser

class Respect:
    def open(self):
        browser.open('https://respect-shoes.com.ua')
        time.sleep(10)
        return self

    def search(self):
        self.open()
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
        return self

    def should_be_search(self, text: str):
        self.filters.should(have.texts(text))
        time.sleep(5)
        return self

