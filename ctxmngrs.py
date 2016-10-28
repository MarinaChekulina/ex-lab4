# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

import time
from datetime import datetime

class timer:
    def __enter__(self):
        self.begin_time = time.clock()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.clock() - self.begin_time)

