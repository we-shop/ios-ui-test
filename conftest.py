import pytest
import os
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage
from ui_page_objects.product_detail_page_object import ProductDetailPage
from ui_page_objects.profile_page_object import ProfilePage
from ui_page_objects.post_page_object import PostPage
from ui_page_objects.inbox_page_object import InboxPage
from ui_page_objects.web_page_object import WebPage
from ui_page_objects.dashboard_page_object import DashboardPage

from appium import webdriver
from ui_page_objects.functions import *
import json

from dotenv import load_dotenv

# needed for pytest-html report configuration
from py.xml import html


load_dotenv()

# Read from file function
def get_data(data):
  return data.split("#")[0]

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
LOGIN_NEW = os.getenv("LOGIN_NEW")
PASSWORD_NEW = os.getenv("PASSWORD_NEW")
LOGIN_INT = os.getenv("LOGIN_INT")
PASSWORD_INT = os.getenv("PASSWORD_INT")
LOGIN_INT_NEW = os.getenv("LOGIN_INT_NEW")
PASSWORD_INT_NEW = os.getenv("PASSWORD_INT_NEW")

# BS CREDENTIALS
BS_LOGIN = os.getenv("BS_LOGIN")
BS_SECRET = os.getenv("BS_SECRET")

prefs = {"download.default_directory": os.getcwd() + "/"}

#caps for Browserstack
# "device" : "Samsung Galaxy S21",
# "os_version" : "11.0"

# {"app_url":"bs://576463a96efb0a64e20d5abe7652b5faa671aba4"}

# /* In your test script, use this "app_url" value to specify the application under test using the "app" capability. During test execution, your app will automatically be installed and launched on the device being tested. */

# caps.setCapability("app", "bs://576463a96efb0a64e20d5abe7652b5faa671aba4")


DROID_desired_cap = {
  "device" : "Samsung Galaxy A51",
  "os_version" : "10.0",
  "project" : "First Python project2", 
  "build" : "browserstack-build-13",
  "name" : "first_test222",
  "appPackage": "com.socialsuperstore",
  "appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",  
  "app_url":"bs://5f5ba99b31e378e943039767abeb7ca35a3d99eb",
  "browser" : "Chrome",
  "browserstack.idleTimeout":10,
  "implicit":8000,
  "autoGrantPermissions": True,
  "unicodeKeyboard": True,
  "noReset:": True,
  "resetKeyboard": True }


# desired_cap = {
#   "appium:platformName": "iOS",
#   "appium:platformVersion": "15.3.1",
#   "appium:deviceName": "iPhone 7",
#   "appium:automationName": "UiAutomator",
#   "app_url":"bs://c9233654e295b4b1aadd17f2a1640a043b462d38"
#   #"appium:app": "C:\\Users\\NEMESIS\\Desktop\\UPW\\weshop\\WeShop.ipa"
# }

desired_cap_ios_COMMENTED = {
  "device" : "iPhone 11",
  "os_version" : "15",
  "project" : "First Python project", 
  "build" : "browserstack-iOS",
  "name" : "iOS_tests",
  "app_url":"bs://656f53461ce084463369c3455b47bb2165d6fc9a"
  # 64cdb538ee26c9d62010a7aa4175c8d33cc5ce69
  #"appium:app": "C:\\Users\\NEMESIS\\Desktop\\UPW\\weshop\\WeShop.ipa"
}

# desired_cap = {
#   "device" : "iPhone 13",
#   "os_version" : "15",
#   "project" : "First Python project", 
#   "build" : "browserstack-iOS",
#   "name" : "iOS_tests",
#   "app_url":"bs://c9233654e295b4b1aadd17f2a1640a043b462d38"
#   #"appium:app": "C:\\Users\\NEMESIS\\Desktop\\UPW\\weshop\\WeShop.ipa"
# }


# desired_cap = {
#     # Set your access credentials
#     "browserstack.user" : "mikevo_e4SQsH",
#     "browserstack.key" : "vAxMnKJJiYcxmsekXNuZ",
  
#     # Set URL of the application under test
#     #"app" : "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
  
#     # Specify device and os_version for testing
#     "device" : "iPhone 7",
#     "os_version" : "10",
      
#     # Set other BrowserStack capabilities
#     "project" : "First Python project", 
#     "build" : "browserstack-build-1",
#     "name" : "first_test"
# }

# fetching capabilities
#json_f = open(os.getcwd() + '/ios_caps.json') # travic CI
json_f = open(os.getcwd() + "/ios_caps.json")
#json_f = open('ios_caps.json') # local
desired_cap = json.load(json_f)
json_f.close()


# BS sessuib data list
SESSION_URLS = []
SESSION_URLS_PUBLIC = []

# Customizing appium driver for Browserstack
@pytest.fixture(autouse=True)
def selenium(request):
    #webdriver
    selenium = webdriver.Remote(
      command_executor=f'https://{BS_LOGIN}:{BS_SECRET}@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)


    get_session_data = selenium.execute_script('browserstack_executor: {"action": "getSessionDetails"}')
    converted_session_data = json.loads(get_session_data)

    
    BS_SESSION_URL = f"https://app-automate.browserstack.com/dashboard/v2/builds/{converted_session_data['build_hashed_id']}/sessions/{converted_session_data['hashed_id']}"
    SESSION_URLS.append(BS_SESSION_URL)
    BS_PUBLIC_SESSION_URL = converted_session_data["public_url"]
    SESSION_URLS_PUBLIC.append(BS_PUBLIC_SESSION_URL)

    yield selenium

    if request.node.rep_call.outcome == "passed":
        test_status = 'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"<tr>", "reason": "<trs>"}}'.replace("<tr>", "passed").replace("<trs>", f"All good! Test {request.node.rep_call.head_line} passed!")
    elif request.node.rep_call.outcome == "failed":
        test_status = 'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"<tr>", "reason": "<trs>"}}'.replace("<tr>", "failed").replace("<trs>", f"Test {request.node.rep_call.head_line} failed! Need to check!")
    else:
        print(f"Something wrong! Check test status {ERROR}") # may be skipped issue
    

    # mark test as passed/failed
    selenium.execute_script(test_status)

    selenium.quit() # marking test is finished for Browserstack
    #selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
    clear_data_from_temp_file() # clearing data in temp_data.txt

# #Customizing appium driver (implicitly waits + app close/kill)
# @pytest.fixture
# def selenium(selenium):
#     #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)
#     selenium.implicitly_wait(7)
#     yield selenium
#     #selenium.remove_app(app_id='com.socialsuperstore') # uninstalling app
#     #selenium.terminate_app('com.socialsuperstore') # put app in background
#     selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
#     clear_data_from_temp_file() # clearing data in temp_data.txt


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # extend pytest html plugin
    pytest_html = item.config.pluginmanager.getplugin('html')


    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + report.when, report)    

    extra = getattr(report, 'extra', [])

    #_html = f'<div><a href="{SESSION_URLS[-1]}">{SESSION_URLS[-1]}</a></div>'
    _html = f'<div><p>BS REPORT public URL: <a href="{SESSION_URLS_PUBLIC[-1]}">{SESSION_URLS_PUBLIC[-1]}</a></p><div><p>BS peport private URL: <a href="{SESSION_URLS[-1]}">{SESSION_URLS[-1]}</a></p>'
        
        
    if report.when == 'teardown':
        extra.append(pytest_html.extras.html(_html))
        

#FIXTURES PAGE OBJECT
@pytest.fixture()
def login_model(request):
  fixture = LoginPage(LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW)
  return fixture

@pytest.fixture()
def debug_model(request):
  fixture = DebugPage()
  return fixture

@pytest.fixture()
def search_model(request):
  fixture = SearchPage()
  return fixture

@pytest.fixture()
def product_page_model(request):
  fixture = ProductDetailPage()
  return fixture

@pytest.fixture()
def profile_model(request):
  fixture = ProfilePage(LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW)
  return fixture

@pytest.fixture()
def post_model(request):
  fixture = PostPage()
  return fixture

@pytest.fixture()
def inbox_model(request):
  fixture = InboxPage()
  return fixture

@pytest.fixture()
def dashboard_model(request):
  fixture = DashboardPage(LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW)
  return fixture

@pytest.fixture()
def web_model(request):
  fixture = WebPage(LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW)
  return fixture