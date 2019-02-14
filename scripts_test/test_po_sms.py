import sys, os

# 导入其他文件夹文件夹类
import pytest

sys.path.append(os.getcwd())
from Page.sms import Send_Msg
from appium import webdriver


class Test_A:

    def setup_class(self):
        # 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "9"
        desired_caps["deviceName"] = '192.168.56.101:5555'  # "huawei"
        # app信息
        desired_caps["appPackage"] = "com.android.messaging"
        desired_caps["appActivity"] = ".ui.conversationlist.ConversationListActivity"

        # 中文输入允许
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # 声明手机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.objbase = Send_Msg(self.driver)

    @pytest.mark.run(order=1)
    def test_input_phone(self):
        self.objbase.add_click_button()
        self.objbase.add_sms_contact("123456780987")

    # @pytest.mark.parametrize("text", "123")
    @pytest.fixture(params=['1234'])
    def test_send_msg(self, request):
        self.objbase.sms_write_msg(request.param)

    def teardown_class(self):
        self.driver.quit()
