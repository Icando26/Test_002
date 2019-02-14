import pytest


@pytest.fixture()  # 用于初始化一些数据
def init_xx():
    print("初始化设置")
    with open("./data.txt", "w") as  f:
        f.write("1")


@pytest.mark.usefixtures("init_xx")  # 作用于整个类，一次
class Test_XX:
    def test_xx(self):
        print("class Test!!!!!")
        with open("./data.txt", "r") as f:
            readData = f.read()
            print("------" + readData)
        assert readData == "1"
