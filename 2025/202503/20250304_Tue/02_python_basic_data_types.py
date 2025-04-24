# 문자열 연산 예시
a = "3"
b = "5"
a + b  # 출력: "35" (문자열 연결)

# 숫자 연산 예시
a = 3
b = 5
a + b  # 출력: 8 (숫자 덧셈)

# 문자열 분리 예시
secPrice = "SEC_2000"
secPrice.split("_")  # 출력: ['SEC', '2000']

# 자료형이란?
# 변할 수 있는 값을 담는 공간
a = 3
b = 2
a = a * b
print(a)  # 출력: 6

# 자료형 확인
A = "3"
print(type(a))  # 출력: <class 'int'>
print(type(A))  # 출력: <class 'str'>

# 변수명 규칙
# 3A = 2  # 오류: 변수명은 숫자로 시작할 수 없음
# if = 3  # 오류: 예약어는 변수명으로 사용할 수 없음

# 1. 수(Number) 자료형
integer_value = 123
float_value = 12.456

# 1. 더하기 연산
sumation = integer_value + float_value
print(sumation)  # 출력: 135.456

# 2. 곱하기 연산
multiple = integer_value * float_value
print(multiple)  # 출력: 1532.088

# 3. 나누기 연산
division = integer_value / float_value
print(division)  # 출력: 9.876543209876543

# 4. 제곱연산
integer_value2 = int(float_value)
exponential = integer_value2**2
print(exponential)  # 출력: 144

# 5. 나머지 연산
mod = integer_value % int(float_value)
print(mod)  # 출력: 3

# 현재 시간과 분을 더하는 예시
import datetime as dt

current_time = dt.datetime.now()
current_hour = current_time.hour
current_minutes = current_time.minute
sumation = current_hour + current_minutes
print(sumation)  # 출력: 현재 시간과 분의 합

# 2. 문자열(String) 자료형
# 문자, 단어등으로 구성된 집합
aType = "This is 'String' value"
print(aType)  # 출력: This is 'String' value
bType = 'This is "String" value'
print(bType)  # 출력: This is "String" value
cType = """ This is
'String" value"""
print(cType)  # 출력: This is 'String" value

# 문자열 기본 연산
# 문자열 더하기
head = "smart"
tail = "analytics"
fullString = head + " " + tail
print(fullString)  # 출력: smart analytics

# 문자열 곱하기
print("*" * 20)  # 출력: ********************

# 문자열 인덱싱 (0부터 시작)
yearweek = "201801"
print(yearweek[0])    # 출력: 2 (첫번째 문자열)
print(yearweek[0:4])  # 출력: 2018 (0~4번째 전 문자열)
print(yearweek[4:])   # 출력: 01 (4번째부터 끝까지)
print(yearweek[-2])   # 출력: 0 (끝에서 두 번째 문자열)
print(yearweek[-2:])  # 출력: 01 (끝에서 두 번째부터 마지막까지)

# 문자열 자주 사용되는 연산
# 문자열 개수세기 (count)
yearweek = "2017W28"
print(yearweek.count("W"))  # 출력: 1

# 문자열 위치확인 (index)
print(yearweek.index("W"))  # 출력: 4
delimeter = yearweek.index("W")
newYearweek = yearweek[:delimeter] + yearweek[delimeter+1:]
print(newYearweek)  # 출력: 201728

# 대소문자 구별함수 (upper/lower)
letters = "LeD_tv"
print(letters.upper())  # 출력: LED_TV
print(letters.lower())  # 출력: led_tv

# 문자 치환 (replace)
repLetters = "2017W28"
print(repLetters.replace("W", "_"))  # 출력: 2017_28

# 문자 분리 (split)
yearweek_list = yearweek.split("W")
print(yearweek_list)  # 출력: ['2017', '28']

# 실습1: 문자열 분리
testData = "SEC 20180212 250"
testDataSplit = testData.split(" ")
stockname = testDataSplit[0]  # 출력: SEC
date = testDataSplit[1]      # 출력: 20180212
value = testDataSplit[2]     # 출력: 250

# 실습2: 문자열 처리
testData2 = "Sec 2017W28 250"
# TODO: 대문자 변환 및 W 삭제 처리

# 자료형 변환
# 문자 → 수(정수)
strValue = "1234"
cvIntValue = int(strValue)
print(type(cvIntValue))  # 출력: <class 'int'>

# 문자 → 수(실수)
strValue = "1234"
cvFloatValue = float(strValue)
print(type(cvFloatValue))  # 출력: <class 'float'>

# 숫자 → 문자
numberValue = 1234
cvStrValue = str(numberValue)
print(type(cvStrValue))  # 출력: <class 'str'>

# 3. 리스트(List) 자료형
# 특정 집합 모음을 표현할 수 있는 자료형
emptyList = []
priceList = [120, 130, 150, 200, 170]
print(priceList)  # 출력: [120, 130, 150, 200, 170]
secInfo = ["SEC", 120, 130, [201712, 201713]]
print(secInfo)  # 출력: ['SEC', 120, 130, [201712, 201713]]

# 리스트 기본 연산
stockName = ["SEC"]
priceList = [120, 130]
dateList = [201712, 201713]
secinfo = stockName + priceList + [dateList]
print(secinfo)  # 출력: ['SEC', 120, 130, [201712, 201713]]

# 리스트 인덱싱
secinfo = ["SEC", 120, 130, [201712, 201713]]
print(secinfo[1])      # 출력: 120
print(secinfo[3])      # 출력: [201712, 201713]
print(secinfo[3][0])   # 출력: 201712
print(secinfo[0:3])    # 출력: ['SEC', 120, 130]
print(secinfo[-4])     # 출력: SEC (끝에서 4번째 인덱스)

# 리스트 값 수정
updateList = [120, 130, 140, 150]
print(updateList)  # 출력: [120, 130, 140, 150]
updateList[2] = 180
print(updateList)  # 출력: [120, 130, 180, 150]

# 리스트 값 삭제
updateList.remove(130)  # 값 130 삭제
del updateList[2]      # 인덱스 2의 값 삭제

"""### [실습]
[120,150,300,500,1000,100,2000]
값에서 최소 최대 값을 뺀 평균을
average 이름의 변수에 담으세요

풀이#1
"""

test = [120,150,300,500,1000,100,2000]

test.remove(min(test))

test.remove(max(test))

test

average = sum(test)/len(test)

average

"""풀이 #2"""

test = [120,150,300,500,1000,100,2000]

minValueIndex = test.index(min(test))
minValueIndex

del test[minValueIndex]

maxValueIndex = test.index(max(test))
maxValueIndex

del test[maxValueIndex]

test

average =0.0
if len(test)!=0:
  average = sum(test)/len(test)
else:
    average = 1

average

average = sum(test)/len(test)

average

"""# 4. 튜플 (Tuple)"""

emptyTuple = ()
timeTuple = (1,2,3,4,5,6)

"""튜플 기본연산"""

#튜플 인덱싱
timeTuple = (1,2,3,4,5,6)

print(timeTuple[1])
print(timeTuple[3])
print(timeTuple[0:3])

# 튜플 길이
len(timeTuple)

"""# 5. Dictionary

(Key, Value) 형태 자료 구조로 특정년도의 주식명을  키로 요청하면 주가총액을 value로 불러오는 형태
"""

dic = {"name":"sec","id":"3000000","address":"suwon"}

print(dic)

dic.keys()

dic.values()

dic = {"name":"sec", "id":"300000", "address":"suwon" }
print(dic)
print(dic["name"])

# dictionary key value 추가/변경
dic["name"] = "sec2"
dic["stock"] = "yes"
print(dic)
print(dic["stock"])

# dictionary 아이템 삭제하기
dic.pop("name")
print(dic)

"""### [실습]
dic = {"name":"sec","id":"300000","address":"suwon"} 에서
id 키 값을 삭제하여 출력하세요
{'name': 'sec', 'address': 'suwon'}
"""

dic = {"name":"sec","id":"300000","address":"suwon"}

dic.keys()

dic.pop("id")

dic

"""# 5. Pandas Dataframe

행/열 구조의 가장 많이 활용되는 자료구조 형태

### 1. 딕셔너리를 활용한 Pandas DataFrame 생성
"""

# 데이터 프레임 라이브러리 활용
import pandas as pd

# 딕셔너리를 활용한 데이터프레임 생성
data = {'name': ['A고객','B고객','C고객','D고객'],
        'age': [27,40,33,29],
        'stock_age': [2,10,5,1]}
dataFrame = pd.DataFrame(data)

# 데이터 프레임 : 스프레드시트 형태의 자료구조
print(dataFrame)

"""### 2. 리스트를 활용한 Pandas DataFrame 생성"""

import pandas as pd
# 리스트 생성
test = [10,100,1000,10000]
# 데이터프레임 변환
testDf = pd.DataFrame(test)
testDf

testDf.columns=["test"]
testDf

import pandas as pd
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
date2 = ['17.02.29', '17.02.26', '17.02.25', '17.02.24', '17.02.23']

date_df = pd.DataFrame(date, columns=['date2'])
date_df2 = pd.DataFrame(date2, columns=['date23'])

final = pd.concat([date_df,date_df2], axis = 1)
final

"""### [실습]
자신만의 데이터프레임을 생성해보세요
"""

