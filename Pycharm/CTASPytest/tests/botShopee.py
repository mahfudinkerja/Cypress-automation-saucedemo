import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
	options = webdriver.ChromeOptions()
	options.add_experimental_option( "detach", True )
	options.add_experimental_option( "excludeSwitches", [ "enable-logging" ] )
	driver = webdriver.Chrome( options = options )
	driver.implicitly_wait( 30 )
	driver.maximize_window()
	yield driver


# driver.quit()


def test_login( driver ):
	driver.get( "https://shopee.co.id/buyer/login/qr" )
	time.sleep( 10 )
	driver.get( "https://id.shp.ee/YitRxWb" )
