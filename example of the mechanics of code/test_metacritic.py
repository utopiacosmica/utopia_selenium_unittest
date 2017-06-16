import unittest
import main_test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Name(main_test.MainTest):

    def test_(self):
        driver = self.driver
        driver.get('http://www.metacritic.com/')
        driver.implicitly_wait(1)

        driver.get('http://www.metacritic.com/movie')
        driver.implicitly_wait(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(1)

        driver.get('http://www.metacritic.com/game/switch')
        driver.implicitly_wait(1)

        element = driver.find_element_by_link_text('High Scores')
        element.click()
        driver.implicitly_wait(1)

        element = driver.find_element_by_link_text('By Year')
        element.click()
        driver.implicitly_wait(1)

        select = Select(driver.find_element_by_name('year_selected'))
        select.select_by_value('2016')
        driver.implicitly_wait(1)

        select = Select(driver.find_element_by_name('year_selected'))
        select.select_by_value('2017')
        driver.implicitly_wait(1)

        element = driver.find_element_by_link_text('PS4')
        element.click()
        driver.implicitly_wait(1)

        select = Select(driver.find_element_by_name('year_selected'))
        select.select_by_value('2014')
        driver.implicitly_wait(1)

        driver.get('http://www.metacritic.com/')
        driver.implicitly_wait(1)


if __name__ == "__main__":
    unittest.main()
