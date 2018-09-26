#  有1，2，3，4四位数，能组成多少个不重复且互不相同的三位数，分别是多少，写函数求出来。进阶版，如果是0，1，2，3呢？
#  不重复是指：各个数位的数字各不相同如123、132、321这样
'''
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
'''

#  进阶版
for i in range(5):
    a = 0
    a += i*100
    for j in range(5):
        b = 0
        b += j*10
        for q in range(5):
            c = 0
            c += q
            d = a + b + c
            if d // 100:
                print(d)
