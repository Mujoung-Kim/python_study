import my_module			# my_module.py를 실행

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

print(num1, num2)

# 덧셈
# 함수/클래스/변수 호출 순서
# 1. 같은 module의 것을 찾아서 호출
# 2. 실행환경에 설치된 module의 것을 호출

# 그 밖의 경우 -> import module을 해야한다.
# import module을 실행해서 그 안에 정의된 함수/클래스/변수들을 메모리에 올리는 작업을 해야한다.
plus_result = my_module.plus(num1, num2)
print(f'result: {plus_result}')