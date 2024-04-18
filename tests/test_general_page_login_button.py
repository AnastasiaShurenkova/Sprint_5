from conftest import driver_general
from conftest import driver_registration
from locators import StellarBurgers


class TestStellarBurgersLoginButtonInGeneral: # класс для тестирования входа в аккаунт
    def test_login_button_in_general(self, driver_general): # метод для проверки входа через кнопку Войти в аккант на главной странице
        driver_general.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_general.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver_general.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver_general.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login



        driver_general.quit()

    def test_cabinet_button_in_general(self, driver_general): # метод для тестирования входа через кнопку Личный Кабинет
        driver_general.find_element(*StellarBurgers.CABINET_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_general.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver_general.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver_general.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login

        driver_general.quit()

    def test_login_from_registration_page(self, driver_registration): # метод для тестирования входа в аккаунт через кнопку Войти в форме регистрации
        driver_registration.find_element(*StellarBurgers.LOGIN_IN_REGISTRATION_WINDOW).click()
        driver_registration.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_registration.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver_registration.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver_registration.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login

        driver_registration.quit()

    def test_login_from_password_page(self, driver_general): # метод для тестирования входа в аккант со страницы восстановления пароля
        driver_general.find_element(*StellarBurgers.LOGIN_BUTTON_IN_GENERAL).click()
        driver_general.find_element(*StellarBurgers.NEW_PASSWORD).click()
        driver_general.find_element(*StellarBurgers.LOGIN_IN_REGISTRATION_WINDOW).click()
        driver_general.find_element(*StellarBurgers.EMAIL_AUTHORIZATION_SELECTOR).send_keys("anastasia_shurenkova_7_124@gmail.com")
        driver_general.find_element(*StellarBurgers.PASSWORD_AUTHORIZATION_SELECTOR).send_keys("123456")

        driver_general.find_element(*StellarBurgers.AUTHORIZATION_BUTTON).click()

        current_url_before_login = driver_general.current_url

        assert 'account/profile/' not in current_url_before_login, 'login' not in current_url_before_login

        driver_general.quit()
