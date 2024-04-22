from conftest import driver
from locators import StellarBurgers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import random_email
import settings

class TestStellarBurgersRegistrationCorrectPassword: # класс для тестирования регистрации
    def test_registration(self, driver):
        driver.get(settings.URL + 'register')
        wait = WebDriverWait(driver, 5)
        driver.find_element(*StellarBurgers.NAME_SELECTOR).send_keys('Анастасия')
        driver.find_element(*StellarBurgers.EMAIL_SELECTOR).send_keys(random_email)
        driver.find_element(*StellarBurgers.PASSWORD_SELECTOR).send_keys("123456")

        driver.find_element(*StellarBurgers.REGISTRATION_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.AUTHORIZATION_BUTTON))

        current_url_before_login = driver.current_url

        assert 'login' in current_url_before_login



