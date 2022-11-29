import multiplelication_table as mt

# TODO Exception
while True:
	print('=' * 149)
	print('1.Infomation')
	print('2.Study')
	print('3.Exam')
	print('4.Config')
	print('5.Exit')
	print('=' * 149)

	try :
		select_num = int(input('select menu : '))
		if	select_num == 1:
			print(f'selected {select_num}')

		elif select_num == 2:
			print(f'selected {select_num}')
			text = input('enter multiplelication: ')
			
			try :
				num = int(text)

				if isinstance(num, int):
					print('=' * 149)
					mt.MultiplelicationTable(num).show_table()
					
			except ValueError:
				print('=' * 149)
				print('please enter to integer_type!')
		
		elif select_num == 3:
			print(f'selected {select_num}')
		
		elif select_num == 4:
			print(f'selected {select_num}')
		
		elif select_num == 5:
			break
	except ValueError:
		print('please enter to menu number!!!')

print('system end!')