"""
有一对兔子，从出生后第 3 个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数
为多少？(不超过100个月)。
有进阶版，如果是从出生后第《4》个月起生一《只》兔子呢？
"""

'''
第一个月是两只小兔子，我们就不考虑近亲结婚生子这样的伦理问题了，他们二🐰需要成长三个月
才能开始繁衍后代，这前两个月都是两只🐰，从第三个月开始他们能生一对🐰就是4只，第四个月是6只，
第五个月是10只，到第六个月是14只，然后从第七个月开始是20只，第八个月是26只，第九个月是34只。。。。。。依次类推去找规律
'''


def get_sum_rabbit(arg):
    for i in range(1, arg + 1):
        two_grow_rabbit = 2
        if i < 3:
            print('第{}个月兔子的总数为---{}'.format(i, 2))
        else:
            div_obj, mod_obj = divmod((i - 2), 2)
            if div_obj < 1:
                pass
            else:
                for j in range(1, div_obj + 1):
                    two_grow_rabbit += (i - j * 2) * 2
            two_grow_rabbit += mod_obj * 2
            print('第%s个月兔子的总数为---%s' % (i, two_grow_rabbit))
    return


get_sum_rabbit(100)


"""
兔子问题进阶版，如果是从第4个月开始生小兔子，然后每个月只生1只兔子呢，不考虑雌雄问题，
假设雌雄是绝对均等，问每个月兔子总数分别是多少
"""


def get_sum_rabbit(arg):
    first_born_rabbit = 2
    second_born_rabbit = 0
    third_born_rabbit = 0
    grown_up_rabbit = 0
    for i in range(1, arg + 1):
        if i == 1:
            pass
        elif i == 2:
            second_born_rabbit = first_born_rabbit
            first_born_rabbit = 0
        elif i == 3:
            third_born_rabbit = second_born_rabbit
            second_born_rabbit = 0
        elif i == 4:
            grown_up_rabbit = third_born_rabbit
            third_born_rabbit = 0
            first_born_rabbit = grown_up_rabbit // 2
        elif i == 5:
            second_born_rabbit = first_born_rabbit
            first_born_rabbit = grown_up_rabbit // 2
        elif i == 6:
            second_born_rabbit = first_born_rabbit
            third_born_rabbit = second_born_rabbit
            first_born_rabbit = grown_up_rabbit // 2
        else:
            second_born = second_born_rabbit
            third_born = third_born_rabbit
            second_born_rabbit = first_born_rabbit
            third_born_rabbit = second_born
            grown_up_rabbit += third_born
            first_born_rabbit = grown_up_rabbit // 2
        last_sum_rabbit = grown_up_rabbit + third_born_rabbit + second_born_rabbit + first_born_rabbit
        print('第%s个月兔子的总数为---%s只' % (i, last_sum_rabbit))


get_sum_rabbit(100)

