import time
from selene import browser, by, be, have
from Respect_testing.model import resp


def test_open():
    resp.open()
def test_search():
    resp.open()
    resp.search()
def test_should_search():
    resp.open()
    resp.search()
    resp.should_be_search('чорний')
def test_search_button():
    resp.open()
    resp.search_button('Босоніжки')



