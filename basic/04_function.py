# 함수
# 함수 정의
def great():                    # 선언부(Header), parameter가 없다.
	# 구현부
	print('hello')
	print('welcome')

# 함수 호출, []-> 선택사항
# [반환값을 받을 변수 = ], 함수이름([parameter]에 전달할 값(argument))
great()

# parameter가 있는 함수
def greeting2(name):
	print(f'Hello {name}.')
	print('Welcome')

greeting2('sancho')				# argument : sancho -> function parameter에 전달하는 값

def greeting3(name, name1):		# 선언된 parameter에는 값이 전달되어야 한다.
	print(f'welcome to {name}, {name1}.')

greeting3('sancho', 'de-gea')

# return이 있는 함수
# return value -> 호출한 곳을 value를 가지고 돌아가라.
def greeting4(name):
    return f'Hello {name}. \nwelcome'

result = greeting4('sancho')
print(result)                   # return value 출력
print(len(result))              # return 글자 수 확인

# return value가 여러 개인 경우 -> data_structure로 묶어서 반환
#                                 set은 불가능 tuple의 경우 ()를 생략하고 return하면 된다.
# return value는 반드시 1개여야 한다.
def calculate(num1, num2):
    # 숫자 두 개를 받아서 사칙연산한 결과를 반환.
    result_sum = num1 + num2
    result_dif = num1 - num2
    result_mul = num1 * num2
    result_di = num1 / num2
    # return [result_sum, result_dif, result_mul, result_di]
    return result_sum, result_dif, result_mul, result_di

result = calculate(10 ,5)
print(result)

# tuple로 반환한 것을 tuple 대입으로 받은 것 -> list 대입도 이와 같은 방식
v1, v2, v3, v4 = calculate(10, 5)
print(v1, v2, v3, v4)

def test(a, b, c, d, e, f, g):
    print(a, b, c, d, e, f, g, sep=' - ')

# positional argument
test(1, 2, 3, 4, 5, 6, 7)

# keyword argument
test(a = 10, b = 20, c = 30, g = 70, d = 40, f = 60, e = 50)

# function define시 parameter 선언
def print_info(name, age, address = None):
    print(f'name : {name}, age : {age}, address : {address}')

print_info('sancho', 20, 'seoul')
print_info('sancho', 20)                    # 기본값이 있는 매개변수(parameter)는 값을 전달하지 않을 수 있다.

def test_info(name, address, age = 0, tel = None):
    pass                                    # 구현부는 생략하겠다. -> for, if, while문에서도 사용가능

def print_info3(name = None, age = 0, address = None, tel = None, tall = 0.0, weight = 0.0):
    print(f'{name}, {age}, {address}, {tel}, {tall}, {weight}')

print_info3('sancho', 30)
print_info3(None, 0, None, None, 182.4, 86) # positional argument
print_info3(tall=182.4, weight=80)          # keyword argument
print_info3('sancho', 30, weight=90.7)      # argument 전달시 positional/keyword argument 구문을 같이 사용할 때

# var args
# 정수 여러 개를 받아서 다 더해주는 함수
def summation(valeus):
    result = 0

    for v in valeus:
        result += v
    
    return result

print(summation([1, 4, 10]))
print(summation((1, 4, 10, 11, 21, 30)))

# *parameter -> 가변인자 선언
# 가변인자 선언을 하면 python에서 parameter를 넘길 때 tuple로 묶어서 넘겨준다.
def summation2(*values):
    print(type(values))
    result = 0

    for v in values:
        result += v

    return result

print(summation2())
print(summation2(1, 2, 3, 4, 5))

# keyword argument로 전달받은 값들을 dictionary로 묶어서 받는다.
def print_info4(**info):
    print(type(info))
    print(info)

print_info4(name = 'sancho')

# 일반변수와 가변인자를 같이 선언할 때
def func2(v1, v2, *args, **kwargs):
    print(v1, v2)
    print(args)
    print(kwargs)

func2(10, 20, 30, 40, 50, 60, a='가', b='나')

# global variable & local variable
name = 'sancho'         # global_variable

def fun1():
    age = 20            # local_variable
    print(name)
    print(age)

def fun2():
    age = 1000
    print(name)
    print(age)

def fun3():
    name = 'de-gea'     # global_variable과 local_variable이 같을 때, 지역변수 이 둘은 다른변수이다.
    print(name)

def fun4():
    global name         # name이라는 변수는 전역변수임을 선언
    name = 'anthoy'
    print(name)

fun3()
fun1()
fun4()
print('-' * 10)
fun1()
fun2()

# first class citizen object
# function 자체를 기능으로만 쓰지말고, 값으로도 사용할 수 있다.
def hello():
    print('hello world')

hello()
my_func = hello()       # hello() 호출 -> return 값을 my_func에 대입
my_fun = hello          # my_fun에 hello 함수를 대입
my_fun()

def plus(num1, num2):
    return num1 + num2

print(plus(10, 20))
print(plus(30, 50))

# 함수를 받을 변수
def calc(func):
    num1, num2 = 100, 200
    result = func(num1, num2)
    # 전달받은 함수에 num1, num2 두 개의 값을 전달해 처리하고
    # 그 처리결과를 result 변수에 대입

    return result

# 두 개의 값을 받아서 처리결과를 리턴하는 함수를 전달
r = calc(plus)          # func = plus와 같음

print(r)

def mul(num1, num2):
    return num1 * num2

print(calc(mul))

# lambda 표현식
r2 = calc(lambda n1, n2 : n1 * n2)
print(r2)

def my_plus(num1, num2):
    return num1 + num2

a = lambda num1, num2 : num1 + num2
print(a(10, 20))

# 여러 개의 처리결과를 반환할 경우 data_structure로 묶어준다.
print(calc(lambda num1, num2 : (num1 + num2, num1 - num2, num1 * num2)))

# 2의 배수만 걸러주기.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x : x % 2 == 0, li)))  # filter(function, data_structure) : function 조건이 true만 반환

str_list = ['a', 'bbb', 'ccc', 'aaa', 'sss', 'sr', 'ssr', 'abc', 'ab', 'bbc', 'new', 'ar']
# sorted()함수, sort() 메소드 -> 방식 : 오름차순, 내림차순, 문자열-사전식
print(sorted(str_list))
print(sorted(str_list, reverse=True))

# key의 함수 : element를 전달 받아서 정렬할 때 사용할 값을 반환하는 함수를 구현
# key가 있을 경우 정렬할 때 list내의 element가 아니라 key의 함수가 반환한 값들을 기준으로 정렬한다.
print(sorted(str_list, key=lambda x : len(x), reverse=True))
print(sorted(str_list, key=lambda x : len(x)))

# 시작값과 끝값 두 개의 정수를 받아서 그 사이의 모든 정수들의 합을 구하여 반환하는 함수
def accumulate(start_num, end_num):
    """
    start_num와 end_num 사이의 모든 정수들의 합을 구하여 반환하는 함수
    [parameter]
        start_num : int - 범위의 시작 정수값
        end_num : int - 범위의 종료 정수값
    [return]
        result : int - 합계
    [exception]
    """
    result = 0

    for val in range(start_num, end_num + 1):
        result += val

    return result

print(accumulate(1, 100))

# help(function|class|method) -> function|class|method에 대한 설명을 출력
help(accumulate)