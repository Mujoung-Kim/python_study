# 입력받은 값만큼 구구단 표를 생성
num = int(input('enter_multiplelication: '))

# if	num == 1:
# 	for i in range(1, 10):
# 		if	i == 9:
# 			print(f'{num} * {i} = {num * i}')
# 			break
# 		print(f'{num} * {i} = {num * i}', end='\t')
# elif num >= 9:
# 	for i in range(1, num + 1):
# 		for j in range(1, num + 1):
# 			if	j == num:
# 				print(f'{i} * {j} = {i * j}')
# 				break
# 			print(f'{i} * {j} = {i * j}', end='\t')
# elif num < 0:
# 	print('양수를 입력해주세요.')
# else:
# 	for i in range(1, num + 1):
# 		for j in range(1, 10):
# 			if	j == 9:
# 				print(f'{i} * {j} = {i * j}')
# 				break
# 			print(f'{i} * {j} = {i * j}', end='\t')

# 함수화
# 예외처리 필요
# 음수일 경우 양수를 다시 입력
# 문자열이 입력되면 다시 입력
def multiplelication(num):
	if	num == 1:
		for i in range(1, 10):
			if	i == 9:
				print(f'{num} * {i} = {num * i}')
				break
			print(f'{num} * {i} = {num * i}', end='\t')
	elif num >= 9:
		for i in range(1, num + 1):
			for j in range(1, num + 1):
				if	j == num:
					print(f'{i} * {j} = {i * j}')
					break
				print(f'{i} * {j} = {i * j}', end='\t')
	elif num < 0:
		print('양수를 입력해주세요.')
	else:
		for i in range(1, num + 1):
			for j in range(1, 10):
				if	j == 9:
					print(f'{i} * {j} = {i * j}')
					break
				print(f'{i} * {j} = {i * j}', end='\t')

multiplelication(num)