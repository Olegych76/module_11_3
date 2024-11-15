from pprint import pprint


class Object:
    pass


def introspection_info(obj_):
    type_ = type(obj_).__name__
    attribute = getattr(obj_, '__dict__', None)
    if attribute is None:
        attribute = []
    else:
        attribute = list(attribute)
    methods = dir(obj_)
    module = obj_.__class__.__module__
    info = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module}
    return info


class MyClass:
    pass


def my_func():
    pass


obj = Object()
number_info = introspection_info(42)
pprint(number_info)
number_info = introspection_info(MyClass)
pprint(number_info)
number_info = introspection_info(my_func)
pprint(number_info)
