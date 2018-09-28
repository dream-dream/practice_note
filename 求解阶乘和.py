# 求1!+2!+3!+...+10!的和。（n!=1*2*3*...*n）
def factorail_func(arg):
    obj = 1
    for i in range(1, arg+1):
        obj *= i
    return obj


emp = 0
for i in range(1, 11):
    ret = factorail_func(i)
    emp += ret
print(emp)
这个题做的是最快的，目前为止，就用了不到十分钟就写出来了，我再看看怎么升级一下，先把这些放上来


# 这里是简洁版
def factorail_func(arg):
    emp_obj = 0
    for i in range(1, arg + 1):
        fir_obj = 1
        for j in range(1, i + 1):
            fir_obj *= j
        emp_obj += fir_obj
    return emp_obj


ret = factorail_func(10)
print(ret)  # 4037913
