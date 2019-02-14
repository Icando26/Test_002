from appium import webdriver

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
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# driver.close_app()


# driver.start_activity("com.android.contacts",".activities.PeopleActivity")

#import base64

#data = base64.b64encode("ss12345678".encode('utf-8'))
#driver.push_file("/sdcard/push.txt", str(data))

#phone_data = driver.pull_file("/sdcard/push.txt")

#ss = base64.b64decode(phone_data)
print(driver.page_source)

driver.quit()
# adb shell dumpsys window windows | grep -E "mCurrentFocus | mFocusedApp" | egrep "ActivityRecord.*" | cut -d " " -f7 | cut -d "/" -f1
# 获取当前页 adb shell dumpsys window windows |grep mFocusedApp
