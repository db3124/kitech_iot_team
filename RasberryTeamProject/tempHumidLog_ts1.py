import base64
from io import BytesIO

import pandas as pd
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
        # fig = Figure()
        # ax = fig.subplots()
        fig, ax = plt.subplots()

        # 온도를 그래프로 그림, 선색 지정
        ax.plot(df['Temp'], color='#ff0303')

        # 그래프 타이틀
        font = {'size': 23}
        title = '{}/{}/{}'.format(df.index.year[0], df.index.month[0], df.index.day[0])+'\'s temperature'
        plt.title(title, fontdict=font)

        # x축, y축 라벨
        ax.set_xlabel('Time', size=16)
        ax.set_ylabel('Temperature(℃)', size=16)
        
        # x축 간격 지정, 2분
        minutes = mdates.MinuteLocator(interval = 2)
        m_fmt = mdates.DateFormatter('%H:%M:%S')
        ax.xaxis.set_major_locator(minutes)
        ax.xaxis.set_major_formatter(m_fmt)

        # Show the major grid lines
        plt.grid(b=True, which='major', color='#b3b3b3', linestyle='-')

        # Show the minor grid lines
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#a6a6a6', linestyle='-', alpha=0.2)
        
        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")

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
        # fig = Figure()
        # ax = fig.subplots()
        fig, ax = plt.subplots()

        # 온도를 그래프로 그림, 선색 지정
        ax.plot(df['Humidity'], color='#ff0303')

        # 그래프 타이틀
        title = '{}/{}/{}'.format(df.index.year[0], df.index.month[0], df.index.day[0])+'\'s humidity'
        font = {'size': 23}
        plt.title(title, fontdict=font)

        # x축, y축 라벨
        ax.set_xlabel('Time', size=16)
        ax.set_ylabel('Humidity(%)', size=16)

        # x축 간격 지정, 2분
        minutes = mdates.MinuteLocator(interval = 2)
        m_fmt = mdates.DateFormatter('%H:%M:%S')
        ax.xaxis.set_major_locator(minutes)
        ax.xaxis.set_major_formatter(m_fmt)

        # Show the major grid lines
        plt.grid(b=True, which='major', color='#b3b3b3', linestyle='-')

        # Show the minor grid lines
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#a6a6a6', linestyle='-', alpha=0.2)
        
        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")

        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")

        return f"<img src='data:image/png;base64,{data}'/>"

    except:
        return "Error"


if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
    