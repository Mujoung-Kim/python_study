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

print('my_module')