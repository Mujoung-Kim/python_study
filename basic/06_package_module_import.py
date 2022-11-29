# 현재 module에서 my_module을 사용
# my_module의 함수/클래스/변수를 호출
# 제일 먼저 import를 해야한다.
# import 단위 - 기본: module, module의 function, class, variable를 개별적으로 import할 수 있다.
# import my_module
# my_module.py가 실행이 되고 그 안에 정의된 function/class/variable들이 python 실행환경에 namespace로 등록된다.

# r1 = my_module.plus(10, 20)
# r2 = my_module.minus(100, 50)

# print(r1, r2)

# import my_module as mm -> my_module.py를 import하고 namespace의 이름을 mm으로 준다.
# import module_name as byname -> byname은 관례적으로 변수명과 같다.

# import package_name.module_name as byname
# import test_module -> byname을 설정하지 않을경우 my_package.test_module.hello_world()식으로 호출
# import my_package.test_module as tm

# tm.hello_world()
# tm.greeting('anthony')
# print(tm.Person('sancho', 20))

# from package_path import module_name as byname
# package가 여러 개의 package를 가질 때 주로 사용
# from my_package import test_module

# test_module.hello_world()
# test_module.greeting('burno')
# print(test_module.Person('martial', 28))

import my_module as mm

r = mm.plus(1, 1)
print(r)

# 현재 실행 중인 module - .py 파일 path 
# : C:\Users\user\Downloads\Study\Python\code -> 현재 working path(directory)
# import module, from package import module 
# -> 현재 working path부터 찾는다.
import my_module as mm				# my_module.py를 현재 working path에서 부터 찾는다.
from my_package import test_module	# my_package directory를 현재 working path에서 찾는다.

# 현재 실행중인 module에서 사용할 module/package가 현재 working path에 없고 other path에 있을 경우
#  -> **PYTHONPATH** 환경변수를 설정해야만 한다.
# **PYTHONPATH** -> 사용할 module/package가 있는 path를 설정해주는 환경변수
# 설정방법
# 1. os의 환경변수로 등록 (한 번만 실행하면 된다.)
# 2. sys module의 path변수에 등록 (실행시마다 해야한다.)
# 현재 working path -> C:\Users\user\Downloads\Study\Python\code
# util.py           -> C:\Users\user\Downloads\Util
import sys                          # sys standard module
sys.path                            # library들이 저장된 path -> import module : module을 찾는 순서
sys.path.append(r'C:\Users\user\Downloads\Util')
print(sys.path, sep='\n')
# import util