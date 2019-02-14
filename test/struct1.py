from selenium.webdriver.support.wait import WebDriverWait

from scripts_test.Init_Driver import init_driver
import os
import base64


def push(tag, pc_path, phone_path, driver=None):
    # tag 1:adb 2:appium
    if tag == 1:
        os.system("adb push %s %s" % (pc_path, phone_path))
    if tag == 2:
        with open(pc_path, 'r')as f:
            data = base64.b64encode(f.read().encode('utf-8'))
            driver.push_file("/sdcard/push.txt", str(data))


def install_apk(tag, path):
    pass


def findById(driver=None):
    try:
        pass
        # driver.find
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == '__main__':
    driver = init_driver()
    try:
        # driver.find_element_by_id("com.android.settings:id/search_action_bar_title").click()
        # time.sleep(2)
        # driver.find_element_by_class_name("com.android.settings:id/search_action_bar_title").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//*[contains(@text,'示')]*").click()
        ele = driver.find_elements_by_id("android:id/title")
        for i in ele:
            print(i.text)
        #显示等待方式
        WebDriverWait(driver,timeout=5,poll_frequency=0.5)\
            .until(lambda x:x.find_elements_by_id("xx"))
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    # push(tag=1,pc_path="./hello.txt",phone_path="/sdcard")

print(os.system("adb devices"))
