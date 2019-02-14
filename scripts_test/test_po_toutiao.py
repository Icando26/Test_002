import sys, os, pytest


sys.path.append(os.getcwd())
# 导入其他文件夹文件夹类
from Page.dev_title import Dev_Title
from appium import webdriver


class Test_TouTiao:
    def setup_class(self):
        # 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "8"
        desired_caps["deviceName"] = 'huawei'  # "huawei",这个使用的
        # app信息
        desired_caps["appPackage"] = "io.manong.developerdaily"
        desired_caps["appActivity"] = "io.toutiao.android.ui.activity.LaunchActivity"

        # 中文输入允许
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # 声明手机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.obj = Dev_Title(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("email,pwd", [("3131135536@qq.com", "zyl93792612")])
    def test_add_article(self, email, pwd):
        self.obj.click_add()
        self.obj.change_login()
        self.obj.login(email, pwd)
