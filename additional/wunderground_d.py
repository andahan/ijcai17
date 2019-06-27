# -*- coding: utf-8 -*-
"""
【天级城市天气】机场代码-日期-降水量-日出-日落
input file:CITY_LIST.csv
output file: ./wunderground_precip_d/机场代码_d.csv ————> PRECIP.csv
output:[Port,Date,Precip, Rise_act,Rise_cil,Set_act,Set_cil]
ZSSS,2015-05-01,0.0,5:10 AM CST,4:45 AM CST,6:33 PM CST,6:59 PM CST,shanghai
"""

#%%
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import numpy as np

CITY_NAME = pd.read_csv('CITY_LIST.csv')
PORT_NAME = CITY_NAME[['AIRPORT_CODE','PORT']].groupby('AIRPORT_CODE',as_index=False).count()
for ind,value in PORT_NAME.iterrows():
    print(value['AIRPORT_CODE'])
#%%
    Port = []
    Date =[]
    Precip = []
    Rise_act = []
    Rise_cil = []
    Set_act = []
    Set_cil = []

    for vYear in range(2015, 2017):
        if vYear == 2015:
            Monthrange = np.arange(5, 13)
            if (value['AIRPORT_CODE']=='ZSJN'):
                Monthrange = np.arange(7, 13)               
        else:
            Monthrange = np.arange(1, 13)
        for vMonth in Monthrange:
            for vDay in range(1, 32):
                if vYear % 4 == 0:
                    if vMonth == 2 and vDay > 29:
                        break
                else:
                    if vMonth == 2 and vDay > 28:
                        break
                if vMonth in [4, 6, 9, 11] and vDay > 30:
                    break
        #%%
                
                theDate = str(vYear) + "/" + str(vMonth) + "/" + str(vDay)
                # print(theDate)
                theDate2 = str(vYear) + "-" + str(vMonth).zfill(2) + "-" + str(vDay).zfill(2)
                print(theDate2)
                theport = value['AIRPORT_CODE']
                print(theport)
                 
                
                theurl = "http://www.wunderground.com/history/wmo/"+ theport +"/" + theDate + "/DailyHistory.html?MR=1"

                # 头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
                req = urllib.request.Request(url=theurl, headers=headers)

                thepage = urllib.request.urlopen(req)
                soup = BeautifulSoup(thepage, "html.parser")
                # print(soup)
                
                soup_detail = soup.find_all('tr')
                
                for soup_detail_row in np.arange(len(soup_detail)):                   
                    if soup_detail[soup_detail_row].text.strip()=='Precipitation':
                        Precip.append( soup_detail[soup_detail_row+1].find_all('td')[1].text.strip() ) 
                        break
                    
                # soup_detail_ast = soup.find_all('div',{"class":"wx-module simple","id":"astronomy-mod"})[0]
                # Port.append(theport)
                # Date.append(theDate2)
                # Rise_act.append(soup_detail_ast.find_all('td')[1].text.strip() )
                # Set_act.append(soup_detail_ast.find_all('td')[2].text.strip() )
                # Rise_cil.append(soup_detail_ast.find_all('td')[4].text.strip() )
                # Set_cil.append(soup_detail_ast.find_all('td')[5].text.strip() )
                

    Port = pd.DataFrame(Port, columns=['Port'])    
    Date = pd.DataFrame(Date, columns=['Date'])               
    Precip = pd.DataFrame(Precip, columns=['Precip'])
    # Rise_act = pd.DataFrame(Rise_act, columns=['Rise_act'])
    # Rise_cil = pd.DataFrame(Rise_cil, columns=['Rise_cil'])
    # Set_act = pd.DataFrame(Set_act, columns=['Set_act'])
    # Set_cil = pd.DataFrame(Set_cil, columns=['Set_cil'])
    
    
    sub_result = pd.concat([Port,Date,Precip, Rise_act,Rise_cil,Set_act,Set_cil  ], axis = 1)
    file_name = './wunderground_precip_d/'+value.AIRPORT_CODE + '_d.csv'
    sub_result.to_csv(file_name,index = False)
    
