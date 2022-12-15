from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

RETAILERS_TOP_CAROUSEL_ITEM_TITLES = "//XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeStaticText[contains(@name, '')][1]"

# all retailers block
SEE_MORE_BTN_ALL_RETAILERS = '(//XCUIElementTypeStaticText[@name="See more"])[1]'
RETAILERS_FIRST_ELEM_IN_ALL_LIST = '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[contains(@name, "")]'
RETAILERS_LIST_ALL_ITEMS = '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[contains(@name, "")]'
ALL_RETAILERS_SEARCH_INPUT = '(//XCUIElementTypeSearchField[@name="Search supported retailers"])[1]'
ALL_RETAILERS_NAV_BAR_BACK_BTN = '//XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]'
ALL_RETAILERS_NAV_BAR_SEARCH_BTN = '//XCUIElementTypeNavigationBar/XCUIElementTypeButton[2]'
ALL_RETAILERS_NAV_BAR_SHARE_BTN = '//XCUIElementTypeNavigationBar/XCUIElementTypeButton[3]'

# detail page
RETAILER_DETAIL_REDIRECT_MODAL_TITLE = 'Taking you to retailer in just a moment'
RETAILER_DETAIL_REDIRECT_MODAL_CONTINUE_BTN = '//XCUIElementTypeButton[contains(@name, "Continue")]'
RETAILER_DETAIL_TITLE = '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[contains(@name, "")]'
SHOP_REDIRECT_TO_RETAILER_BTN = '//XCUIElementTypeButton[contains(@name, "Shop direct")]'



# BROWSER_URL_BAR = "//XCUIElementTypeOther[@name='URL']" #"TabBarItemTitle"
# EXTERNAL_BROWSER_URL_BAR = "TabBarItemTitle"


# Mike (Mykhailo) Pastushenko
#   22:13
# Search retailers all list (//XCUIElementTypeSearchField[@name="Search supported retailers"])[1]
# 22:17
# All lst //XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther
#//XCUIElementTypeSearchField[@name="Search"]

# Mike (Mykhailo) Pastushenko
#   22:33
# //XCUIElementTypeApplication[@name="WeQA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]
# //XCUIElementTypeStaticText[@name="Acer UK"]
# 22:35
# //XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText