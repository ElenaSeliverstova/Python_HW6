# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def multi_pairs(list_num):
    new_list = []
    for i in range((int(len(list_num)//2)+int(len(list_num)%2))):
        new_list.append(list_num[i]*list_num[-1-i])
    return new_list

list_num = [1,2,3,4,5,6]

print(f"{list_num} - > {multi_pairs(list_num)}")

# 2

def mult_list(nums):
    return[nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]
