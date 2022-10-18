from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.debug_locators import *
from locators.login_locators import *

class DebugPage:
	# iOS done
	def switch_to_uat(self, driver):
		# switching to UAT and going to login screen
		debug_btn_click = xpath_click(driver, DEBUG_BTN)
		change_env_to_uat_click = xpath_click(driver, UAT_ENV_RADIO_BTN)
		driver.back()
		click_on_sign_in_btn = xpath_click(driver, SIGN_IN_BTN_IOS)

		# make sure that "Forgot password link" is present
		el_xpath(driver, FORGOT_PASS_LINK)

		# updating data about env
		create_temp_file_and_write_data("uat")

	# iOS done	
	def switch_to_int(self, driver):
		# switching to UAT and going to login screen
		debug_btn_click = xpath_click(driver, DEBUG_BTN)
		change_env_to_int_click = xpath_click(driver, INT_ENV_RADIO_BTN)
		driver.back()
		click_on_sign_in_btn = xpath_click(driver, SIGN_IN_BTN_IOS)

		# make sure that "Forgot password link" is present
		el_xpath(driver, FORGOT_PASS_LINK)

		# updating data about env
		create_temp_file_and_write_data("int")

	# iOS done	
	def switch_to_prod(self, driver):
		# switching to UAT and going to login screen
		debug_btn_click = xpath_click(driver, DEBUG_BTN)
		change_env_to_prod_click = xpath_click(driver, PROD_ENV_RADIO_BTN)
		driver.back()
		click_on_sign_in_btn = xpath_click(driver, SIGN_IN_BTN_IOS)

		# make sure that "Forgot password link" is present
		el_xpath(driver, FORGOT_PASS_LINK)

		# updating data about env
		create_temp_file_and_write_data("prod")	

	def switch_to_uat_version_check(self, driver):
		# read version
		debug_btn_click = xpath_click(driver, DEBUG_BTN)
		read_app_version = el_xpath(driver, DEBUG_INFO_VERSION).text.split("; ")[2]

		change_env_to_uat_click = xpath_click(driver, UAT_ENV_RADIO_BTN)
		driver.back()
		click_on_sign_in_btn = xpath_click(driver, SIGN_IN_BTN_IOS)
		
		# make sure that "Forgot password link" is present
		el_xpath(driver, FORGOT_PASS_LINK)

		create_temp_file_and_write_data("uat")
		#print(read_app_version)
		#print(len(read_app_version))
		update_temp_file(read_app_version)

	def switch_to_int_version_check(self, driver):
		# read version
		read_app_version = el_id(driver, APP_VERSION_LOGIN_SCREEN).text

		debug_btn_click = id_click(driver, DEBUG_BTN)
		change_configuration_menu_click = xpath_click(driver, CHANGE_CONFIG_MENU)
		change_env_to_int_click = xpath_click(driver, INT_ENV_RADIO_BTN)
		toast_msg_env_config = get_toast_msg(driver)
		
		# asserting toast env config message
		assert toast_msg_env_config == "Webapp configuration switched to int"

		change_api_to_int_click = xpath_click(driver, INT_API_RADIO_BTN)
		toast_msg_api_config = get_toast_msg(driver)

		# asserting toast api config message
		assert toast_msg_api_config == "API configuration switched to int"

		go_to_login_screen_click = id_click(driver, GO_TO_LOG_SCR)
		create_temp_file_and_write_data("int")
		update_temp_file(read_app_version)
