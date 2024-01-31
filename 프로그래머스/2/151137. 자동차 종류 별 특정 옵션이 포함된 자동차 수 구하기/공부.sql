# ISSUE
# >>> 최초 IN 절을 사용하여 처리를 하였으나, 데이터가 추출되지 않음
# SCRIPT
# >>> IN 함수의 기능을 찾아보니 입력한 문자열이 포함이 아닌 일치한 경우 추출하도록 되어있음
# DATA = '가나다라마바' 인 경우 IN ('가나다') x / IN ('가나다라마바') O
# 1. LIKE OR 반복
  #반복되는 실수 %가죽시트%를 가죽시트%로 하는 실수들
# 2. REGEXP 정규식 사용하여 처리
SELECT      CAR_TYPE
        ,   COUNT(1) AS  CARS
FROM        CAR_RENTAL_COMPANY_CAR
WHERE       OPTIONS  REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY    CAR_TYPE
ORDER BY    1;
