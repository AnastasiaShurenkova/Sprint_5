from conftest import driver
from locators import StellarBurgers
import settings


class TestStellarBurgersLoginButtonInGeneral: # класс для тестирования входа в аккаунт
    def test_login_button_in_general(self, driver): # метод для проверки входа через кнопку Войти в аккант на главной странице
        driver.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login





    def test_cabinet_button_in_general(self, driver): # метод для тестирования входа через кнопку Личный Кабинет
        driver.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login



    def test_login_from_registration_page(self, driver): # метод для тестирования входа в аккаунт через кнопку Войти в форме регистрации
        driver.get(settings.URL + 'register')
        driver.find_element(*StellarBurgers.LOGIN_IN_REGISTRATION_WINDOW).click()
        driver.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login



    def test_login_from_password_page(self, driver): # метод для тестирования входа в аккант со страницы восстановления пароля
        driver.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver.find_element(*StellarBurgers.NEW_PASSWORD).click()
        driver.find_element(*StellarBurgers.LOGIN_IN_REGISTRATION_WINDOW).click()
        driver.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login


