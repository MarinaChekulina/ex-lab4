# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно


def print_result(print_func):
    def decorated_func(*args, **kwargs):
        print(print_func.__name__)
        result = print_func(*args, **kwargs)
        if type(result) is list:
            #"\n".join()- сборка строки из списка с разделителем "\n"
            #join(map())- для списка с числами
            print("\n".join(map(str, result)))
        elif type(result) is dict:
                print("\n".join([str(k)+"="+str(v)for k,v in result.items()]))
        else:
            print(result)
        return result
    return decorated_func


# def test(**kwargs):
#     print("Переменные:", kwargs)
# test(a=1, b=2, c=3)
#
# def test2(*args):
#     print("Переменные:", args)
# test2(1, 2, 3)
#
# def test3(* args,**kwargs):
#     print("Переменные:", kwargs, args)
# test3(1, 2, 3, a=7, b=9)