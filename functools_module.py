import functools

def myDocoratorWithFunctools(func):
    """
    docstring of myDocoratorWithFunctools
    """
    @functools.wraps(func)
    def wrapper1(*args, **kwargs):
        """
        docstring of wrapper1
        """
        print('调用已经装饰的函数')
        return func(*args, **kwargs)
    return wrapper1

def myDocoratorWithoutFunctools(func):
    """
    docstring of myDocoratorWithoutFunctools
    """
    def wrapper2(*args, **kwargs):
        """
        docstring of wrapper2
        """
        print('调用已经装饰的函数')
        return func(*args, **kwargs)
    return wrapper2

# 保护了被装饰函数的属性
@myDocoratorWithFunctools
def testFunc1():
    """
    docstring of testFunc1
    """
    return "调用testFunc1"

@myDocoratorWithoutFunctools
def testFunc2():
    """
    docstring of testFunc2
    """
    return "调用testFunc2"


if __name__ == "__main__":
    f1 = testFunc1
    f2 = testFunc2
    print(f1(), f1.__name__, f1.__qualname__, f1.__doc__, f1.__module__, sep='\n')
    print(f2(), f2.__name__, f2.__qualname__, f2.__doc__, f2.__module__, sep='\n')