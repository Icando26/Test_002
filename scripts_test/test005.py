import pytest


class Test_aa:

    @pytest.fixture()
    def data(self):
        return 1

    @pytest.fixture(params=[1, 2, 3])
    def data_1(self, request):
        return request.param

    def test_1(self, data):
        print("传参数形式----初始化1")
        assert data == 1

    @pytest.mark.usefixtures("data")
    def test_2(self):
        print("传参数形式----初始化2")
        assert True

    def test_3(self, data_1):
        print("传多值参数形式----初始化1")
        assert data_1 == 1

    # 多类型，多值传入
    @pytest.mark.parametrize("a,b,c", [(1, 2, 3), (4, 5, 6)])
    def test_4(self, a, b, c):
        assert a + b + c == 6
