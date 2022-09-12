# # тесты страницы https://www.labirint.ru/
import time

import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
import params
from config import TestData
from pages.BasePage import WebPage
from pages.BasketPage import BasketPage

from selenium.webdriver.common.keys import Keys
from pages.LabirintCabinet import LabirintCabinetPage
from pages.Labirint import LabirintHomePage

def test_visit(driver):
    LabirintPage = LabirintHomePage(driver)
    LabirintPage.visit()

def test_open_home_labirint(web_browser):
    """ Проверка открытия домашней страницы. """
    page = LabirintHomePage(web_browser)
    assert page.get_current_url() == params.home_page_url, 'Не верный адрес'


def test_search(web_browser):
    """ Проверяем поиск лабиринта. """
    page = LabirintHomePage(web_browser)
    # close_pop_up(page)
    page.search.send_keys(params.search_request + Keys.ENTER)
    # page.search.send_keys('Пушкин')
    # page.search_btn.click()
    assert page.count_product != 0, 'Товаров не нашлось'


def test_add_to_basket(web_browser):
    """ Ищем книгу и добавляем ее в корзину. """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.code_input.send_keys(Keys.CONTROL + 'a')
    page.code_input.send_keys(params.valid_code)
    page.login_btn.click()
    sleep(10)  # ждем пока закроется всплывающее окно
    page.search.send_keys(params.book_name + Keys.ENTER)
    page.in_basket.click()
    page.basket.click()  # переход в корзину
    page.go_to_buy.click()  # оформить заказ
    page.wait_page_loaded()
    assert page.chekout_btn.is_clickable(), 'Кнопка не автивна'
    page.return_to_basket.click()  # переход в корзину
    page.clear_basket.click()  # после проверки очистить корзину


def test_login_positive(web_browser):
    """ Проверка авторизации. """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.email_input.send_keys(Keys.CONTROL + 'a')
    page.email_input.send_keys(params.valid_email)
    page.login_btn.click()
    page.input_code.send_keys(params.valid_code)
    page.verify_enter_btn.click()
    sleep(10)  # ждем пока закроется всплывающее окно
    page.my_labirint.click()
    assert page.cabinet.get_text() == 'Код скидки ' + params.valid_code, 'Авторизация не удалась'


@pytest.mark.parametrize('invalid_code', params.invalid_codes, ids=params.ids_invalid_codes)
def test_login_negative(web_browser, invalid_code):
    """ Проверка авторизации (код скидки не верный). """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.email_input.send_keys(Keys.CONTROL + 'a')
    page.email_input.send_keys(params.valid_email)
    page.login_btn.click()
    page.input_code.send_keys(invalid_code)
    page.verify_enter_btn.click()
    page.wait_page_loaded()
    assert page.invalid_code.get_text() == 'Введенного кода не существует'


@pytest.mark.parametrize('invalid_code_spec', params.invalid_codes_spec, ids=params.ids_invalid_codes_spec)
def test_login_negative_spec(web_browser, invalid_code_spec):
    """ Проверка авторизации (попытка ввести в поле ввода кода спецсимволы). """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.email_input.send_keys(Keys.CONTROL + 'a')
    page.email_input.send_keys(params.valid_email)
    page.login_btn.click()
    page.input_code.send_keys(invalid_code_spec)
    assert page.invalid_code.get_text() == 'Нельзя использовать символ «' + str(invalid_code_spec) + '»'


def test_change_location(web_browser):
    """ Смена локации. """
    page = LabirintHomePage(web_browser)
    page.change_location.click()
    page.location_input.send_keys('Барнаул')
    page.wait_page_loaded()
    page.location_input.send_keys(Keys.DOWN + Keys.ENTER)
    assert page.location.get_text() == 'Барнаул', 'Не удалось изменить локацию'

    # test that button "Книги" exits
    def test_books_button_visible(self):
        self.homePage = WebPage(self.driver)
        button = self.homePage.is_visible(WebPage.BOOKS)
        assert button is True

        # test that button "Книги" has proper name
        def test_books_button_has_proper_name(self):
            self.homePage = WebPage(self.driver)
            button_name = self.homePage.get_element_text(WebPage.BOOKS)
            assert button_name == TestData.BOOKS_BUTTON_DESCRIPTION

        # test button "Книги" is clickable and leads to proper page
        def test_books_button_clickable(self):
            self.homePage = WebPage(self.driver)
            self.homePage.do_click(WebPage.BOOKS)
            book_page_header = self.homePage.get_element_text(WebPage.BOOKS_PAGE_HEADER)
            assert book_page_header == TestData.TITLE_OF_BOOKS

        # test submenu "Главное 2022" of button "Книги" is clickable and leads to proper page - submenu "Главное 2022"
        def test_submenu_books_of_year_in_book_button(self):
            self.homePage = WebPage(self.driver)
            self.homePage.move_to_submenu_and_click_at_first_level(WebPage.BOOKS, WebPage.MAIN_OF_THE_YEAR)
            books_main_of_the_year_title = self.homePage.get_element_text(WebPage.MAIN_OF_THE_YEAR_HEADER)
            assert books_main_of_the_year_title == TestData.TITLE_OF_HEADER_BEST

        # test submenu "Все книги" of button "Книги" is clickable and leads to proper page - submenu "Книги"
        def test_submenu_all_books_in_book_button(self):
            self.homePage = WebPage(self.driver)
            self.homePage.move_to_submenu_and_click_at_first_level(WebPage.BOOKS, WebPage.ALL_BOOKS)
            all_books_title = self.homePage.get_element_text(WebPage.ALL_BOOKS_HEADER)
            assert all_books_title == TestData.TITLE_OF_BOOKS

        # test submenu "Молодежная литература" of button "Книги" is clickable and leads to proper page - submenu "Книги"
        def test_submenu_teens_books_in_book_button(self):
            self.homePage = WebPage(self.driver)
            self.homePage.move_to_submenu_and_click_at_first_level(WebPage.BOOKS, WebPage.TEENS_BOOKS)
            teens_books_title = self.homePage.get_element_text(WebPage.TEENS_BOOKS_HEADER)
            assert teens_books_title == TestData.TITLE_TEENS_BOOKS

        # test submenu "Периодические издания" of button "Книги" is clickable and leads to proper page - submenu "Книги"
        def test_periodicals_books_in_book_button(self):
            self.homePage = WebPage(self.driver)
            self.homePage.move_to_submenu_and_click_at_first_level(WebPage.BOOKS, WebPage.PERIODICAL_BOOKS)
            periodicals_title = self.homePage.get_element_text(WebPage.PERIODICAL_BOOKS_HEADER)
            assert periodicals_title == TestData.TITLE_PERIODICALS_BOOKS

        #test submenu "Билингвы и книги на иностранных языках" of button "Книги" is clickable
       
        def test_bilingual_in_book_button_at_second_submenu(self):
            self.homePage = WebPage(self.driver)
            self.homePage.move_to_submenu_and_click_at_second_level(WebPage.BOOKS, WebPage.BILINGUAL_FIRST_SUBMENU,
                                                                    WebPage.BILINGUAL_BOOKS)
            bilingual_title = self.homePage.get_element_text(WebPage.BILINGUAL_BOOKS_HEADER)
            assert bilingual_title == TestData.TITLE_MANGA_BOOKS

        # test submenu "Комиксы, Манга, Артбуки" of button "Книги" is clickable
        def test_manga_in_book_button_at_second_submenu(self):
            self.homePage = WebPage(self.driver)
            self.homePage.move_to_submenu_and_click_at_second_level(WebPage.BOOKS,WebPage.MANGA_FIRST_SUBMENU,
                                                                    WebPage.MANGA_BOOKS)
            manga_books_title = self.homePage.get_element_text(WebPage.MANGA_BOOKS_HEADER)
            assert manga_books_title == TestData.TITLE_MANGA_BOOKS

        # test submenu "Комиксы, Манга, Артбуки" of button "Книги" is clickable and leads to proper page - submenu "Манга"
        def test_religion_in_book_button_at_second_submenu(self):
            self.homePage = WebPage(self.driver)
            self.homePage.move_to_submenu_and_click_at_second_level(WebPage.BOOKS, WebPage.RELIGION_FIRST_SUBMENU,
                                                                    WebPage.RELIGION_BOOKS)
            religion_books_title = self.homePage.get_element_text(WebPage.RELIGION_BOOKS_HEADER)
            assert religion_books_title == TestData.TITLE_RELIGION_BOOKS


            # this test check that "Очистить корзину" button displayed at right side above order details clean the basket
            def test_that_clear_basket_button_clean_basket(self):
                self.basketPage = BasketPage(self.driver)
                self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
                    BasketPage.MOVE_BOOK_TO_BASKET)
                self.list_of_buttons_move_into_basket[0].click()
                self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
                self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
                self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
                price_of_first_book_string = self.list_of_book_prices_in_basket[0]
                self.basketPage.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
                result = self.basketPage.get_element_text(BasketPage.BASKET_IS_EMPTY)
                assert self.basketPage.element_is_not_visible(price_of_first_book_string)
                assert result.lower() == TestData.YOUR_BASKET_IS_EMPTY_TEXT.lower()

               # this test check that initial quantity of item (book) added into basket by "В КОРЗИНУ" button is "1" (one piece)
            def test_that_initial_quantity_of_item_added_in_basket_is_one(self):
                self.basketPage = BasketPage(self.driver)
                self.basketPage.remove_all_good_in_basket_and_reload_page()
                self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
                    BasketPage.MOVE_BOOK_TO_BASKET)
                self.list_of_buttons_move_into_basket[0].click()
                self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
                self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
                self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
                    BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
                first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
                quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
                assert int(quantity_of_first_book) == 1

               # this test check that "Оформить" button displayed at right side above order details leads to check out page
            def test_that_start_checkout_button_open_checkout_page(self):
                self.basketPage = BasketPage(self.driver)
                self.basketPage.remove_all_good_in_basket_and_reload_page()
                self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
                    BasketPage.MOVE_BOOK_TO_BASKET)
                self.list_of_buttons_move_into_basket[0].click()
                self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
                self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
                self.basketPage.do_click(BasketPage.START_CHECKOUT)
                self.basketPage.is_visible(BasketPage.CHECKOUT_AND_PAY)
                current_url = self.basketPage.get_current_url()
                assert current_url == BasketPage.BASKET_URL2
