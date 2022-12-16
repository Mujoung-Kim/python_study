# 1. 두 정수 사이의 합
# for문
# def solution(a, b) :
# 	answer = 0
	
# 	if a <= b :
# 		for i in range(a, b + 1) :
# 			answer += i
# 	else :
# 		for i in range(b, a + 1) :
# 			answer += i
	
# 	return answer

# method 활용
# def solution(a, b) :
# 	if a > b :
# 		a, b = b, a

# 	return sum(range(a, b + 1))

# a, b = map(int, input().split())
# print(solution(a, b))

# 2. 수박수박수박...
# def solution(n):
# 	answer = ''
	
# 	if n % 2 != 0:
# 		for i in range(1, n + 1) :
# 			if i % 2 == 0 :
# 				answer += '박'
# 			else :
# 				answer += '수'
# 	else :
# 		for i in range(1, n + 1) :
# 			if i % 2 != 0 :
# 				answer += '수'
# 			else :
# 				answer += '박'
		
# 	return answer

# 모범답안
# def solution(n) :
# 	answer = '수박' * n

# 	return answer[:n]

# print(solution(int(input())))

# 3. 서울에서 김서방 찾기
# list를 이용한 풀이
# def solution(seoul):
# 	result = [idx for idx in range(len(seoul)) if 'Kim' in seoul[idx]]
# 	answer = f'김서방은 {result}에 있다'
	
# 	return answer

# 모범 답안
# def solution(seoul):
# 	answer = f'김서방은 {seoul.index("Kim")}에 있다'
	
# 	return answer

# print(solution(['Jane', 'Kim']))

# 4. 약수의 합
# def solution(n) :
# 	answer = 0

# 	for i in range(1, n + 1) :
# 		if n % i == 0:
# 			answer += i

# 	return answer

# print(solution(int(input())))

# 5. 문자열 내 p와 y의 개수는?
# def solution(s) :
# 	answer = False

# 	if s.upper().count('P') == s.upper().count('Y') : answer = True

# 	return answer

# 모범답안
# def solution(s) :
# 	return s.upper().count('P') == s.upper().count('Y')

# print(solution(input()))

# 6. 같은 문자는 싫어!(연속으로 중복된 숫자 제거)
# def solution(arr) :
# 	answer = []

# 	# 중복제거
# 	# for value in arr :
# 	# 	if value not in answer :
# 	# 		answer.append(value)

# 	for i in range(len(arr)) :
# 		if i == 0 :
# 			answer.append(arr[i])
# 		elif i != 0 and arr[i - 1] != arr[i] :
# 			answer.append(arr[i])

# 	return answer

# 모범답안

# print(solution(list(input())))

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