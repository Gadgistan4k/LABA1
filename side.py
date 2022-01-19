f2 = open('pokemon_full.json')
pokemons2 = f2.readlines()

pokemon = input('Веведите покемона для просмотра среднего эволюционного прироста: ')
n = 0
count = 0
count2 = 1
evolution = []
total = []

for i in range(len(pokemons2)):
    line = pokemons2[i]
    if line.count('"name"') == 1 and line.count(pokemon) == 1:
        while n != 1:
            count = count + 1
            line2 = pokemons2[i+count]
            if line2.count('"evolution": ['):
                line3 = pokemons2[i + count + 1]
                while line3.count(']') != 1:
                    name = (((line3.replace('"', '')).replace(',', '')).replace(' ', '')).replace('\n', '')
                    evolution.append(name)
                    count2 = count2 + 1
                    line3 = pokemons2[i + count + count2]
                    n = 1

for pokemon1 in evolution:
    for i in range(len(pokemons2)):
        line = pokemons2[i]
        count = 0
        count2 = 0
        m = 0
        if line.count('"name"') == 1 and line.count(pokemon1) == 1:
            while m != 1:
                count = count + 1
                line2 = pokemons2[i + count]
                if line2.count('"total":'):
                    total.append(int((line2.replace('"total": ', '')).replace(' ', '')))
                    m = 1

all_stat = 0

for i in range(len(total) - 1):
    all_stat = total[i + 1] - total[i] + all_stat

print(f'Средний прерост характеристик:{all_stat / (len(total) - 1)}')