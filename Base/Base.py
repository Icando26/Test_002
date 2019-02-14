from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll=0.5):
        """
        :param loc:
        :param loc_value:
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll). \
            until(lambda x: x.find_element(*loc))  # *元组，解包

    def click_element(self, loc):
        """
        :param loc:
        :param loc_value:
        :return:
        """
        self.find_element(loc).click()

    def input_element(self, loc, text):
        """
       :param loc ：元祖类型 (By.XPATH,"xpath语句") (By.ID,"id属性值")
       :param text: 输入内容
       :return:
       """
        ele = self.find_element(loc)
        ele.clear()
        ele.send_keys(text)

    def wait_ele(self, loc):
        """
        :param loc:
        :param path:
        :return:
        """
        return WebDriverWait(self.driver, 5, 0.5). \
            until(lambda x: x.find_element(*loc))

# if __name__ == '__main__':
#     wait_ele(By.XPATH, "//*[contains(@text,'Network')]").click()
