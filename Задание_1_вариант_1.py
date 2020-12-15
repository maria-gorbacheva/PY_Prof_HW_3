
from datetime import datetime

def logger(function):
    def oncall(*args, **kwargs):
        dict = {'call_date': datetime.isoformat(datetime.now()),
                'func_name': function.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': function(*args, **kwargs)}

        with open('Задание_1_вариант_1.txt', 'a', encoding='utf-8') as file:
            file.write(f'{dict}')
            file.write('\n')

        return function(*args, **kwargs)
    return oncall


@logger
def multiple(a, b):
    return a*b


if __name__ == '__main__':

    multiple(2, 3)
    print(multiple(3,4))