from selenium.webdriver.common.by import By

class MainPageLocator(object):
	GO_BUTTON = (By.NAME, "submit_search")
	SIGNIN_BUTTON = (By.CLASS_NAME, "header_user_info")
	WOMEN_SECTION = (By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[1]/a")

class SigninPageLocator(object):
	SIGNIN_SUBMIT_BUTTON = (By.NAME, "SubmitLogin")
	CREATE_ACCOUNT_BUTTON = (By.NAME, "SubmitCreate")

class CreateAccountPageLocator(object):
	HEADING = (By.CLASS_NAME, "page-heading")
	TITLE_MR = (By.ID, "uniform-id_gender1")
	TITLE_MRS = (By.ID, "uniform-id_gender2")
	REGISTER_ACCOUNT = (By.NAME, "submitAccount")

class MyAccountPageLocator(object):
	PERSONAL_INFO = (By.CLASS_NAME, "icon-user")

class WomenSectionPageLocator(object):
	SELECT_FIRST_ITEM = (By.XPATH, "//*[@id=\"center_column\"]/ul/li[1]/div/div[1]/div/a[1]/img")

class ItemPageLocator(object):
	ADD_TO_CART = (By.XPATH, "//*[@id=\"add_to_cart\"]/button")
	GOTO_CART = (By.XPATH, "//*[@id=\"header\"]/div[3]/div/div/div[3]/div/a")