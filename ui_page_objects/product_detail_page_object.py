from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.product_detail_locators import *
from locators.profile_locators import *
from locators.login_locators import *
from locators.search_locators import *
from locators.debug_locators import *
from locators.post_locators import *


class ProductDetailPage:
	# iOS done
	def add_product_to_wishlist(self, driver):
		# add product to wishlist

		# temprorary commented, need support from devs
		# get_add_btn_ = el_acc_id(driver, WISHLIST_STAR_BUTTON)
		# attrs=[]
		# print(get_add_btn_)
		# print(dir(get_add_btn_))
		# for attr in get_add_btn_.get_property('attributes'):
		# 	attrs.append([attr['name'], attr['value']])
		# print(attrs)

		click_on_star_btn = acc_id_click(driver, WISHLIST_STAR_BUTTON)
		get_add_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
		
		is_removed = None

		if get_add_btn_text == "Remove":
			is_removed = True
			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)

		elif get_add_btn_text == "Add":
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
	
		else:
			print(get_add_btn_text)
			print(f"{ERROR}")

		if is_removed:
			# add product to wishlist
			click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			
			# remove product from wishlist
			click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
			get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
			assert get_remove_btn_text == "Remove"	

			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
		else:
			# remove product from wishlist
			click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
			get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)

	# iOS done
	def add_product_to_wishlist_and_check_in_profile(self, driver):
		# add product to wishlist
		GET_PRODUCT_NAME = el_acc_id(driver, PRODUCT_NAME_PRICE_BLOCK).text
		WISHLIST_NAME = []
		click_on_star_btn = acc_id_click(driver, WISHLIST_STAR_BUTTON)
		get_add_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text

		is_removed = None

		if get_add_btn_text == "Remove":
			is_removed = True
			WISHLIST_NAME.append(el_xpath(driver, NAME_OF_WISHLIST_PRODUCT_PAGE).text)
			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			#toast_msg_wishlist_removed = get_toast_msg(driver)
			#assert toast_msg_wishlist_removed == "Product removed from your wishlist!"
		elif get_add_btn_text == "Add":
			WISHLIST_NAME.append(el_xpath(driver, NAME_OF_WISHLIST_PRODUCT_PAGE).text)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			#toast_msg_wishlist_added = get_toast_msg(driver)
			#assert toast_msg_wishlist_added == "Product added to your wishlist!"	
		else:
			print(get_add_btn_text)
			print(f"{ERROR}")

		if is_removed:
			# add product to wishlist
			click_on_star_btn = acc_id_click(driver, WISHLIST_STAR_BUTTON)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			#toast_msg_wishlist_added = get_toast_msg(driver)
			#assert toast_msg_wishlist_added == "Product added to your wishlist!"
			
		# going back to profile
		click_on_back_btn = acc_id_click(driver, CLOSE_BTN)
		time.sleep(1)
		driver.back() # additional step
		profile_footer_icon_click = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		wishlist_profile_click = xpath_click(driver, PROFILE_WISHLIST_TAB)

		# checking if item was indeed added to correct wishlist
		# Note: can't avoid try/except block, because of java error (stale element exception > unknown DOM issue)
		try:
			list_of_all_wishlists = elems_xpath(driver, WISHLIST_ITEMS_TITLE_LIST)
			click_on_wishlist_with_correct_name = [i.click() for i in list_of_all_wishlists if i.text == WISHLIST_NAME[0]]
		except:
			pass

		list_of_all_items_inside_wishlist = elems_xpath(driver, LIST_OF_ITEMS_INSIDE_WISHLIST)

		# try/except block to avoid unknown java issue
		try:
			click_on_correct_product_name_inside_wishlist = [x.click() for x in list_of_all_items_inside_wishlist if x.text == GET_PRODUCT_NAME]
		except:
			pass

		get_product_name_from_product_detail_page = el_acc_id(driver, PRODUCT_NAME_PRICE_BLOCK).text

		# checking correctness of added product to checklist
		assert get_product_name_from_product_detail_page == GET_PRODUCT_NAME

	# iOS done	
	def open_product_website(self, driver):
		# going to detail product page
		click_on_home_footer_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		scroll_on_feed_page_ios(driver)

		read_product_title = el_acc_id(driver, FEED_PRODUCT_TITLE).text
		product_title_click = acc_id_click(driver, FEED_PRODUCT_TITLE)
		read_product_name_on_detail_page = el_acc_id(driver, PRODUCT_NAME_PRICE_BLOCK).text

		assert read_product_title == read_product_name_on_detail_page

		# checking website URL
		click_on_by_now_btn = id_click(driver, BUY_NOW_BTN)
		taking_you_to_win_ios(driver) # passing modal window
		#select_chrome_browser(driver)
		time.sleep(5) # to read correct url, theoretically can be removed

		page_url = el_acc_id(driver, BROWSER_URL_BAR).text
		assert len(page_url) > 8

	# iOS in done
	def add_product_to_post(self, driver):
		# going to detail product page
		click_on_home_footer_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		#scroll_on_feed_page(driver)
		scroll_on_feed_page_ios(driver)
		click_on_first_product_in_feed = acc_id_click(driver, FEED_PRODUCT_TITLE)

		# product detail page steps > add to post
		read_product_name = el_acc_id(driver, PRODUCT_NAME_PRICE_BLOCK).text
		open_product_sub_menu = acc_id_click(driver, PRODUCT_PAGE_SUB_MENU)
		click_on_add_to_post_sub_menu_item = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)

		# assert product name on post creation step #1				
		assert el_xpath(driver, PRODUCT_NAME_PRODUCTS_TAB_FILLED_IMAGE).is_displayed()
		scroll_on_post_page_ios(driver)
		read_product_name_in_post_creation_step = el_xpath(driver, f"//XCUIElementTypeStaticText[@name='{read_product_name}']").text #el_xpath(driver, PRODUCT_NAME_POST_CREATION).text

		# print(read_product_name_in_post_creation_step)
		# print(read_product_name)
		assert read_product_name == read_product_name_in_post_creation_step

	# iOS in progress
	def add_product_to_question(self, driver):
		random_question_text = "question " + str(random.randint(1000, 10000000))

		# going to detail product page
		click_on_home_footer_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		scroll_on_feed_page_ios(driver)
		click_on_first_product_in_feed = acc_id_click(driver, FEED_PRODUCT_TITLE)

		# product detail page steps > add to question
		read_product_name = el_acc_id(driver, PRODUCT_NAME_PRICE_BLOCK).text
		open_product_sub_menu = acc_id_click(driver, PRODUCT_PAGE_SUB_MENU)
		click_on_add_to_question_sub_menu_item = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)

		# assert product name on question creation step #2
		xpath_keys(driver, QUESTION_TEXT_STEP_ONE, random_question_text)
		click_next_btn = acc_id_click(driver, STEP_BTN_ADD_PRODUCT)

		click_next_btn_again = acc_id_click(driver, STEP_BTN_ADD_PRODUCT)

		# assert product name on post creation step #1				
		assert el_xpath(driver, PRODUCT_NAME_PRODUCTS_TAB_FILLED_IMAGE).is_displayed()
		scroll_on_post_page_ios(driver)
		read_product_name_in_post_creation_step = el_xpath(driver, f"//XCUIElementTypeStaticText[@name='{read_product_name}']").text #PRODUCT_NAME_POST_CREATION).text

		#print(read_product_name_in_post_creation_step)
		#print(read_product_name)
		assert read_product_name == read_product_name_in_post_creation_step


	def open_description_and_terms(self, driver):
		# read description
		scroll_down_deep(driver)
		read_description_text = el_id(driver, DESCRIPTION_TEXT).text

		#assert len(read_description_text) > 10 # depends on product, description can be empty

		# read terms 
		switch_to_terms_tab = acc_id_click(driver, TERMS_TAB)
		read_terms_text = el_id(driver, TERMS_TEXT).text

		assert len(read_terms_text) > 10

		# buy now > read terms
		click_on_buynow_btn = id_click(driver, BUY_NOW_BTN)
		click_on_read_terms_btn_in_window = id_click(driver, PRODUCT_MODAL_READ_TERMS_BTN)

		read_terms_text_in_window = el_xpath(driver, TERMS_TEXT_IN_WINDOW).text
		assert len(read_terms_text_in_window) > 10

			


		