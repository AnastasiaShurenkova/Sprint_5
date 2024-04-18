from conftest import driver_general
from locators import StellarBurgers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersTransitionToPersonalAccount:
    def test_transition_to_personal_account(self, driver_general): # метод для тестирования входа в личный кабинет
        wait = WebDriverWait(driver_general, 5)
        driver_general.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_general.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")
        driver_general.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()
        driver_general.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarBurgers.ACCOUNT_TEXT))

        current_url_before_login = driver_general.current_url

        assert 'account/profile' in current_url_before_login



        driver_general.quit()