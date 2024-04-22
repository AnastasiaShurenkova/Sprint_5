from conftest import driver
from locators import StellarBurgers
import settings

class TestStellarBurgersRegistrationNotCorrectPassword: # класс для тестирования регистрации и проверки вывода ошибки ввода пароля короче шести символов
    def test_registration(self, driver):
        driver.get(settings.URL + 'register')
        driver.find_element(*StellarBurgers.PASSWORD_SELECTOR).send_keys("123")
        driver.find_element(*StellarBurgers.NAME_SELECTOR).send_keys('Анастасия')


        assert driver.find_element(*StellarBurgers.PASSWORD_ERROR).is_displayed()


