from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By
import time
import pytest
import random
import requests
from ui_page_objects.functions import *
from locators.profile_locators import *
from locators.login_locators import *
from locators.search_locators import *
from locators.debug_locators import *
from locators.post_locators import *
from locators.retailers_locators import *


class RetailersPage:
	# def __init__(self, LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW):
	# 	self.LOGIN_URL = LOGIN_URL
	# 	self.LOGIN = LOGIN
	# 	self.PASSWORD = PASSWORD
	# 	self.LOGIN_NEW = LOGIN_NEW
	# 	self.PASSWORD_NEW = PASSWORD_NEW
	# 	self.LOGIN_INT = LOGIN_INT
	# 	self.PASSWORD_INT = PASSWORD_INT
	# 	self.LOGIN_INT_NEW = LOGIN_INT_NEW
	# 	self.PASSWORD_INT_NEW = PASSWORD_INT_NEW

	# iOS in progress
	def retailers_overview(self, driver):
		#time.sleep(11)
		

		# going to profile settings
		#click_on_profile_footer_item = acc_id_click(driver, FOOTER_ITEM_PROFILE)

		# return back to weshop page
		#click_on_weshop_footer_item = acc_id_click(driver, FOOTER_ITEM_SEARCH)

		wait_for_carousel = long_wait_el_xpath(driver, RETAILERS_TOP_CAROUSEL_ITEM_TITLES)
		#time.sleep(5)
		titles_from_top_carousel_before_scroll = [i.text for i in elems_xpath(driver, RETAILERS_TOP_CAROUSEL_ITEM_TITLES)]
		horisontal_scroll_retailers_top_carousel(driver)
		time.sleep(0.3) # obligatory
		titles_from_top_carousel_after_scroll = [i.text for i in elems_xpath(driver, RETAILERS_TOP_CAROUSEL_ITEM_TITLES)]

		assert titles_from_top_carousel_before_scroll != titles_from_top_carousel_after_scroll

		#print(titles_from_top_carousel_before_scroll)
		#print(titles_from_top_carousel_after_scroll)
		# read count of followers and following
		# profile_followers = int(el_xpath(driver, FOLLOWERS_COUNT).text)
		# profile_following = int(el_xpath(driver, FOLLOWINGS_COUNT).text)

		# # going to followers/following and reading real count of followers/following
		# click_on_followers_btn = xpath_click(driver, FOLLOWERS_LABEL_PROFILE)
		# total_count_of_existing_followers = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))
		# click_on_following_tab = xpath_click(driver, FOLLOWINGS_LABEL_PROFILE)
		# total_count_of_existing_following = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))
