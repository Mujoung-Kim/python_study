print("hello word")
    # tab: 자동완성
100 + 200

a = 10
b = 20
c = a + b
print(c)

# 변수
name = 'sancho'
age = 25
print(name) # 변수의 값을 사용(조회) => 변수이름을 값(사용함) 자리에 넣는다.
print(age)

# 값을 변경
print(name)
name = 'ronaldo'
print(name)
age = age + 20
print(age)
age += 20
print(age)

num1 = num2 = num3 = 10
a, b, c = 10, 20, 'hi'
print(num1, num2, num3)
print(a, b, c)

# 변수를 메모리에서 제거(삭제)
# del 변수명
del a   # 변수 a를 삭제
# print(a)

age = 20.8
print(type(age))   # 값의 데이터타입을 반환하는 함수

# type error 방지하는 법
if type(age) != str:
    print(age + 10)
    
# 논리연산자 - and (&)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# 논리연산자 - or (|)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# 논리연산자 - not (단항 연산자)
print(not True)
print(not False)

age = 20
print(not age > 10)

# 삼항연산자
num = 10
print("양수" if num >= 0 else "음수")

# 문자열
name = 'sancho'
address = "seoul"
print(name)
print(address)

# txt와 txt2는 같은 방법
txt = "파이썬은 컴퓨터 언어입니다.\n파이썬은 귀도 반 로섬이란 네덜란드 프로그래머가\n1991년에 만들었습니다."
txt2 = '''파이썬은 컴퓨터 언어입니다.
파이썬은 귀도 반 로섬이란 네덜란드 프로그래머가
1991년에 만들었습니다.'''
print(txt)

path = "c:\\text\\back\\n.txt"
path = r"c:\text\back\n.txt"    # r-string (row) => escape 문자 사용안할 때
print(path)

# "abc"def"
'abc"def'
"abd\"def"

# 'abc'def'
'abc\'def'

# 문자열 연산
# + : 합치기(붙이기)
name = 'sancho'
print('name: ' + name)  # 데이터 타입별로 연산
age = 20
print('age: ' + str(age))   # 숫자를 문자열로 변경하여 합치기 연산처리

# 문자열 * 정수 => 문자열을 정수배 만큼 합친다.
a = '*+' * 50
print(a)
print('hello\n'*10)

# 문자열1 in 문자열2 : 문자열2가 문자열1을 포함하는지 => 결과 : bool
# 문자열1 not in 문자열2 : 문자열2가 문자열1을 포함하지 않는지 => 결과 : bool
address = '서울시 동작구 신대방동'
print('동작구' in address)  # address 문자열안에 '동작구'가 있는지 확인
print('종로구' in address)

print('동작구' not in address)  # address 문자열안에 '동작구'가 없는지 확인
print('종로구' not in address)

# 문자열 길이 확인 - len(문자열)
print(len(address))
print(len('123456'))

# 회원가입시 id는 10글자 이상이어야 한다.
id = 'aaaaaa'
print('적당한 id' if len(id) >= 10 else '글자 수 부족한 id')

# 문자열 indexing 문자열의 index는 양수값, 음수값이 존재한다.
s = '0123456789'
print(s)
print(s[0])     # 첫 번째 글자 조회
print(s[3])     # 네 번째 글자 조회
print(s[-1])    # 뒤에서 첫 번째 글자 조회
print(s[-5])    # 뒤에서 다섯 번째 글자 조회
# print(s[100]) 없는 index의 글자 조회 시 index error 발생

# 문자열 slicling
# s[ start index : end index : 간격] 간격(defalut = 1)은 생략 가능
print(s[2:5])   # end index는 포함이 안되니 이점 유의할 것
print(s[2:])    # 2 ~ 끝까지. end index 생략
print(s[:5])    # 0 ~ 4. start idnex 생략
print(s[1:8:2]) # 1 ~ 7 , 간격2
print(s[1:8:3]) # 1 ~ 7 , 간격3

# start index > end index, 간격을 음수 => reverse
print(s[8:1:-1])
print(s[8:1:-2])
print(s[:])     # string 전부 호출
print(s[::-1])  # reverse
print(s[-5:-3]) # 뒤에서 5번째 ~ 뒤에서 2번째
print(s[5:7])
print(s[-5:7])

# 문자열 formatting -> 포맷을 하나 만들어서 여러 개의 데이터를 입력할 때
name1, age1, address1 = 'sancho', 20, 'seoul'
name2, age2, address2 = 'ronaldo', 30, 'busan'

# name: {}, age: {}, address: {}
layout = 'name: {}, age: {}, address: {}'   # 나중에 들어갈 부분을 {}로 표시
info1 = layout.format(name1, age1, address1)
info2 = layout.format(name2, age2, address2)
print(info1)
print(info2)

# 문자열 f formatting -> 주로 하나의 format을 만들 때 / python 3.6부터 이용가능
info3 = f'name: {name}, age: {age}, address: {address}'
print(info3)

# 형식문자를 이용한 format
tall = 182.6
info4 = 'name: %s, age: %d, address: %s, tall: %.2f' %(name, age, address1, tall)
print(info4)

# 221122 format
# 논리연산자 and(&), or(|), not, xor((True)^(False)) -> 비트와이즈 연산을 할 때는 묶어서
info2 = "name: {name}, age: {age}".format(name='ronaldo', age=20)
print(info2)
info2 = 'name: {0}, age: {1}, name: {0}'.format(name1, age1)
print(info2)

# 파이썬의 모든 데이터는 객체
v = "   abc     "
print(v)

# 문자열 v의 좌우 공백을 제거
r = v.strip()
print(r)
print(len(v), len(r))

v = 'asdfasdfaweghaetjaweraqwh aegsd'

# a가 몇 개 있는지 확인하는 메소드
r = v.count('a')

# we가 몇 개 있는지 확인하는 메소드
r = v.count('we')
print(r)
v = 'computer monitor mouse headphone keybord'
v = 'computer,monitor,mouse,headphone,keybored'

# 특정 문자(열)을 기준으로 문자열을 나누기 (token화)
r = v.split()      # 나누는 기준 문자열의 default = 공백
r = v.split(',')
print(r)
print(r[0])

v = 'www.naver.com'

# v가 https로 시작하는지 확인하는 메소드
r = v.startswith('https')
r = v.startswith('www')
print(r)

# v가 com으로 끝나는지 확인하는 메소드
r = v.endswith('com')
r = v.endswith('co.kr')
print(r)

# 중간에 있는 문자 확인할 때는 in 연산자 사용
# str.index(str, int) => str = 찾는 문자열, int = 검색을 시작할 주소
# index()와 find()의 차이 찾는 값이 없을 때 index()는 error를 return하고, find()는 -1을 return 한다
print(v.index('w'))
print(v.index('w', 2))  # 2번 index부터 찾는다.

# 다른 타입 -> 문자열: str(value)
a = 20
print(type(a))
r = str(a)
print(type(r))

# 다른 타입 -> 정수형: int(value)
a = 36.73
r = int(a)
print(r)
a2 = '326'
r2 = int(a2)    # 정수형의 문자열만 변환가능
print(type(r2), type(a2))

# 다른 타입 -> 실수형: float(value)
a = 200
r = float(a)
print(type(r), r)
a2 = '327.32'
r2 = float(a2)
print(type(r2), r2)

# 다른 타입 -> 논리형: bool(value)
print(bool(10), bool(-10), bool(0))
print(bool('abc'), bool(' '), bool())
print(bool(None))

# user로부터 문자열을 입력받아서 반환해주는 함수
# input(value) : value를 입력하면 label을 입력가능
input()
v = input("int:")   # label 입력
print(v)

# 숫자 두 개를 받아서 더하기
n1 = input('int:')
num1 = float(n1)
n2 = input('int:')
num2 = float(n2)
result = num1 + num2
print(f"result: {result}")