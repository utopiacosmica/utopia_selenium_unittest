import unittest
from selenium import webdriver
# import os



class MainTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('driver_mac/chromedriver')
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.close()
