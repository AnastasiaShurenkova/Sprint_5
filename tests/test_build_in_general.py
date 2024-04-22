from conftest import driver
from locators import StellarBurgers


class TestIngridients: # класс для тестирования вкладок с булками, соусами и начинками
    def test_roll_page(self,driver):
        driver.find_element(*StellarBurgers.SAUCES).click()
        driver.find_element(*StellarBurgers.ROLLS).click()

        rolls_section = driver.find_element(*StellarBurgers.ROLLS_SECTION)

        assert 'current' in rolls_section.get_attribute('class')



    def test_sauces_page(self, driver):
        driver.find_element(*StellarBurgers.SAUCES).click()

        sauces_section = driver.find_element(*StellarBurgers.SAUCES_SECTION)

        assert 'current' in sauces_section.get_attribute('class')



    def test_fillings_page(self, driver):
        driver.find_element(*StellarBurgers.FILLINGS).click()

        fillings_section = driver.find_element(*StellarBurgers.FILLINGS_SECTION)

        assert 'current' in fillings_section.get_attribute('class')



