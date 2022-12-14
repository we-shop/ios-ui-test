from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF iOS LOCATORS FOR SEARCH PAGE MODEL
SEARCH_BTN_HEAD_BAR = "Find products, people & retailers"
SEARCH_BTN_HEAD_BAR_FILLLED_STATE = "navigation bar search"
COLLAPSED_SEARCH_INPUT_FIELD = "Find products, people & retailers" #"Search for a product" 
SELECT_SUGGESTED_ITEM_SEARCH = "//XCUIElementTypeTable[@name='Search results']/XCUIElementTypeCell[2]/XCUIElementTypeStaticText[2]"
FIRST_ITEM_NAME_SEARCH = "(//XCUIElementTypeStaticText[@name='titleLabel'])[1]"
SECOND_ITEM_NAME_SEARCH = "(//XCUIElementTypeStaticText[@name='titleLabel'])[2]"
CLEAR_SEARCH_X_BTN = "Clear text"
RECENT_SEARCH_ITEM_TEXT = '//XCUIElementTypeCell/XCUIElementTypeStaticText'





# SEARCH_INPUT_FIELD = "com.socialsuperstore:id/searchInput"
# COLLAPSED_SEARCH_INPUT_FIELD = "//android.widget.EditText" #"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText" #"com.socialsuperstore:id/collapsedSearchInput" #"com.socialsuperstore:id/textinput_placeholder" 
# SELECT_SUGGESTED_ITEM_SEARCH = "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[1]" #"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView"
# SELECT_SUGGESTED_ITEM_SEARCH_PROFILE = "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView[1]"
# CLEAR_SEARCH_X_BTN ="com.socialsuperstore:id/search"
# FIRST_ITEM_NAME_SEARCH = "//*[contains(@resource-id, 'productTitle')]"
# CLEAR_SEARCH_BTN = "com.socialsuperstore:id/searchClear"
# RECENT_SEARCH_ITEM_TEXT = "com.socialsuperstore:id/recentSearchItemText"
# SEARCH_FIRST_PRODUCT_DETAIL_PAGE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]"
# SEARCH_RESULT_ONE_ITEM_TEXT = "com.socialsuperstore:id/titleText"
# SEARCH_RESULT_SECOND_ITEM = "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]"
# PRODUCT_NAME_PRICE_BLOCK = "com.socialsuperstore.feature_product_detail:id/productName"