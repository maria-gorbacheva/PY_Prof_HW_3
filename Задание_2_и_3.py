from datetime import datetime
import hashlib
import os

def superlogger(log_path=None):
    # по умолчанию, если не указан путь к файлу с логами, создает файл log_list_default.txt
    # в папке проекта
    def logger(function):
        def oncall(*args, **kwargs):
            dict = {'call_date': datetime.isoformat(datetime.now()),
                    'func_name': function.__name__,
                    'args': args,
                    'kwargs': kwargs,
                    'result': function(*args, **kwargs)}
            nonlocal log_path
            if log_path is None:
                log_path = 'log_list_default.txt'

            with open(log_path, 'a', encoding='utf-8') as file:
                file.write(f'{dict}')
                file.write('\n')

            return function(*args, **kwargs)

        return oncall

    return logger

# Применение декоратора с параметром пути к функции-генератору,
# которая принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.

@superlogger('C:/Users/Mashlenok/Desktop/pyton/Generators_Iterators/HW_2/HW_3/Задание_1_вариант_1.txt')
def my_generator(file: str):
    file_path = os.path.join(os.getcwd(), file)
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            data = f.readline()
            if not data:
                break
            hash_line = hashlib.md5(data.encode())
            yield hash_line.hexdigest()

@superlogger()
def devision(a, b):
    return a / b

if __name__ == '__main__':
    for line in my_generator('wiki_links.txt'):
        print(line)
