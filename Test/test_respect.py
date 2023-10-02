import time
from selene import have, by
from selene.support.shared import browser
from Respect_testing.model import resp

def test_open():
    resp.open()
