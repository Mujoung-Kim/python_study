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

# 자료구조(Data Structure)<br>

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
<br>

# 함수(Function)<br>

## 함수란?
 - 하나의 작업, 기능, 동작을 처리하기 위한 명령문들의 묶음으로 사용자 정의 연산자라고 할 수 있다.
 - 처리하는 기능을 의미한다.
   - 만들어진 함수는 동일한 작업이 필요할 때 마다 재사용될 수 있다.
   - 함수를 만드는 것을 함수 정의라고 한다.
   - 정의된 함수를 사용하는 것을 함수 호출이라고 한다.
   - python에서 함수는 일급 시민 객체(First Class Citizen Object)이다.
     - 일급 시민 객체 : 변수에 할당할 수 있고, 인수로 전달할 수 있고, 반환 값으로 반환할 수 있는 객체를 말한다.
   - 매개변수(parameter), 전달인자(argument), 반환값(return value)<br><br>

## 함수구문
 - 함수의 정의
   - 새로운 함수를 만드는것을 함수의 정의라고 한다.
   - 함수의 선언부와 구현부로 나누어진다.
     - 선언부(Header) : 함수의 이름과 인수를 받을 변수(parameter)를 지정한다
     - 구현부(Body) : 함수가 호출 되었을 때 실행할 실행문들을 순서대로 작성한다.
     - ```python
        def fuction_name([parameter, parameter2, argument, ...]):  # Header
          pass                                                     # Body
          return result_value
        ```
     - 함수 선언 마지막에는 :을 넣어 구현부와 구분한다.
     - 매개변수(parameter)는 인수를 받기 위한 변수로 0개 이상 선언할 수 있다.
     - 함수의 실행구문은 반드시 공백 4개 or 탭 이후에 작성한다.
     - 결과값이 있을 경우 `return`을 넣고 없을 경우 `return`은 생략할 수 있다.
       - `return`이 없는 함수는 `None`을 반환한다.
     - 함수 이름 관례
       - 모두 소문자로 작성하고 단어와 단어가 합쳐지 경우 `_`로 구분한다.<br><br>

### argument 전달 방법
 - argument : 함수/메소드를 호출할 때 parameter에 전달해 주는 값.
 - positional argument : 선언된 parameter 순서에 맞춰서 값을 전달.
   - ```python
        def fuction_name(parameter, parameter2, parameter3, parameter4):
          print(parameter, parameter2, parameter3, parameter4, sep=' - ')
        ```
 - keyword argument : parameter_name = argument_value -> 어떤 parameter에 어떤 argument_value를 전달할 지 지정.
   - ```python
        def fuction_name(para, para2, para3)
          print(para, para2, para3, sep=' - ')
        function_name(para = 10, para2 = 20, para3 = 30)
        ```
    - 순서대로 전달할 필요가 없다.<br><br>

### 함수 정의 시 매개변수(parameter) 선언 방법
 - 기본값(default_value)이 있는 매개변수(parameter)
   - 매개변수(parameter) 선언 시 기본값(default_value)을 대입
   - ```python
        def fun(name = None, age = 0):
          pass 
        ```
     - 호출시 값이 전달되지 않으면 함수는 기본값을 사용하고 전달되면 전달된 값을 사용한다.
 - 매개변수 선언 순서
   - 기본값이 없는 매개변수들을 먼저 선언해야한다.
   - ```python
          def fun(name, age, address = None, tel = None): # 가능
          def fun(name = None, age = 0, address, tel):    # 불가능
          def fun(name, age = 0, address = None, tel):    # 불가능
        ```
        <br>

## 가변인자(Var args)
 - 인수의 개수를 정하지 않고 받을 경우 사용한다.
 - 매개변수 앞에 `*`를 붙인다.
   - 가변인자는 tuple로 처리된다.
   - 호출헐 때는 값들을 0 ~ n개 나열하면 된다.
   - 관례적으로 변수명은 `*args`로 준다
 - 매개변수 앞에 `**`를 붙인다.
   - 가변인자는 dictionary로 처리된다.
   - keyword argument형식으로 인수를 전달한다.
   - 관례적으로 변수명은 `**kwargs`로 준다.
 - 일반변수와 같이 선언할 경우 가변인자는 마지막에 선언해야 한다.
 - `*`와 `**`는 각각 하나씩만 선언할 수 있다.<br><br>

# 전역변수(Global Variable)와 지역변수(Local Variable)
 - 전역변수
   - 함수밖에 선언된 변수
   - 모든 함수들이 공통적으로 사용할 수 있다.
 - 지역변수
   - 함수안에 선언된 변수
   - 선언된 그 함수 안에서만 사용할 수 있다.<br><br>

# Python에서 함수는 일급시민객체(First Class Citizen Object) -> 함수는 값이다.
  - 일급시민객체
    1. 변수에 할당(대입)할 수 있다.
    2. 함수 호출할 때 argument로 전달할 수 있다.
    3. 함수의 return 값으로 사용할 수 있다.
 - 구문
   - ```python
        def hello():
          print('hello world')
        ```
        <br><br>

# 람다식(Lambda Expression)
 - 함수를 하나의 구문으로 만드는 표현식
 - 일회성 함수를 만들 때 사용 -> 함수를 다른 함수 호출할 때 argument로 전달하는 경우
 - 구문
   - ```python
        lambda [parameter1, ...] : operation
        ```
   - 명령문은 하나의 명령문만 가능
   - 명령문이 처리한 결과는 자동으로 return된다.
   - 문법적으로 매개변수를 생략할 수 있지만 안받을 경우 그냥 결과를 입력한다.<br><br>

# Docstring
 - function, class, method에 대한 설명
 - 구현부 맨 처음에 달아준다. `"""..."""`을 이용해 설명을 작성
   - 구문
   - ```python
          def function(parameter, parameter):
            """
            함수에 대한 설명
            [parameter]
              변수1 : 타입 - 설명
              변수2 : 타입 - 설명
            [return]
              타입 - 설명
            [exception]         # 함수가 실행되다 발생할 가능성이 있는 오류
              타입 - 설명
            """
            pass
        ```
        <br>

# 객체지향프로그래밍(Object-Oriented Programming)
 - 객체(object)
   - 연관성 있는 값들과 함수들을 묶어서 가지고 있는 값
     - 하나의 데이터가 여러 개의 값으로 구성되있고, 그 값들과 관련된 기능이 필요할 때 이것들을 묶어서 구성한 것이 객체이다.
   - 속성(attribute) == state
     - 객체를 구성하는 값으로 객체의 속성, 상태이다.
   - Instance 메소드(method) == operator, behavior
     - 객체가 제공하는 기능으로 객체의 속성을 처리하는 기능을 제공한다.
     - 값을 처리하는 연산자라고 할 수 있다.
   - 클래스(class)
     - 객체가 가지는 속성과 메소드를 정의한 객체의 설계도
     - 사용자 정의 데이터타입
     - 클래스로부터 객체를 생성해 사용한다.
     - ```python
          class ClassName:                           # instance 생성
            def _init_(attribute, attribute, ...):   # attribute 선언
              self.attribute = attribute
              self.attribute = attribute

            def function():                          # instance method 선언
              pass
          ```
     - class 이름 관례 -> 파스칼 표기법 : 각 단어의 첫글자는 대문자 나머진 소문자로 정의
     - class를 구현(정의)하고, 그 클래스로부터 객체를 생성해서 사용합니다.
     - instance화(instantiate)
       - 객체를 생성하는 작업
       - 구문
         - ```python
                variable = ClassName()            # 객체 생성 -> ClassName 생성된 객체를 변수에 넣어서 사용
              ```
         - 
     - instance
       - 클래스로부터 생성된 객체<br><br>

## instance에 속성을 정의
 - 속성(attribute)
   - 객체의 data, 상태(state)<br><br>

### instance에 속성을 추가/조회
  - 추가
    1. Initializer를 이용해서 추가
    2. `instance.attribute_name = value` : 추가/변경
       > 주로 변경 시에 사용
    3. method를 이용해서 추가/변경
       > 주로 변경 시에 사용
  - 조회
    - 사용할 곳에서 `instance.attribute_name`<br><br>

### 생성자(Initializer)
 - class에서 객체 생성할 때 호출되는 특수 method
   - 객체 생성시에만 호출 할 수 있다.
 - 주로 attribute의 값을 초기화 하는 역할을 한다.
   > variable 초기화 : 변수를 처음 만들어서 첫 번째 값을 대입
 - 구문
   - ```python
          class ClassName:
            def __init__(self, param, param2):
              # 구현부
              self.attribute_name = param
              self.attribute_name2 = param2
        ```
   - self 변수
     - method의 첫 번째 parameter로 선언.
       > method는 반드시 한 개이상의 parameter를 선언해야 하고, 그 첫 번째 parameter를 의미
     - 그 method를 가지는 객체를 받는다
       - initalizer : 생성한 객체
       - method : method를 호출할 때 사용한 객체<br><br>

### instance 메소드(method)
  - instance가 제공하는 기능
    - instance의 attribute 값들을 처리하는 역할
  - 구문
    - ```python
          class ClassName:
            def method_name(self):
              # attribute 값을 사용할 경우 self 변수를 이용
              pass
        ```
    - 반드시 하나 이상의 parameter를 선언해야한다.
  - 호출
    - `instance.method_name(arg, arg, ...)`<br><br>

## 정보 은닉(Information hiding)
 - attribute의 값을 외부에서 마음대로 바꾸지 못하도록 하는 방법
   - attribute에 값을 직접 대입하는 것을 막는다.
   - 직접 대입할 경우 그 attibute가 가질 수 없는 값이 대입되는 것을 막을 수 없다.
   > 대신 method를 통해 값을 변경하도록 한다.
     - setter method : attribute_variable을 변경하는 method
     - getter method : attribute_variable을 조회(반환)하는 method
 - 구현방법
   - attribute_name을 `__`로 시작한다. (단 `__`로 끝나면 안됨)
   - attribute_variable을 변경/조회하는 두 개의 method를 제공한다.
     - setter는 관례상 `set`으로 getter는 관례상 `get`로 시작한다.<br><br>

## 상속
 - 기존 클랫를 확장하여 instance 변수나 method를 추가하는 방식
   - 기반(base)class, 상위(super)class, 부모(parent)class
     - 물려주는 class, 좀 더 추상적
   - 파생(derived)class, 하위(sub)class, 자식(child)class
     - 상속하는 class 좀 더 구체적
   - 상위 class와 하위 class는 계층 관계를 이룬다.
   - python은 다중상속을 지원한다.
     - 하나의 class가 여러 class로부터 상속할 수 있다.
     - 하나의 class가 여러 class의 기능을 가져와서 사용할 때 이용
   - 구문
     - ```python
            class ClassName(SuperClassName[SuperClassName], ...):
              pass
          ```
          <br><br>

## Method overriding
 - method 재정의
   - 상위class에 정의된 method 구현을 하위class에서 재정의 하는 것
   - 상위class의 추상적인 구현을 하위class에서 그 class에 맞게 구체적으로 구현하는 방법<br><br>

## 상속과 attribute
 - `super()` : 상위 class의 객체를 반환
   - 하위 class에서 상위 class에 선언된 method는 attribute을 호출할 때 사용
      > 반드시 사용해야하는 경우 : 하위 class에서 method overriding한 method가 상위 class의 원본 method를 호출 해야할 경우
 - 같은 기반의 instance method를 호출할 때
   - `self.method()`를 이용<br><br>

### 다중 상속
 - 다중 상속
   - 하나의 class가 여러 class로부터 상속하는 것.
   - 구문
     - ```python
            class SuperClase:
                pass

            class SuperClass2:
                pass

            # SuperClass와 SuperClass2를 동시에 상속
            class SubClass(SuperClass, SuperClass2, [...]):
                pass
        ```
   - MRO(Method Resolution Order) -> method 호출 순서
     1. 자기 자신 것을 호출
     2. 상위 class것을 호출
       - 다중 상속의 경우 먼저 선언된 class부터 찾아서 호출<br><br>

# 객체 관련 특수 메소드/변수
 - `isinstance(object, class_name), isinstance(object, (class_name1, class_name2, ...))` : return type(bool)
   - 객체가 두 번째 parameter로 지정한 class의 타입이면 True, 아니면 False 반환
 - `object.__dict__` : 객체가 가지고 있는 instance 변수들과 대입된 값을 dictionary에 넣어 반환
 - `object.__class__` : 객체의 타입을 반환<br><br>

## 특수 메소드(Special Method) = 매직 메소드(Magic Method), 던더(DUNDER)
 - 특수 메소드란?
   - class에 정의하는 약속된 method로 객체가 특정한 상황에서 사용될 때 자동으로 호출되는 method들이다
   - method_name에 `__`으로 시작하고 끝난다.
     - `__init__()`
   - 제공되는 던더 method
     - https://docs.python.org/ko/3/reference/datamodel.html#special-method-names
   - 주요 special method
     - `__init__(self, [param, ...])`
       - initalizer
       - self는 새롭게 생성되는 instance가 전달된다.
       - 객체 생성시 가져야하는 default instance 변수를 정의할 때 사용
     - `__call__(self, [param, ...])` 
       - 객체를 함수처럼 호출할 때 실행되는 method
     - `__repr__(self)` : 객체에 대한 표현식을 문자열로 만들어준다.
       - instance를 문자열로 바꿀 때 사용할 문자열 값을 만들어 반환한다.
       - 내장 함수 `repr()` 객체를 전달하면 호출된다.
       - 대화형 IDE에서 변수를 값을 출력할 때도 호출된다.
       - 반환된 문자열을 `eval()`에 넣어 동일한 attribute를 가진 객체를 생성할 수 있도록 정의한다.
     - `__str__(self)` : 객체의 값을 문자열로 만들어준다.
       - `__repr()__`과 비슷하게 instance를 문자열로 바꿀 때 사용할 문자열 값을 반환한다.
         - 내장 함수 `str(object)`나 `print()`함수에 의해 호출된다.
         - 출력 시 객체에 `__str__()`이 없으면 `__repr__()`이 호출된다.
       - 주로 instance의 attribute값들을 하나의 문자열로 합쳐 반환하도록 구현한다.
     - 비교 연산자
       - `__eq__(self, other)` : self == other
       - `__lt__(self, other)` : self < other
       - `__gt__(self, other)` : self > other
       - `__le__(self, other)` : self <= other
       - `__ge__(self, other)` : self >= other
       - `__ne__(self, other)` : self != other
     - 산술 연산자
       - `__add__(self, other)` : self + other
       - `__sub__(self, other)` : self - other
       - `__mul__(self, other)` : self * other
       - `__truediv__(self, other)` : self / other
       - `__floordiv__(self, other)` : self // other
       - `__mod__(self, other)` : self % other <br><br>

# Class Variable/Class Method, 정적 메소드(Static method)
 - 객체가 아닌 class자체의 method, variable
   - 객체 별로 생성되는 것이 아니라 class에 속하게 된다.
   - class method는 class variable와 관련된 기능을 제공하는 method를 만들 때 사용
 - class variable 선언
   - ```python
        class ClassName:
            class_variable = None
        ```
   - class block에 선언한 변수로 `class_name.variable`로 호출
 - class method 선언
   - ```python
        class ClassName:
            class_variable = None

            @classmethod
            def add_variable(cls, parameter):
                cls.class_variable = parameter
        ```
   - method 선언부에 `@classmethod`를 붙인다
   - 반드시 한 개의 parameter를 선언해야 한다.
     > 첫 번째 parameter로 class 자신을 받는 variable를 선언해 다른 class 멤버들을 호출할 수 있다.
   - class variable/method 호출
     - className을 이용해 호출
     - 객체를 이용해서 호출
 - 정적 메소드(static method)
   - class에 선언된 method로 객체와 상관없이 class의 기능을 제공
     - 객체와 상관없는 class만의 기능을 제공하는 method를 만들 때 사용
   - 구현
     - ```python
            class ClassName:
                @staticmethod
                def static_method(param, param):
                    pass
        ```
     - class method와 다르게 class를 받는 parameter를 선언하지 않는다.
       - class_variable에 직접 접근하지 못한다.
   - 호출
     - `className.method_name()`으로 호출<br><br>