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
		RANGE_ITEMS_INDEXES = list(range(1, 4)) #list(range(1, 9))
		RANDOM_INX = random.randint(0, 2)

		# check carousel
		wait_for_carousel = long_wait_el_xpath(driver, RETAILERS_TOP_CAROUSEL_ITEM_TITLES)
		#time.sleep(5)
		titles_from_top_carousel_before_scroll = [i.text for i in elems_xpath(driver, RETAILERS_TOP_CAROUSEL_ITEM_TITLES)]
		horisontal_scroll_retailers_top_carousel(driver)
		time.sleep(0.3) # obligatory
		titles_from_top_carousel_after_scroll = [i.text for i in elems_xpath(driver, RETAILERS_TOP_CAROUSEL_ITEM_TITLES)]

		assert titles_from_top_carousel_before_scroll != titles_from_top_carousel_after_scroll

		# check all retailers
		click_on_see_more_btn_all_ret = xpath_click(driver, SEE_MORE_BTN_ALL_RETAILERS)
		wait_all_ret_list_first_elem = long_wait_el_xpath(driver, RETAILERS_FIRST_ELEM_IN_ALL_LIST)
		
		assert len(el_xpath(driver, RETAILERS_FIRST_ELEM_IN_ALL_LIST).text) > 2 # "HP" can be as exception, but it's far away (deep in list)
		#print(el_xpath(driver, RETAILERS_FIRST_ELEM_IN_ALL_LIST).text)
		#get_names_of_all_retailers = [i.text for i in elems_xpath(driver, RETAILERS_LIST_ALL_ITEMS)]

		wait_all_present_retailers_xpaths = [el_xpath(driver, f'//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[{i}]/XCUIElementTypeStaticText[contains(@name, "")]') for i in RANGE_ITEMS_INDEXES]
		get_title_of_click_retailer = wait_all_present_retailers_xpaths[RANDOM_INX].text
		click_on_random_retailer_in_all_lst = wait_all_present_retailers_xpaths[RANDOM_INX].click()
		#print(get_title_of_click_retailer)

		# retailer detail page
		get_title_on_retailer_detail_page = el_xpath(driver, RETAILER_DETAIL_TITLE).text
		#print(get_title_on_retailer_detail_page)

		assert get_title_on_retailer_detail_page == get_title_of_click_retailer

		# go to retailers page (site)
		wait_for_shop_direct_btn = long_wait_el_xpath(driver, SHOP_REDIRECT_TO_RETAILER_BTN)
		click_on_shop_direct_btn = xpath_click(driver, SHOP_REDIRECT_TO_RETAILER_BTN)
		wait_modal_title_text = el_acc_id(driver, RETAILER_DETAIL_REDIRECT_MODAL_TITLE)
		wait_for_on_continue_btn = el_xpath(driver, RETAILER_DETAIL_REDIRECT_MODAL_CONTINUE_BTN)

		assert wait_for_on_continue_btn.is_enabled()

		#wait_for_browser_url_line = long_wait_el_xpath(driver, EXTERNAL_BROWSER_URL_BAR)
		wait_for_browser_url_line = long_wait_el_acc_id(driver, EXTERNAL_BROWSER_URL_BAR)
		#print(el_xpath(driver, BROWSER_URL_BAR).text)
		print(el_acc_id(driver, EXTERNAL_BROWSER_URL_BAR).text)
		#EXTERNAL_BROWSER_URL_BAR
		time.sleep(2)
		

		#print(el_xpath(driver, ).text)
		
		#get_all = elems_xpath_special(driver, RETAILERS_LIST_ALL_ITEMS)
		#print(len(get_all))
		#print(get_names_of_all_retailers)

		#go_to_selected_retailer_site = xpath_click(driver, SHOP_REDIRECT_TO_RETAILER_BTN)

		#get_names_of_all_retailers = [i.text for i in elems_xpath(driver, RETAILERS_LIST_ALL_ITEMS)]
		

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
