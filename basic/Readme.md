# 변수(Variable)<br>

## 변수선언 및 초기화
- 변수명 = 값
  - 변수는 반드시 선언하면서 값을 대입한다.
  - 처음 변수를 만들면서 값을 대입하는 것을 초기화라고 한다.
  - 변수를 초기화할 값이 없을 경우 `None`을 대입한다. (ex: `name = None` )<br><br>

## 변수에 값을 대입하는 방법
1. 변수명 = 값
2. 변수명_1 = 변수명_2 = 변수명_3 = 값
    - 여러변수에 동일한 값을 대입 (ex: `num1 = num2 = num3 = 10` )
3. 변수명_1, 변수명_2, 변수명_3 = 값1, 값2, 값3
   - 여러변수에 서로 다른값을 대입하는 것을 한 실행구문으로 작성 (ex: `a, b, c = 10, 20, 'hello'` )<br><br>

### 문자열 indexing과 slicing
   - indexing: 문자열에서 한 글자를 조회할 때 사용.
   - slicing: 문자열에서 범위로 여러 글자를 조회할 때 사용.<br><br>

## format 문자열
  - 문자열에 문장 layout을 미리 만들어 놓고 값은 나중에 대입하는 방식으로 문자열을 만드는 것<br><br>

### format 함수 이용
  - 문자열을 만들 때 나중에 넣을 곳을 {}로 표시하고 `format()` 메소드에서 { }에 들어갈 순서대로 넣는다.
     - `myformat = 'name: {}, age: {}, address: {}'`
     - `myformat = 'name: {name}, age: {age}, address {address}`
     - `value = myformat.format(name = 'sancho', age = 20, address = 'korea')`<br><br>
  - 형식문자를 이용한 format
    - `myformat = 'name: %s, age: %d, tall: %.2f`  
  - f-string
    - python 3.6에 추가된 형식
     - 값을 넣을 자리에 { value }을 이용해 value가 가진 값을 문자열에 추가한다.
       - `myformat = f'name: {name}, age: {age}, address: {address}'`<br><br>

## 문자열 주요 메소드
  - `strip()` : 문자열의 좌우 공백을 제거하는 메소드
  - `count(value)` : 문자열에서 value가 몇 개 있는지 확인하는 메소드
  - `split(value)` : 문자열에서 value을 기준으로 나누는 메소드
  - `startswith(value)` : 문자열이 value로 시작하는지 확인하는 메소드
  - `endswith(value)` : 문자열이 value로 끝나는지 확인하는 메소드
  - `index(value, int)` : 문자열에서 value를 int부터 검색하는 메소드
  - `find(value, int)` : 문자열에서 value를 int부터 검색하는 메소드
    - `index()`와 `find()`의 차이 찾는 값이 없을 때 `index()`는 error를 return하고, `find()`는 -1을 return 한다.<br><br>

## 타입 변환 함수
  - `str(value)` : value를 문자열로 변환
  - `int(value)` : value를 정수형으로 변환
  - `float(value)` : value를 실수형으로 변환
  - `bool(value)` : value를 논리형으로 변환<br>

## input()
  - `input(label)` : 사용자로부터 문자열을 입력받아서 반환해주는 함수 label로 힌트 설정가능<br><br>

# 자료구조<br>

## 자료구조란
  - 여러 개의 값들을 모아서 관리하는 데이터 타입
  - 데이터를 모앙서 관리하는 방식에 따라
    - List 순서가 있으며 중복을 허용하고 구성하는 값들을 변경할 수 있다.
    - Tuple 순서가 있으며 중복을 허용하는데 구성하는 값들을 변경할 수 없다.
    - Dictionary key-value 형태로 값들을 저장해 관리한다. key는 중복되면 안되지만 value는 중복되도 상관없다. ( ex. `{ key : value }` )
    - Set 중복을 허용하지 않고 값들의 순서가 없고 데이터를 추출할 수 없다.
    - List와 Tuple은 index를 가지고 조회를 하기 때문에 특정값들만 가져와서 사용할 때 불편하다 이때 Dictionary를 이용
  - 원소, 성분, 요소, element
    - 자료구조의 값들을 구성하는 개별 값들
    - `len(data_structure)`
      - 자료구조 내의 원소의 개수를 반환한다.

## 리스트(List)
  - 값을 순서대로 모아서 관리하는 구조
  - 특징
    - 각 원소들을 순서를 나타내는 index를 가지며 index로 관리(조회, 변경)된다.
    - 다른 데이터 타입의 값들을 모을 수 있다.
    - 중복된 값들을 저장할 수 있다.
    - 리스트를 구성하는 원소들을 변경할 수 있다. (추가, 삭제, 변경이 가능)
  - 생성
    - 구문
      - `[value, value, value, ...]`
    - value는 ,로 구분해서 넣는다.<br><br>

### 리스트 연산자
  - indexing, slicing, +, *
  - 구문
    - `list[index]` -> list에서 해당 index를 value를 조회
    - `list[start_index : end_index : step]` -> list에서 start_index부터 end_index까지 step 간격만큼 value를 조회 
    - `result_list = list1 + list2` -> list1과 list2를 덧붙여 result_list에 대입
    - `result_list = list * int_value` -> list를 int_value만큼 반복하여 result_list에 대입
  - 중첩 list
    - `list = [ value, [ value, value, ...], ...]` -> list가 value로 list를 가지고 있을 경우를 의미한다.
    - `list[list_index][value_index]` -> 중첩 list의 value를 조회할 때<br><br>

### 리스트 대입
  - list의 원소들을 나눠서 value들에 대입
  - value의 개수와 list 원소의 개수는 동일해야한다.<br><br>

### 리스트 주요 메소드
  - `append(value)` : list의 마지막 index의 원소로 value를 추가
  - `extend(value, value)` : 한 번에 여러 개의 value를 추가
    - \+ 연산자의 차이 + 연산자는 새로운 list에 둘을 합치지만 `extend(value)`는 list의 value를 합친다.
  - `insert(index, value)` : list의 index에 value를 삽입
  - `remove(value)` : list에서 처음 만나는 value를 삭제
  - `del list[index]` : list의 특정 index의 value를 삭제
  - `clear()` : list가 가진 원소를 모두 삭제
  - `pop(index)` : index의 value를 삭제하면서 반환
  - `count(value)` : list의 원소 중 value가 몇 개 있는지 조회<br><br>

### 리스트 정렬
  - 내림차순
    - `sorted(list, reverse=True)` : 원본은 바꾸지 않고 정렬한 새로운 리스트를 변환
      - 모든 자료구조에 공통으로 사용가능
  - 오름차순
    - `sorted(list)`
  - 리스트의 정렬 메소드
    - `sort()` : list의 원소들을 오름차순으로 정렬한다.<br><br>

## 튜플(Tuple)
  - list와 같이 순서대로 원소들을 저장하는 자료구조이다.
  - 원소를 변경할 수 없다.
  - tuple은 각 index마다 정해진 의미가 있고, 그 value가 한 번 설정되면 바뀌지 않는 경우에 많이 사용한다.
  - 생성
    - 구문
      - `tuple = (value, value, value, ...)`
      - `tuple = (value,)` or `tuple = value,` -> 하나의 value만 넣을 때
  - indexing, slicling 를 이용하여 데이터 조회가능
  - \+ , * 연산자를 이용하면 연산하여 새로운 결과를 가지는 tuple을 생성
  - list의 추가, 제거, 변경하는 기능을 제외한 조회, 반환기능만 사용가능
    - `sorted(tuple)` -> 정렬한 결과를 새로운 list에 담아서 반환<br><br>

## 사전(Dictionary)
  - 값을 키(key)-값(value)쌍의 형태로 저장하는 자료구조
    - list나 tuple의 index의 역할을 하는 key를 직접 저장한다.
    - key는 중복을 허용하지 않지만 value는 중복을 허용한다.
  - 생성
    - 구문
      - `dict = { key : value, key : value, ...}`
      - `dict(key=value, key=value)`  -> 메소드를 활용하여 생성하는 방법
    - 생성 시 없는 key를 입력하면 자동으로 key-value를 추가한다.
  - 원소 조회 및 변경
    - `dict[key]` -> indexing으로 key의 value를 조회
    - `dict.get(key)` -> `dict`의 메소드를 이용하여 key의 value를 조회
    - indexing로 조회 시 없는 key를 검색하면 keyerror를 발생
    - `dict.get(key)`로 조회 시 값이 없으면 `None` or default 값을 반환
    - `dict.get(key, default_value)` 값이 없을 때 반환할 default 값을 설정
    - `dict[key] = value` -> key에 value를 대입하여 변경
    - `dict[key] = value`시 없는 key일 경우 새로운 key와 value를 추가
   - 주요 메소드
     - `get(key, default_value)` : key와 연결된 value를 반환하고, key가 없으면 default_value를 반환
     - `keys()` : key값들만 모아서 반환
     - `values()` : value값들만 모아서 반환
     - `items()` : key와 value를 tuple로 묶어서 반환
     - `pop(key)` : key의 items을 삭제하면서 value를 반환
     - `len(dict)` : items의 개수
     - `in, not in` : 어떤 value가 dictionary의 key로 존재하는지 확인
     - `del dict[key]` : key를 조회하고 삭제<br><br>

## 집합(Set)
 - 중복되는 값을 허용하지 않고 순서를 신경 쓰지 않는다.
 - indexing, slicing를 지원하지 않는다.
 - 생성
   - 구문
     - `set = { value, value, value}`
     - `set = { }` -> 이거는 set이 아닌 빈 dictionary이다.
 - 주요 메소드
   - `add(value)` : set에 value 추가
   - `update(data_structure_value)` : 한 번에 여러 개의 data_structure_value를 추가
   - `pop()` : value를 하나씩 반환하여 삭제
   - `remove(value)` : value 값을 제거
   - `len(set)` : set안의 요소 개수
   - `in, not in` : 어떤 값이 set의 원소에 있는지를 확인
 - 집합 연산
   - 합집합
     - `set | set`
     - `union(set)`  
   - 교집합
     - `set & set`
     - `intersection(set)`
   - 차집합
     - `set - set`
     - `difference(set)`<br><br>

## 자료구조 타입 변환함수
  - `list(data_structure)` : date_structure를 list로 변환
  - `tuple(data_structure)` : data_structure를 tuple로 변환
  - `set(data_structure)` : data_structure를 set로 변환
  - dictionary로 변환하는 함수는 없다.
  - 변환할 대상 data_structure가 dictionary일 경우 key 값들만 모아서 변환<br><br>

# 제어문(Control Statement)<br>

## 조건문(분기문)
  - 프로그램이 명령문들을 실행하는 도중 특정 순서에서 흐름이 나뉘져야하는 경우 사용한다.
  - if문
    - 들여쓰기(tab)을 통해 조건문을 구분
    - 구문
      - ```python
          if    a == 0:
                b = 10 / a
                print(b)
          print('end')
        ``` 
  - if else문
    - 구문
      - ```python
          if    a == 0:
                b = 10 / a
                print(b)
          else  :
                print('end')
        ```
<br>

## 반복문
   - 특정 조건이 True인 동안 명령문을 반복해서 실행한다.
   - 구문
     - ```python
        while    value > 5:
            value += 1
            print(f'value: {value}')
        ```
   - Iterable한 객체가 값이 없을 때까지 반복 조회한다.
   - Iterable한 객체란?
     - 반복가능한 객체를 말한다.
     - `for in`을 이용해 원소들을 조회할 수 있는 객체
     - `for`은 iterable 타입의 객체가 가지고 있는 값들을 순회하며 조회할 때 사용
     - 구문
       - ```python
            for element in data_structure:
                print(f'{element}')
            ```     
     - `for element in data_structure`문 관련 함수
       - `range(start_value, end_value, step)` : 특정 정수 범위내에서 특정 값만큼 증가하는 값들을 제공하는 함수
          1. value 1개 : end_value. 0 ~ end_value-1까지 1씩 증가하는 정수를 제공
          2. value 2개 : start_value, end_value. start_value ~ end_value-1까지 1씩 증가하는 정수 제공
          3. value 3개 : start_value, end_value, step. start_value ~ end_value-1까지 step만큼 증가하는 정수 제공
       - `enumerate(data_structure, start_value)` : 현재 몇 번째 값을 제공하는지, 원소를 tuple로 묶어서 제공하는 함수
         1. data_structure : 값을 제공할 객체
         2. start_value : 몇 번째 값을 제공하는지의 시작점 ( default = 0 )
       - `zip(data_structure, data_structure, ...)` : 각 data_structure에서 같은 index의 값들을 묶어서 반환하는 함수
         1. data_structure : 2개 이상 값으로 넣어야 된다.
     - 자료구조, 문자열이 대표적인 Iterable이다.<br><br>

##  continue, break
 - 반복문 안에서 사용하는 반복문을 제어하는 구문
 - continue
   - 다음 반복을 실행해라.
   - 뒤에 있는 명령은 실행하지 않는다.
 - break
   - 반복을 멈춰라.

## 컴프리헨션(Comprehension)
 - 기존 data_structure가 가진 element들을 이용해 새로운 data_structure를 만드는 구문
   - 주로 기존 date_structure의 element들을 처리한 결과를 새로운 data_structure에 넣을 때 사용한다.
   - 결과를 넣을 새로운 data_structure에 따라 다음 세가지가 있다.
     - list comprehension
     - dictionary comprehension
     - set comprehension
   - tuple comprehension은 없다.
   - dictionary, set comprehension은 python 3.0부터 지원
 - 구문
   - ```python
        [ elem for elem in list ]
        { key : value for key, value in dictionary }
        { elem for elem in set }
        ```