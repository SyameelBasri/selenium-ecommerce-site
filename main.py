import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import page

# class SearchboxTest(unittest.TestCase):

# 	def setUp(self) -> None:
# 		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# 		self.driver.get("http://automationpractice.com/index.php")

# 	def test_search_box(self):
# 		mainPage = page.MainPage(self.driver)
# 		mainPage.search_text_element = "dress"
# 		mainPage.click_go_button()

# 	def tearDown(self) -> None:
# 		self.driver.close()

# class SignInTest(unittest.TestCase):

# 	def setUp(self) -> None:
# 		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# 		self.driver.get("http://automationpractice.com/index.php")

# 	def test_sign_in(self):
# 		mainPage = page.MainPage(self.driver)
# 		mainPage.goto_signin()

# 		signinPage = page.SigninPage(self.driver)
# 		assert signinPage.is_title_matches()
# 		signinPage.email_signin = "benheatgrade@gmail.com"
# 		signinPage.password_signin = "12345"
# 		signinPage.click_signin()

# 		accountPage = page.AccountPage(self.driver)
# 		assert accountPage.is_title_matches()

# 	def tearDown(self) -> None:
# 		self.driver.close()
	
# class RegisterTest(unittest.TestCase):

# 	def setUp(self) -> None:
# 		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# 		self.driver.get("http://automationpractice.com/index.php")
	
# 	def test_register(self):
# 		mainPage = page.MainPage(self.driver)
# 		mainPage.goto_signin()

# 		signinPage = page.SigninPage(self.driver)
# 		assert signinPage.is_title_matches()
# 		signinPage.email_create = "mel123@gmail.com"
# 		signinPage.click_create_account()

# 		createAccountPage = page.CreateAccountPage(self.driver)
# 		try:
# 			heading = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'page-heading')))
# 			print("Page is ready!")
# 		except TimeoutError:
# 			print("Loading took too much time!")

# 		# createAccountPage = page.CreateAccountPage(self.driver)
# 		# assert createAccountPage.is_heading_matches()
		
# 		createAccountPage.customer_first_name = "Mel"
# 		createAccountPage.customer_last_name = "Maru"
# 		createAccountPage.password = "mel123"
# 		createAccountPage.select_day()
# 		createAccountPage.select_month()
# 		createAccountPage.select_year()
# 		createAccountPage.address_first_name = "Mel"
# 		createAccountPage.address_last_name = "Maru"
# 		createAccountPage.address = "Home"
# 		createAccountPage.city = "Bandar"
# 		createAccountPage.select_state()
# 		createAccountPage.zipcode = "12345"
# 		createAccountPage.mobile_phone = "0123456789"
# 		createAccountPage.select_title()
# 		createAccountPage.click_register()

# 	def tearDown(self) -> None:
# 		self.driver.close()

class AddItemToCart(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
		self.driver.get("http://automationpractice.com/index.php")

	def testAddItemToCart(self):
		mainPage = page.MainPage(self.driver)
		mainPage.goto_women_section()
		womenSectionPage = page.WomenSectionPage(self.driver)
		womenSectionPage.select_item()
		itemPage = page.ItemPage(self.driver)
		itemPage.select_size()
		itemPage.add_to_cart()

	def tearDown(self) -> None:
		self.driver.close()

if __name__ == "__main__":
	unittest.main()