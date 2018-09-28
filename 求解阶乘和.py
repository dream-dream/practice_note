# 求1!+2!+3!+...+10!的和。（n!=1*2*3*...*n）
def fun(arg):
    obj = 1
    for i in range(1, arg+1):
        obj *= i
    return obj


emp = 0
for i in range(1, 11):
    ret = fun(i)
    emp += ret
print(emp)
# 这个题做的是最快的，目前为止，就用了不到十分钟就写出来了，我再看看怎么升级一下，先把这些放上来
