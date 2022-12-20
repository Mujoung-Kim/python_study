# 1. 두 정수 사이의 합
# for문
def solution(a, b) :
	answer = 0
	
	if a <= b :
		for i in range(a, b + 1) :
			answer += i
	else :
		for i in range(b, a + 1) :
			answer += i
	
	return answer

# method 활용
def solution(a, b) :
	if a > b :
		a, b = b, a

	return sum(range(a, b + 1))

a, b = map(int, input().split())
print(solution(a, b))

# 2. 수박수박수박...
def solution(n):
	answer = ''
	
	if n % 2 != 0:
		for i in range(1, n + 1) :
			if i % 2 == 0 :
				answer += '박'
			else :
				answer += '수'
	else :
		for i in range(1, n + 1) :
			if i % 2 != 0 :
				answer += '수'
			else :
				answer += '박'
		
	return answer

# 모범답안
def solution(n) :
	answer = '수박' * n

	return answer[:n]

print(solution(int(input())))

# 3. 서울에서 김서방 찾기
# list를 이용한 풀이
def solution(seoul):
	result = [idx for idx in range(len(seoul)) if 'Kim' in seoul[idx]]
	answer = f'김서방은 {result}에 있다'
	
	return answer

# 모범 답안
def solution(seoul):
	answer = f'김서방은 {seoul.index("Kim")}에 있다'
	
	return answer

print(solution(['Jane', 'Kim']))

# 4. 약수의 합
def solution(n) :
	answer = 0

	for i in range(1, n + 1) :
		if n % i == 0:
			answer += i

	return answer

print(solution(int(input())))

# 5. 문자열 내 p와 y의 개수는?
def solution(s) :
	answer = False

	if s.upper().count('P') == s.upper().count('Y') : answer = True

	return answer

# 모범답안
def solution(s) :
	return s.upper().count('P') == s.upper().count('Y')

print(solution(input()))

# 6. 같은 문자는 싫어!(연속으로 중복된 숫자 제거)
def solution(arr) :
	answer = []

	# 중복제거
	# for value in arr :
	# 	if value not in answer :
	# 		answer.append(value)

	for i in range(len(arr)) :
		if i == 0 :
			answer.append(arr[i])
		elif i != 0 and arr[i - 1] != arr[i] :
			answer.append(arr[i])

	return answer

# 모범답안

print(solution(list(input())))

# 7. 가운데 글자 가져오기

def solution(s) :
	answer = ''
	idx = len(s) / 2
	
	if len(s) % 2 != 0 :
		answer += s[int(idx) : int(idx) + 1]
	else :
		answer = s[int(idx) - 1 : int(idx) + 1]

	return answer

print(solution(input()))

#  8. x만큼 간격이 있는 n개의 숫자

# for
def solution(x, n) :
	answer = []

	for i in range(1, n + 1) :
		answer.append(x * i)

	return answer

# comprehension
def solution(x, n) :
	return [x * i for i in range(1, n + 1)]

x, n = map(int, input().split())
print(solution(x, n))

# 9. 직사각형 별찍기

a, b = map(int, input().strip().split(' '))

# 내 풀이
for _ in range(b) :
	print('*' * a)

# 다른 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*' * a + '\n') * b
print(answer)

# 10. 평균 구하기

# for
def solution(arr) :
	answer = 0

	for i in arr :
		answer += i

	return answer / len(arr)

# method 이용
def solution(arr) :
	return sum(arr) / len(arr)

arr = [1, 2, 3, 4]
print(solution(arr))

# 11. 행렬의 덧셈

# comprehension
def solution(arr1, arr2) :
	return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

# numpy
import numpy as np

def solution(arr1, arr2) :
	answer = np.matrix(arr1) + np.matrix(arr2)
	
	return answer.tolist()

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
print(solution(arr1, arr2))

# 12. 짝수와 홀수

# if
def solution(num) :
	answer = ''

	if num % 2 == 0 :
		answer = 'Even'
	else : 
		answer = 'Odd'

	return answer

# one_line if
def solution(num) :
	return 'Even' if num % 2 == 0 else 'Odd'

print(solution(int(input())))

# 13. 자릿수 더하기

# comprehension
def solution(n) :
	return sum([int(val) for val in str(n)])
	
# comprehension + map method
def solution(n) :
	return sum([val for val in map(int, str(n))])

print(solution(int(input())))


# 14. 최대공약수와 최소공배수

# 유클리드 호제법
# 최대공약수
def gcd(n, m) :
    while (m) :
        n, m = m, n % m
        
    return n

# 최소공배수
def solution(n, m):
    result = (n * m) // gcd(n, m)
    
    return [gcd(n, m), result]
    
n, m = map(int, input().split())
print(solution(n, m))

# 15. 정수 제곱근 판별
import math

# method
def solution(n) :
    answer = math.sqrt(n)

    if answer == int(answer) :
        return int((answer + 1) ** 2)
    else :
        return -1

# one_line method
def solution(n) :
    return int((math.sqrt(n) + 1) ** 2) if math.sqrt(n) == int(math.sqrt(n)) else -1

print(solution(int(input())))