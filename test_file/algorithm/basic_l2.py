# 16. 문자열 다루기 기본

# if
# def solution(s) :
# 	return True if s.isdigit() == True and (len(s) == 4 or len(s) == 6) else False

# print(solution(input()))

# 17. 정수 내림차순으로 배치하기

# for + method
# def solution(n) :
# 	answer = ''
# 	result = []

# 	for val in str(n) :
# 		result.append(val)
# 	result.sort(reverse=True)

# 	for val in result :
# 		answer += val
	
# 	return int(answer)

# method - sort + join
# def solution(s) :
# 	result = list(str(s))
# 	result.sort(reverse=True)

# 	return int("".join(result))

# print(solution(int(input())))

# 18. 자연수 뒤집어 배열로 만들기

# method
# def solution(n) :
# 	temp = list(str(n))
# 	temp.reverse()

# 	return [int(val) for val in temp]

# one_line method
# def solution(n) :
# 	return list(map(int, reversed(str(n))))

# print(solution(int(input())))

# 19. 핸드폰 번호 가리기

# slicing
# def solution(phone_number) :
# 	return '*' * (len(phone_number) - 4) + phone_number[-4:len(phone_number):1]

# 개선
# def solution(phone_number) :
# 	return '*' * (len(phone_number) - 4) + phone_number[-4:]

# print(solution(input()))

# 20. K번째 수

# for
# def solution(array, commands) :
# 	result = []

# 	for start, end, target in commands :
# 		temp = array[start - 1: end]
# 		temp.sort()
# 		result.append(temp[target - 1])

# 	return result

# one_line + method(sorted) / lambda
# def solution(array, commands) :
# 	return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# arr, com = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(arr, com))

# 21. 하샤드 수

# for
# def solution(number) :
# 	result = 0

# 	for i in str(number) :
# 		result += int(i)

# 	return True if number % result == 0 else False

# one_line method
# def solution(number) :
# 	return number % sum([int(num) for num in str(number)]) == 0

# print(solution(int(input())))

# 22. 나누어 떨어지는 숫자 배열

# 조건 나누어 떨어지는게 있는가?
# 1. 모두 나누어 떨어진다 -> 정렬해서 넣는다.
# 2. 한 개는 있다. -> 정렬해서 넣는다.
# 3. 하나도 없다. -> -1를 반환한다.
# def solution(arr, divisor) :
# 	result = []

# 	for val in arr :
# 		if val % divisor == 0 :
# 			result.append(val)
# 			result.sort()
		# elif arr in (val % divisor != 0) :
		# 	return [-1]

	# return result
	# return [val for val in arr if val % divisor == 0]

# arr = [10, 9, 7, 5]
# print(solution(arr, int(input())))

# 23. 모의고사

# 들어오는 데이터는 배열임
# 가장 높은 점수를 받은 사람만 반환
# 생성단계
# 1번놈 -> 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ... -> range(1, 6)를 len(answer)만큼 반복
# 2번놈 -> 2, 1, 2, 3, 2, 4, 2, 5 ... -> 2를 넣고 그 다음 [1, 3, 4, 5]를 len(answer)만큼 반복
# 3번놈 -> 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ... -> [3, 1, 2, 4, 5]를 각각 2번씩 넣는걸 len(answer)만큼 반복
# 로직
# 1. answer 크기 만큼 답안지 생성
# 2. answer == 시험응시자의 답안지 같은지 비교해서 같은 수를 정답에 넣음
# 3. 넣은 정답의 갯수가 많은 사람만 반환
def create(num) :
	one, two, three = [], [], []

	while len(three) < num :
		one.append(list(range(1, 6)))
		# for i in range(1, 6) :
		# 	one.append(i)
		for i in [2, 1, 2, 3, 2, 4, 2, 5] :
			two.append(i)
		for i in [3, 1, 2, 4, 5] :
			three.append(i)

	return [list for list in [one, two, three]]

def solution(answer) :
	winner = []
	create(len(answer))
	# one, two, three = [], [], []

	# for i in answer :
	# 	one.append(i)

	return [range(1, 5) for _ in answer]
	# return winner

answer = [1, 2, 3, 4, 5]
answer1 = [1, 3, 2, 4, 2]
# print(solution(answer1))
print(create(len(answer)))