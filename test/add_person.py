from appium import webdriver
import time,base64
# server 启动参数
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

# 启动参数
desired_caps = {}
# 设备信息
desired_caps["platformName"] = "Android"
# desired_caps["platformVersion"] = "6.0.1"
desired_caps["deviceName"] = "192.168.56.101:5555"
# # app信息
desired_caps["appPackage"] = "com.amaze.filemanager"
desired_caps["appActivity"] = ".activities.MainActivity"

# 声明手机驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
# driver.find_element_by_id("com.android.contacts:id/fab").click()
#start_ele = driver.find_element_by_xpath("//*[contains(@text,'Sound')]")
#end_ele = driver.find_element_by_xpath("//*[contains(@text,'Network')]")

# driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
# time.sleep(10)

# driver.scroll(end_ele,start_ele)
#driver.drag_and_drop(start_ele, end_ele)
# driver.swipe(305,2198,305,1024,5000)

#API
# print(driver.device_time)
#
# print(driver.get_window_size())
#
# for i in range(3):
#     driver.keyevent(25)

#driver.open_notifications()

#driver.find_element_by_id("com.android.systemui:id/qs_drag_handle_view").click()
ele = driver.find_element_by_xpath("//*[contains(@text,'Alarms')]")
TouchAction(driver).long_press(el=ele,duration=2000).perform()

#TouchAction(driver).press(x=1000,y=1000).wait(100).move_to(x=600,y=0).release().perform()
#driver.keyevent(3)
time.sleep(5)
driver.quit()
