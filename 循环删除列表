#  给一个列表A，再给一个列表B，B中是A的索引，在循环中删除B
def del_index(l, index_l):
    a = 0
    for j in index_l:
        del l[j - a]
        a += 1
    return l


l1 = [1, 2, 3, 4, 5]
l2 = [0, 2, 3]
obj = del_index(l1, l2)
print(obj)
'''
[2, 5]
'''
