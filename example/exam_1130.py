# TODO - 간단한 메모장
# 사용자로부터 파일명을 입력받는다.
# 사용자로 부터 파일에 저장할 문장을 입력받아서 파일에 저장한다.
# 사용자가 !q 를 입력하면 종료한다.
# 사용자가 저장한 파일을 읽어서 출력한다.
import os
file_name = input('flie_name : ')
path = f'./example/{file_name}.txt'

# 쓰기
with open(path, 'wt', encoding='utf-8') as file:	
	try :
		text = input('text : ')

		while (text not in '!q') :
			file.write(f'{text}\n')
			text = input('text : ')
	except Exception as e: 
		print(e, 'error')

# 읽기
with open(path, 'rt', encoding='utf-8') as file:
	try :
		for line, txt in enumerate(file.readlines(), start=1):
			print(f'{line}. {txt}', end='')
	except Exception as e:
		print(e, 'error')

# 모범 답안 -> directory까지 자동생성
print('파일명을 입력하세요.')
filename = input()

# os.mkdir()						# directory를 생성
# os.makedirs()						# directory를 생성 -> 상위 directory까지 생성
save_dir = 'text'
os.makedirs(save_dir, exist_ok=True)	# exist_ok -> True면 있으면 생성 없으면 생성하지 않음 default=False
file_path = f'{save_dir}/{filename}'
print(f'저장경로 : {file_path}')

with open(file_path, 'wt', encoding='utf-8') as fw:
	print('저장할 내용을 입력하세요.')
	print('=' * 30)
	
	try : 
		while True:
			line_txt = input()
			if line_txt == '!q':
				break
			fw.write(f'{line_txt}\n')
	except Exception as e:
		print(e, '오류 발생')

with open(file_path, encoding='utf-8') as fr:
	try :
		for line, txt in enumerate(fr.readlines(), start=1):
			print(f'{line}. {txt}', end='')
	except Exception as e:
		print(e, '오류 발생')