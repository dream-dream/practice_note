# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵.
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
# 这里是最优化的解决方案   
# 这里我们可以直接把上面给出的X或者Y里面的内容给替换掉，这样就不必申请新的空间，
# 在资源上更加节约，
for i in range(3):
    for j in range(3):
        X[i][j] = X[i][j] + Y[i][j]  # 这样就可以直接替换掉原来的X矩阵了
# '''
print('[', end='')  # 这里可以在print里面直接加上所要打印的参数即可，用逗号分割，第一行直接打印中括号，把空格去掉即可跟下面一行紧挨着
for i in X[0:-1]:  # 循环可以用切片也可以用range（len（li）-1），只循环出前两行
    print(i, ',', sep='')
print(X[-1], ']', sep='', end="")  # 这里打印列表的最后一行，把多余的空格和换行都去掉，然后把中括号加上即可
# '''

# 如下是个人思路
# fir_0 = X[0][0] + Y[0][0]
# fir_1 = X[0][1] + Y[0][1]
# print(fir_0, fir_1)

li = []
for i in range(3):
    l = []
    for j in range(3):
        obj = X[i][j] + Y[i][j]
        l.append(obj)
    li.append(l)
# a = 0
# for i in X:
#     if a == 0:
#         print("[" + str(i) + ",")
#     elif a == 1:
#         print(str(i) + ",")
#     else:
#         print(str(i) + "]")
#     a += 1





