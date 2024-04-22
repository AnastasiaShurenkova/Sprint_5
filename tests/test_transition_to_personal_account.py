from conftest import driver
from locators import StellarBurgers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersTransitionToPersonalAccount:
    def test_transition_to_personal_account(self, driver): # метод для тестирования входа в личный кабинет
        wait = WebDriverWait(driver, 5)
        driver.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")
        driver.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()
        driver.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.ACCOUNT_TEXT))

        current_url_before_login = driver.current_url

        assert 'account/profile' in current_url_before_login




