pipimport pytest
from selenium import webdriver
import settings


@pytest.fixture(scope='function') # фикстура, когда необходимо зайти и протестировать функциональность на странице регистрации
def driver_registration():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL_registration)

    return chrome_driver

@pytest.fixture(scope='function') # фикстура, когда необходимо тестировать, начиная с главной страницы
def driver_general():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL_general)

    return chrome_driver

