# -*- coding: utf-8 -*-

'''
todo：
'''

__author__ = 'anhan'

import math
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
import datetime
from textwrap import wrap
import xgboost as xgb
import lightgbm as lgb
import copy
import re

import seaborn as sns




'''
time:
month-hour_n
'''
def get_pic_time_hour_n_month(dataset):
    sns.set_style('ticks')
    sns.set_context("notebook", font_scale= 1.4)
    plt.figure(figsize = (18,8))
    day_n_2015=dataset[dataset.year==2015].groupby(['month'], as_index=False)['hour_n'].sum()
    day_n_2016=dataset[dataset.year==2016].groupby(['month'], as_index=False)['hour_n'].sum()
    # print(day_n_2016.hour_n)
    plt.plot(['201507','201508','201509','201510','201511','201512','201601','201602','201603','201604','201605','201606','201607','201608','201609','201610'],
             [1159,5250,1504,320,6578,2348,16327.089986,6410.681326,5877.192726,357.169923,4568.681328,8251.530944,38329.105548,41013.751386,25426.591288,7940.945990],
             linestyle='-.', color='b',label = 'count of  pay')
    plt.yscale('log') #y用对数展示
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.legend() #显示图例
    plt.savefig('./pic_time_hour_n_month.jpg')


def get_pic_time_hour_n_hour(dataset):
    # 提取出每小时需求均值
    dataset['number of pay']=dataset['hour_n']
    Hour_tendency=dataset.groupby('hour')[['number of pay']].mean()
    # 绘制图像
    sns.set_style('ticks')
    sns.set_context("notebook", font_scale= 1.4)
    Hour_tendency.plot(linestyle='--',color='b',figsize=(12,6))
    # plt.title('Hour Pay Tendency',fontsize=15)
    # plt.grid(linestyle='--',alpha=0.8)
    # plt.ylim(0,550)
    plt.xlabel('Hour',fontsize=13)
    plt.ylabel('Count',fontsize=13)
    plt.legend()  # 显示图例
    plt.savefig('./pic_time_hour_n_hour.jpg')

def get_pic_time_hour_n_holi(dataset):
    dataset['holiday_type']=dataset['holi']
    plt.figure(figsize=(12,6))
    sns.pointplot(x='hour',y='hour_n',hue='holiday_type',data=dataset,linestyle=['--','-.','-'],markers=["*","x","o"],ci=0)
    plt.xlabel('Hour',fontsize=13)
    plt.ylabel('Count',fontsize=13)
    plt.grid(linestyle='--',alpha=0.5)
    plt.savefig('./pic_time_hour_n_holi.jpg')


def get_pic_weather_hour_n_temp_speed_humi_pres(dataset):
    # 温度与风速的关系度量
    plt.figure(figsize=(10, 6))
    sns.kdeplot(dataset['h_temp'], dataset['h_wind_speed'], shade=True, shade_lowest=False, cut=10, cmap='YlGnBu', cbar=True)
    sns.despine(left=True)
    plt.grid(linestyle='--', alpha=0.4)
    plt.xlabel('Temperature', fontsize=13)
    plt.ylabel('Windspeed', fontsize=13)
    plt.savefig('./pic_weather_hour_n_temp_speed.jpg')

    plt.figure(figsize=(10, 6))
    sns.kdeplot(dataset['h_temp'], dataset['h_humidity'], shade=True, shade_lowest=False, cut=10, cmap='YlGnBu', cbar=True)
    sns.despine(left=True)
    plt.grid(linestyle='--', alpha=0.4)
    plt.xlabel('Temperature', fontsize=13)
    plt.ylabel('Humudity', fontsize=13)
    plt.savefig('./pic_weather_hour_n_temp_humi.jpg')

    plt.figure(figsize=(10, 6))
    sns.kdeplot(dataset['h_temp'], dataset['h_pressure'], shade=True, shade_lowest=False, cut=10, cmap='YlGnBu', cbar=True)
    sns.despine(left=True)
    plt.grid(linestyle='--', alpha=0.4)
    plt.xlabel('Temperature', fontsize=13)
    plt.ylabel('Pressure', fontsize=13)
    plt.savefig('./pic_weather_hour_n_temp_pres.jpg')



if __name__ == '__main__':
    dataset = pd.read_csv('ijcai17_context_merge_d_zh_visual.csv')
    # print(dataset.columns)
    '''
    ['year', 'month', 'day', 'hour','hour_n', 'holi', 'h_temp', 'h_humidity','h_pressure', 'h_wind_speed']
    '''

    # get_pic_time_hour_n_month(dataset)
    # get_pic_time_hour_n_hour(dataset)
    # get_pic_time_hour_n_holi(dataset)
    get_pic_weather_hour_n_temp_speed_humi_pres(dataset)



