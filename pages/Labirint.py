# описание элементов страницы https://www.labirint.ru/

import os
import params
from pages.BasePage import WebPage
from config import TestData

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.elements import WebElement
from pages.elements import ManyWebElements
#from config import url


class LabirintHomePage(WebPage):
    """By locators - OR"""
    URL = TestData.BASE_URL

    # locator for "Лабиринт" logo by which we can return at home page
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # locator for button "Принять" accept cookies policy
    COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    # locators of main menu bar for button "Книги" and submenu buttons
    BOOKS = (By.XPATH, '//a[@class="b-header-b-menu-e-text" and contains(text(), "Книги")]')
    BOOKS_PAGE_HEADER = (By.XPATH, '//h1[contains(text(), "Книги")]')
    MAIN_OF_THE_YEAR = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                                  '"Главное 2022")]')
    MAIN_OF_THE_YEAR_HEADER = (By.XPATH, '//h1[contains(text(), "Главные книги 2022")]')
    ALL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Все книги")]')
    ALL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Книги")]')
    TEENS_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Молодежная '
                             'литература")]')
    TEENS_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Молодежная литература")]')
    PERIODICAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                                  '"Периодические издания")]')
    PERIODICAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Периодические издания")]')

    # locators of main menu bar for button "Книги" for books type at second hidden submenu
    BILINGUAL_FIRST_SUBMENU = (By.XPATH,
                               '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                               '"Билингвы и книги на иностранных языках")]')
    BILINGUAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Билингвы")]')
    BILINGUAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Билингвы")]')

    CHILD_BOOKS_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains('
                                           'text(), "Книги для детей")]')
    CHILD_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Детский досуг")]')
    CHILD_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Детский досуг")]')

    MANGA_FIRST_SUBMENU = (By.XPATH,
                           '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Комиксы, '
                           'Манга, Артбуки")]')
    MANGA_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Манга для детей")]')
    MANGA_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Манга для детей")]')

    RELIGION_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text('
                                        '), "Религия")]')
    RELIGION_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Религии мира")]')
    RELIGION_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Религии мира")]')

    # locators for setting of user region location
    REGION_ICON_BUTTON = (By.XPATH, '//span[@class="js-header-menu-region-name"]')
    REGION_CURRENT_SETTING = (By.XPATH, '//span[@class="region-location-icon-txt "]')
    REGION_SEARCH_FIELD = (By.ID, "region-post")
    # locator for auto-advice in search region field
    REGION_GUESS_LUST = (By.XPATH, '//a[@class="a-item"]')

    # locators for header panel
    # for button "Сообщения"
    MESSAGE_BUTTON = (By.XPATH, '//span[@class="b-header-b-personal-e-text" and contains(text(), "Сообщения")]')
    # for popup "Сообщения" window
    POPUP_MESSAGE_BUTTON_WINDOW = (By.XPATH, '//div[@class="b-menu-list-title font_regular"]')

    # for button "Мой Лабиринт"
    MY_LABIRINT_BUTTON = (By.XPATH, '//li[@class="b-header-b-personal-e-list-item have-dropdown '
                                    'b-header-b-personal-e-list-item_cabinet"]')
    POPUP_MY_LABIRINT_BUTTON_WINDOW = (By.XPATH, '//div[@class="b-header-login-action-logo-e-wrap"]')

    # for button "Отложено"
    POSTPONED_BOOKS_BUTTON = (By.XPATH,
                              '//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-putorder '
                              'b-header-e-sprite-background"]')
    POPUP_POSTPONED_BOOKS_WINDOW = (By.XPATH, '//div[contains(text(), '
                                              '"Здесь будут храниться ваши отложенные товары.")]')

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or params.home_page_url
        super().__init__(web_driver, url)

    def visit(self):
       self.driver.get()

    # строка поиска
    search = WebElement(id='search-field')

    # кнопка поиска
    search_btn = WebElement(xpath='//*[@id="searchform"]/div[1]/button/span[1]')

    # кнопка закрыть pop-up
    close_pop_up_btn = WebElement(xpath='//*[@id="minwidth"]/div[3]/div[1]/a/span/span')

    # счетчик найденных товаров
    count_product = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[1]/a/span[2]')

    # мой лабиринт
    my_labirint = WebElement(css_selector='.b-header-b-personal-e-icon.b-header-b-personal-e-icon-m-profile'
                                          '.b-header-e-sprite-background')

    # поле ввода email
    email_input = WebElement(css_selector='.full-input__input.formvalidate-error')

    # кнопка Войти
    login_btn = WebElement(id='g-recap-0-btn')

    # поле ввода скидки
    input_code = WebElement(css_selector='.full-input__input.formvalidate-error')

    # кнопка Проверить код и войти
    verify_enter_btn = WebElement(xpath='//*[@id="auth-email-sent"]/input[5]')

    # Личный кабинет
    cabinet = WebElement(xpath='//*[@id="minwidth"]/div[3]/div[1]/div/div[1]/div/span[2]')

    # не верный код скидки
    invalid_code = WebElement(xpath='//*[@id="auth-email-sent"]/div[3]/span[3]/small')

    # сменить локацию
    change_location = WebElement(css_selector='.region-location-icon.region-location-icon-m-hover-hide.b-header-e-sprite-background')

    # строка региона
    location_input = WebElement(css_selector='#region-post')

    # текущая локация
    location = WebElement(css_selector='.region-location-icon-txt')

    # кнопка в корзину
    in_basket = WebElement(css_selector='#buy588504')

    # корзина
    basket = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[6]/a/span[1]/span[1]/span[3]')

    # перейти к оформлению
    go_to_buy = WebElement(css_selector='#cart-total-default > button > span.vue-object')

    # очистить корзину
    clear_basket = WebElement(css_selector='#basket-step1-tabs > div.basket-page__title > div > '
                                           'div.text-regular.empty-basket-link > a')

    # оформить заказ
    chekout_btn = WebElement(xpath='//*[@id="app"]/div[2]/div[3]/div[1]/div[1]/div[1]/div')

    # вернуться в корзину
    return_to_basket = WebElement(css_selector='#app > div.checkout.set-width > div.checkout__header > '
                                               'div.book-shelf.set-width.padding-set > span')

    # поле ввода кода
    code_input = WebElement(css_selector='.full-input__input.formvalidate-error')

    # результаты поиска
    result_search = ManyWebElements(css_selector='#rubric-tab > div.b-search-page-content > div:nth-child(1) > '
                                                 'div.products-row-outer.responsive-cards > div')
    def get_home_page_title(self, title):
        return self.get_title(title)

    def move_away_from_element(self, by_locator):
        element_to_move = self.find_one_element(by_locator)
        action: ActionChains = ActionChains(self.driver)
        action.move_to_element(element_to_move).perform()