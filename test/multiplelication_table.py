# 입력받은 값만큼 구구단 표를 생성

# TODO exception 정의 + module화
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
	# elif num == -1:
	# 	for i in range(-10, 0):
	# 		if	i == 9:
	# 			print(f'{num} * {i} = {num * i}')
	# 			break
	else:
		for i in range(1, num + 1):
			for j in range(1, 10):
				if	j == 9:
					print(f'{i} * {j} = {i * j}')
					break
				print(f'{i} * {j} = {i * j}', end='\t')

# 객체화
class MultiplelicationTable():
	def __init__(self, num) -> None:
		self.num = num

	def show_table(self):
		if	self.num == 1:
			for idx in range(1, 10):
				print(f'{self.num} * {idx} = {self.num * idx}')
		elif self.num >= 9:
			for	idx in range(1, self.num + 1):
				for i in range(1, self.num + 1):
					if	i == self.num:
						print(f'{idx} * {i} = {idx * i}')
						break
					print(f'{idx} * {i} = {idx * i}', end='\t')
		else:
			for i in range(1, self.num + 1):
				for j in range(1, 10):
					if	j == 9:
						print(f'{i} * {j} = {i * j}')
						break
					print(f'{i} * {j} = {i * j}', end='\t')

# multiplelication(-1)