from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR LOGIN PAGE MODEL
ALREADY_HAVE_ACC_LINK = "com.socialsuperstore:id/signInBtn"
LOG_FIELD = "loginTextField"
PASS_FIELD = "passwordTextField"
SIGN_IN_BTN = '//XCUIElementTypeButton[@name="Sign in"]'
CREATE_ACC_BTN = '//XCUIElementTypeButton[@name="Create an account"]'
MAKE_LOGIN_BTN = "continueButton"
ACCEPT_NOTIFICATION_MODAL_BTN = '//XCUIElementTypeAlert[@name="“WeQA” Would Like to Send You Notifications"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]'
INCORRECT_PASSWORD_MSG = "This account doesn’t exist, try checking your details again."
LOGIN_SCREEN_TITLE = "Earn shares in the world’s first shoppable social network owned by you"



FORGOT_PASS_LINK = '//XCUIElementTypeStaticText[@name="Forgot password"]'
CLOSE_BTN_LOGIN ='//XCUIElementTypeButton[@name="cross"]'
PUSH_NOTIFICATION_TEXT = "//XCUIElementTypeButton[@name='NotificationCell']"
WESHOP_EXPERIENCE_WIN_ALLOW_BTN = "//XCUIElementTypeButton[@name='Allow']"


# STEP BUTTNON NAMES
NEXT_STEP_FIRST_BUTTON_TEXT = "Next step: Your details"
NEXT_STEP_SECOND_BUTTON_TEXT = "Next step: Set a password"
NEXT_STEP_THIRD_BUTTON_TEXT = "Next step: Your birthday"
NEXT_STEP_FOURTH_BUTTON_TEXT = "Next step: Your gender"
NEXT_STEP_FIFTH_BUTTON_TEXT = "Next step: Your username"
NEXT_STEP_SIXTH_BUTTON_TEXT = "Next steps: Your interests"
NEXT_STEP_SEVENTH_BUTTON_TEXT = "Final step: Legal bits"
FINAL_STEP_BUTTON_TEXT = "Start shopping"

# REGISTRATION BLOCK - FIRST STEP
WHO_INVITED_YOU_INPUT = "//XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField"
STEPS_COUNTER = '//XCUIElementTypeOther[2]/XCUIElementTypeStaticText[contains(@name, "")]'
NEXT_STEP_BTN = '//XCUIElementTypeButton[@name="continueButton"]' #"continueButton" # 


# REGISTRATION BLOCK - SECOND STEP
REG_FIRST_NAME_INPUT = "firstNameField"
REG_LAST_NAME_INPUT = "lastNameField"
REG_EMAIL_INPUT = "emailField"

# REGISTRATION BLOCK - THIRD STEP
REG_PASSWORD_INPUT = "passwordField"

# REGISTRATION BLOCK - FOURTH STEP
REG_DATE_DD = "//XCUIElementTypeOther/XCUIElementTypeTextField[1]"
REG_DATE_MM = "//XCUIElementTypeOther/XCUIElementTypeTextField[2]"
REG_DATE_YYYY = "//XCUIElementTypeOther/XCUIElementTypeTextField[3]"
REG_DATE_WHEEL_DD = '//XCUIElementTypeDatePicker[@name="datePicker"]/XCUIElementTypePicker/XCUIElementTypePickerWheel[1]'
REG_DATE_WHEEL_MM = '//XCUIElementTypeDatePicker[@name="datePicker"]/XCUIElementTypePicker/XCUIElementTypePickerWheel[2]'
REG_DATE_WHEEL_YYYY = '//XCUIElementTypeDatePicker[@name="datePicker"]/XCUIElementTypePicker/XCUIElementTypePickerWheel[3]'
REG_DATE_STEP_CANCEL_BTN = "Cancel"
REG_DATE_STEP_DONE_BTN = "Done"

# driver.find_element_by_ios_predicate('wdName == "Buttons"') # ios predicate example - need to debug and investigate

# REGISTRATION BLOCK - FIFTH STEP
REG_MALE_GENDER = '//XCUIElementTypeStaticText[@name="Male"]'
REG_FEMALE_GENDER = '//XCUIElementTypeStaticText[@name="Female"]'
REG_NON_BINARY_GENDER = '//XCUIElementTypeStaticText[@name="Non-Binary"]'
REG_PREFER_NOT_TO_SAY_GENDER = '//XCUIElementTypeStaticText[@name="Prefer not to say"]'
REG_ALL_GENDERS_BTNS = '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton'
REG_ALL_GENDERS_TEXT = '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText'

# REGISTRATION BLOCK - SIXTH STEP
REG_USERNAME_INPUT_FIELD = "usernameField"
REG_FIRST_SUGGESTED_USERNAME = "//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]" # first cell - suggested username
REG_ALL_SUGGESTED_USERNAMES_TEXT = '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[contains(@name, "")]'
REG_ALL_SUGGESTED_USERNAMES_BTNS = '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton'

# REGISTRATION BLOCK - SEVENTH STEP
REG_FIRST_INTEREST_ITEM = '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[contains(@name, "")]'
ALL_INTEREST_ITEMS =  '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[contains(@name, "")]'


# REGISTRATION BLOCK - FINAL STEP
REG_TERMS_AND_COND_RADIO_BTN = 'termsConditionButton'
REG_UPDATES_RADIO_BTN = 'updatesButton'
REG_ACC_HOLDER_AGREEMENT_LINK = '//XCUIElementTypeLink[@name="WeShop Account Holder Agreement"]'
REG_PRIVACT_AND_POLICY_LINK = '//XCUIElementTypeLink[@name="Privacy Policy"]'
REG_TERMS_WEB_PAGE_TITLE = '//XCUIElementTypeStaticText[@name="WESHOP TERMS OF SERVICE"]'
REG_PRIVACY_WEB_PAGE_TITLE = '//XCUIElementTypeStaticText[@name="Privacy Policy"]'
REG_FINAL_STEP_CLOSE_BTN = 'Close'


# AFTER REG LOCATORS
LOGIN_MODAL_SLIDE_NEXT_BTN = '//XCUIElementTypeButton[@name="Next"]'
LOGIN_TEXT_INSIDE_MODAL_SLIDE_WINDOW = '//XCUIElementTypeScrollView/XCUIElementTypeOther/..'
LOGIN_MODAL_SLIDE_START_SHOP_BTN = '//XCUIElementTypeButton[@name="Start shopping"]'


#NEED TO switch to profile and verifi first last name and username











