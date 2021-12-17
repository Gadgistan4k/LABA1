f = open('pokemon_full.json')
file = f.read()

vse = len(file)  # Ищем количество символов в файле

not_probel = file.replace(" ", "")  # Убираем все пробелы из файла
znaki = 0
for i in ('.', ',', '[', ']', '(', ')', ':', ';', '{', '}', "'", '"'):
    znaki = znaki + file.count(i)  # Считаем количество всех знаков препинания
vse2 = len(not_probel) - znaki  # Получаем искомый ответ

f2 = open('pokemon_full.json')
file2 = f2.readlines()
max_opisanie = 0
for i in range(0, len(file2)):
    stroka = file2[i]
    if stroka.count('"name"') == 1:
        # Находим имя покемона для которго дано писание
        name = stroka
    if stroka.count('"description"') == 1:
        opisanie = len(stroka)
        if opisanie > max_opisanie:
            # Находим максимальную длину описания
            max_opisanie = opisanie
            name_with_max_opisanie = name
name_with_max_opisanie = ((name_with_max_opisanie.replace('"name": "', '')).replace('",', '')).replace('    ', '')
# Избавимся от лишних символов в строке кроме имени

slov = 0
for i in range(0, len(file2)):
    s = 0
    n = 1
    stroka = file2[i]
    if stroka.count('"abilities"') == 1:
        # Находим начало описания способностей и запускаем цикл по перебору их
        while s != 1:
            stroka = file2[i + n]
            n = n + 1
            if stroka.count(']') == 1:
                # Заверщаем цикл перебора
                s = 1
            if stroka.count(" ") - stroka.count(' "') > slov:
                # По количеству пробелов определяем максимальную длину слова
                # И исключаем ощибку где способность написанна с пробелом в конце
                slov = stroka.count(" ")
                abilit = stroka
abilit = (abilit.replace('"', '')).replace('      ', '')
# Очищаем название способности от лишних символов

print('Общее количество символов в файле:', vse)
print('')
print('общее количесто символов без пробелов и знаков препинания:', vse2)
print('')
print('Покемон с самым длинным описанием:', name_with_max_opisanie)
print('Способность с наибольшим количеством слов:', abilit)
