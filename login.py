# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


# caps = {}
# caps["platformName"] = "Android"
# caps["deviceName"] = "zb"
# caps["appPackage"] = "qqw.app.smpos13"
# caps["appActivity"] = "name='qqw.app.smpos.login.SplashActivity"
# caps["noReset"] = "true"
# caps["unicodeKeyboard"] = True
# caps["resetKeyboard"] = True


class Logintest():
    def login(self, driver):
        """打开应用程序"""
        driver.find_element_by_accessibility_id("数智POS3").click()
        """跳过等待"""
        driver.find_element_by_id("qqw.app.smpos13:id/txt_count_down").click()
        """查看订单列表"""
        driver.find_element_by_id("qqw.app.smpos13:id/tab_home").click()
        """获取订单编号"""
        order_id = \
            driver.find_element_by_id("qqw.app.smpos13:id/txt_item_order_list_fragment_orderNum").text.split(': ', 1)[1]
        """备货并打印小票"""
        driver.find_element_by_id("qqw.app.smpos13:id/txt_item_order_list_fragment_restore").click()
        """进入代发货界面"""
        driver.find_element_by_id("qqw.app.smpos13:id/rb_order_fragment_delivery").click()
        """搜索订单编号"""
        driver.find_element_by_id("qqw.app.smpos13:id/editText").click()
        driver.find_element_by_id("qqw.app.smpos13:id/edit_search_activity_content").send_keys(order_id)
        driver.press_keycode(66)
        # ActionChains(driver).send_keys(Keys.ENTER).perform()
        print(1111111111111111111111)
        driver.find_element_by_id("qqw.app.smpos13:id/txt_item_order_list_fragment_restore").click()
        driver.find_element_by_id("qqw.app.smpos13:id/txt_popup_order_window_sure").click()
        driver.find_element_by_id("qqw.app.smpos13:id/imageVie1").click()
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[2]").click()
        driver.find_element_by_id("qqw.app.smpos13:id/bt_distribution_layout_commit").click()
        driver.find_element_by_id("qqw.app.smpos13:id/txt_item_order_list_fragment_stockUp").click()
        driver.quit()

# el3 = driver.find_element_by_id("qqw.app.smpos13:id/txt_item_order_list_fragment_restore")
# el3.click()
# el4 = driver.find_element_by_id("qqw.app.smpos13:id/rb_order_fragment_delivery")
# el4.click()
# el5 = driver.find_element_by_id("qqw.app.smpos13:id/editText")
# el5.click()
# el6 = driver.find_element_by_id("qqw.app.smpos13:id/edit_search_activity_content")
# el6.click()
# el6.send_keys("120125708589")

#
