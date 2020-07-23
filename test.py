from login import Logintest
from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "zb"
caps["appPackage"] = "qqw.app.smpos13"
caps["appActivity"] = "name='qqw.app.smpos.login.SplashActivity"
caps["noReset"] = "true"
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
Logintest().login(driver)
