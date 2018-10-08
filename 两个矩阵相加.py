# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵.
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# 思路
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
print(li)


