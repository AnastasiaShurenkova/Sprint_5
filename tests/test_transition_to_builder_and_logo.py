from conftest import driver
from locators import StellarBurgers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersTransitionToBuilderAndLogo:
    def test_transition_to_builder(self, driver): # метод для тестирования перехода из личного кабинета в конструктор
        wait = WebDriverWait(driver, 5)
        driver.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")
        driver.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()
        driver.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.BUILDER_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.BUTTON_CHECKOUT))

        current_url_before_login = driver.current_url

        assert 'login' not in current_url_before_login




    def test_transition_to_logo(self, driver): # метод для тестирования клика по логотипу находясь в личном кабинете
        wait = WebDriverWait(driver, 5)
        driver.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")
        driver.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()
        driver.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.LOGO).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.BUTTON_CHECKOUT))

        current_url_before_login = driver.current_url

        assert 'login' not in current_url_before_login

