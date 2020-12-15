from time import sleep
from datetime import datetime


class Logger:
    """
    Логгер для задания 1
    """
    log_list = []

    def __init__(self, function):
        self.calls = 0
        self.function = function

    def __call__(self, *args, **kwargs):
        self.calls += 1
        dict = {'call_date': datetime.isoformat(datetime.now()),
                'func_name': self.function.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': self.function(*args, **kwargs)}
        Logger.log_list.append(dict)

        with open('Задание_1_вариант_2.txt', 'a', encoding='utf-8') as file:
            file.write(f'{dict}')
            file.write('\n')
        return self.function(*args, **kwargs)


@Logger
def mult(x, y):
    return x * y



if __name__ == '__main__':

    a = mult(1, 3)
    sleep(5)
    b = mult(2, 32)



