from googletrend import googletrend
import pandas as pd
import datetime
import json

def convert_strtime(str_time):
    import datetime
    convert_date = datetime.datetime.strptime(str_time, "%Y-%m-%d").date()
    return convert_date

def timeminus(date, days=30):
    import datetime
    minusdate = date + datetime.timedelta(days=days)
    return str(minusdate)[:10]

#glowpick 엑셀데이터 불러오기
df_raw = pd.read_excel('7. 데이터 활용 매뉴얼 - 방송정보메타데이타샘플.xls')
#print(df.head())
#print(df_raw[['방송일','브랜드','품목']].head())
df = df_raw[['방송일','브랜드','품목']]

#적재할 빈데이터프레임
result = pd.DataFrame(index=range(0,61))

#여기서 부터 줄마다 for 문 돌리기, 입력변수 1. 날짜간격.
for i, row in df.iterrows():
    
    #적재할 빈데이터프레임
    #columns=['idx', 'number'])

    #api에 넘길 시작일, 종료일 계산하기
    today = convert_strtime(row['방송일'])
    start_date , enddate = timeminus(today, -30), timeminus(today, 30)
    #print(start_date, enddate)

    #브랜드+품목명 네이버 검색
    keyword = row['브랜드']+' '+row['품목']
    print(keyword)
    try:
        naver_data1 =  googletrend([keyword], start_date, enddate)
        result[keyword]=naver_data1.reset_index(drop=True)
    except:
        continue

    #naver_data1 = naver_data1.reset_index(drop=True)
    

    #품목으로 네이버 검색
    keyword = row['상품명']
    print(keyword)
    try:
        naver_data1 =  googletrend([keyword], start_date, enddate)
        result[keyword]=naver_data1.reset_index(drop=True)
    except:
        continue
    
    #print(len(naver_data1))
result.to_csv('google.csv',encoding='utf-8-sig')
