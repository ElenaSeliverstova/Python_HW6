# 2- Найти сумму чисел списка стоящих на нечетной позиции

def sum_odd_index(list_of_num : list):
    sum_of_num = 0
    for i in list(filter(lambda a : list_of_num.index(a)%2 != 0  , list_of_num)):
        sum_of_num += i
    return sum_of_num

list_of_num = [1,2,3,4,5,6,7,8,9]
print(f"sum of nums with odd index in {list_of_num} => {sum_odd_index(list_of_num)} ")

# Вариант 2

from functools import reduce
def sum_list(n):
    nums = list(range(1, n+1))
    return reduce(lambda a, b: a+b, nums[1::2])
print(sum_list(9))