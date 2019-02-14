from Base.Base import Base
from selenium.webdriver.common.by import By


class Send_Msg:

    def __init__(self, driver):
        self.objbase = Base(driver);
        self.add_sms = (By.ID, "com.android.messaging:id/start_new_conversation_button")
        self.sms_accept = (By.XPATH, "//*[contains(@text,'To')]")
        self.add_accept = (By.XPATH, "//*[contains(@text,'ALL')]")
        self.write_msg = (By.CLASS_NAME, "android.widget.EditText")

    def add_click_button(self):
        self.objbase.click_element(self.add_sms)

    def add_sms_contact(self, phone):
        self.objbase.input_element(self.sms_accept, phone)
        self.objbase.click_element(self.add_accept)

    def sms_write_msg(self, msg):
        self.objbase.input_element(self.write_msg, msg)
