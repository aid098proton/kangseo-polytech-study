### 가격: 가격, 프로모션 정보 활용 비율 계산
# price....
price = 5000
promtion = 500

# 할인율이 30%인 경우
price = 1000
promotion = 0.3
price * promotion  # 300.0 출력

print("파이썬 기초 프로그램 스마트금융과_김효관")

# 1.자료형
a = "10"
b = "5"
a + b  # "105" 출력 (문자열 연결)

# 할인 가격 계산
orgPrice = 3000
promotionRation = 0.2
## 할인 가격
discountPrice = orgPrice * promotionRation  # 600.0
## 최종 가격
finalPrice = orgPrice - discountPrice  # 2400.0
print(finalPrice)

# 변수명은 대소문자 구분
orgPrice = 3000
ORGPRICE = 5000

print(orgPrice)  # 3000
print(ORGPRICE)  # 5000

# 숫자형 자료형
intValue = 10
floatValue = 10.5

# 더하기 연산
sumValue = intValue + floatValue  # 20.5
# 빼기 연산
minusValue = intValue - floatValue  # -0.5
# 나누기 연산
divValue = intValue / floatValue  # 0.9523809523809523
# 곱하기 연산
multiValue = intValue * floatValue  # 105.0

# print(sumValue)
# print(divValue)
# print(multiValue)
# print(minusValue)

# type(sumValue)  # <class 'float'>

# 나머지 연산을 잘 활용하면 패턴을 잡아낼 수 있다.
targetWeek = 10
pattern = 4
# 타겟주차를 패턴으로 나눈 나머지가 0인 경우에만 공급
targetWeek % pattern  # 2 출력

# 제곱 연산
expValue = intValue ** 2  # 100
expValue

# 현재 시간과 분을 입력값으로 받아서
# 두개의 값을 더하는 연산을 수행하세요.
hour = 10
minute = 36
sum = hour + minute  # 46

# 현재시간과 분을 더하는 연산
currentHour = 10
currentMin = 41
totalHour = currentHour + currentMin  # 51
totalHour

# 시간 계산 라이브러리
import datetime
# 현재 날짜 정보 라이브러리 활용해서 가지고 오기.
currentDate = datetime.datetime.now()
currentHour = currentDate.hour
currentMin = currentDate.minute
print(currentHour)  # 현재 시간 출력
print(currentMin)  # 현재 분 출력

# !pip install fintechlab  # 주석 처리된 설치 명령어

# 문자열 연산
stringValue = "smartFinance"
type(stringValue)  # <class 'str'>
headChar = "smart"
tailChar = "Financa"
headChar + tailChar  # "smartFinanca"

# 인덱싱
currYearweek = "202509"
yearTerm = 4

currYear = currYearweek[:yearTerm]  # currYearweek[0:yearTerm] # '2025'
currWeek = currYearweek[yearTerm:]  # '09'
print(currYear)  # 2025
print(currWeek)  # 09

# 검색 문자 찾기 (몇 번 등장하는지) count
targetLetters = "LED_LED_TV"
serchWord = "LED_"
targetLetters.count(serchWord)  # 2

# 원하는 문자의 인덱스 가져오기
# inYearweek = "2025W09"
inYearweek = "10001w09"  # 만약 'W' 를 'w' 로 하게 되면 오류가 발생한다.

# 전처리 : 입력값 대문자로 변경
inYearweek = inYearweek.upper()  # "10001W09"

# 원하는 문자의 인덱스 가져와서 연도 주차정보 획득
delimeter = "W"
delimeterIndex = inYearweek.index(delimeter)

inYear = inYearweek[:delimeterIndex]  # "10001"
inWeek = inYearweek[delimeterIndex + 1:]  # "09"

print("현재 주차는 모르겠습니다.")
print(f"현재 주차는 {inWeek} 입니다.")  # 현재 주차는 09 입니다.

# 모든 구분자는"_" 로 변경한다.
# replace 함수 : 타겟값을 원하는 값으로 변경
targetYearweek = "2025/09"
orgDelimeter = "/"
newDelimeter = "_"
targetYearweek = targetYearweek.replace(orgDelimeter, newDelimeter)  # "2025_09"
targetYearweek

# split 특정 값으로 분리시켜라!!!
targetYearweek = "2025W09"
targetYearweek = targetYearweek.upper()

specificChar = "W"
resultValue = targetYearweek.split(specificChar)  # ['2025', '09']
resultValue

# 문자열 슬라이싱
targetValue = 202522
targetValue = str(targetValue)
targetValue[0:4]  # targetValue[:4]  # "2025"
targetValue[4:]  # "22"

# 숫자형 변환
targetValue = "202522"
yearValue = str(int(targetValue) / 100)  # "2025.22"
yearValue

targetValue = "202522"
intValue = int(targetValue)  # 202522
floatValue = float(intValue)  # 202522.0
floatValue