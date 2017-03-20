import unittest
import main_test
from selenium.webdriver.common.keys import Keys


class PythonOrgSiteSearch(main_test.MainTest):

    def test_(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source



if __name__ == "__main__":
    unittest.main()
