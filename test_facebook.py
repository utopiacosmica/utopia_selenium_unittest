import unittest
import main_test
from selenium.webdriver.common.keys import Keys


class FaceBook(main_test.MainTest):

    def test_(self):
        driver = self.driver
        driver.get('https://www.facebook.com')

        elem = driver.find_element_by_id('email')
        elem.clear()
        elem.send_keys('')

        elem = driver.find_element_by_id('pass')
        elem.clear()
        elem.send_keys('')

        elem = driver.find_element_by_id('u_0_q')
        elem.send_keys(Keys.RETURN)

        elem = driver.find_element_by_id('userNavigationLabel')
        elem.click()
        driver.implicitly_wait(5)
        elem = driver.find_element_by_xpath('//*[@id="BLUE_BAR_ID_DO_NOT_USE"]/div/div/div[1]/div/div/ul/li[12]/a/span/span')
        elem.click()




if __name__ == "__main__":
    unittest.main()
