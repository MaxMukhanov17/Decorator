import os
from datetime import datetime
import datetime

def decorator_logger(path):
    def _decorator_logger(func):
        def new_func(*args, **kwargs):
            datetime_func_call = datetime.datetime.today()
            name_func = func.__name__
            arg_func = args
            result = func(*args, **kwargs)
            print(path)
            with open('decor_info.log', 'a', encoding='utf-8') as file:
                file.write(f'Дата и время - {datetime_func_call}\n'
                f'Имя функции - {name_func}\n'
                f'Аргумент функции - {arg_func}\n'
                f'Возвращаемое значение - {result}')
            return result
        return new_func
    return _decorator_logger

path_file_log = os.path.abspath('decor_info.log')
decorator_logger_path_file_log = decorator_logger(path_file_log)

@decorator_logger_path_file_log
def comparison_intelligence(dict_intelligence):
  clever_superhero = max(dict_intelligence, key = dict_intelligence.get)
  return f'Самый умный супергерой - {clever_superhero}'

print(comparison_intelligence({'Hulk': 88, 'Captain Amerika': 69, 'Thanos': 100}))

# def say(greeting):
#     result = greeting + ' world!'
#     return result

# print(say('Hello'))