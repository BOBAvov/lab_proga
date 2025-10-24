"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Лаба:       №7 — Списки. Часть 2
Задание 2:  После каждого чётного элемента добавить его удвоенное значение.
Описание:   Ввод списка целых чисел. После каждого чётного элемента
            вставляется его удвоенное значение без insert, append и срезов.
"""

while True:
    try:
        source_list = list(map(int, input("Введите элементы списка через пробел: ").split()))
        break
    except ValueError:
        print('Неверно введённые данные!')

cnt_ud_elem = 0
for i in source_list:
    if i % 2 == 0:
        cnt_ud_elem +=1

i = len(source_list) - 1
source_list += [0] * cnt_ud_elem
r = len(source_list) - 1

while i>=0:
    if source_list[i]%2==0:
        source_list[r] = source_list[i] * 2
        r-=1
        source_list[r] = source_list[i]
        r-=1
    else:
        source_list[r] = source_list[i]
        r -= 1
    i -= 1

print(source_list)
