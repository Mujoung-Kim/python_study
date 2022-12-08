# TODO 서울 지하철 교통-혼잡도
# 데이터 출처 : https://www.data.go.kr/tcs/dss/selectFileDataDetailView.do?publicDataPk=15071311
# 서울교통공사 1-8호선 30분 단위 평균 혼잡도로 30분간 지나는 열차들의 평균 혼잡도
# (정원대비 승차인원으로, 승차인과 좌석수가 일치할 경우를 혼잡도 34%로 산정) 입니다.
# (단위: %). 서울교통공사 혼잡도 데이터는 
# 조사일자(평일, 토요일, 일요일), 호선, 역번호, 역명, 상하선구분, 30분단위 별 혼잡도 데이터로 구성되어 있습니다.
# (2년 단위 업데이트 자료 입니다.)
# path : ./data/서울교통공사_지하철혼잡도정보_20211231.csv
# 추출할 데이터 호선별/시간 때 혼잡도 평균
#  -> 출퇴근 시간 역별 혼잡도 계산
#  -> 역도착 정보관련 데이터 있으면 이와 합쳐서 어느 때 오래걸리는지 확인
#  -> pandas.merge()이용
# index : 1704 / columns : 42
# Nam : 0 / dytype - float(37), int(2), object(3)
# 노인 승하차 인원 정보
# 데이터 출처 : https://www.data.go.kr/data/15101985/fileData.do?recommendDataYn=Y
# 서울교통공사 역별 일별 시간대별 노인 승하차인원 정보입니다. 
# 해당 데이터는 연번,일자,역번호,역명,구분,시간대별 인원수로 구성되어 있으며, 
# 데이터 개방이 가능한 2021년 7월부터 개방합니다.
# (데이터 제공신청으로 인해 2022년 5월 데이터까지 개방합니다. )

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = 'SubwayCongestionInfo_20211231.csv'
path = f'./test_file/data/SeoulMetro_{file_name}'

# TODO 호선/시간별 혼잡도 그래프 그리기 + 함수화
metro = pd.read_csv(path, encoding='cp949', index_col='연번')

# TODO 한 figure안에 2개로 그리는 작업 -> plot()할 때 pivot_table?
# 1호선 정차역별 시간 때에 따른 혼잡도 (상하행)
# one_up : 1호선 상선 / 평일
# one_down : 1호선 하선 / 평일
# x축 : 정차역 / y축 : 혼잡도 / value : 0530 ~ 2330 혼잡도
line_one = metro[metro['호선'] == 1]
one_up = line_one[(line_one['구분'] == '상선') & (line_one['조사일자'] == '평일')]
one_up.set_index('역명', inplace=True)
one_up.drop(columns=['호선', '역번호'], inplace=True)
one_down = line_one[(line_one['구분'] == '하선') & (line_one['조사일자'] == '평일')]
one_down.set_index('역명', inplace=True)
one_down.drop(columns=['호선', '역번호'], inplace=True)

# print(one_up[0])

# 상행 그래프
# fig -> (20, 10)의 도화지에 ax1을 subplot로 넣고 ax1.plot(x, y)로 그려라
# fig = plt.figure(figsize=(20, 10))
# plt.addsubplot(2, 1, 1)
# ax1 = fig.add_subplot(211)
one_up.plot(figsize=(20, 10))
plt.title('1호선 혼잡도 상행', fontsize=30)
plt.xlabel('정차역')
plt.xticks(range(0, 10), labels=[n for n in one_up.index])
plt.ylabel('혼잡도')
plt.grid(True, linestyle=':')

plt.legend(bbox_to_anchor=(1, 1.175), loc='upper left')

# 하행 그래프
# plt.subplot(2, 1, 2)
one_down.plot(figsize=(20, 10))
plt.title('1호선 혼잡도 하행', fontsize=30)
plt.xlabel('정차역')
plt.xticks(range(0, 10), labels=[n for n in one_down.index])
plt.ylabel('혼잡도')
plt.grid(True, linestyle=':')

plt.legend(bbox_to_anchor=(1, 1.175), loc='upper left')

plt.show()

if __name__ == '__main__' :
	print(__name__)
	# print(metro)
	# file_name = 'TrainOperationStatus_20210405.csv'
	# print(pd.read_csv(path, encoding='cp949', index_col='연번'))
	# file_name = 'NumberOfElderlyPeopleInfo_20220531.csv'
	# print(pd.read_csv(path, encoding='cp949', index_col='연번'))

	# plt.show()