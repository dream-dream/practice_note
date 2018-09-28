"""
flag 是一种标记思想，一般用来表示状态改变。
"""


# 有一个列表，如果每个对象都是int则返回True，否则返回False
def func(a: list):
    flag = True
    for i in a:
        if type(i) != int:
            flag = False
    return flag


li = [12, 15, 8, 6, '78']
print(func(li))
