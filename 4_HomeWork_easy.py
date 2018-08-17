# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
arr = [1, 2, 4, 0]
res = []
for i in arr:
    res.append(i**2)
print(res)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
arr = ['Apple', 'Pineapple', 'Orange', 'Banana']
arr2 = ['Apple', 'Pineapple']
res = []
for i in arr:
    for j in arr2:
        if i == j:
            res.append(i)
print(res)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
arr = [3, 9, 8, -10]
res = []
for i in arr:
    if i > 0 and i % 3 == 0 and i % 4 != 0:
        res.append(i)
print(res)