#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'brown'},
    {'title1': 'Шкаф', 'price': 8000, 'color': 'brown'}

]

# Реализация задания 1

for item in gen_random(1, 7, 9):
    print (item, end=" ")
print()
for item in field(goods, "title1"):
    print(item, end=" ")
    print()
