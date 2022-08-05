import requests
import os
from os import listdir
import re
import os.path
from bs4 import BeautifulSoup
from glob import glob

# создаю пустой список, в него "накоплю" (+= [y]) все каталоги с указанного пути в os.walk,
# кстати, walk создает каталоги рекурсивно, что очень хорошо для решения данной задачи
#
# не без особенностей: вывод пути через пересчет address в цикле не совсем корректный. Все что после //test
# выводит с обратными слешами \\, а это не есть путь для интерпретатора.
# Для того, чтобы путь был "путем" через re.sub меняем слеши на нужные(перем. address позволяет, тип str) и да,
# пришлось сделать их двойными, так как \ срабатывает как экранирование и интерпретатор
# ожидает какое-то регулярное выражение.

Directory = []
for address, dirs, files in os.walk('//106-dc01//aida//Sbor//test'):
    y = re.sub(r'\\', '//', address)
    Directory += [y]
Directory.pop(0)  # удаление первого корневого каталога (//test) указанного в os.walk.
# Он нам не нужен, т.к. в нем нет htm файлов согласно исходным данным.
print(Directory)
print()

# далее обращаюсь к подкаталогам списка Directory
# в цикле перечисляемая переменная dir предстает в виде списка,
# ее я использую для построения списка файлов в данном каталоге (listdir),
# а так же для указания текущего каталога интерпретатору(os.chdir),
# чтобы тот понимал с какого католога ему считывать файлы
for dir in Directory:
    os.chdir(dir)
    print(f'current DIR {os.getcwd()}')  # текущий
    new_list = listdir(dir)
    W = []
    # т.к. исходные данные содержат папки внутри подпапок, переданных в new_list,
    # то listdir считывает и их тоже. Для того, чтобы убрать их из списка
    # (иначе парсер(см.ниже) не сможет прочитать файлы с папками в листе), использую еще один цикл с условием
    # if new_list[i] != 'sh_us'
    # и из списка new_list извлекаю индекс, содержащий значение 'sh_us' и все кроме 'sh_us'
    # добавляю в ранее созданный еще один список W
    for i in range(len(new_list)):
        if new_list[i] != 'sh_us':
            W.append(new_list[i])
    # цикл перечисляет файлы в подкаталогах из списка W, открывает их, считывает в переменную
    # result и далее уже "парсер" через библиотеку BeatifulSoup, извлекает разметку,
    # разделяет ее на строки и согласно ключевому индивидуальному заданию
    # (вывести список файлов в которых упоминается заданное выражение)  производит поиск
    # перечисляемых в цикле файлах
    #
    # далее результат передается в строковую переменную v, построчно, с дозаписываением файла
    # (режим записи 'a') методом out производится заполнение файла по указанному пути.

    for htmlfiles in W:
        f = open(htmlfiles, 'r')
        result = f.read()
        soup = BeautifulSoup(result, 'lxml')
        strings = soup.find_all(string=re.compile('Windows 7'))
        v = ''
        for txt in strings:
            # это строки вывод строк, в каких именно встречается указанное в re.compile
            # print(" ".join(txt.split()))
            # это вывод названия файлов в которых упоминается заданное выражения
            v = htmlfiles
        # запись в файл
        with open('//106-dc01//aida//Sbor//test//output.txt', 'a') as out:
            print(v, file=out)
        print(v)
