#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'天级-城市天气-温度-风级'

__author__ = 'anhan'


import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

target_year_list = ["2015", "2016"]
target_month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

def get_urls(city_pinyin):
    urls = []

    for year in target_year_list:
        for month in target_month_list:
            date = year + month
            urls.append("http://www.tianqihoubao.com/lishi/{}/month/{}.html".format(city_pinyin, date))
    # url = "http://www.tianqihoubao.com/lishi/beijing/month/201812.html"
    return urls


def get_soup(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 若请求不成功,抛出HTTPError 异常
        # r.encoding = 'gbk'
        soup = BeautifulSoup(r.text, "html.parser")
        return soup
    # except HTTPError:
    #  return "Request Error"
    except Exception as e:
        print(e)
        pass


def get_data(url):
    print(url)
    try:
        soup = get_soup(url)
        all_weather = soup.find('div', class_="wdetail").find('table').find_all("tr")
        data = list()
        for tr in all_weather[1:]:
            td_li = tr.find_all("td")
            for td in td_li:
                s = td.get_text()
                # print(s.split())
                data.append("".join(s.split()))

        res = np.array(data).reshape(-1, 4)

        return res

    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':

    CITY_NAME = pd.read_csv('CITY_LIST.csv')
    city_pinyin = CITY_NAME['CITY_EN']

    for city in city_pinyin:
        data_ = list()
        urls = get_urls(city)

        for url in urls:
            try:
                data_.extend(get_data(url))  # 列表合并，将某个城市所有月份的天气信息写到data_
            except Exception as e:
                print(e)
                pass

        df = pd.DataFrame(data_, columns=['date', 'tq', 'temp', 'wind'])
        df['CITY_EN']=city

        df.to_csv("./weather_houbao_d_data/"+city+"_houbao_d.csv", index=False)
