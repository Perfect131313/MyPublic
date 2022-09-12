# тесты на проверку корректности ссылок в футере

from selenium.webdriver.common.keys import Keys
from pages.LabirintFooter import LabirintFooter
from selenium.webdriver.common.action_chains import ActionChains


def open_scroll_to_footer(web_browser):
    """Открываем браузер, переходим вниз страницы"""
    page = LabirintFooter(web_browser)
    actions = ActionChains(web_browser)
    actions.key_down(Keys.END).perform()
    page.cookie_accept.click()
    return page


def test_click_sales(web_browser):
    """ Переход по ссылке Акции. """
    page = open_scroll_to_footer(web_browser)
    page.sales.click()
    url_current = page.get_current_url()
    assert url_current == 'https://www.labirint.ru/actions/', 'Не верный переход'


def test_click_best_books(web_browser):
    """ Переход по ссылке Главные книги. """
    page = open_scroll_to_footer(web_browser)
    page.bests_books.click()
    url_current = page.get_current_url()
    assert url_current == 'https://www.labirint.ru/best/', 'Не верный переход'


def test_click_bonus(web_browser):
    """ Переход по ссылке Бонус за рецензию. """
    page = open_scroll_to_footer(web_browser)
    page.bonus.click()
    url_current = page.get_current_url()
    assert url_current == 'https://www.labirint.ru/top/bonus-za-recenziyu/', 'Не верный переход'


def test_click_certificates(web_browser):
    """ Переход по ссылке Сертификаты. """
    page = open_scroll_to_footer(web_browser)
    page.certificates.click()
    url_current = page.get_current_url()
    assert url_current == 'https://www.labirint.ru/top/certificates/', 'Не верный переход'


def test_click_exclusive(web_browser):
    """ Переход по ссылке Только у нас. """
    page = open_scroll_to_footer(web_browser)
    page.exclusive.click()
    url_current = page.get_current_url()
    assert url_current == 'https://www.labirint.ru/top/exclusive/', 'Не верный переход'


def test_click_pre_order(web_browser):
    """ Переход по ссылке Предзаказы. """
    page = open_scroll_to_footer(web_browser)
    page.pre_order.click()
    url_current = page.get_current_url()
    assert url_current == 'https://www.labirint.ru/top/skoro-v-prodazhe/', 'Не верный переход'