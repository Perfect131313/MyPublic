# описание элементов футера

import os
import params
from pages.BasePage import WebPage
from pages.elements import WebElement


class LabirintFooter(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or params.home_page_url
        super().__init__(web_driver, url)

    # раздел Важно
    # принять cookie
    cookie_accept = WebElement(css_selector='#minwidth > div.top-header > div.cookie-policy > button')

    # Акции
    sales = WebElement(css_selector='#body-top > div.b-rfooter-wrapper > div.b-rfooter-links-content.b-rfooter-m-'
                                    'paralax > div > div:nth-child(2) > div:nth-child(2) > div.b-rfooter-e-item-'
                                    'list-m-wrapper > ul > li:nth-child(1) > a')

    # Главные книги
    bests_books = WebElement(css_selector='#body-top > div.b-rfooter-wrapper > div.b-rfooter-links-content.b-rfooter-'
                                          'm-paralax > div > div:nth-child(2) > div:nth-child(2) > div.b-rfooter-e-'
                                          'item-list-m-wrapper > ul > li:nth-child(2) > a')

    # Бонус за рецензию
    bonus = WebElement(css_selector='#body-top > div.b-rfooter-wrapper > div.b-rfooter-links-content.b-rfooter-m-'
                                    'paralax > div > div:nth-child(2) > div:nth-child(2) > div.b-rfooter-e-item-list-'
                                    'm-wrapper > ul > li:nth-child(3) > a')

    # Сертификаты
    certificates = WebElement(css_selector='#body-top > div.b-rfooter-wrapper > div.b-rfooter-links-content.b-rfooter-'
                                           'm-paralax > div > div:nth-child(2) > div:nth-child(2) > div.b-rfooter-e-'
                                           'item-list-m-wrapper > ul > li:nth-child(4) > a')

    # Только у нас
    exclusive = WebElement(css_selector='#body-top > div.b-rfooter-wrapper > div.b-rfooter-links-content.b-rfooter-m-'
                                        'paralax > div > div:nth-child(2) > div:nth-child(2) > div.b-rfooter-e-item-'
                                        'list-m-wrapper > ul > li:nth-child(5) > a')

    # Предзаказы
    pre_order = WebElement(css_selector='#body-top > div.b-rfooter-wrapper > div.b-rfooter-links-content.b-rfooter-m-'
                                        'paralax > div > div:nth-child(2) > div:nth-child(2) > div.b-rfooter-e-item-'
                                        'list-m-wrapper > ul > li:nth-child(6) > a')
