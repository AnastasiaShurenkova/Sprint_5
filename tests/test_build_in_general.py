from conftest import driver_general
from locators import StellarBurgers


class TestIngridients: # класс для тестирования вкладок с булками, соусами и начинками
    def test_roll_page(self,driver_general):
        driver_general.find_element(*StellarBurgers.SAUCES).click()
        driver_general.find_element(*StellarBurgers.ROLLS).click()

        rolls_section = driver_general.find_element(*StellarBurgers.ROLLS_SECTION)

        assert 'current' in rolls_section.get_attribute('class')

        driver_general.quit()

    def test_sauces_page(self, driver_general):
        driver_general.find_element(*StellarBurgers.SAUCES).click()

        sauces_section = driver_general.find_element(*StellarBurgers.SAUCES_SECTION)

        assert 'current' in sauces_section.get_attribute('class')

        driver_general.quit()

    def test_fillings_page(self, driver_general):
        driver_general.find_element(*StellarBurgers.FILLINGS).click()

        fillings_section = driver_general.find_element(*StellarBurgers.FILLINGS_SECTION)

        assert 'current' in fillings_section.get_attribute('class')

        driver_general.quit()
