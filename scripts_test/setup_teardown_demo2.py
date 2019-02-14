import pytest

# 函数级别setup()／teardown() 运行一次测试函数会运行一次setup和teardown

class Test_ST:

    def setup_class(self):
        pass
    def teardown_class(self):
        pass

    def test_a(self):
        print("test_a>>>>>>>>>")
        assert True

    @pytest.mark.run(order=1)
    def test_b(self):
        print("test_b>>>>>>>>")
        assert False

