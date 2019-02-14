import allure
import pytest


class Test_ABC:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="步骤描述")
    def test_1(self):
        allure.attach("这是一个描述", "说一下")
        assert False

# if __name__ == '__main__':
#     pytest
