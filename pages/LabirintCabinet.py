# описание элементов страницы https://www.labirint.ru/cabinet/

import os
import params
from pages.BasePage import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class LabirintCabinetPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or params.cabinet_url
        super().__init__(web_driver, url)

    def visit(self):
        self.driver.get(url)

    # строка поиска
    search = WebElement(id='search-field')

    # поле ввода кода
    code_input = WebElement(css_selector='.full-input__input.formvalidate-error')

    # кнопка Войти
    login_btn = WebElement(id='g-recap-0-btn')

    # Личный кабинет
    cabinet = WebElement(xpath='//*[@id="minwidth"]/div[3]/div[1]/div/div[1]/div/span[2]')

    # результаты поиска
    result_search = ManyWebElements(css_selector='#rubric-tab > div.b-search-page-content > div:nth-child(1) > '
                                                 'div.products-row-outer.responsive-cards > div')

    # мои данные и настройки
    my_settings = WebElement(css_selector='#minwidth > div.top-margin > div.top-content > div > div.cabinet-menu.'
                                          'swiper-container-initialized.swiper-container-horizontal.swiper-container-'
                                          'free-mode > ul > li:nth-child(10) > a')

    # фамилия
    lastname = WebElement(css_selector='#lastname')

    # имя
    firstname = WebElement(css_selector='#firstname')

    # отчество
    middlename = WebElement(css_selector='#middlename')

    # день рождения
    birthday = WebElement(css_selector='#bday')

    # телефон
    phone = WebElement(css_selector='#user_add_number_mobile')

    # сохранить все изменения
    save_all = WebElement(css_selector='#info_form > div.mt20.mb30 > input')