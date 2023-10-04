import time
from selene import browser, by, be, have
from Respect_testing.model import resp

def test_e2e():
    resp.open()
    resp.search()
    resp.should_be_search('39')
    time.sleep(10)
    resp.search_button('Босоніжки')