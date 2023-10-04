import time
from selene import browser, by, be, have
from Respect_testing.model import resp

def test_open():
    resp.open('https://respect-shoes.com.ua')

def test_search():
    resp.search()
    # resp.should_be_search('https://respect-shoes.com.ua', 'чорний')

def test_s():
    resp.should_be_search()

