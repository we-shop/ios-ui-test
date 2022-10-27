import pytest
import os
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage
from ui_page_objects.product_detail_page_object import ProductDetailPage
from ui_page_objects.profile_page_object import ProfilePage
from ui_page_objects.post_page_object import PostPage
from ui_page_objects.inbox_page_object import InboxPage
from ui_page_objects.dashboard_page_object import DashboardPage
from appium import webdriver
from ui_page_objects.functions import *


from dotenv import load_dotenv

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


prefs = {"download.default_directory": os.getcwd() + "/"}


#Customizing appium driver (implicitly waits + app close/kill)
@pytest.fixture
def selenium(selenium):
    #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)
    selenium.implicitly_wait(7)
    yield selenium
    #selenium.remove_app(app_id='com.socialsuperstore') # uninstalling app
    #selenium.terminate_app('com.socialsuperstore') # put app in background
    selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
    clear_data_from_temp_file() # clearing data in temp_data.txt


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
