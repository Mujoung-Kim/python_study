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

def solution(n) :
	result = []

	for val in str(n) :
		result.append(val)
	result.sort(reverse=True)

	return list(map(int, result))

print(solution(int(input())))