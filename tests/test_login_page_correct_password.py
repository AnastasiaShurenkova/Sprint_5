from conftest import driver_registration
from locators import StellarBurgers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random_mail import random_email

class TestStellarBurgersRegistrationCorrectPassword: # класс для тестирования регистрации
    def test_registration(self, driver_registration):
        wait = WebDriverWait(driver_registration, 5)
        driver_registration.find_element(*StellarBurgers.NAME_SELECTOR).send_keys('Анастасия')
        driver_registration.find_element(*StellarBurgers.EMAIL_SELECTOR).send_keys(random_email)
        driver_registration.find_element(*StellarBurgers.PASSWORD_SELECTOR).send_keys("123456")

        driver_registration.find_element(*StellarBurgers.REGISTRATION_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.AUTHORIZATION_BUTTON))

        current_url_before_login = driver_registration.current_url

        assert 'login' in current_url_before_login


        driver_registration.quit()

