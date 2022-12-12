import os
import csv

unique = 1		# 파일 덮어쓰기 방지

# 중복된 파일이 있을 경우
def file_unqiue(target, name) :
	global unique
	
	while os.path.exists(target + f'{name}.jpg') : 
		result = target + f'{name}({unique}).jpg'
		unique += 1
		
		return result

# 파일 이동
# TODO 파일 읽기 -> 파일 쓰기 -> 원본 삭제
# TODO .jpg 파일만 이동되는데 image_file, text_file 둘 다 가능하도록 exception 처리 -> file_ext
def file_move(src, name) :
	with open(src, 'rb') as fr :
		target = './test_file/data/image/'
		with open(target + f'{name}.jpg', 'wb') as fw :
			data = fr.read()
			fw.write(data)

# 파일 복사
# TODO .jpg 파일만 이동되는데 image_file, text_file 둘 다 가능하도록 exception 처리 -> file_ext
def file_copy(src, name) :
	with open(src, 'rb') as fr :
		target = './test_file/data/image/'
		result = file_unqiue(target, name)
		if result == None :
			with open(target + f'{name}.jpg', 'wb') as fw :
				data = fr.read()
				fw.write(data)
		else :
			print(result)
			with open(result, 'wb') as fw :
				data = fr.read()
				fw.write(data)

# test_area
if __name__ == '__main__' :
	print(__name__)
	file_name = str(input('sech_file : '))
	path = f'C:/Users/user/Downloads/{file_name}.jpg'
	file_copy(path, file_name)
	print(unique)
	# file_move(path, file_name)