# my_module.py - 현재 모듈(import_exam.py)와 같은 패키지에 있다
# test_module.py - 현재 모듈이 있는 패키지의 하위 패키지인 my_package 아래있다.

# my_module을 import
# import my_module as mm
# print(mm.plus(1, 2), mm.minus(10, 2), mm.multiply(2, 5), mm.divide(10, 2))

# my_module안의 특정 함수를 import
# from my_module import minus, divide
# print(minus(10, 2), divide(10, 2))

# import할 대상이 많아서 여러줄에 걸쳐 작성해야 할 경우 ( )로 묶어준다.
# from my_module import (plus, minus
						# , divide)

# from my_module import *
# print(plus(1, 2), minus(10 ,2), multiply(5, 3), divide(10, 4), sep=', ')

# package 안에 있는 모듈 import
# import my_package.test_module

# my_package.test_module.hello_world()
# my_package.test_module.greeting('rashford')
# p = my_package.test_module.Person('burno', 26)
# print(p)

# package와 module을 분리해서 import
# from my_package import test_module
# test_module.hello_world()

# function, class를 import -> 현재 module의 namespace에 등록된다.
from my_package.test_module import hello_world, greeting

hello_world()
greeting('rashford')