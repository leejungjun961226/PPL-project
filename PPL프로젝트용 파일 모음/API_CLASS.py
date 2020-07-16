
import os
import re 
import sys
import pandas as pd
import urllib.request
import json 
import time
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

def convert_strtime(str_time):
    import datetime
    convert_date = datetime.datetime.strptime(str_time, "%Y-%m-%d").date()
    return convert_date

def timeminus(date, days):
    import datetime
    minusdate = date + datetime.timedelta(days=days)
    return str(minusdate)[:10]

# 디폴트 enddate (오늘)
date = convert_strtime(today) 
# 디폴트 startdate (오늘 - 30 )
minusdate = timeminus(date, -30)



class NaverApi():
   
    def __init__(self,searchword='기본',startdate=minusdate,enddate=today):
        self.searchword = searchword
        self.startdate = startdate
        self.enddate = enddate 
        self.dt_index = pd.date_range(start=startdate, end=enddate)
        self.dt_list = self.dt_index.strftime("%Y%m%d").tolist()
   
        # 네이버 API 접근 계정
        client_id = "AVhdmntSqAjNNYaVEUMZ"
        client_secret = "S_sUCMIcai"


        # URL
        url = "https://openapi.naver.com/v1/datalab/search"

        # 질의문
        body = "{\"startDate\":\"%s\",\
                \"endDate\":\"%s\",\
                \"timeUnit\":\"date\",\
                \"keywordGroups\":[{\
                \"groupName\":\"%s\",\
                \"keywords\":[\"%s\"]}]}" %(startdate,enddate,searchword,searchword)


        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        request.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(request, data=body.encode("utf-8")) 
   
        self.data = json.loads(response.read())
     
        self.rescode = response.getcode()

    def set_startdate(self,startdate):
        self.startdate = startdate

    def set_enddate(self,enddate):
        self.enddate = enddate
        
    def search(self,searchword):
        self.searchword = searchword
        startdate=self.startdate
        enddate =self.enddate
        self.dt_index = pd.date_range(start=startdate, end=enddate)
        self.dt_list = self.dt_index.strftime("%Y%m%d").tolist()
   
        # 네이버 API 접근 계정
        client_id = "I4Fva_A2tRCvTccEOaAX"
        client_secret = "jC5ic5g9wu"


        # URL
        url = "https://openapi.naver.com/v1/datalab/search"

        # 질의문
        body = "{\"startDate\":\"%s\",\
                \"endDate\":\"%s\",\
                \"timeUnit\":\"date\",\
                \"keywordGroups\":[{\
                \"groupName\":\"%s\",\
                \"keywords\":[\"%s\"]}]}" %(startdate,enddate,searchword,searchword)


        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        request.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(request, data=body.encode("utf-8")) 
   
        self.data = json.loads(response.read())
     
        self.rescode = response.getcode() 

        

    def get_data(self):
        if(self.rescode==200):
            return(self.data)
        else:
            print('API request ERROR')
            
    def get_keyword(self):
        return(self.searchword)


    def get_missingdate(self):
        missing_date = []
        result_date = []
        result = self.data['results'][0]['data']
        for period in result:
            result_date.append(period['period'].replace('-',''))
             
        
        for i in range(1,len(self.dt_list)):
            if self.dt_list[i] not in result_date:
                missing_date.append(self.dt_list[i])
        missing_date = "Date Missing on {}".format(missing_date)
        return(missing_date)
        

    def get_period(self):
        date_period = self.date_period = []
        result = self.data['results'][0]['data']
        for period in result:
            period= period['period'] 
            date_period.append(period.replace('-',''))
        return(date_period)

    def get_rate(self):
         date_ratio = self.date_ratio = [] 
         result = self.data['results'][0]['data']
         for rate in result:
             rate = rate['ratio']
             date_ratio.append(rate)
         return(date_ratio)

        


    def to_dataframe(self):
        result_ratio = []
        result = self.data['results'][0]['data']
        for rate in result:
            rate = rate['ratio']
            result_ratio.append(rate)

        result_date = []
        result = self.data['results'][0]['data']
        for period in result:
            period= period['period'] 
            result_date.append(period.replace('-',''))

        
        dt_list = self.dt_list 
 
        df = pd.DataFrame(columns=['날짜','비율'])

       
        for i in range(0,len(result_ratio)):
            df = df.append(
            {
                '날짜' : result_date[i],
                '비율' : result_ratio[i]

            }, ignore_index=True 
            )
       
            

        # 전체 날짜 가지고 있는 값없는 df
        df2 = pd.DataFrame(columns=['날짜','비율'])
        for i in range(0,len(dt_list)):
                df2 = df2.append(
                {
                    '날짜': dt_list[i]
                }, ignore_index=True 
                )
    

        df_final = pd.merge(df,df2,on='날짜',how='right')
         
        df_final = df_final.sort_values(['날짜'],ascending=[True])
        df_final = df_final.drop('비율_y',axis=1)

        df_final = df_final.set_index('날짜')
        df_final = df_final.astype(float).fillna(0)
        return(df_final)
    
    def to_excel(self,filepath):
        df = self.to_dataframe()
        df.to_excel(filepath, encoding='UTF-8')
        return(df)
    
    def to_csv(self,filepath):
        df = self.to_dataframe()
        df.to_csv(filepath, encoding='ms949')
        return(df)


                

       

if __name__ == '__main__':

    na = NaverApi('달고나','2019-06-11','2020-06-11')    
    print(na.to_dataframe())
   