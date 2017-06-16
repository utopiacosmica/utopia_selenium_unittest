import unittest
import main_test
from selenium.webdriver.common.keys import Keys


class Name(main_test.MainTest):

	def test_(self):
		driver = self.driver
		driver.get('https://www.rottentomatoes.com/')

		element = driver.find_element_by_id('movieMenu')
		element.click()

		element = driver.find_element_by_link_text('New Releases')
		element.click()

		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		element = driver.find_element_by_id('footer-jobs')
		element.click()

		driver.back()




if __name__ == "__main__":
	unittest.main()
