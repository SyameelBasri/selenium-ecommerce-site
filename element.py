from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
	#set value of an element
	def __set__(self, obj, value):
		driver = obj.driver
		WebDriverWait(driver, 100).until(
			lambda driver: driver.find_element_by_name(self.locator)
		)
		driver.find_element_by_name(self.locator).clear()
		driver.find_element_by_name(self.locator).send_keys(value)

	#get value of an element
	def __get__(self, obj, owner):
		driver = obj.driver
		WebDriverWait(driver, 100).until(
			lambda driver: driver.find_element_by_name(self.locator)
		)
		element = lambda driver: driver.find_element_by_name(self.locator)
		return element.get_attribute("value")

class SearchTextElement(BasePageElement):
	locator = "search_query"

class SigninEmailTextElement(BasePageElement):
	locator = "email"

class SiginPasswordTextElement(BasePageElement):
	locator = "passwd"

class CreateEmailTextElement(BasePageElement):
	locator = "email_create"

class FirstNameTextElement(BasePageElement):
	locator = "customer_firstname"

class LastNameTextElement(BasePageElement):
	locator = "customer_lastname"

class CreatePasswordTextElement(BasePageElement):
	locator = "passwd"

class AddressFirstNameTextElement(BasePageElement):
	locator = "firstname"

class AddressLastNameTextElement(BasePageElement):
	locator = "lastname"

class AddressTextElement(BasePageElement):
	locator = "address1"

class CityTextElement(BasePageElement):
	locator = "city"

class ZipCodeTextElement(BasePageElement):
	locator = "postcode"

class MobilePhoneTextElement(BasePageElement):
	locator = "phone_mobile"