from appium import webdriver
import time, base64
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

# 启动参数
desired_caps = {}
# 设备信息
desired_caps["platformName"] = "Android"
# desired_caps["platformVersion"] = "6.0.1"
desired_caps["deviceName"] = "192.168.56.101:5555"
# # app信息
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"


def wait_element(xpa):
    return WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_xpath(xpa))

# 声明手机驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)

start_ele = wait_element("//*[contains(@text,'Sound')]")
end_ele = wait_element("//*[contains(@text,'Network')]")

driver.scroll(start_ele, end_ele)

time.sleep(3)
wait_element("//*[contains(@text,'Security')]").click()

wait_element("//*[contains(@text,'Screen')]").click()

wait_element("//*[contains(@text,'Pattern')]").click()

TouchAction(driver).press(x=342, y=1085).move_to(x=723, y=1085) \
    .move_to(x=723, y=1470).move_to(x=723, y=1846).release().perform()
