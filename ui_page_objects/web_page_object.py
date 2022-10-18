from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random


from ui_page_objects.functions import *
from locators.profile_locators import *
from locators.login_locators import *
from locators.search_locators import *
from locators.debug_locators import *
from locators.post_locators import *
from locators.product_detail_locators import *

# core
from locators.web_locators import *
from ui_page_objects.web_functions import *



class WebPage:
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


	def subscribe_to_acc_on_web(self, web_driver):
		# selecting credentials

		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = "mike-qathree"
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = "nemesisten"
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")

		web_driver.set_window_size(1920, 1080)
		web_driver.get(f"https://{current_env}.we.shop/s/login")

		cookie_accept_btn = web_xpath_click(web_driver, COOKIE_ACCEPT_BTN)
		enter_login = web_xpath_keys(web_driver, LOGIN_INPUT_FIELD, USERNAME)
		enter_password = web_xpath_keys(web_driver, PASSWORD_INPUT_FIELD, PASSWORD)
		make_login_btn_click = web_xpath_click(web_driver, MAKE_LOGIN_BTN)

		web_el_xpath(web_driver, PROFILE_EDIT_BTN) # wait purpose
		web_driver.get(f'https://{current_env}.we.shop/u/{USERNAME[0:7]}')

		# getting text of follow button and further flow
		get_user_follow_state = web_el_xpath(web_driver, PROFILE_FOLLOW_UNFOLLOW_USER_BTN).text

		if get_user_follow_state == "Unfollow":
			web_xpath_click(web_driver, PROFILE_FOLLOW_UNFOLLOW_USER_BTN)
			time.sleep(2)
			web_driver.get(f'https://{current_env}.we.shop')
			time.sleep(3)
			web_driver.get(f'https://{current_env}.we.shop/u/{USERNAME[0:7]}')
			time.sleep(2)
			web_xpath_click(web_driver, PROFILE_FOLLOW_UNFOLLOW_USER_BTN)
			time.sleep(2)

		elif get_user_follow_state == "Follow":
			web_xpath_click(web_driver, PROFILE_FOLLOW_UNFOLLOW_USER_BTN)

		else:
			print(f"{SOMETHING_WRONG_WITH_FOLLOW_USER_BTN}")


		print(current_env)
		web_driver.close()
		#time.sleep(2)
		# go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)
		# go_to_wenews_tab = acc_id_click(driver, DASHBOARD_WENEWS_TAB)

		# # open first news item
		# read_first_post_title = el_id(driver, DASH_WENEWS_POST_TITLE).text
		# first_news_item_read_more_click = id_click(driver, DASH_WENEWS_READ_MORE_BTN)
		# read_post_title_inside = el_xpath(driver, DASH_WENEWS_READ_MORE_POST_TITLE).text

	def stub_function(self, driver):
		pass