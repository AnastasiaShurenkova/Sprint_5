from conftest import driver_general
from locators import StellarBurgers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersTransitionToBuilderAndLogo:
    def test_transition_to_builder(self, driver_general): # метод для тестирования перехода из личного кабинета в конструктор
        wait = WebDriverWait(driver_general, 5)
        driver_general.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_general.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")
        driver_general.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()
        driver_general.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.BUILDER_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.BUTTON_CHECKOUT))

        current_url_before_login = driver_general.current_url

        assert 'login' not in current_url_before_login




    def test_transition_to_logo(self, driver_general): # метод для тестирования клика по логотипу находясь в личном кабинете
        wait = WebDriverWait(driver_general, 5)
        driver_general.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_general.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")
        driver_general.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()
        driver_general.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.LOGO).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.BUTTON_CHECKOUT))

        current_url_before_login = driver_general.current_url

        assert 'login' not in current_url_before_login

