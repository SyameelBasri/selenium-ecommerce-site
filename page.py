from locator import *
from element import *
from selenium.webdriver.support.ui import Select

class BasePage(object):
	def __init__(self, driver) -> None:
		self.driver = driver

#HOMEPAGE

class MainPage(BasePage):
	search_text_element = SearchTextElement()

	def click_go_button(self):
		element = self.driver.find_element(*MainPageLocator.GO_BUTTON)
		element.click()

	def goto_signin(self):
		element = self.driver.find_element(*MainPageLocator.SIGNIN_BUTTON)
		element.click()

	def goto_women_section(self):
		element = self.driver.find_element(*MainPageLocator.WOMEN_SECTION)
		element.click()

#SIGN IN PAGE

class SigninPage(BasePage):
	email_signin = SigninEmailTextElement()
	password_signin = SiginPasswordTextElement()
	email_create = CreateEmailTextElement()

	def is_title_matches(self):
		return "Login" in self.driver.title

	def click_signin(self):
		element = self.driver.find_element(*SigninPageLocator.SIGNIN_SUBMIT_BUTTON)
		element.click()

	def click_create_account(self):
		element = self.driver.find_element(*SigninPageLocator.CREATE_ACCOUNT_BUTTON)
		element.click()

#CREATE ACCOUNT PAGE

class CreateAccountPage(BasePage):
	
	customer_first_name = FirstNameTextElement()
	customer_last_name = LastNameTextElement()
	password = CreatePasswordTextElement()
	address_first_name = AddressFirstNameTextElement()
	address_last_name = AddressLastNameTextElement()
	address = AddressTextElement()
	city = CityTextElement()
	zipcode = ZipCodeTextElement()
	mobile_phone = MobilePhoneTextElement()

	def is_heading_matches(self):
		heading = self.driver.find_element(*CreateAccountPageLocator.HEADING)
		print(heading.text)
		return "Create an account" in heading.text
	
	def select_title(self):
		element = self.driver.find_element(*CreateAccountPageLocator.TITLE_MR)
		element.click()
	
	def select_day(self):
		select = Select(self.driver.find_element_by_id("days"))
		select.select_by_value('1')

	def select_month(self):
		select = Select(self.driver.find_element_by_id("months"))
		select.select_by_value('1')

	def select_year(self):
		select = Select(self.driver.find_element_by_id("years"))
		select.select_by_value('2000')

	def select_state(self):
		select = Select(self.driver.find_element_by_id("id_state"))
		select.select_by_value('1')

	def click_register(self):
		element = self.driver.find_element(*CreateAccountPageLocator.REGISTER_ACCOUNT)
		element.click()

#ACCOUNT PAGE

class AccountPage(BasePage):
	def is_title_matches(self):
		return "My account" in self.driver.title

	def goto_personal_info(self):
		element = self.driver.find_element(*MyAccountPageLocator.PERSONAL_INFO)
		element.click()

class WomenSectionPage(BasePage):
	def select_item(self):
		element = self.driver.find_element(*WomenSectionPageLocator.SELECT_FIRST_ITEM)
		element.click()

class ItemPage(BasePage):
	def select_size(self):
		select = Select(self.driver.find_element_by_xpath("//*[@id=\"group_1\"]"))
		select.select_by_value('2')

	def add_to_cart(self):
		element = self.driver.find_element(*ItemPageLocator.ADD_TO_CART)
		element.click()

	def goto_cart(self):
		element = self.driver.find_element(*ItemPageLocator.GOTO_CART)
		element.click()