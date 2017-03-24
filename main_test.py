import unittest
from selenium import webdriver
import os



class MainTest(unittest.TestCase):

	def setUp(self):
		driver_path = os.path.realpath('chromedriver')
		self.driver = webdriver.Chrome(driver_path)
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.close()






