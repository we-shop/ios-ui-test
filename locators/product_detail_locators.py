from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF iOS LOCATORS FOR SEARCH PAGE MODEL
PRODUCT_NAME_PRICE_BLOCK = "titleTextView" #//XCUIElementTypeTextView[@name="titleTextView"]
WISHLIST_STAR_BUTTON = "saveToWishListButton"
ADD_BUTTON_IN_WISHLIST = '(//XCUIElementTypeButton[@name="wishlistItemActionButton"])[1]'
NAME_OF_WISHLIST_INPUT_FIELD = "wishlistNameTextField"
SAVE_BTN_NEW_WISHLIST = "saveButton"
NAME_OF_WISHLIST_PRODUCT_PAGE = '(//XCUIElementTypeStaticText[@name="wishlistItemTitleLabel"])[1]'
CLOSE_BTN = "Close"

WISHLIST_ITEMS_TITLE_LIST = '//XCUIElementTypeCollectionView[@name="wishlistCollectionsView"]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText'
LIST_OF_ITEMS_INSIDE_WISHLIST = '//XCUIElementTypeCollectionView[@name="collectionDetailsCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[1]'
FEED_PRODUCT_TITLE = 'nameLabel'
BUY_NOW_BTN = 'defaultOfferBuyButton'
PRODUCT_MODAL_CONTINUE_BTN = '//XCUIElementTypeButton[contains(@name, "Continue")]'
PRODUCT_PAGE_SUB_MENU = "actionButton"
PRODUCT_NAME_PRODUCTS_TAB_FILLED_IMAGE = '//XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage'
PRODUCT_NAME_POST_CREATION = "//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther//XCUIElementTypeStaticText[@name]"


# //XCUIElementTypeButton[@name="Add to post"]
# //XCUIElementTypeButton[@name="Ask a question"]

# titleTextView
# //XCUIElementTypeTextView[@name="titleTextView”]/XCUIElementTypeTextView
# //XCUIElementTypeTextView[@name="titleTextView"]
# //XCUIElementTypeTextView[@name="titleTextView"]
# wishlistNameTextField  (name of whishlist input field)
# saveButton (new wishlist creation)





# WISHLIST_STAR_BUTTON = "com.socialsuperstore.feature_product_detail:id/saveToWishlistBtn"
# ADD_BUTTON_IN_WISHLIST = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.Button"
# 
# PRODUCT_NAME_TITLE = "com.socialsuperstore.feature_product_detail:id/productName" #"com.socialsuperstore:id/toolbarText"

# PRODUCT_NAME_POST_CREATION = "com.socialsuperstore.feature_post_editor:id/name"
# PRODUCT_NAME_PRODUCTS_TAB_FILLED_IMAGE = "//*[contains(@resource-id, 'com.socialsuperstore.feature_post_editor:id/productImage')]"

# PRODUCT_PAGE_SUB_MENU = "com.socialsuperstore.feature_product_detail:id/moreActionsBtn"
# PROFILE_FOOTER_ITEM = "com.socialsuperstore:id/action_profile"
# WISHLIST_PROFILE_CLICK = "Wishlists"
# WISHLIST_FIRST_ITEM_TITLE = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[2]"
# WISHLIST_ITEMS_TITLE_LIST = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView"
# LIST_OF_ITEMS_INSIDE_WISHLIST = "//*[contains(@resource-id, 'com.socialsuperstore:id/productTitle')]"
# NAME_OF_WISHLIST_PRODUCT_PAGE = "com.socialsuperstore:id/productTitle" #"com.socialsuperstore:id/titleTextView"
# PROGRESS_BAR_WISHLIST = "com.socialsuperstore:id/progress"
# BUY_NOW_BTN = "com.socialsuperstore.feature_product_detail:id/stickyBuyBtn"
# FOOTER_PRODUCT_PRICE = "com.socialsuperstore.feature_product_detail:id/stickyPrice"
# FOOTER_PRODUCT_RETAILER = "com.socialsuperstore.feature_product_detail:id/stickyRetailer"
# FEED_PRODUCT_TITLE = "com.socialsuperstore:id/productTitle"


# DESCRIPTION_TAB = "Description"
# TERMS_TAB = "Terms"
# DESCRIPTION_TEXT = "com.socialsuperstore.feature_product_detail:id/descriptionPlainTextView"
# TERMS_TEXT = "com.socialsuperstore:id/term"

# # "Taking you to" window locators
# PRODUCT_MODAL_READ_TERMS_BTN = "com.socialsuperstore:id/readTermsButton"
#PRODUCT_MODAL_CONTINUE_BTN = "com.socialsuperstore:id/continueButton"
# PRODUCT_MODAL_TITLE_TEXT = "com.socialsuperstore:id/titleText"
# TERMS_TEXT_IN_WINDOW = "//androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView" # //androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.TextView
