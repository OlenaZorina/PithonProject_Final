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
def test_registration_name():
    resp.open()
    resp.registration_open()
    resp.registration_name('Зоріна', 'Олена', 'Миколаївна')
def test_registration_birthday():
    resp.open()
    resp.registration_open()
    resp.registration_birthday('25121983')
def test_registration_passwd():
    resp.open()
    resp.registration_open()
    resp.registration_passwd('a0822a10f2', 'a0822a10f2')

def test_registration_address():
    resp.open()
    resp.registration_open()
    resp.registration_address('Харків', '61003', 'майдан Павлівський, 10')

def test_registration():
    resp.open()
    resp.registration_open()
    resp.registration()
def test_authorization():
    resp.open()
    resp.authorization('zorinae83@gmail.com', 'a0822a10f2')

def test_should_be_authorization():
    resp.open()
    resp.authorization('zorinae83@gmail.com', 'a0822a10f2')
    resp.should_be_authorization('Мій')
def test_desired_products():
    resp.open()
    resp.desired_products()
def test_should_be_desired1():
    resp.open()
    resp.desired_products()
    resp.should_be_desired1('ТОВАР ДОДАНО В ОБРНЕ!')
def test_should_be_desired2():
    resp.open()
    resp.desired_products()
    resp.should_be_desired2('3,790 грн')
def test_adding_to_cart():
    resp.open()
    resp.desired_products()
    resp.adding_to_cart()
def test_edit():
    resp.open()
    resp.edit()
def test_should_be_edit():
    resp.open()
    resp.edit()
    resp.should_be_edit('2')
def test_remove():
    resp.open()
    resp.edit()
    resp.remove()
def test_should_be_remove():
    resp.open()
    resp.edit()
    resp.remove()
    time.sleep(2)
    resp.should_be_remove('Ваш кошик порожній!')
