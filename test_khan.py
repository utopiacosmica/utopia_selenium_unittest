import unittest
import main_test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep as sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class KhanSimpleBrowse(main_test.MainTest):

    def test_(self):
        driver = self.driver
        driver.get('https://www.khanacademy.org/')
        driver.implicitly_wait(10)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        element = driver.find_element_by_link_text('Volunteer')
        element.click()
        driver.implicitly_wait(10)
        sleep(1)

        element = driver.find_element_by_link_text('Leadership')
        element.click()
        driver.implicitly_wait(10)
        sleep(1)

        element = driver.find_element_by_link_text('Supporters')
        element.click()
        driver.implicitly_wait(10)
        sleep(1)

        element = driver.find_element_by_link_text('Interns')
        element.click()
        driver.implicitly_wait(10)
        sleep(1)

        element = driver.find_element_by_link_text('Team')
        element.click()
        driver.implicitly_wait(10)
        sleep(1)

        element = driver.find_element_by_link_text('About')
        element.click()
        driver.implicitly_wait(10)
        sleep(1)

        driver.execute_script("window.scrollTo(0, 900);")
        driver.implicitly_wait(10)
        sleep(1)

        element = driver.find_element_by_link_text('Learn more about coaching')
        element.click()
        driver.implicitly_wait(10)
        sleep(1)

        driver.execute_script("window.scrollTo(0, 1700);")
        driver.implicitly_wait(10)
        sleep(5)

        driver.get('https://www.khanacademy.org/resources/quick-start/what-is-khan-academy/v/what-is-khan-academy')
        driver.implicitly_wait(5)
        element = driver.find_element_by_class_name('playButton_11v27ws')
        element.click()
        sleep(20)
        driver.get_screenshot_as_file('test_khan.png')
        sleep(28)


        element = driver.find_element_by_link_text('Subjects')
        element.click()
        driver.implicitly_wait(10)
        element = driver.find_element_by_link_text('Art history')
        element.click()
        driver.implicitly_wait(10)

        driver.get('https://www.khanacademy.org/')
        sleep(5)


if __name__ == "__main__":
    unittest.main()
