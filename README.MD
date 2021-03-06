# A quick start guide to Selenium:

## Need for work:

- Python 2.7
- selenium (3.3.1)
- unittest2 (1.1.0)




## dropdown (menu)
```
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_name('location_id'))
select.select_by_value('640650')
```

## action chains (hide menu)
```
from selenium.webdriver.common.action_chains import ActionChains

menu = driver.find_element_by_link_text('MTB')
hidden_submenu = driver.find_element_by_link_text('Components')
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
```

## parsing by elements
```
posts = driver.find_elements_by_class_name('js-catalog-item-enum')
for post in posts:
	print post.text
```

## parsing in write to file
```
posts = driver.find_elements_by_class_name('js-catalog-item-enum')
for post in posts:
	file = open ('/Users/utopia/Desktop/avito.txt', 'a')
	file.write(post.text.encode('utf8'))
	file.close()
```

## scroll down
```
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

## scroll x,y
```
driver.execute_script("window.scrollTo(0, 500);")
```

## maximize window
```
driver.maximize_window()
```

## wait
```
driver.implicitly_wait(5)
```

## To move backwards and forwards in your browser’s history:
```
driver.forward()
driver.back()
```

## Take screenshot
```
driver.get_screenshot_as_file('Yandex.png')
```

## Locating Elements
```
	•	find_element_by_id
	•	find_element_by_name
	•	find_element_by_xpath
	•	find_element_by_link_text
	•	find_element_by_partial_link_text
	•	find_element_by_tag_name
	•	find_element_by_class_name
	•	find_element_by_css_selector
```

## Download file
```
chromeOptions = webdriver.ChromeOptions()
prefs = {
"download.default_directory" : "/Users/utopia/Downloads",
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": True
}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "driver_mac/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
driver.maximize_window()
```

## To find multiple elements (these methods will return a list):
```
	•	find_elements_by_name
	•	find_elements_by_xpath
	•	find_elements_by_link_text
	•	find_elements_by_partial_link_text
	•	find_elements_by_tag_name
	•	find_elements_by_class_name
	•	find_elements_by_css_selector
```


## 3.3. Drag and drop
You can use drag and drop, either moving an element by a certain amount, or on to another element:
```
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
```



## Then, you can access the classes like this:
```
webdriver.Firefox
webdriver.FirefoxProfile
webdriver.Chrome
webdriver.ChromeOptions
webdriver.Ie
webdriver.Opera
webdriver.PhantomJS
webdriver.Remote
webdriver.DesiredCapabilities
webdriver.ActionChains
webdriver.TouchActions
webdriver.Proxy
```


## test1
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/utopia/Desktop/sel/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```
## test2
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/utopia/Dropbox/sel/chromedriver')

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://www.python.org")
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
```


## Install
```
virtualenv --no-site-packages selenv
source bin/activate
pip install selenium
pip install unittest2
```
http://selenium-python.readthedocs.io/navigating.html

## run_all.sh
```
#!/bin/sh

python -m unittest discover --pattern=test*.py
```
## main_test.py
```
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
```
## test_python_org
```
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
```
