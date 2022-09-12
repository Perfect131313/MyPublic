import pytest
import uuid
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestData:
    CHROME_EXECUTABLE_PATH = "C:/Users/1/Desktop/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "/Firefox/geckodriver.exe"

    BASE_URL = "https://www.labirint.ru/"

    # HOME PAGE данные для тестирования - кнопка  "Книги"
    BOOKS_BUTTON_DESCRIPTION = "Книги"
    TITLE_OF_HEADER_BEST = "Главное 2022"
    TITLE_FOREIGION_BOOKS = "Билингвы и книги на иностранных яхыках"
    TITLE_CHILD_BOOKS = "Книги для детей"
    TITLE_MANGA_BOOKS = "Комиксы, Манга, Артбуки"
    TITLE_TEENS_BOOKS= "Молодежная литература"
    TITLE_NONFICTION_BOOKS= "Нехудожественная литература"
    TITLE_PERIODICALS_BOOKS = "Периодические издания"
    TITLE_RELIGION_BOOKS = "Религия"
    TITLE_OF_HEADER_SCHOOL = "Учебная,методическаялитература и словари"
    TITLE_OF_BOOKS = "Художественная литература"


    ATTRIBUTE_ID = "id"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_VALUE = "value"

    # locator for button to close popup which appear after any action ("В Корзину", "ОТЛОЖИТЬ", etc)
    CLOSE_POPUP_ANY_ACTION = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    # locator for Basket "Корзина" counter
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

    """for BASKET"""
    # locator for Basket "Корзина" button at header
    BASKET_BUTTON_AT_HEADER = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js '
                                         'cart-icon-js"]')
    # locator for Basket "Корзина" counter
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    # Successful deletion of books from Basket
    YOUR_BASKET_IS_EMPTY_TEXT = "Ваша корзина пуста. Почему?"

    # CURRENT Region setting
 #   CITY_TO_SET = "Казань"
 #   CURRENT_CITY = "Казань"

    # equal to "москва" in cyrillic
#    CITY_TO_SET_IN_CYRILLIC = "Владивосток"
#    FIRST_CITY_IN_AUTO_ADVICE = "Владивосток"

#    CITY_TO_SET_WRONG_LANGUAGE = "Rfkbybyuhfl"
#    FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC = "Калининград"

    # Data for PostponePage tests
#    NUMBER_OF_BOOKS_TO_POSTPONE = 3

    # Successful deletion of postponed books message
#   SUCCESSFUL_DELETION = "Выбранные товары удалены!"

    # Successful deletion of books from Basket
 #   YOUR_BASKET_IS_EMPTY_TEXT = "Ваша корзина пуста. Почему?"



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1200, 1000)

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Attach screenshot to Allure report:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
