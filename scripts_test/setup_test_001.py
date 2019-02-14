import pytest, time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# from appium.webdriver.common.touch_action import TouchAction


# 函数级别setup()／teardown() 运行一次测试函数会运行一次setup和teardown

class Test_ST:

    def setup_class(self):  # steup_class默认进入一次
        # print(">>>>>>>>>setup_class")
        # 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "9"
        desired_caps["deviceName"] = "huawei"
        # app信息
        desired_caps["appPackage"] = "com.android.settings"
        desired_caps["appActivity"] = ".Settings"

        # 声明手机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.driver.quit()

    def wait_element(self, xpathx):
        return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element_by_xpath(xpathx))

    @pytest.mark.run(order=1)
    def test_vpn(self):
        print("test!!!!!!!!!")
        self.wait_element("//*[contains(@text,'Network')]").click()
        #
        ele_list = self.driver.find_elements_by_id("android:id/title")
        text_value = []
        for ele in ele_list:
            text_value.append(ele.text)

        assert "Wi‑Fi" in text_value, "他不在"

    @pytest.mark.run(order=2)
    def test_net(self):
        print("************>test_net")
        self.wait_element("//*[contains(@text,'Mobile network')]").click()
        #time(5)

        #
    #
    # def test_001(self):
    # time.sleep(5)
    #
    # start_ele = self.wait_element("//*[contains(@text,'Sound')]")
    # end_ele = self.wait_element("//*[contains(@text,'Network')]")
    #
    # self.driver.scroll(start_ele, end_ele)
    #
    # time.sleep(3)
    # self.wait_element("//*[contains(@text,'Security')]").click()
    #
    # self.wait_element("//*[contains(@text,'Screen')]").click()
    #
    # self.wait_element("//*[contains(@text,'Pattern')]").click()
    #
    # TouchAction(self.driver).press(x=342, y=1085).move_to(x=723, y=1085) \
    #     .move_to(x=723, y=1470).move_to(x=723, y=1846).release().perform()

# def test_a(self):
#     print("test_a>>>>>>>>>")
#     assert True
#
# # @pytest.mark.run(order=1)
# def test_b(self):
#     print("test_b>>>>>>>>")
#     assert False

# if __name__ == '__main__':
#     pytest
