# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Словарь
# возможность доступа по человеко-чистаемым ключам, словарь похож
# на субдд (но не является ею), висит в оп, чтобы разместится на
# HDD нужна сериализация. Применяется для относительно небольших словарей.
# дубликаты недопустимы как и со множествами (в примере ниже, чтобы записать две лады 2101 пришлось
# их так сказать идентифицировать, первая1 и вторая2.
# ключи в словаре не изменяются, но меняется их значение (key:value)

X = {
    'Lada1': {'model': '2101',
              'color': 'Синий',
              'age': '1997'},
    'Lada2': {'model': '2101',
              'color': 'Синий',
              'age': '1997'},
    'Chevrolet': {'model': 'aveo',
                  'color': 'Красный',
                  'age': '2010'},
    'УАЗ': {'model': 'Патриот',
            'color': 'Серый',
            'age': '2017'}
}
name1 = input("Введите модель: ")
flag = True
for search_emploers in X:
    if X[search_emploers]['model'] == name1:
        print(X[search_emploers]['color'])
        print(X[search_emploers]['age'])
        flag = False
if flag:
    print('нет такого значения')

print(X)
print(X['Chevrolet']['model'])
print(X['УАЗ']['color'])

# список:
# работает только по числовым ключам,
# допускается замена, присваивание, удаление, добавление индексов и их значений (в порядке индекс и его значение, если наоборот ошибка)
# допускаются дубликаты, в словаре такого не допускается.

# в данном примере в переменную name1, ввели значение индекса УАЗ, после чего методом .index
# получили его индекс в данном списке, в последующем принте, прибавив к нему 1, выводим
# параметры которые присущи введенному индексу предложенного списка
avtomobili = [
    ['lada'], ['model:2101',
               'color:Синий',
               'age:1997'],
    ['lada'], ['model:2101',
               'color:Синий',
               'age:1997'],
    ['Chevrolet'], ['model:aveo',
                    'color:Красный',
                    'age:2010'],
    ['УАЗ'], ['model:Патриот',
              'color:Серый',
              'age:2017'],
]
name1 = input('Введите модель: ')
z = (avtomobili.index([name1]) + 1)
print(avtomobili[z][0])
# либо
print(avtomobili[z])

# Множество
# По сути множество это словарь без значений. Поэтому и синтаксически они обозначаются одинаково.
# понравилось, что элементы множества легко перебираются циклом, лекго определить в переменные (brend, model, color, age) и вывести

# далее ниже реализован пример с True and False находится ли введенное множество в переменной.
avtomobili = {
    ('lada', '2101', 'Синий', '1997'),
    ('lada', '2101', 'Синий', '1997'),
    ('Chevrolet', 'aveo', 'Красный', '2010'),
    ('УАЗ', 'Патриот', 'Серый', '2017'),
}
for brend, model, color, age in avtomobili:
    print(brend, model)

name1 = input('Введите бренд:')
name2 = input('Введите модель:')
name3 = input('Введите цвет:')
name4 = input('Введите год:')

# проверка вхождения элемента множества в переменной avtomobili
print((name1, name2, name3, name4) in avtomobili)
