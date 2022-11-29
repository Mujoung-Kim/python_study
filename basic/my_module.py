# module : 재사용 가능한 함수들, 클래스들, 전역변수들을 모아놓은 스크립트 파일

def plus(num1, num2):
	return num1 + num2

def minus(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	if num2 != 0:
		return num1 / num2
	else:
		print('0으로 나눌 수 없습니다.')

# main module과 sub module의 흐름을 확인 -> `__name__`을 활용
# module 내에서 result 결과 값을 조회할 때 사용
if __name__ == '__main__':
	print(__name__)			# main module or sub module로 실행될 때 주는 이름을 저장되는 변수
	print(plus(1, 2))
	print(minus(100, 50))
	print(multiply(2, 10))
	print(divide(10, 2))