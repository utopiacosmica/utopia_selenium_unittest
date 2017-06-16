import unittest
import main_test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Name(main_test.MainTest):

    def test_(self):
        driver = self.driver
        driver.get('http://www.chainreactioncycles.com/ru/ru')
        driver.implicitly_wait(1)

        element = driver.find_element_by_link_text('RUBRUB')
        element.click()

        select = Select(driver.find_element_by_name('/atg/userprofiling/ProfileFormHandler.value.language'))
        select.select_by_value('en')

        element = driver.find_element_by_name('/atg/userprofiling/ProfileFormHandler.updateLocaleInfo')
        element.click()

        menu = driver.find_element_by_link_text('MTB')
        hidden_submenu = driver.find_element_by_link_text('Components')
        actions = ActionChains(driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
        actions.perform()
        driver.implicitly_wait(1)

        element = driver.find_element_by_link_text('Groupsets')
        element.click()
        driver.implicitly_wait(1)

        select = Select(driver.find_element_by_id('sortByDropDowntop'))
        select.select_by_value('pricelow')
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()
