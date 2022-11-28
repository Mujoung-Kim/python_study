# 현재 module에서 my_module을 사용
# my_module의 함수/클래스/변수를 호출
# 제일 먼저 import를 해야한다.
# import 단위 - 기본: module, module의 function, class, variable를 개별적으로 import할 수 있다.
import my_module
# my_module.py가 실행이 되고 그 안에 정의된 function/class/variable들이 python 실행환경에 namespace로 등록된다.

r1 = my_module.plus(10, 20)
r2 = my_module.minus(100, 50)

print(r1, r2)

# import my_module as mm -> my_module.py를 import하고 namespace의 이름을 mm으로 준다.
# import module_name as byname -> byname은 관례적으로 변수명과 같다.

# import package_name.module_name as byname
# import test_module -> byname을 설정하지 않을경우 my_package.test_module.hello_world()식으로 호출
import my_package.test_module as tm

tm.hello_world()
tm.greeting('anthony')
print(tm.Person('sancho', 20))

# from package_path import module_name as byname
# package가 여러 개의 package를 가질 때 주로 사용
from my_package import test_module

test_module.hello_world()
test_module.greeting('burno')
print(test_module.Person('martial', 28))