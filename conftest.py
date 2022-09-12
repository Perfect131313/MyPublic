import pytest
from selenium import webdriver
from config import TestData

@pytest.fixture (scope="function")
def driver(request):
    path=str(request.fspath)
    driver = webdriver.Chrome(f"{path[:path.find('page_object')]}page_object/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        web_driver.set_window_size(1400, 1000)

    request.cls.driver = web_driver
    yield
    web_driver.quit()