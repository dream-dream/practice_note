"""
for i in range(1, 5):
    a = 0
    a += i * 100
    for j in range(1, 5):
        b = 0
        b += j * 10
        for q in range(1, 5):
            c = 0
            c += q
            d = a + b + c
            print(d)
"""
# 下面这样写和你的写法结果相同，思考一下
# for i in range(1, 5):
#     a = i * 100
#     for j in range(1, 5):
#         b = j * 10
#         for q in range(1, 5):
#             c = q
#             d = a + b + c
#             print(d)
# 通过排列的公式试试实现这道题。
emp = ' '
star = '*'
first = emp * 3 + star + emp * 2
second = (emp + star) * 3 + emp * 2
third = (star + emp) * 4
obj = first + '\n' + second + '\n'
obj_re = obj.join('')
ret = first + '\n' + second + '\n' + third + '\n' + second + '\n' + first
print(ret)
