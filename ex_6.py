#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
   #return (sorted(unique(field(arg,"job-name"),ignore_case=True)))
   return sorted(unique(field(arg, "job-name"), ignore_case=1), key=lambda x:x.lower())


# startswith-проверяет(точнее возвращает флаг) начинается ли строка с такого-то слова
@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"), arg))


#map-функция для преобразования коллекции
@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


#zip- для слияния по парам (например, a=[1,2], b=[3,4], print zip(a,b), [(1,3),(2,4)]
@print_result
def f4(arg):
    #return ["{}, зарплата {} руб.".format(work, salary) for (work, salary) in zip(arg, gen_random(100000, 200000, len(arg)))]
    a = list(gen_random(100000, 200000, len(arg)))
    return list('{}, зарплата {} руб.'.format(arg, a) for arg, a in zip(arg, a))


with timer():
    f4(f3(f2(f1(data))))
