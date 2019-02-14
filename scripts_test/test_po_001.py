import sys, os

# 导入其他文件夹文件夹类
sys.path.append(os.getcwd())
from Base.Base import Base
from selenium.webdriver.common.by import By
from appium import webdriver


class Test_A:
    def setup(self):
        # 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "9"
        desired_caps["deviceName"] = '192.168.56.101:5555'  # "huawei"
        # app信息
        desired_caps["appPackage"] = "com.android.settings"
        desired_caps["appActivity"] = ".Settings"

        # 中文输入允许
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # 声明手机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.objbase = Base(self.driver)

    def test_001(self):
        s_b = (By.XPATH, "//*[contains(@text,'Network')]")
        self.objbase.find_element(s_b)
        s_r = (By.ID, "com.android.settings:id/search_action_bar")
        s_t = (By.ID, "android:id/search_src_text",)

        self.objbase.click_element(s_r)
        self.objbase.input_element(s_t, "123")

    def teardown(self):
        self.driver.quit()
