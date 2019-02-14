from Base.Base import Base
import Page


class Dev_Title(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_add(self):
        # 添加文章
        self.click_element(Page.dev_add_title)

    def change_login(self):
        self.click_element(Page.dev_login_email)

    def login(self, email, pwd):
        self.input_element(Page.dev_input_email, email)
        self.input_element(Page.dev_input_pwd, pwd)
        self.click_element(Page.dev_login_enter)
