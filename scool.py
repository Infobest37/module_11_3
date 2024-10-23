# конечно есть встроенная помощь
import inspect
import sys
from pprint import pprint

import requests

some_string = "i am a string"
some_number = 42
some_list = [some_string, some_number]

def some_func(param, param_2 = "n/a"):
    print("my params is", param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

# Пример 1 - Атрибут класса __name__
f = some_func

# функция dir() возвращает отсортированный список
# атрибуты и методы, доступны для указанного объекта, который может быть объявленной переменной или функцией
# print(dir(some_object))
# print(some_object.attribute_1)
# pprint(dir(some_number))
# print(dir(some_list))
# print(some_func.__name__)
# print(SomeClass.__name__)
# print(requests.__name__)
# print(f.__name__)
# print(type(some_number) is int)
# print(type(some_string) is str)
# print(type(some_number) is list)
# print(type(requests))
# print(some_string.__name__)
# print(some_object.__name__)

"""Урок 2 """
# Пример 1- функция hasattr() - проверка на существование атрибута
# pprint(dir(some_object))
attr_name = "attribute_2"
# print(hasattr(some_object, attr_name))
# print(hasattr(some_object, "attribute_1"))
'''функция getattr'''
# Пример 2 - функция getattr - получение атрибутов
# print(getattr(some_object, "attribute_1"))
# print(getattr(some_object, attr_name))

# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))
# print(help(getattr))
"""функция isinstance()"""
# Пример 3 - функция isinstance() - мы можем определить, является ли определенный объект
# экземпляром указанного класса
# print(isinstance(some_object, SomeClass))
# print(isinstance(some_number, str))
# print(isinstance(some_number, int))
# print(isinstance(some_number, SomeClass))


"""функция callable()"""
# Пример 4 - функция callable() - проверка на то, можем ли мы вызвать этот объект

# print(callable(some_string))
# print(callable(some_func))
# print(callable(some_object.attribute_1))
# print(callable(some_object.some_class_method))

"""Модуль inspect """
#  Модуль inspect - этот модуль собирает удобные методы и классы для отображения интраспективной информации

# Пример 5 - самое употребимые функции

# print(inspect.getmembers(some_object, inspect.isfunction))
# print(inspect.ismodule(some_object))
# print(inspect.isclass(some_object))
# print(inspect.ismodule(requests))
# print(inspect.isclass(requests))
# print(inspect.isbuiltin(requests))
# print(inspect.isfunction(requests))
#
# some_func_module = inspect.getmembers(some_func)
# print(type(some_func_module), some_func_module)

"""Урок 3"""
"""Интроспеция"""
# полезный системный покет - sys
# pprint(dir(sys))

# Путь к интерпритатору пайтон
# print(sys.executable)

# какой операционной системе мы работаем
print(sys.platform)


# Текущая версия пайтон
# print(sys.version)
# print(type(sys.version))
# print(sys.version_info)

# Список содержащий параметры командной строки если она была задана
# print(sys.path)

# словарь, который отображает имена модулей в объектах модулей для всех загруженных в текущих момент модулей
# print(sys.modules)

# Стоит упомянуть __builtins__ псевда-модуль, встроенный в интерпритатор объекта
# константы исключения функции
# print(__builtins__)
# pprint(dir(__builtins__))

def factrial(n):
    if n == 1:
        return 1
    else:
        return n * factrial(n - 1)
sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(1000000)
print(factrial(5000))
print(sys.getsizeof(factrial(5000)))

