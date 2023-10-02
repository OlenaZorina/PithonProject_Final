from selene import have, command
from selene.support import by
from selene.support.shared import browser



class Respect:

    def __init__(self):
        self.respect_list = browser.all(by.css('.result'))

    def open(self):
        browser.open('https://respect-shoes.com.ua')
        return