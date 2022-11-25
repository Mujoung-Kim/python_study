#(1) 다음 점수 구간에 맞게 학점을 출력하세요.
# 91 ~ 100 : A학점
# 81 ~ 90 :  B학점
# 71 ~ 80 :  C학점
# 61 ~ 70 :  D학점
# 60이하   :  F학점
num = int(input('enter_score: '))

if	90 < num <= 100:
	print('1 : A학점')
elif 80 < num <= 90:
	print('1 : B학점')
elif 70 < num <= 80:
	print('1 : C학점')
elif 60 < num <= 70:
	print('1 : D학점')
elif 0 <= num <= 60:
	print('1 : F학점')
else:
	print(f'1 : {num}는 잘못 입력된 점수입니다. 0 ~ 100사이의 점수를 입력하세요.')

# 모범답안
jumsu = int(input('enter_score: '))
result = None

if	jumsu < 0 or jumsu > 100:
	result = f'{jumsu}는 잘못된 점수입니다. 0 ~ 100사이의 점수를 입력하세요.'
elif jumsu > 90:
	result = 'A학점'
elif jumsu > 80:
	result = 'B학점'
elif jumsu > 70:
	result = 'C학점'
elif jumsu > 60:
	result = 'D학점'
else:
	result = 'F학점'
print(f'1at : {result}')

#(2) 사용자로 부터 ID를 입력 받은 뒤 입력받은 ID가 5글자 이상이면 "사용할 수 있습니다."를 5글자 미만이면 "사용할 수 없는 ID입니다."를 출력하세요.
user_id = input('user_id: ')

if	len(user_id) >= 5:
	print('2 : 사용할 수 있습니다.')
elif len(user_id) < 5:
	print('2 : 사용할 수 없는 ID입니다.')

# 모범답안
id = input('enter_id: ')

if	len(id) > 4:
	print(f'2at : {id}는 사용할 수 있습니다.')
else:
	print(f'2at : {id}는 사용할 수 없습니다. 5글자 이상 입력하세요.')

#(3) 사용자로부터 우리나라 도시명을 입력 받은 뒤 입력받은 도시명이 서울이면 "특별시"를 인천,부산,광주,대구,대전,울산 이면 "광역시"를 나머지는 "특별시나 광역시가 아닙니다."를 출력하세요.
city = input('address: ')
if	city == '서울' or city == 'seoul':
	print('3 : 특별시')
elif city == '인천' or city == 'incheon':
	print('3 : 광역시')
elif city == '부산' or city == 'busan':
	print('3 : 광역시')
elif city == '광주' or city == 'gwangju':
	print('3 : 광역시')
elif city == '대구' or city == 'daegu':
	print('3 : 광역시')
elif city == '대전' or city == 'daejeon':
	print('3 : 광역시')
elif city == '울산' or city == 'ulsan':
	print('3 : 광역시')
else:
	print('3 : 특별시나 광역시가 아닙니다.')

# 모범답안
city = input('enter_address: ')
result = None

if	city == '서울' or city == 'seoul':
	result = f'{city}특별시'
elif city in ['인천', '부산', '광주', '대구', '대전', '울산', 'incheon', 'busan', 'gwanju', 'daegu', 'daejeon', 'ulsan']:
	result = f'{city}광역시'
else:
	result = f'{city}는 특별시나 광역시가 아닙니다.'
print(f'3at : {result}')

#(4) 아래 리스트의 평균을 구하시오. (반복문 이용)
jumsu = [100, 90, 100, 80, 70, 100, 80, 90, 95, 85]
result_sum = 0

for val in jumsu:
	result_sum += val
print(f'4 : {result_sum / len(jumsu)}')

# 모범답안
jumsu_sum = 0

for v in jumsu:
	jumsu_sum += v
print(f'4at 합계 : {jumsu_sum}, 평균 : {jumsu_sum / len(jumsu)}')

#(5) 위 jumsu리스트에서 평균점수이상은 pass, 미만은 fail을 index번호와 함께 출력하시오. (ex: 0-pass, 1-pass, 2-fail)
print('5 :', end=' ')
for idx, val in enumerate(jumsu):
	if	val < (result_sum / len(jumsu)):
		print(f'{idx}-fail {val}', end=', ')
	elif val >= (result_sum / len(jumsu)):
		print(f'{idx}-pass {val}', end=', ')
print()

# 모범답안
jumsu_avg = jumsu_sum / len(jumsu)

print('5at :', end=' ')
for idx, value in enumerate(jumsu):
	if	value >= jumsu_avg:
		print(f'{idx} - pass {value}', end=', ')
	else:
		print(f'{idx} - fail {value}', end=', ')
print()

#(6) 아래 리스트 값들 중 최대값을 조회해 출력하시오. (반복문 이용)
jumsu = [60, 90, 80, 80, 70, 55, 80, 90, 95, 85]
maxim = 0
for val in jumsu:
	if	maxim < val:
		maxim = val
print(f'6 : {maxim}')

# 모범답안
max_value = 0

for value in jumsu:
	if	max_value < value:
		max_value = value
print('6at : ', max_value)

# jumsu list안데 70점이 있는지 여부
result = False

for value in jumsu:
	if	value == 70:
		result = True
		break					# 단순이 있는지 여부를 확인하는 것이므로 찾았으면 조회를 멈춘다.
print(result)
print('70점이 있습니다.' if result else '70점이 없습니다.')

# data_structure 연산함수
print(sum(jumsu))				# sum(data_structure)
print(sum(jumsu)/len(jumsu))	# 평균값
print(max(jumsu), min(jumsu))	# max(data_structure), min(data_structure)

#(7) 다음 리스트 중에서 "쥐"와 "토끼" 제외한 나머지를 출력하세요.
str_list = ["쥐", "소", "호랑이", "토끼", "용", "뱀"]
print('7 :', end=' ')
for val in str_list:
	if	val == '쥐':
		continue
	elif val == '토끼':
		continue
	elif val == '뱀':
		print(val)
		break
	print(val, end=', ')

# 모범답안
print('7at :', end=' ')
for v in str_list:
	# if	v != '쥐' and v != '토끼':
	# if v not in ['쥐', '토끼']:
	# 	print(v, end=', ')
	if v in ['쥐', '토끼']:
		continue
	print(v, end=', ')
print()

#(8) 사용자로부터 정수를 입력받아 그 단의 구구단을 출력하시오. (반복문 이용)
# ex) 단을 입력하시오 : 2
# 2 x 1 = 2
# 2 x 2 = 4
#..
# 2 x 9 = 18
num = int(input('int_input: '))
count = 0

while count < 9:
	count += 1
	if	count == 1:
		print(f'8 : {num} * {count} = {num * count}', end=', ')
		continue
	elif	count == 9:
		print(f'{num} * {count} = {num * count}')
		break
	print(f'{num} * {count} = {num * count}', end=', ')

# 모범답안
dan = int(input('단을 입력하세요: '))

print('8at :', end=' ')
for i in range(1, 10):
	if	i == 9:
		print(f'{dan} * {i} = {dan * i}')
		break
	print(f'{dan} * {i} = {dan * i}', end=', ')

#컴프리헨션
#(9) 다음 리스트가 가진 값에 두배(* 2)를 가지는 새로운 리스트를 만드시오. (리스트 컴프리헨션 이용)
lst = [10, 30, 70, 5, 120, 700, 1, 35]
result_list = [val * 2 for val in lst]
print(f'9 : {result_list}')

# 모범답안
result = [v * 2 for v in lst]
print(f'9at : {result}')

#(10) 다음 리스트가 가진 값에 10배의 값을 가지는 값을 (원래값, 10배값) 의 튜플 묶음으로 가지는 리스트를 만드시오. (리스트 컴프리헨션 이용)
# Ex) [(10,100), (30,300), .., (35, 350)]
lst = [10, 30, 70, 5, 5, 120, 700, 1, 35, 35]
result_list = [(val, val * 10) for val in lst]
print(f'10 : {result_list}')

# 모범답안
result = [(v, v * 10) for v in lst]
print(f'10at : {result}')

# index와 함께 뽑아서 입력
reuslt2 = [(i, v) for i, v in enumerate(lst) if i % 2 == 0]
print(reuslt2)

#(11) 다음 리스트가 가진 값들 중 3의 배수만 가지는 리스트를 만드시오. (리스트 컴프리헨션 이용)
lst2 = [ 3, 20, 33, 21, 33, 8, 11, 10, 7, 17, 60, 120, 2]
result_list = [val for val in lst2 if val % 3 == 0]
print(f'11 : {result_list}')

# 모범답안
result = [v for v in lst2 if v % 3 == 0]
print(f'11at : {result}')

#(12) 다음 파일이름들을 담은 리스트에서 확장자가 exe인 파일만 골라서 새로운 리스트에 담으시오. (string의 endswith()함수 이용)
file_name=["test.txt", "a.exe", "jupyter.bat", "function.exe", "b.exe", "cat.jpg", "dog.png", "run.exe", "i.dll"]
result_list = []

for val in file_name:
	if	val.endswith('.exe'):
		result_list.append(val)
print(f'12 : {result_list}')

# 모범답안
result = [fn for fn in file_name if fn.endswith('.exe')]
print(f'12at : {result}')

#(13) 다음 중 10글자 이상인 파일명(확장자포함)만 가지는 리스트를 만드시오. (mapping)
file_name=["mystroy.txt", "a.exe", "jupyter.bat", "function.exe", "b.exe", "cat.jpg", "dog.png", "run.exe", "i.dll"]
result_list = [val for val in file_name if len(val) >= 10]
print(f'13 : {result_list}')

# 모범답안
result = [fn for fn in file_name if len(fn) > 9]
print(f'13at : {result}')

# 글자수까지 포함하여 dictionary로 생성
result2 = [{fn : len(fn)} for fn in file_name if len(fn) > 9]
print(result2)

#(14) 다음 리스트에서 소문자만 가지는 새로운 리스트를 만드시오. (mapping)
str_list = ["A", "B", "c", "D", "E", "F", "g", "h", "I", "J", "k"]
result_list = []
for val in str_list:
	if	val == 'c':
		result_list.append(val)
	elif val == 'g':
		result_list.append(val)
	elif val == 'h':
		result_list.append(val)
	elif val == 'k':
		result_list.append(val)
print(f'14 : {result_list}')

# 모범답안
result = [v for v in str_list if v.islower()]
print(f'14at : {result}')

# str 대소문자 함수
print('A'.islower())		# 소문자
print('aAaaaa'.islower())
print('AAA'.isupper())		# 대문자
print('aaaa'.isupper())

# 모두 대문자로 변환 함수
result = [v.upper() for v in str_list]
print(result)
result = [v.lower() for v in str_list]
print(result)