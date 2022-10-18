from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.login_locators import *
from locators.profile_locators import *

#from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# import string
# import random
# from appium.webdriver.common.mobileby import By
# from appium.webdriver.common.mobileby import MobileBy
# import pytest
# from locators.product_detail_locators import PRODUCT_MODAL_CONTINUE_BTN
# from appium.webdriver.common.touch_action import TouchAction


class LoginPage:
	def __init__(self, LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW):
		self.LOGIN_URL = LOGIN_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD
		self.LOGIN_NEW = LOGIN_NEW
		self.PASSWORD_NEW = PASSWORD_NEW
		self.LOGIN_INT = LOGIN_INT
		self.PASSWORD_INT = PASSWORD_INT
		self.LOGIN_INT_NEW = LOGIN_INT_NEW
		self.PASSWORD_INT_NEW = PASSWORD_INT_NEW

	# iOS done	
	def login_only(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = self.LOGIN
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")

		# making login
		login_field = acc_id_keys(driver, LOG_FIELD, USERNAME)
		password_field = acc_id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = acc_id_click(driver, MAKE_LOGIN_BTN)

		# handle notification alert
		handle_notification_alert(driver)

		# handling info block after login
		try:
			xpath_click(driver, CLOSE_BTN_LOGIN)
		except:
			pass

		update_temp_file(self.LOGIN)

	# iOS done	
	def login_only_new_acc(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT_NEW
			PASSWORD = self.PASSWORD_INT_NEW
		elif current_env == "uat":
			USERNAME = self.LOGIN_NEW
			PASSWORD = self.PASSWORD_NEW
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")

		# making login
		login_field = id_keys(driver, LOG_FIELD, USERNAME)
		password_field = id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = id_click(driver, MAKE_LOGIN_BTN)
		update_temp_file(self.LOGIN)

	# iOS done	
	def login_go_to_profile(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = self.LOGIN
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")

		# making login
		login_field = acc_id_keys(driver, LOG_FIELD, USERNAME)
		password_field = acc_id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = acc_id_click(driver, MAKE_LOGIN_BTN)		

		# going to profile settings
		handle_notification_alert(driver)

		# handling info block after login
		try:
			xpath_click(driver, CLOSE_BTN_LOGIN)
		except:
			pass

		click_on_profile_footer_item = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		update_temp_file(self.LOGIN)

	# iOS done
	def login_with_assert(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = self.LOGIN
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")


		# making login
		#time.sleep(2)
		login_field = acc_id_keys(driver, LOG_FIELD, USERNAME)
		password_field = acc_id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = acc_id_click(driver, MAKE_LOGIN_BTN)

		# handle notification alert
		handle_notification_alert(driver)

		# handling info block after login
		try:
			xpath_click(driver, CLOSE_BTN_LOGIN)
		except:
			pass

		# going to profile settings
		go_to_settings = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		profile_first_n_last_name_text = el_acc_id(driver, PROFILE_FIRST_N_LAST_NAMES).text
		profile_username_name_text = el_acc_id(driver, PROFILE_USERNAME).text

		assert profile_username_name_text == f"@{USERNAME}"

	# iOS done	
	def login_to_prod(self, driver):
		# making login to production (without debug step)
		already_have_acc_btn_click = id_click(driver, ALREADY_HAVE_ACC_LINK)
		login_field = id_keys(driver, LOG_FIELD, self.LOGIN)
		password_field = id_keys(driver, PASS_FIELD, self.PASSWORD)
		sign_in_btn_click = id_click(driver, MAKE_LOGIN_BTN)

		# handling info block after login
		try:
			xpath_click(driver, CLOSE_BTN_LOGIN)
		except:
			pass

		# commented, because can be various scenarios
		# # going to profile settings
		# click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)

		# # verify profile first and last name + username
		# profile_first_n_last_name_text = el_id(driver, PROFILE_FIRST_N_LAST_NAMES).text
		# profile_username_name_text = el_id(driver, PROFILE_USERNAME).text

		# assert profile_username_name_text == f"@{self.LOGIN}"

		# click_on_settings_btn = id_click(driver, SETTINGS_BTN_PROFILE)

	# iOS done	
	def login_with_incorrect_creds(self, driver):
		# making login with incorrect creds
		login_field = id_keys(driver, LOG_FIELD, "qatestqa")
		password_field = id_keys(driver, PASS_FIELD, "qatestpassqa")
		sign_in_btn_click = id_click(driver, MAKE_LOGIN_BTN)

		# asserting toast incorrect credentials message
		incorrect_password_msg = el_acc_id(driver, INCORRECT_PASSWORD_MSG).text
		assert incorrect_password_msg == "This account doesn’t exist, try checking your details again."

	# iOS done
	def logout(self, driver):
		# sign out
		click_on_settings_btn = acc_id_click(driver, PROFILE_SETTINGS_BTN)
		scroll_down_ios(driver)
		sign_out_btn_click = acc_id_click(driver, PROFILE_SETTINGS_SIGN_OUT)
		click_yes_in_logout_modal = xpath_click(driver, PROFILE_SIGN_OUT_MODAL_YES_BTN)
		
		# verify login screen title (means that you are successfully logged out)
		login_screen_title_text = el_acc_id(driver, LOGIN_SCREEN_TITLE).text
		assert login_screen_title_text == "Earn shares in the world’s first shoppable social network owned by you"

	def logout_from_main_screen(self, driver):
		# sign out
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		click_on_settings_btn = id_click(driver, SETTINGS_BTN_PROFILE)
		driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
		sign_out_btn_click = xpath_click(driver, SIGN_OUT_BTN)
		click_yes_in_logout_modal = id_click(driver, ACCEPT_MODAL_BTN_LOGOUT)
		
		# verify login screen title (means that you are successfully logged out)
		login_screen_title_text = el_id(driver, LOGIN_SCREEN_TITLE).text
		assert login_screen_title_text == "Earn shares in the world’s first shoppable social network owned by you"


######################################
# funtctions for push up notifications
######################################
	def push_up_subscribe_notification_check(self, driver):
		# sign out
		#driver.open_notifications()
		#time.sleep(3)
		#login_field = id_keys(driver, LOG_FIELD, USERNAME)
		time.sleep(2)



		#driver.lock()
		#time.sleep(2)
		#driver.unlock()

		#push_notification = el_xpath(driver, PUSH_NOTIFICATION_TEXT).text
		#print(push_notification)

		acc_id_click(driver, FOOTER_ITEM_INBOX)





		time.sleep(7)
		#drive.close()