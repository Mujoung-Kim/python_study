# 입력받은 값만큼 구구단 표를 생성

# if절 다듬어서 한 번에 처리하도록 설정필요. -> code 간소화 필요?
# def multiplelication(num):
# 	if isinstance(num, int):
# 		if	num == 1:
# 			for i in range(1, 10):
# 				if	i == 9:
# 					print(f'{num} * {i} = {num * i}')
# 					break
# 				print(f'{num} * {i} = {num * i}', end='\t')
# 		elif num >= 9:
# 			for i in range(1, num + 1):
# 				for j in range(1, num + 1):
# 					if	j == num:
# 						print(f'{i} * {j} = {i * j}')
# 						break
# 					print(f'{i} * {j} = {i * j}', end='\t')
# 		elif num == -1:
# 			for i in range(1, 10):
# 				if	i == 9:
# 					print(f'{num} * {i} = {num * i}')
# 					break
# 				print(f'{num} * {i} = {num * i}')
# 		elif -9 < num < 0:
# 			for i in range(1, -num + 1):
# 				for j in range(1, 10):
# 					if	j == 9:
# 						print(f'{-i} * {j} = {-i * j}')
# 						break
# 					print(f'{-i} * {j} = {-i * j}', end='\t')
# 		elif num <= -9:
# 			for i in range(1, -num + 1):
# 				for j in range(1, -num + 1):
# 					if	j == num:
# 						print(f'{-i} * {j} = {-i * j}')
# 						break
# 					print(f'{-i} * {j} = {-i * j}', end='\t')
# 		else:
# 			for i in range(1, num + 1):
# 				for j in range(1, 10):
# 					if	j == 9:
# 						print(f'{i} * {j} = {i * j}')
# 						break
# 					print(f'{i} * {j} = {i * j}', end='\t')
# 	elif isinstance(num, float):
# 		print('please enter to integer_type.')
# 	else:
# 		print('please enter to integer_type')

# 객체화
class MultiplelicationTable():
	def __init__(self, num) -> None:
		self.num = num

	def show_table(self):
		if self.num > 0:
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
		elif self.num < 0:
			if	self.num == -1:
				for idx in range(1, 10):
					print(f'{self.num} * {idx} = {self.num * idx}')
			elif self.num <= -9:
				for	idx in range(1, -self.num + 1):
					for i in range(1, -self.num + 1):
						if	i == self.num:
							print(f'{-idx} * {i} = {-idx * i}')
							break
						print(f'{-idx} * {i} = {-idx * i}', end='\t')
			else:
				for i in range(1, -self.num + 1):
					for j in range(1, 10):
						if	j == 9:
							print(f'{-i} * {j} = {-i * j}')
							break
						print(f'{-i} * {j} = {-i * j}', end='\t')