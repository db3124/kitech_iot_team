import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 로그파일 불러오기
df = pd.read_csv("tempHumid-2020-03-18.log",
                    names=['Datetime', 'etc'],
                    header=None, index_col='Datetime')
        
# 인덱스를 datetimeindex로 바꾸기
df.index = pd.to_datetime(df.index)

# etc 컬럼 나누기
df[['etc1', 'etc2', 'etc3', 'Temp', 'Humidity']] = \
        df['etc'].str.split(' ', n=5, expand=True)

# Temp 컬럼에서 숫자만 빼오기, str->numeric
df['Temp'] = df['Temp'].str.slice(start=5, stop=-1)
df['Temp'] = df['Temp'].apply(pd.to_numeric)

df_cond = df[df['Temp'] == df['Temp'].max()]
df_max = df_cond.loc[:, ['Temp']]
max_idx = mpl.dates.date2num(df_max.index.to_pydatetime())
print(len(max_idx))
print(max_idx)

# 최고점, 최저점 그래프상에 표시하기
# idx_float = mpl.dates.date2num(df.index.to_pydatetime())
# plt.annotate('Peak', xy=(idx_float, df['Temp']))
# plt.annotate('Peak',  xy=(0, df['Temp'].min()))