import multiplelication_table as mt
import friend_meet as fm
import file_copy_io as fc

# TODO Exception
while True:
	print('=' * 149)
	print('1.Infomation')
	print('2.multiplelication')
	print('3.friend_meet')
	print('4.file_copy & move')
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

			time = int(input('meet_time : '))
			fm.meet_friend(time)
		
		elif select_num == 4:
			file_name = input('file_name : ')
			path = f'C:/Users/user/Downloads/{file_name}.jpg'

			fc.file_copy(path, file_name)
		
		elif select_num == 5:
			break
	except ValueError:
		print('please enter to menu number!!!')

print('system end!')