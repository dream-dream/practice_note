# 输入年份，得到返回值true/false，判断是否是闰年
'''
# 这里是用字符串转换，效率太低
def get_bissextile(arg):
    str_obj = str(arg)

    if str_obj.isdigit():
        if str_obj[-2:] == '00':
            ret = arg % 400
            return False if ret else True
        x = arg % 4
        return False if x else True
    raise TypeError
'''


# """
# 要换成数字去操作提升效率, 带上逻辑运算符
def get_bissextile(arg):
    if str(arg).isdigit():
        return (arg % 100 == 0) and (arg % 400 == 0) or (arg % 4 == 0) and (arg % 100 != 0)
    raise TypeError


# """


# 脚本入口文件
if __name__ == '__main__':
    while True:
        a = input('>>:')
        if a.upper() == 'Q':
            break
        elif a.isdigit():
            b = get_bissextile(int(a))
            print(b)
