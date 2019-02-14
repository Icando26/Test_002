import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
"""
    只声明一次driver 

    1.测试方法1---进入设置，进入更多判断是否有VPN
    2.测试方法2-—- 进入移动网络，点击首选网络类型，设置为2G，判断当前页是否有2G
"""
class Test_ord:
    def setup_class(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 中文输入允许
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    def teardown_class(self):
        self.driver.quit()
    @pytest.mark.run(order=1) # 因为先进入更多
    def test_vpn(self):
        # 点击更多
        G_D = WebDriverWait(self.driver,5,1)\
            .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'更多')]"))
        G_D.click()
        # 定位所有id=android:id/title元素
        text_list = self.driver.find_elements_by_id("android:id/title")
        text_value = []
        for i in text_list:
            text_value.append(i.text)
        assert "VPN" in text_value,"他不在"

    @pytest.mark.run(order=2) # 在更多页面点击移动网络
    def test_2G(self):
        # 点击移动网络
        Y_D = WebDriverWait(self.driver,5,1)\
            .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'移动网络')]"))
        Y_D.click()
        # 定位首选网络
        S_X_W_L =  WebDriverWait(self.driver,5,1)\
            .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'首选网络')]"))
        S_X_W_L.click()
        # 点击2G
        G_2 = WebDriverWait(self.driver,5,1)\
            .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'2G')]"))
        G_2.click()
        # 获取text文本
        text_lis = self.driver.find_elements_by_id("android:id/summary")
        text_lis_value = []
        for i in text_lis:
            text_lis_value.append(i.text)

        assert "2G" in text_lis_value

