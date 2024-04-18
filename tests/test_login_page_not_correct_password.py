from conftest import driver_registration
from locators import StellarBurgers

class TestStellarBurgersRegistrationNotCorrectPassword: # класс для тестирования регистрации и проверки вывода ошибки ввода пароля короче шести символов
    def test_registration(self, driver_registration):
        driver_registration.find_element(*StellarBurgers.PASSWORD_SELECTOR).send_keys("123")
        driver_registration.find_element(*StellarBurgers.NAME_SELECTOR).send_keys('Анастасия')


        assert driver_registration.find_element(*StellarBurgers.PASSWORD_ERROR).is_displayed()

        driver_registration.quit()