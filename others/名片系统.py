# TODO pass作为是占位符
"""
名片系统
"""
card_list = []


# del show_menu():
def new_card():
    """新增名片"""
    print("_" * 50)
    print("新增名片")
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话： ")
    qq_str = input("请输入QQ： ")
    email_str = input("请输入邮箱： ")
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    card_list.append(card_dict)
    print(card_list)
    print("添加  %s 名片成功" % name_str)
    print("_" * 50)


def show_all():
    """end= 后面表示分隔符"""
    print("-" * 50)
    print("显示所有名片")
    for tab_title in ["姓名", "电话", "QQ", "邮箱"]:
        print(tab_title, end="\t\t")
    print("")
    print("=" * 50)

    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                        card["phone"],
                                        card["qq"], card["email"]))
    print("")
    print("-" * 50)


def search_card():
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入查询的姓名： ")
    for card in card_list:
        if card["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                            card["phone"],
                                            card["qq"], card["email"]))

            break

    else:
        print("抱歉没有找到%s！" % find_name)

    print("")
    print("-" * 50)


def input_card(dict_value, tip_message):
    """
    :param dict_value:
    :param tip_message:
    :return:
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value


flag = True

while (flag):
    action_str = input("请输入的数字：")
    print("请你选择的操作[%s]" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            new_card()
        elif action_str == "2":
            search_card()
        else:
            show_all()
    elif action_str == "0":
        flag = False
        print("退出系统")
    else:
        print("你输入的不对")
