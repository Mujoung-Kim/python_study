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

def solution(phone_number) :
	result = list(phone_number)[-1:-4]

	return result

print(solution(input()))