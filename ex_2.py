from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['A', 'a', 'B', 'b']

# Реализация задания 2

for i in Unique(list(data1), ignore_case=True):
    print(i, end=" ")
print()

for i in Unique(list(data2)):
    print(i, end=" ")
print()

for i in Unique(list(data3)):
    print(i, end=" ")
print()

for i in Unique(list(data3), ignore_case=True):
    print(i, end=" ")
print()


