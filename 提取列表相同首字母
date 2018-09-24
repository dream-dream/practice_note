#  把列表中相同首字母提取出来存入一个单独列表中，最后返回修改过的列表
def get_list(l):
    l0 = []
    dic = {}
    for i in l:
        if not dic.get(i[0]):
            global l1
            l1 = []
            dic[i[0]] = l1
        l1.append(i)
    for value in dic.values():
        l0.append(value)
    return l0


ll = ['a1', 'b1', 'b1', 'c22', 'c31', 'd43']
obj = get_list(ll)
print(obj)
'''
[['a1'], ['b1', 'b1'], ['c22', 'c31'], ['d43']]
'''
