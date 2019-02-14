import pytest

# @pytest.fixture(scope="class", autouse=True)  # 用于初始化一些数据
@pytest.fixture(scope="function", autouse=True)
def init_xx():
    print("初始化设置")
    return [1, 3, 2]


class Test_XX:
    def test_xx(self,init_xx):
        print("class Test!!!!!")
        assert init_xx == "4"
