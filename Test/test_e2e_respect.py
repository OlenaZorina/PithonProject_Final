import time
from selene import browser, by, be, have
from Respect_testing.model import resp

def test_e2e():
    resp.open()
    resp.search()
    resp.should_be_search('39')
    time.sleep(2)
    resp.search_button('Босоніжки')
    resp.registration_open()
    resp.registration_name('Зоріна', 'Олена', 'Миколаївна')
    resp.registration_birthday('25121983')
    resp.registration_passwd('a0822a10f2', 'a0822a10f2')
    resp.registration_address('Харків', '61003', 'майдан Павлівський, 10')
    resp.authorization('zorinae83@gmail.com', 'a0822a10f2')
    resp.should_be_authorization('Мій')
    resp.desired_products()
    resp.should_be_desired1('ТОВАР ДОДАНО В ОБРНЕ!')
    resp.should_be_desired2('3,790 грн')
    time.sleep(5)
    resp.adding_to_cart()
    resp.edit()
    resp.should_be_edit('2')
    resp.remove()
    resp.should_be_remove('Ваш кошик порожній!')
