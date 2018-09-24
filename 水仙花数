# 写函数：输入一个三位数，该数字每一位数的立方值相加等于该数本身，返回这样的数
'''
# 字符串转换效率太低
def daffodil_num(arg):
    str_obj = str(arg)
    if str_obj.isdigit():
        zero = 0
        for i in range(3):
            num_obj = int(str_obj[i])
            num_obj = num_obj ** 3
            zero += num_obj
        if int(arg) == zero and len(str_obj) > 2:  # 这里只有if判断，没有else，所以不满足条件就会接着走下面的程序代码，
            return arg
    else:  # 所以这里要对应上面的isdigit判断加上else，否则就会从上面的if判断直接执行这里的触发异常
        raise TypeError
'''


# """
# 要换成数字操作，固定的三位数，如何取到个十百三个数字，用取余，对100取余得到商百位数字，余数紧接着对10取余，得到商是十位数，余数是个位数
def daffodil_num(arg):
    str_obj = str(arg)
    if str_obj.isdigit():
        h_num, ret_num = divmod(arg, 100)
        decode_num, unit_num = divmod(ret_num, 10)
        num_obj = h_num ** 3 + decode_num ** 3 + unit_num ** 3
        if num_obj == arg:
            return arg
    else:
        raise TypeError


# """

# for i in range(1000):
#     if len(str(i)) > 2:
#         obj = daffodil_num(i)
#         if obj is not None and len(str(obj)) > 2:
#             print(obj)  # 153 370 371 407
if __name__ == '__main__':
    while True:
        obj = input(">>:")
        if obj.isdigit():
            ret = daffodil_num(int(obj))
            print(ret)
        elif obj.upper() == 'Q':
            break
