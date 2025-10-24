"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Лаба:       №7 — Списки. Часть 2
Задание 1:  Удалить все чётные элементы списка.
Описание:   Ввод целочисленного списка. Удаление всех чётных элементов за один цикл,
            без использования del, pop, remove, срезов. Вывод изменённого списка.
"""
while True:
    try:
        source_list = list(map(int, input("Введите элементы списка через пробел: ").split()))
        break
    except ValueError:
        print('Неверно введённые данные!')

j = 0
cnt_del_elem = 0
for i in range(len(source_list)):
    if source_list[i]%2==0:
        cnt_del_elem += 1
        continue
    source_list[j] = source_list[i]
    j+=1

print("Изменённый список:", source_list[:j])