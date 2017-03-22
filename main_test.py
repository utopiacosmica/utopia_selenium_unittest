import unittest
from selenium import webdriver
import os



class MainTest(unittest.TestCase):

	def setUp(self):
		# driver_path = os.path.realpath('chromedriver')
		self.driver = webdriver.PhantomJS('/Users/utopia/GitHub/utopia_test/phantomjs')
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.close()






