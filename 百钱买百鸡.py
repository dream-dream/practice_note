"""
编写程序解决“百钱买百鸡”问题。公鸡五钱一只，母鸡三钱一只，小鸡一钱三只，现有百钱欲买百鸡，共有多少种买法？
"""
# 分析边界


def get_sum_of_kinds_to_buy(arg):
    """
    用循环遍历的方式，时间复杂度是O（n**2）
    :param arg: 总钱数
    :return: 多少种买法
    """
    sum_kinds = 0
    for i in range(1, arg + 1):
        for j in range(1, arg + 1):
            q = 100 - i - j
            if i * 5 + j * 3 + q / 3 == 100:
                print("可以买{}只公鸡和{}只母鸡还有{}只小鸡".format(i, j, q))
                sum_kinds += 1
                i += 1
                j += 1
    return "一共有{}种买法".format(sum_kinds)


ret = get_sum_of_kinds_to_buy(100)
print(ret)
# 可以买4只公鸡和18只母鸡还有78只小鸡
# 可以买8只公鸡和11只母鸡还有81只小鸡
# 可以买12只公鸡和4只母鸡还有84只小鸡
# 一共有3种买法
