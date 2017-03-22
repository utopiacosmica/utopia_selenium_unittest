import unittest
import main_test
from selenium.webdriver.common.keys import Keys


class PythonOrgSiteSearch(main_test.MainTest):

    def test_(self):
        driver = self.driver
        driver.implicitly_wait(2)
        driver.get("http://www.python.org")
        driver.implicitly_wait(2)
        self.assertIn("Python", driver.title)
        driver.implicitly_wait(2)
        elem = driver.find_element_by_name("q")
        driver.implicitly_wait(2)
        elem.send_keys("pycon")
        driver.implicitly_wait(2)
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(2)
        assert "No results found." not in driver.page_source



if __name__ == "__main__":
    unittest.main()
