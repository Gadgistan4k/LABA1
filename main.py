f = open('pokemon_full.json')
pokemons = f.read()

all = len(pokemons)  # Ищем количество символов в файле

not_space = pokemons.replace(" ", "")  # Убираем все пробелы из файла
signs = 0
for i in ('.', ',', '[', ']', '(', ')', ':', ';', '{', '}', "'", '"'):
    signs = signs + pokemons.count(i)  # Считаем количество всех знаков препинания
all2 = len(not_space) - signs  # Получаем искомый ответ

f2 = open('pokemon_full.json')
pokemons2 = f2.readlines()
max_description = 0
for i in range(0, len(pokemons2)):
    line = pokemons2[i]
    if line.count('"name"') == 1:
        # Находим имя покемона для которго дано писание
        name = line
    if line.count('"description"') == 1:
        description = len(line)
        if description > max_description:
            # Находим максимальную длину описания
            max_description = description
            name_with_max_description = name
name_with_max_description = ((name_with_max_description.replace('"name": "', '')).replace('",', '')).replace('    ', '')
# Избавимся от лишних символов в строке кроме имени

words = 0
for i in range(0, len(pokemons2)):
    count = 0
    count_2 = 1
    line = pokemons2[i]
    if line.count('"abilities"') == 1:
        # Находим начало описания способностей и запускаем цикл по перебору их
        while count != 1:
            line = pokemons2[i + count_2]
            count_2 = count_2 + 1
            if line.count(']') == 1:
                # Заверщаем цикл перебора
                count = 1
            if line.count(" ") - line.count(' "') > words:
                # По количеству пробелов определяем максимальную длину слова
                # И исключаем ошибку где способность написанна с пробелом в конце
                words = line.count(" ")
                abilit = line
abilit = (abilit.replace('"', '')).replace('      ', '')
# Очищаем название способности от лишних символов

print(f'Общее количество символов в файле:{all}')
print('')
print(f'Общее количесто символов без пробелов и знаков препинания:{all2}')
print('')
print(f'Покемон с самым длинным описанием:{name_with_max_description}')
print(f'Способность с наибольшим количеством слов:{abilit}')
