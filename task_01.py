# 1- Определить, присутствует ли в заданном списке строк, некоторое число

def find_number(list_of_text: str, number: str):
    return len(list(filter(lambda a: a in number, list_of_text.split()))) > 0


text = "bla bla 222 bla"
number = "22"
print(f"{number} in text : '{text}' - > is {find_number(text, number)}")


# Вариант 2
lst = ['мама', 'сшила', 'м0не', 'штаны', 'и7з', 'берез9овой', 'кор45ы', '893.']
def is_num(lst, number):
    return list(filter(lambda element: str(number) in element, lst))
#    return any(filter(lambda element: str(number) in element, lst))
print(is_num(lst, 0))