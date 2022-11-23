# txt = 0

# while txt < 5:
# 	print('==' * 20)
# 	print('1.Info')
# 	print('2.Study')
# 	print('3.Game')
# 	print('4.Config')
# 	print('5.Exit')
# 	print('==' * 20)
# 	txt = int(input('int_type: '))
# 	if	txt == 1:
# 		print(f'input_data: {txt}')
# 	elif txt == 2:
# 		print(f'input_data: {txt}')
# 	elif txt == 3:
# 		print(f'input_data: {txt}')
# 	elif txt == 4:
# 		print(f'input_data: {txt}')
# print('end')

while True:
	print('=' * 20)
	print('1.Infomation')
	print('2.Study')
	print('3.Exam')
	print('4.Config')
	print('5.Exit')
	print('=' * 20)

	text = int(input('select menu : '))
	if	text == 1:
		print(f'selected {text}')
	elif text == 2:
		print(f'selected {text}')
	elif text == 3:
		print(f'selected {text}')
	elif text == 4:
		print(f'selected {text}')
	elif text == 5:
		break
print('end')