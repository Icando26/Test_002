import pytest


def re_data_list():
    lis_data = []
    with open("/Users/zyl/Desktop/python/data.txt", "r") as f:
        for i in f.readlines():
            lis_data.append(eval(i.split("=")[-1]));
    print(lis_data)


class Test_XX:
    def test_xx(self):
        print("class Test!!!!!")


re_data_list()
