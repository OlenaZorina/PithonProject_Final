import time
from Respect_testing.model import resp

def test_search():
    resp.open()
    resp.search()
    resp.should_be_search('чорний')
def test_search_button():
    resp.open()
    resp.search_button('tamaris')
    resp.should_be_search_button()
def test_registration():
    resp.open()
    resp.registration_open()
    resp.registration_name('Зоріна', 'Олена', 'Миколаївна')
    resp.registration_birthday('25121983')
    resp.registration_passwd('a0822a10f2', 'a0822a10f2')
    resp.registration_address('Харків', '61003', 'майдан Павлівський, 10')
def test_authorization():
    resp.open()
    resp.authorization('zorinae83@gmail.com', 'a0822a10f2')
    resp.should_be_authorization('Мій обліковий запис')
    resp.desired_products()
    resp.should_be_desired('ТОВАР ДОДАНО В ОБРНЕ!')
def test_adding_to_cart():
    resp.open()
    resp.adding_to_cart()
    resp.edit()
    resp.should_be_edit('2')
    resp.remove()
    resp.should_be_remove('Ваш кошик порожній!')

