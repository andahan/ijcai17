#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

__author__ = 'anhan'

df_full = pd.read_csv('./weather_houbao_d_full.csv')
df_precip = pd.read_csv('./PRECIP.csv')
print(len(df_full))

df_new=df_full.dropna()
df_new=df_new.drop_duplicates()

print(len(df_new))

# df_new.to_csv('./weather_houbao_d_full.csv',index=False)
