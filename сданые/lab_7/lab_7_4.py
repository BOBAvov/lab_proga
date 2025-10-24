"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Лаба:       №7 — Списки. Часть 2
Задание 4:  Замена всех строчных гласных английских букв на заглавные.
Описание:   Ввод списка строк. Во всех элементах списка каждая строчная
            английская гласная (a, e, i, o, u) заменяется на заглавную.
            Вывод изменённого списка.
"""
while True:
    try:
        source_list = input("Введите элементы списка строк через ; : ").split(';')
        break
    except ValueError:
        print('Неверно введённые данные!')

ang_gvas = 'aeiou'

for i in range(len(source_list)):
    # source_list[i] = "".join(map(lambda x: x.upper() if x in ang_gvas else x, source_list[i]))
    source_list[i] = list(source_list[i])
    for j in range(len(source_list[i])):
        if source_list[i][j] in ang_gvas:
            source_list[i][j] = source_list[i][j].upper()
    source_list[i] = "".join(source_list[i])


print("Изменённый список:", source_list)