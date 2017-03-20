import unittest
import main_test
from selenium.webdriver.common.keys import Keys



class Name(main_test.MainTest):

	def test_(self):
		driver = self.driver
		driver.get('https://yandex.ru')

		element = driver.find_element_by_name('login')
		element.clear()
		element.send_keys('')

		element = driver.find_element_by_name('passwd')
		element.clear()
		element.send_keys('')

		element = driver.find_element_by_class_name('auth__button')
		element.click()

		driver.implicitly_wait(5)

		element = driver.find_element_by_class_name('mail-ComposeButton')
		element.click()

		element = driver.find_element_by_name('to')
		element.send_keys('utopiacosmica@icloud.com')

		element = driver.find_element_by_class_name('cke_editable')
		element.send_keys('TEST TEST TEST TEST TEST TEST TEST TEST ')

		element = driver.find_element_by_class_name('js-send')
		element.click()



if __name__ == "__main__":
	unittest.main()
