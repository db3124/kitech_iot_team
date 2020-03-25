import base64
from io import BytesIO

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.dates as mdates

from datetime import datetime

from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/log/t-graph/<thDate>", methods=['GET'])
def t_time(thDate):

    data_dic = thDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("tempHumid-"+data_dic+".log",
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

        # Generate the figure **without using pyplot**.
        fig, ax = plt.subplots()
        
        # 습도를 그래프로 그림, 선색 지정
        ax.plot(df['Temp'], color='#ff0303')

        # 그래프 타이틀
        title = '{}.{}.{}'.format(df.index.year[0], df.index.month[0], df.index.day[0])\
            +'\'s temperature\n'\
            +'──────────────────────\n'\
            +'Highest: {}℃ / '.format(df['Temp'].max())\
            +'Lowest: {}℃'.format(df['Temp'].min())
           
        font = {'size': 20}
        plt.title(title, fontdict=font)

        # x축, y축 라벨
        ax.set_xlabel('Time', size=16)
        ax.set_ylabel('Temperature(℃)', size=16)
        
        # 주석 달았을 때 그래프 밖으로 삐져 나오는 것 방지
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        # x축 간격 지정, 5분
        hours = mdates.HourLocator(interval = 1)
        h_fmt = mdates.DateFormatter('%H:%M:%S')
        ax.xaxis.set_major_locator(hours)
        ax.xaxis.set_major_formatter(h_fmt)

        # Show the major grid lines
        plt.grid(b=True, which='major', color='#b3b3b3', linestyle='-')

        # # Show the minor grid lines
        # plt.minorticks_on()
        # plt.grid(b=True, which='minor', color='#a6a6a6', linestyle='--', alpha=0.1)
        
        # 최고 온도일 때 주석
        # df_cond_max = df[df['Temp'] == df['Temp'].max()]
        # df_max = df_cond_max.loc[:, ['Temp']]
        # max_idx = mpl.dates.date2num(df_max.index.to_pydatetime())
        # 최고 온도가 2개 이상일 때 처리
        # arrowprops = dict(arrowstyle="->")
        # for i in range(0, len(max_idx)):
        #     plt.annotate('{}'.format(df['Temp'].max()),\
        #         xy=(max_idx[i], df['Temp'].max()),\
        #         xytext=(max_idx[i]+0.0005, df['Temp'].max()),\
        #         horizontalalignment='left', verticalalignment='top', color='#154a31'
        #         )

        # 최저 온도일 때 주석
        # df_cond_min = df[df['Temp'] == df['Temp'].min()]
        # df_min = df_cond_min.loc[:, ['Temp']]
        # min_idx = mpl.dates.date2num(df_min.index.to_pydatetime())
        # 최저 온도가 2개 이상일 때 처리
        # for i in range(0, len(min_idx)):
        #     plt.annotate('{}'.format(df['Temp'].min()),\
        #         xy=(min_idx[i], df['Temp'].min()),\
        #         xytext=(min_idx[i]+0.0005, df['Temp'].min()),\
        #         horizontalalignment='left', verticalalignment='top', color='#154a31',
        #         )

        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.set_size_inches(12, 9)
        fig.savefig(buf, format="png", dpi=70)

        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")

        return f"<img src='data:image/png;base64,{data}'/>"

    except: 
        return "Error"


@app.route("/log/h-graph/<thDate>", methods=['GET'])
def h_time(thDate):

    data_dic = thDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("tempHumid-"+data_dic+".log",
                    names=['Datetime', 'etc'],
                    header=None, index_col='Datetime')
        
        # 인덱스를 datetimeindex로 바꾸기
        df.index = pd.to_datetime(df.index)

        # etc 컬럼 나누기
        df[['etc1', 'etc2', 'etc3', 'Temp', 'Humidity']] = \
            df['etc'].str.split(' ', n=5, expand=True)

        # Humidity 컬럼에서 숫자만 빼오기, str->numeric
        df['Humidity'] = df['Humidity'].str.slice(start=9, stop=-1)
        df['Humidity'] = df['Humidity'].apply(pd.to_numeric)

        # Generate the figure **without using pyplot**.
        fig, ax = plt.subplots()
        
        # 습도를 그래프로 그림, 선색 지정
        ax.plot(df['Humidity'], color='#ff0303')

        # 그래프 타이틀
        title = '{}.{}.{}'.format(df.index.year[0], df.index.month[0], df.index.day[0])\
            +'\'s humidity\n'\
            +'──────────────────────\n'\
            +'Highest: {}% / '.format(df['Humidity'].max())\
            +'Lowest: {}%'.format(df['Humidity'].min())
           
        font = {'size': 20}
        plt.title(title, fontdict=font)

        # x축, y축 라벨
        ax.set_xlabel('Time', size=16)
        ax.set_ylabel('Humidity(%)', size=16)

        # 주석 달았을 때 그래프 밖으로 삐져 나오는 것 방지
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        # x축 간격 지정, 5분
        hours = mdates.HourLocator(interval = 1)
        h_fmt = mdates.DateFormatter('%H:%M:%S')
        ax.xaxis.set_major_locator(hours)
        ax.xaxis.set_major_formatter(h_fmt)

        # Show the major grid lines
        plt.grid(b=True, which='major', color='#b3b3b3', linestyle='-')

        # Show the minor grid lines
        # plt.minorticks_on()
        # plt.grid(b=True, which='minor', color='#a6a6a6', linestyle='--', alpha=0.2)
        
        # # 최고 습도일 때 주석
        # df_cond_max = df[df['Humidity'] == df['Humidity'].max()]
        # df_max = df_cond_max.loc[:, ['Humidity']]
        # max_idx = mpl.dates.date2num(df_max.index.to_pydatetime())
        # arrowprops = dict(arrowstyle="->")
        # # 최고 습도가 2개 이상일 때 처리
        # for i in range(0, len(max_idx)):
        #     plt.annotate('{}'.format(df['Humidity'].max()),\
        #         xy=(max_idx[i], df['Humidity'].max()),\
        #         xytext=(max_idx[i]+0.0005, df['Humidity'].max()),\
        #         horizontalalignment='left', verticalalignment='top', color='#154a31',\
        #         arrowprops=arrowprops, va='center')

        # # 최저 습도일 때 주석
        # df_cond_min = df[df['Humidity'] == df['Humidity'].min()]
        # df_min = df_cond_min.loc[:, ['Humidity']]
        # min_idx = mpl.dates.date2num(df_min.index.to_pydatetime())
        # # 최저 습도가 2개 이상일 때 처리
        # for i in range(0, len(min_idx)):
        #     plt.annotate('{}'.format(df['Humidity'].min()),\
        #         xy=(min_idx[i], df['Humidity'].min()),\
        #         xytext=(min_idx[i]+0.0005, df['Humidity'].min()),\
        #         horizontalalignment='left', verticalalignment='top', color='#154a31',\
        #         arrowprops=arrowprops, va='center')

        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.set_size_inches(12, 9)
        fig.savefig(buf, format="png", dpi=70)

        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")

        return f"<img src='data:image/png;base64,{data}'/>"

    except:
        return "Error"


if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
    