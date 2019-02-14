from appium import webdriver
def init_driver():
 # 启动参数
 desired_caps = {}
 # 设备信息
 desired_caps["platformName"] = "Android"
 desired_caps["platformVersion"] = "9"
 desired_caps["deviceName"] = '192.168.56.101:5555'#"huawei"
 # app信息
 desired_caps["appPackage"] = "com.android.settings"
 desired_caps["appActivity"] = ".Settings"

 # 声明手机驱动对象
 driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

 return driver