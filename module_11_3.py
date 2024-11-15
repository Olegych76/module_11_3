from pprint import pprint


class Object:
    pass


def introspection_info(obj):
    type_ = type(obj).__name__
    attribute = getattr(obj, '__dict__', None)
    if attribute is None:
        attribute = []
    else:
        attribute = list(attribute)
    methods = dir(obj)
    module = obj.__class__.__module__
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
