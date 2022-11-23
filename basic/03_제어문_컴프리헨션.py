# 조건문(분기문)
num = input('int_type: ')	# 입력결과는 string 타입

# num = 0 이라면 '영입니다.'를 출력한다.
if	num == '0':
	print('num is zero')
	print(f'num * 100 is zero: {int(num) * 100}')
print('end')

# 입력받은 text가 한 글자 이상이면 '한 글자 이상입니다.'를 출력
# 빈 문자열일 경우 '한 글자 이상을 입력하세요.'를 출력
text = input('str_type: ')
if	text:					# len(text) >= 1과 같은 조건
	print('한 글자 이상입니다.')
	print(f'입력한 글자는: {text}이고, 글자수는 {len(text)}입니다.')
else:
	print('한 글자 이상을 입력하세요.')
print('종료')

# 입력받은 값이 0이면 '0입니다.' 출력하고
# 양수이면 '양수입니다.'를 출력하고
# 음수이면 '음수입니다.'를 출력한다.
# 조건이 여러 개인 경우
n = float(input('float_type: '))
if	n > 0.0:
	print('양수입니다.')
	print(f'양수입니다. 입력한 숫자: {n}')
elif	n < 0.0:
	print('음수입니다.')
	print(f'음수입니다. 입력한 숫자: {n}')
else:
	print('0입니다.')
print('end')

# if문을 사용할 때 좋지 않은 예시
n = float(input('float_type: '))
if	n > 0.0:
	print('양수입니다.')
	print(f'양수입니다. 입력한 숫자: {n}')
if	n < 0.0:
	print('음수입니다.')
	print(f'음수입니다. 입력한 숫자: {n}')
if	n == 0.0:
	print('0입니다.')
print('end')

# while문
limit = int(input('반복할 횟수: '))	
count = 0							# 현재 몇 번째 반복인지 저장할 변수

# count가 limit보다 적은 동안 count값을 1증가 시키고 출력한다.
# count가 even이면 출력
while	count < limit:
	count += 1
	if	count % 2 == 0:
		print(f'count: {count}')

# = -> 대입연산자 변수 = 값
# 복합대입연산자 : 변수 연산자 = 값 -> 변수와 값을 연산자로 연산한 결과를 다시 그 변수에 대입
a = 0
a = a + 20							# 복합대입연산자

# for in문
l = [10, 20, 30, 40, 50]

# list l의 원소들에 5를 더한 값을 출력
for elem in l:
	print(elem + 5)

# tuple
for elem in (1, 2, 3, 4, 5):
	print(elem)

# set
for elem in {10, 20, 30, 40, 50}:
	print(elem)

# 문자열 -> 한 글자씩 반환
for char in '가나다라1234abcd=+/':
	print(char, end='\t')
print()

# dictionary
dict = {'name' : 'sancho', 'age' : 20, 'address' : 'seoul'}
for key in dict:					# key값만 출력
	if	key == 'age':
		print(key, dict[key] + 20)
	else:
		print(key, dict[key])

# value만 필요한 경우
for value in dict.values():
	print(value, end='\t')
print()

# items에서 뽑아온 값들을 출력
for a, b in dict.items():
	print(value)
	a, b = value
	print(a, b)
	print('=' * 20)

print(10, end='\t')					# end='끝맺음' -> 끝맺음 설정
print()
print(10, 20, 30, 40)				# 공백을 구분자로 나열해서 출력
print(10, 20, 30, 40, sep=',')		# sep='구분자' -> 구분자를 설정

# 중첩 list의 값들을 하나씩 가져옴
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for v1, v2, v3 in a:
	print(v1, v2, v3)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list의 값들 중 3의 배수만 출력
for value in l:
	if value % 3 != 0:
		continue					# value가 3의 배수가 아니면 다음 원소를 반복해라.(출력하지 않고)
	print(value)

l = [1, 56, 2, 3, 100, 30, 40, 10, -20, -3]

# list의 값들을 출력한다.
# 단 원소의 값이 100일 경우 더 이상 실행하지 않는다.
for value in l:
	print(value, end='\t')
	if	value == 100:
		break
print()

# 사용자로부터 글을 입력받아서 출력
# 만약에 사용자가 '!q'를 입력하면 종료
while True:
	txt = input('string_type: ')
	if	txt == '!q':
		break
	print(txt)
print('end')

# 중첩 list를 1, 2, 3, 10, 20, 30, 100, 200, 300으로 출력
l = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for val in l:
	for value in val:
		if	value == 300:
			print(value)
			break
		print(value, end=', ')

# 1, 2, 3
# 10, 20, 30
# 100, 200, 300
for val in l:
	for value in val:
		print(value, end=', ')
	print()

# 만약에 원소가 20이면 그만 출력한다.
# 중첩 반복문에서 안쪽의 반복문안에서 break할 때 전체 반복을 멈추려는 경우
is_finsih = False					# 전체 반복문을 멈출지 여부
for val in l:
	for elem in val:
		if	elem == 20:
			is_finsih = True
			print(elem)
			break
		print(elem, end=', ')
	if	is_finsih == True:
		break

# 3중첩 list
l = [[[1, 2, 3], [10, 20, 30], [100, 200, 300]], [[4, 5, 6], [40, 50, 60], [400, 500, 600]]]

for val in l:
	for value in val:
		for	elem in value:
			if	elem == 600:
				print(elem)
				break
			print(elem, end=', ')

# range(argument)
for val in range(5):				# end_value만 입력
	print(val, end='\t')
print()

for val in range(5, 9):				# start_value, end_value 입력
	print(val, end='\t')
print()

for val in range(1, 7, 2):			# start_value, end_value, step 입력
	print(val, end='\t')
print()

for val in range(10, -10, -2):		# reverse
	print(val, end='\t')
# print()

# 'hello'을 5번 출력
for _ in range(5):					# 관례적으로 사용하지 않는 변수명은 _으로 한다.
	print('hello')

# range를 활용하여 data_structure 생성 -> data_structure의 경우 메모리에 미리 할당하고 있지만
#                                        range를 사용하면 필요할 때 해당 데이터를 가져온다.
list(range(1, 11))
tuple(range(1, 11))
set(range(1, 11))

# enumerate(argemuent)
l = ['apple', 'banana', 'watermelon']

for idx, value in enumerate(l, start=100):
    print(idx, value, sep=' - ')

for idx, value in enumerate(range(100000)):
    if  idx % 10000 == 0:
        print(f'{idx}. 기록한다')

# 같은 index의 값들이 한 사람의 정보
# 한 사람의 정보를 한 줄에 출력
names = ['sancho', 'ronaldo', 'de-gea']
ages = [25, 38, 30]
addresses = ['Seoul', 'Busan', 'Incheon']
emails = ['sancho@manchester.com', 'ronaldo@manchester.com', 'de-gea@manchester.com', 'burno@manchester.com']

for val in zip(names, ages, addresses):
    print(val)

# 각각의 값별로 처리할 때 -> 각 data_structure의 원소 개수가 다를 경우 적은 것에 맞춘다.
for name, age, address, email in zip(names, ages, addresses, emails):
    print(name, age, address, email)

# comprehension
li = [10, 5, 7, 20, 35, 6, 20, 100, 100, 7]

# list의 element들을 5배한 값들을 가지는 새로운 list를 생성
result = []                 # 결과를 담을 list
for val in li:
    result.append(val * 5)
print(result)

# list comprehension
resutl_list = [val * 5 for val in li]     # 결과가 list가 된다.

# set comprehension
result_set = {val * 5 for val in li}     # 결과가 set이 된다.

# dictionary comprehension
result_dict = {f'reuslt{idx}': val * 5 for idx, val in li}     # 결과가 dictionary가 된다.

result_dict = {}
for idx, val in enumerate(li):
    # print('result' + str(idx))
    result_dict['result' + str(idx)] = val * 5
print(result_dict)

# list의 값들 중 even만 가지는 새로운 list 생성
result = []
for val in li:
    if  val % 2 == 0:
        result.append(val)
print(li)
print(result)

[val for val in li if val % 2 == 0]             # list의 값들 중 even만 가지는 list comprehension -> filltering(특정조건의 값을 조회)
[val * 10 for val in li if val % 2 == 0]        # mapping(모든 element들을 일괄적으로 처리)

list = [[1, 2, 3], [4, 5], [6, 7, 8]]
result = []
for val in list:
    for v in val:
        result.append(v * 10)
print(result)

# 위의 구문을 comprehension으로 변환
result_list = [v * 10 for val in list for v in val if v % 2 == 0]   # 너무 복잡한 comprehension이 되면 가독성이 떨어지므로 for문으로 작성
print(result_list)

# l3의 문자열들 중 세 글자 이상인 것들만 모아서 리스트에 저장
l3 = ['a', 'b', 'abc', 'asdasd', 'asdasdasdas', 'aaaa', 'ss']
result_l3 = [val.upper() for val in l3 if len(val) >= 3]
print(l3)
print(result_l3)

result_l3 = {val:len(val) for val in l3}
print(result_l3)