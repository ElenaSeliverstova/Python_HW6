# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

list_of_coord = "1 2 5 6"

def distance_between_two_dots(text : str):
    x1,y1,x2,y2 = list(map(int ,text.split()))
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

print(f"distance between x1,y1,x2,y2 [{list_of_coord}] -> {distance_between_two_dots(list_of_coord):.2f}")

# 2

from functools import reduce
p1= list(map(int, input('Введите координаты первой точки: ').split()))
p2= list(map(int, input('Введите координаты второй точки: ').split()))
d = reduce(
        lambda a, b: (a+b)**(1/2),
        (map(
            lambda p: (p[1] - p[0])**2,
            zip(p1, p2))))
print(d)