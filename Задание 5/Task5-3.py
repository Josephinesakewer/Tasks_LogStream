import random

import my_module

def accept_list():
    k = int(input("Введите кол-во, которое будет принимать список:"))
    list = []
    for i in range(k):
        x = input("Введите элемент списка:")
        list.append(x)
    print(list)

    random.shuffle(list)
    print(list)
accept_list()

# Пример использования функций модуля
radius = float(input("Введите радиус круга: "))
print("Площадь круга:", my_module.get_area_circle(radius))

scores = [int(x) for x in input("Введите оценки через пробел: ").split()]
print("Средний балл:", my_module.average_score(scores))

sum_cost = float(input("Введите сумму денег: "))
print("Количество акций Сбера, которые можно купить:", my_module.num_papers(sum_cost))

    