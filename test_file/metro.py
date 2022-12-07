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

# TODO 호선별 역명 뽑아내고, 시간별 혼잡도 추출 후 그래프
# 호선과 시간별로 혼잡도를 빼서 x축 : station, y축 : congestion 으로 그래프 그리기
# 호선별 역명 추출 
# 호선별 역명 상행/하행 구분
# 
# >
metro = pd.read_csv(path, encoding='cp949', index_col='연번')
line_station = metro.groupby('호선')['역명'].unique()
line_time = metro.groupby(['호선', '역명'])['5시30분'].head(10)
# print(line_time)
# y = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
# plt.plot(line_station, y)
# plt.show()
# plt.figure(figsize=(8, 7))
# plt.plot(line_station, line_time)
# plt.show()

if __name__ == '__main__' :
	print(__name__)
	# print(metro)
	print(line_station)
	print(line_time)
	plt.figure(figsize=(15, 5))
	plt.plot(line_station.iloc[0], line_time.head(10))
	plt.title('1호선 역별 혼잡도', fontsize=30)
	plt.ylabel('혼잡도')

	plt.show()
	# print(test.select_dtypes(include='float').sum())
	# file_name = 'TrainOperationStatus_20210405.csv'
	# print(pd.read_csv(path, encoding='cp949', index_col='연번'))
	# file_name = 'NumberOfElderlyPeopleInfo_20220531.csv'
	# print(pd.read_csv(path, encoding='cp949', index_col='연번'))