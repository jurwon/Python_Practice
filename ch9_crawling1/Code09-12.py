import csv
import time
import datetime
# 시스템의 날짜 및 시간을  -> csv 파일 저장.

csvName = 'C:/PythonTest/Python_note/ch9_crawling1/datetime_231208.csv'
#파이썬 키워드 with 시작한다. 기능 -> 파일 입출력하기 위한 객체 필요
#해당 객체를 이용 후 자원 반납
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초'])

count = 10
while count > 0:
    count -= 1

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss]
    #출력형식 2가지 1)콘솔에 출력
    print(time_list)

    # 2) csv 파일에 출력함. 내용 저장
# 날짜 , 시간의 내용을 쓰는 작업. a : 추가하기.
#csvFp : 파일 포인터
    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(time_list)

    time.sleep(3)