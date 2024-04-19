from conftest import driver_general
from locators import StellarBurgers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersExitFromAccount: # класс для тестирования выхода из аккаунта
    def test_exit_from_account(self, driver_general):
        wait = WebDriverWait(driver_general, 5)
        driver_general.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_general.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")
        driver_general.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()
        driver_general.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()
        wait.until(expected_conditions.visibility_of_element_located((StellarBurgers.EXIT_BUTTON)))
        driver_general.find_element(*StellarBurgers.EXIT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located((StellarBurgers.AUTHORIZATION_BUTTON)))

        current_url_before_login = driver_general.current_url

        assert 'account/profile' not in current_url_before_login


