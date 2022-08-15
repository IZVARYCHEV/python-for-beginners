import requests
import os
from os import listdir
import re
import os.path
from bs4 import BeautifulSoup
from glob import glob

# исключение папок из проверок
exception = 'sh_us'

#перехорд в каталог и удаление файла output.txt, если он есть
os.chdir('//106-dc01//aida//Sbor//test')  # выбрать каталог
print(f'current DIR: {os.getcwd()}')  # отображение текущего

if os.path.isfile("//106-dc01//aida//Sbor//test//output.txt"):
    os.remove("//106-dc01//aida//Sbor//test//output.txt")
    print("File output.txt deleted success")
else:
    print("File output.txt doesn't exists!")


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
Directory.pop(0)# удаление первого корневого каталога (//test) указанного в os.walk.
# Он нам не нужен, т.к. в нем нет htm файлов согласно исходным данным.

#исключение папок из работы парсера (исключение происходит из строковой переменной exception).
#создается пустой список происходит проверка по строкам(в условии), далее перенос обратно в список
S = ''
for dir in Directory:
    if (not exception in dir):
        S += (dir + '\n')
rows = S.splitlines()
Directory = rows
print(Directory)

# далее обращаюсь к подкаталогам списка Directory
# в цикле перечисляемая переменная dir предстает в виде списка,
# ее я использую для построения списка файлов в данном каталоге (listdir),
# а так же для указания текущего каталога интерпретатору(os.chdir),
# чтобы тот понимал с какого католога ему считывать файлы

for dir in Directory:
    os.chdir(dir)
    print(f'current DIR: {os.getcwd()}')  # отображение текущего
    new_list = listdir(dir)
    # print(new_list)
    W = []
    # т.к. исходные данные содержат папки внутри подпапок, переданных в new_list,
    # то listdir считывает и их тоже. Для того, чтобы убрать их из списка
    # (иначе парсер(см.ниже) не сможет прочитать файлы с папками в листе), использую еще один цикл с условием
    # if new_list[i] != 'sh_us'
    # и из списка new_list извлекаю индекс, содержащий значение 'sh_us' и все кроме 'sh_us'
    # добавляю в ранее созданный еще один список W
    for i in range(len(new_list)):
        if new_list[i] != exception:
            W.append(new_list[i])
    # цикл перебирает файлы в подкаталогах из списка W, открывает их, считывает в переменную
    # result и далее уже "парсер" через библиотеку BeatifulSoup, извлекает разметку,
    # разделяет ее на строки и согласно ключевому индивидуальному заданию
    # (вывести список файлов в которых упоминается заданное выражение или строка) происходит поиск
    # перечисляемых в цикле файлов.
    # далее, информация с парсера через функцию get_text преобразуется в строки, затем в цикле
    # происходит перебор элементов списка words и вывод строк с искомыми словами в файл output.txt

    for htmlfiles in W:
        f = open(htmlfiles, 'r')
        result = f.read()
        soup = BeautifulSoup(result, 'lxml')
        res_str = soup.get_text()

        words = [
            'Имя компьютера  ',
            'Имя пользователя  ',
            'Тип ЦП  ',
            'Системная плата  ',
            'Системная память  ',
        ]
        otbor = ''
        v = ''
        for w in words:
            for stroka in res_str.split('\n'):
                v = htmlfiles
                if w in stroka:
                    otbor += (stroka + '\n')
        rows = otbor.splitlines()
        unique_rows = dict.fromkeys(rows)
        new_text = "\n".join(unique_rows)
        # print(v)
        # print()
        # print(new_text + '\n')
        with open('//106-dc01//aida//Sbor//test//output.txt', 'a') as out:
            print(new_text, v, file=out)