



def function(obj):
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    obj_dict = {
        'type': type(obj).__name__,  # Название типа объекта
        'attributes': attributes,  # Список атрибутов
        'methods': methods,  # Список методов
        'module': obj.__mod__  # Модуль, к которому принадлежит объект
    }

    return obj_dict

result = function("funct")
print(result)