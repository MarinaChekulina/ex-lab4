#Модуль random предоставляет функции для генерации случайных чисел, букв, случайного выбора элементов последовательности.
#random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
from random import randint

# реализовать генератор,который последовательно выведет значения ключей словарей массива
def field(list,*args):
    #assert позволяет производить проверки истинности утверждений, что может быть использовано в отладочных целях
    #Если проверка не пройдена, возбуждается исключение
    #для ситуаций, которые не должны происходить вовсе, которые нельзя обработать или это не имеет смысла
    assert len(args) > 0, "There are no input arguments"
    if len(args) == 1:
        for item in list:
            if item.get(args[0]):
                yield item[args[0]]
    else:
        for item in list:
            dictionary = {}
            for element in args:
                if item.get(element):
                    dictionary[element] = item[element]
            if dictionary:
                # вызывающему коду выдается значение dictionary, так как дошли до yield
                yield dictionary

#реализовать генератор, который последовательно выдает заданное
#количество случайных чисел в заданном диапазоне

def gen_random(begin, end, num_count):
    for item in range(num_count):
        yield randint(begin, end)

