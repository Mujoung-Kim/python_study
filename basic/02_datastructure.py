# 생성
l1 = [10, 20, 30, 40, 50]
l2 = [10, 20.76, 'hello', True]
l3 = [10, ['a', 'b', 'c'], [1, 2, 3, 4]]    # List(자료구조)도 하나의 value
print(l1)
print(type(l1))

# value 조회
# indexing(하나의 원소), slicing(범위로 조회)
# indexing
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[0], l[4])
print(l[-1], l[-3])

# value 변경
print(l)
l[0] = 100

# 마지막 index의 value를 9000 으로 변경
l[-1] = 9000
print(l)

# slicing
print(l[2:6])                   # 2 ~ 5 step = 1
print(l[1:9:3])                 # 1 ~ 8 step = 3
print(l[:5])                    # start ~ 4 step = 1
print(l[4:])                    # 4 ~ end step = 1
print(l[1::3])                  # 4 ~ end step = 3
print(l[5:1:-1])                # reverse
print(l[::-1])                  # reverse

# slicling을 이용한 value 변경
print(l)
l[1:4] = [200, 300, 400]        # 1 ~ 3 index의 value를 200, 300, 400으로 변경
l[1:4] = [10, 20, 30, 40, 50]   # 1 ~ 3 index부터 value를 10, 20, 30, 40, 50으로 추가해서 변경

# list 연산자
l1 = [1, 2, 3]
l2 = [100, 200, 300, 400]
result = l1 + l2                # list + list
result = l1 * 30                # list * int => list를 입력한 int만큼 더한다.
print(result)
print(l1)
print(l2)

# value (not) in list => value가 list안에 원소로 있는지 확인
result = 1 in l1 
result = 100 in l1 
result = 100 not in l1 
result = [1, 2] in l1 
print(result)

# 중첩 list
l3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
len(l3)
l3[0][0]                        # list안의 list value를 찾을 때

# list 대입
v1, v2 = [1, 2, 3, 4], [5, 6, 7, 8]
l = []                          # 원소가 없는 리스트
l.append(10)                    # 리스트의 마지막 index의 원소로 value(10)을 추가
l.append(20)
l.append(200)
l.extend([30, 40, 50])          # 여러 개의 데이터를 한 번에 추가하는 메소드
l.insert(3, 5000)               # list의 index(3)에 value(5000)을 삽입
l.remove(20)                    # list의 value를 삭제
del l[3]                        # 특정 index의 value를 삭제
l.clear()                       # list의 value를 모두 삭제
print(l)

# 정렬
l = [100, 1, 80, 120, 4000, 5, 30, 9, 400]
result = sorted(l)
result2 = sorted(l, reverse=True)   # 내림차순
print(result, result2)
l.sort()
l.sort(reverse=True)                # 내림차순
print(l)
v = l.pop(1)                        # 삭제하면서 반환
print(v)
l = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
print(len(l), l.count(2))

# tuple
t1 = (1, 2, 3, 4, 5)
t2 = (1, 'abe', True)
t3 = 10, 20, 30, 40
v1, v2, v3 = 10, 20, 30             # tuple 대입
t4 = (100)
t5 = (100,)
t6 = 100,                           # tuple ()는 생략 가능
print(t1)
print(t2)
print(type(t3), t3)
print(v1, v2, v3)
print(type(t4), t4)
print(type(t5), t5)
print(type(t6), t6)

# tuple value 조회 -> indexing, slicing
print(t1)
print(t1[1])
print(t1[3])
print(t1[-1])
print(t1[-3])
print(t1[:4])

# tuple 연산자
result = t1 + t2
print(result)
print(sorted(t3, reverse=True))     # 정렬한 결과를 새로운 list로 반환
print(10 in result)                 # 특정 원소가 tuple에 있는지 확인

# dictionary 생성
di = { 'apple': 100, 'banana': 200, 'watermelon': 255, 'mango': 335}
di2 = dict(apple=200, banana=300)
print(type(di2), di2)

# dictionary 조회 -> indexing, dict.get(key)
print(di['apple'])
print(di.get('apple'))

# value 변경 및 추가
print(di)
di['apple'] = 555
print(di)

# dictionary 주요 메소드
print(di.pop('apple'))              # key item을 삭제하면서 value를 반환
print(di.keys())                    # key값들만 모아서 조회
print(di.values())                  # value값들만 모아서 조회
print(di.items())                   # item들을 묶어서 조회
print('banana' in di)               # key가 dictionary에 있는지 확인

# set
s1 = {1, 2, 3, 4, 5}
s2 = {1, 'abe', False, True}
s3 = {1, 1, 1, 2, 2, 2, 3, 3, 3}    # 중복된 값은 하나만 저장 => 중복을 허용안함
print(s3)
print(len(s3))                      # set의 요소 개수
print(1 in s3)
print(1 not in s3)
s1.add(10)                          # 추가
s1.update({100, 200, 300})          # 여러 개의 value 를 추가
s1.remove(200)                      # value값을 제거 -> 없는 value를 지우면 error
print(s1)
print(s1.pop())

# set 연산
s1 = {1, 2, 3, 4}
s2 = {6, 7, 8, 9}
result = s1 + s2                    # 합집합
result = s1.union(s2)               
reuslt = s1 & s2                    # 교집합
result = s1.intersection(s2)
result = s1 - s2                    # 차집합
result = s1.difference(s2)
print(result)

# tuple에 값을 추가하는 방법 -> 우회(애초에 tuple로 설정하면 안되는 유형)
t = (1, 2, 3, 4, 5)
l = list(t)
l.append(100)
t = tuple(l)
print(t)

# 중복된 값을 한 번에 제거하는 방법
l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 9, 1]
s = set(l)
print(s)