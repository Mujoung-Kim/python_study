# 입출력
# 1. 연결 - open()
# 2. 입력(read()), 출력(write())
# 3. 연결닫기 - close()

# 현재 directory 조회
import os
print(os.getcwd())
# os.chdir(directory_path)              # 현재 directory를 변경

txt = '※ best 11'
txt2 = """
       rashford
sancho bruno anthony
    elicksen casemiru
shaw risandro varan dalot
        de-gea
"""
txt3 = 'sub : martial, garnacho, malracia, mactominy, alranga, megaier, van de vick'
txt_list = [txt, txt2, txt3]

# text 입출력
# 현재 경로의 text.txt 파일에 변수 txt의 문자열을 출력
path = 'text.txt'                       # 저장할 파일경로(상대경로) -> `./`생략가능
path2 = 'text2.txt'

# mode : w -> 파일이 없으면 새로 생성해서 연결, 있으면 지우고 다시 생성해서 연결
fw = open(path, 'wt', encoding='UTF-8') # 연결
print(type(fw))

# 출력
fw.write(txt)
fw.write(txt2)
fw.write(txt3)
try :
    # 연결
    fw = open(path2, 'w', encoding='utf-8')
    # 입출력
    fw.writelines(txt_list)
except Exception as e:
    # 연결/입출력 시 발생하는 exception_handing
    print('출력중 예외발생 - 처리중', e)
finally :
    # 연결닫기
    fw.close()
fw.close()                              # 연결 닫기

# 입력
# text.txt 파일의 text를 읽어서 화면 출력
try :
    fr = open(path, 'rt', encoding='UTF-8')
    print(type(fr))
    # 입력
    result = fr.read()
    print(result)
except Exception as e:
    print('읽는 도중 예외발생 - 처리중', e)
finally :
    fr.close()

try : 
    fr = open(path, encoding='utf-8')
    # result = fr.readline()              # 한 줄
    # print(result, end='')
    results = fr.readlines()            # 줄별로 읽어서 return list
    print(results)
except Exception as e:
    print(e)
finally :
    fr.close()

# 한 줄씩 읽어서 어떤 처리를 해야하는 경우
# for in 문을 사용
try :
    fr = open(path, encoding='utf-8')
    for line, txt in enumerate(fr, start=1):
        print(f'{line}. {txt}', end='')
    print()
except Exception as e:
    print(e)
finally :
    fr.close()

fr = open(path, encoding='utf-8')
print(fr)
print(fr.read())
# UnicodeDecodeError : 잘못된 인코딩방식으로 읽을 때 발생
# utf-8 <-> cp949로 해결
fr.close()

# with문
# with open() as variable_name
with open(path, encoding='utf-8') as fr:
    result = fr.read()
    print(result)
# with block이 종료되면 fr.close()가 자동으로 실행된다.

# binary data 입출력
# open()시 mode = b로 설정
# 파일복사 function
def copy(src, target):
    # src_path의 file을 target_path의 file로 복사
    # src에서 읽어서 target에 쓰기

    # fr = open(src, 'rb')
    # fw = open(target, 'wb')
    # fw.write(fr.read())
    # fr.close()
    # fw.close()
    # 위의 logic을 with문으로 작성
    with open(src, 'rb') as fr:
        with open(target, 'wb') as fw:
            data = fr.read()
            print(type(data))
            fw.write(data)

copy('../../../red_panda.jpg', 'red_panda_copy.jpg')

# pickle 입출력
# i = 20                                # input_type
# with open('a.data', 'wb') as f:
#     f.write(i)
import pickle

# 저장
i = 20
filename = 'int_data.pkl'               # pickle의 file 확장자는 .pkl or .pickle

with open(filename, 'wb') as fw:
    pickle.dump(i, fw)

# 읽어오기
with open(filename, 'rb') as fr:
    x = pickle.load(fr)
    print(x)

# 해당 값들을 저장하고 불러오기
l = [10, 20, 30, 'abc']
# l2 = []
filename = 'list_data.pkl'

with open(filename, 'wb') as fw:
    pickle.dump(l, fw)

with open(filename, 'rb') as fr:
    l2 = pickle.load(fr)
print(l2, type(l2))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'name : {self.name}, age : {self.age}'

p = Person('rashford', 23)
filename = 'person_data.pkl'

with open(filename, 'wb') as fw:
    pickle.dump(p, fw)

with open(filename, 'rb') as fr:
    p2 = pickle.load(fr)
print(p2.name, p2.age)