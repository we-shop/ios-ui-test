from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR POST PAGE MODEL
FOOTER_ITEM_REC_PRODUCT = "//XCUIElementTypeButton[@name='Add to post']"
FOOTER_ITEM_ASK_QUESTION = "//XCUIElementTypeButton[@name='Ask a question']"



# new post
ASK_QUESTION_PLUS_MENU = "Ask Question"
REC_PRODUCT_PLUS_MENU = "Recommend a product"
SEARCH_INPUT_POST_CREATION_STEP_ONE = "//XCUIElementTypeButton[@name='Find products to recommend']"
SEARCH_PRODUCT_POST_CREATION = "//XCUIElementTypeSearchField[@name='Search']"

SEARCH_RESULT_PRODUCT_ONE = "(//XCUIElementTypeButton[@name='inactive checkbox icon'])[1]"
SEARCH_RESULT_PRODUCT_TWO = "(//XCUIElementTypeButton[@name='inactive checkbox icon'])[2]"
SEARCH_RESULT_PRODUCT_THREE = "(//XCUIElementTypeButton[@name='inactive checkbox icon'])[3]"
DONE_BTN_ADD_PRODUCT = "Done"
NEXT_BTN_ADD_PRODUCT = "Next"
PRODUCT_ADD_FOOTER_ITEM_MEDIA = "//XCUIElementTypeStaticText[@name='Media']"
MEDIA_IMAGE_FROM_PRODUCT = "//XCUIElementTypeButton[@name='Use product image']"
CAPTION_INPUT_FIELD = "//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView"
PUBLISH_BTN_ADD_PRODUCT = "//XCUIElementTypeButton[@name='Publish']"

# new question
QUESTION_TEXT_STEP_ONE = "//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView" #"//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView"
QUESTION_BREAD_CRUMBS = "//XCUIElementTypeStaticText[@name='pageIndexLabel']"
QUESTION_UPLOAD_FROM_DESIGNS = "//XCUIElementTypeButton[@name='Popular designs']"
CUSTOM_BACKGROUND_ITEMS = "//XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeImage"
SAVE_BTN_BACKGROUND_ITEMS = "Save"
ALL_TEXT_STYLES = "//XCUIElementTypeCollectionView/XCUIElementTypeCell"
BACKGROUND_TEXT_COLOUR_TAB = "Text colour"
DONE_STEP_BTN_ADD_PRODUCT = "Done"
NEXT_STEP_BTN_ADD_PRODUCT = "Next"
#CAPTION_INPUT_FIELD_QUEST = "//XCUIElementTypeScrollView/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView"
POST_TIME_AGO_TEXT = "creationDateLabel"
FEED_POST_DESCRIPTION = "readMoreLabel"


# ADD_FIRST_PRODUCT_PLUS_INPUT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[4]/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView[1]"
# SEARCH_RESULT_PRODUCT_ONE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.CheckBox"
# SEARCH_RESULT_PRODUCT_TWO = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.CheckBox"
# SEARCH_RESULT_PRODUCT_THREE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.CheckBox"

# PRODUCT_ADD_FOOTER_ITEM_PRODUCTS = "Products"
# 
# PRODUCT_ADD_FOOTER_ITEM_CAPTION = "Caption"
# MEDIA_IMAGE_FROM_GALLERY = "com.socialsuperstore.feature_post_editor:id/fromGallery"

# MEDIA_IMAGE_FROM_CAMERA = "com.socialsuperstore.feature_post_editor:id/fromCamera"
# 
# POST_DOTS_SUB_MENU = "com.socialsuperstore:id/postActionsBtn"
# POST_DOTS_SUB_MENU_EDIT_POST = "//androidx.recyclerview.widget.RecyclerView/android.widget.Button[1]"
# POST_DOTS_SUB_MENU_DELETE_POST = "//androidx.recyclerview.widget.RecyclerView/android.widget.Button[2]"
# POST_DOTS_SUB_MENU_FLAG_CONTENT_ITEMS = "com.socialsuperstore:id/actionText"
# POST_FLAG_CONTENT_SUCCESS_WIN_TITLE = "com.socialsuperstore:id/title"
# POST_FLAG_CONTENT_SUCCESS_WIN_DONE_BTN = "com.socialsuperstore:id/doneButton"
# POST_SUB_MENU_ACTION_ITEMS_ID = "com.socialsuperstore:id/actionText"
# POST_MEDIA_LAYOUT = "com.socialsuperstore:id/postProductsMediaLayout"
# READ_ALL_PRODUCT_LINEAR_LAYOUTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout"
# READ_SINGLE_PRODUCT_LINEAR_LAYOUTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout"
# PRODUCT_EDIT_FIRST_CHECKBOX = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.CheckBox"
# POST_USERNAME = "com.socialsuperstore:id/postUserName"







#QUESTION_TEXT_STEP_ONE = "com.socialsuperstore.feature_post_editor:id/questionTextInputEditText"
# QUESTION_TEXT_MEDIA_TAB = "com.socialsuperstore.feature_post_editor:id/questionText"

# QUESTION_UPLOAD_FROM_LIBRARY = "com.socialsuperstore.feature_post_editor:id/fromGallery"
# QUESTION_UPLOAD_FROM_CAMERA = "com.socialsuperstore.feature_post_editor:id/fromCamera"

# QUESTION_REPLY_LABEL = "com.socialsuperstore:id/postQuestionReplyPanel"


# BACKGROUND_STYLE_AND_SIZE_TAB = "Style & size"
# TEXT_SIZE_BAR = "com.socialsuperstore.feature_post_editor:id/textSizeSeekBar"
# BACKGROUND_CROP_BTN = "com.socialsuperstore.feature_post_editor:id/cropBtn"
# BACKGROUND_DELETE_BTN = "com.socialsuperstore.feature_post_editor:id/deleteBtn"
# ALL_TEXT_COLOURS = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout" #"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout"
# LIKES_IN_POST = "com.socialsuperstore:id/interactionsLikes"
# COMMENTS_IN_POST = "com.socialsuperstore:id/interactionsComments"
# GO_TO_COMMENTS_BTN = "com.socialsuperstore:id/interactionsCommentBtn"
# COMMENTS_INPUT_TEXT_FIELD = "com.socialsuperstore.feature_comments:id/commentEditText"
# COMMENTS_SEND_BTN = "com.socialsuperstore.feature_comments:id/sendCommentButton"
# COMMENT_TEXT_ID = "com.socialsuperstore.feature_comments:id/commentTextView"
# NO_COMMENTS_STUB = "com.socialsuperstore.feature_comments:id/noContentText"

# # Try to adding a product first (modal in question comments)
# MODAL_TITLE_TEXT = "com.socialsuperstore:id/titleTopText"
# CLOSE_MODAL_BTN = "com.socialsuperstore:id/closeButton"
# LET_ME_ADD_PRODUCT_FIRST_BTN = "com.socialsuperstore:id/negativeButton"
# CONTINUE_WITHOUT_PRODUCT_BTN = "com.socialsuperstore:id/positiveButton"



# # home feed carousel
# FEED_SLIDE_UPPERLINE = "//*[contains(@resource-id, 'slideSuperscript')]"
# FEED_SLIDE_HEADLINE = "//*[contains(@resource-id, 'slideHeadline')]"

