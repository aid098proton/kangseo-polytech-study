# 2025년도 01 주차 부터 202540주차까지에서 4주 패턴으로 물량을 공급한다.
# 따라서 (예 "202504 주차 공급") 이라고 출력되도록 코드를 개발하시오.

# 시작 주차와 종료 주차 설정
startYearWeek = 202501
endYearWeek = 202541

# 주차 리스트 생성
yearWeekList = list(range(startYearWeek, endYearWeek))
yearWeekListLen = len(yearWeekList)

# 각 주차별 공급 여부 확인 및 출력
for i in range(0, yearWeekListLen):
    # 2025 다음 두 글자를 추출한다.
    yearWeek = str(yearWeekList[i])
    week = yearWeek[-2:]

    # 추출 한 두 글자를 정수로 변환하여 나머지 연산으로 4주차를 확인한다.
    if int(week) % 4 == 0:
        print(f'{yearWeek} 주차 공급')
    else:
        print(f'{yearWeek} 주차 공급 안함')
