# # тесты страницы https://www.labirint.ru/cabinet

from time import sleep
from selenium.webdriver.common.keys import Keys
from pages.LabirintCabinet import LabirintCabinetPage
from pages.Labirint import LabirintHomePage
from pages.LabirintFooter import LabirintFooter

import params



def login_cabinet(web_browser):
    page = LabirintCabinetPage(web_browser)
    page.code_input.send_keys(Keys.CONTROL + 'a')
    page.code_input.send_keys(params.valid_code)
    page.login_btn.click()
    sleep(10)  # ждем пока закроется всплывающее окно
    return page


def test_open_cabinet_page(web_browser):
    """ Пользовательне авторизован, переход в личный кабинет. """
    page = login_cabinet(web_browser)
    assert page.get_current_url() == params.cabinet_url, 'Указан не верный адрес'
    assert page.cabinet.get_text() == 'Код скидки ' + params.valid_code, 'Авторизация не удалась'


def test_change_settings(web_browser):
    """ Авторизуемся в личном кабинете и изменяем ФИО. """
    page = login_cabinet(web_browser)
    page.my_settings.click()
    fio = page.lastname.get_attribute('value') + ' ' + page.firstname.get_attribute('value') + ' ' + \
          page.middlename.get_attribute('value')
    if fio == params.fio1:
        fio = params.fio2
        page.lastname.send_keys(params.fio2.split()[0])
        page.firstname.send_keys(params.fio2.split()[1])
        page.middlename.send_keys(params.fio2.split()[2])
    else:
        fio = params.fio1
        page.lastname.send_keys(params.fio1.split()[0])
        page.firstname.send_keys(params.fio1.split()[1])
        page.middlename.send_keys(params.fio1.split()[2])
    page.save_all.click()
    web_browser.switch_to.alert.accept()  # нажать ОК в модальном окне
    page.wait_page_loaded()
    assert fio == page.lastname.get_attribute('value') + ' ' + page.firstname.get_attribute('value') + ' ' + \
           page.middlename.get_attribute('value')