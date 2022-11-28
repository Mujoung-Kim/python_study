import multiplelication_table as mt

while True:
	print('=' * 149)
	print('1.Infomation')
	print('2.Study')
	print('3.Exam')
	print('4.Config')
	print('5.Exit')
	print('=' * 149)

	select_num = int(input('select menu : '))
	if	select_num == 1:
		print(f'selected {select_num}')
	elif select_num == 2:
		print(f'selected {select_num}')
		num = int(input('enter multiplelication: '))
		if isinstance(num, int):
			print('=' * 149)
			mt.MultiplelicationTable(num).show_table()
		else:
			raise TypeError('enter integer type!!')
	elif select_num == 3:
		print(f'selected {select_num}')
	elif select_num == 4:
		print(f'selected {select_num}')
	elif select_num == 5:
		break
print('system end!')