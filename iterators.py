# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        # self.ignore_case = False

        #isinstance- проверка принадлежности объекта указанному классу(принадлежит ли items list )
        self.items = iter(items) if isinstance(items, list) else items
        self.ignore_case = kwargs.get('ignore_case')
        self.unique = []
        if kwargs.get('ignore_case'):
            self.ignore_case = True

    def __next__(self):
        # Нужно реализовать __next__
        for element in self.items:
            if self.ignore_case:
                #lower()- преобразование строки к нижнему регистру
                if str(element).lower() not in self.unique:
                    #str()- строковое представление объекта
                    self.unique.append(str(element).lower())
                    return element
            else:
                if element not in self.unique:
                    self.unique.append(element)
                    return element
        raise StopIteration()

    def __iter__(self):
        return self