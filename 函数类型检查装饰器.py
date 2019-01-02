# 该模块实现一个对被装饰的函数的参数类型检查的装饰器

from inspect import signature

# test
def typeAssert(*ty_args, **ty_kwargs):
    def docorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        def wrapper(*args, **kwargs):
            for name, obj in sig.bind(*ty_args, **ty_kwargs).arguments:
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError("{0} must be {1}".format(name, btypes[name]))
            return func(*args, **kwargs)
        return wrapper
    return docorator

@typeAssert(int, str, list)
def func_1(a, b, c):
    print(a, b, c)

if __name__ == "__main__":
    func_1(1, 2, 3)
    func_1(1, 'a', [])
