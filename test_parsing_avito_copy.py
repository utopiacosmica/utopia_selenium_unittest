import unittest
import main_test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep



class Avito(main_test.MainTest):

	def test_avito(self):
		driver = self.driver
		driver.get('https://www.avito.ru')
		element = driver.find_element_by_id('region_640310')
		element.click()
		driver.implicitly_wait(5)

		select = Select(driver.find_element_by_name('location_id'))
		select.select_by_value('640650')

		select = Select(driver.find_element_by_name('category_id'))
		select.select_by_value('98')

		element = driver.find_element_by_id('images_exists')
		element.click()

		element = driver.find_element_by_class_name('search-form__submit')
		element.click()

		posts = driver.find_elements_by_class_name('js-catalog-item-enum')
		for post in posts:
			file = open ('/Users/utopia/Desktop/avito.txt', 'a')
			file.write(post.text.encode('utf8'))
			file.close()

		driver.implicitly_wait(5)

		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		element = driver.find_element_by_class_name('pagination-page')
		element.click()

		sleep(2)

		posts = driver.find_elements_by_class_name('js-catalog-item-enum')
		for post in posts:
			print post


if __name__ == "__main__":
	unittest.main()








		