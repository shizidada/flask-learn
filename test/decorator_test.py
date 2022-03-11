# -*- coding: utf-8 -*-

from time import ctime
from time import sleep

'''
*args 传递标示单个参数 --> tuple
**kwargs 表示关键字参数 --> dict
'''


# 函数带多个参数，装饰器对应修改以适合多种情况

def login_required(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('1'):
            return 'in'

        return func(*args, **kwargs)

    return wrapper


@login_required
def login(*args, **kwargs):
    return 'not in'


# 函数带多个参数，装饰器也带多个参数
def decorator_a(*dargs, **dkwargs):
    print('decorator_a outter')

    def wrapper(func):
        print('decorator_a wrapper')

        def _wrapper(*args, **kwargs):
            print('decorator_a _wrapper')
            return func(*args, **kwargs)

        return _wrapper

    return wrapper


def decorator_b(*dargs, **dkwargs):
    print('decorator_b outter')

    def wrapper(func):
        print('decorator_b wrapper')

        def _wrapper(*args, **kwargs):
            print('decorator_b _wrapper')
            return func(*args, **kwargs)

        return _wrapper

    return wrapper


@decorator_b(2, a=3)
@decorator_a(1, a=2)
def test(*args, **kwargs):
    pass


if __name__ == '__main__':
    test()
    # stu = {'name': 'test', 'age': 12}
    # r = login(1, 2, 3, **stu)
    # print(r)

# @decorator_b(2, a=3)
# @decorator_a(1, a=2)
#     decorator_b outter
#     decorator_a outter
#     decorator_a wrapper
#     decorator_b wrapper
#     decorator_b _wrapper
#     decorator_a _wrapper


# @decorator_a(1, a=2)
# @decorator_b(2, a=3)
#     decorator_a outter
#     decorator_b outter
#     decorator_b wrapper
#     decorator_a wrapper
#     decorator_a _wrapper
#     decorator_b _wrapper