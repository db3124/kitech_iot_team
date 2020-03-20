import base64
from io import BytesIO

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from datetime import datetime

from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/log/temp/graph/<thDate>", methods=['GET'])
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
        fig = Figure()
        ax = fig.subplots()
        ax.plot(df['Temp'])
        ax.set_xlabel('Time')
        ax.set_ylabel('Temprature(℃)')

        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")

        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")

        return f"<img src='data:image/png;base64,{data}'/>"

    except:
        return "Error"


@app.route("/log/humidity/graph/<thDate>", methods=['GET'])
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
        fig = Figure()
        ax = fig.subplots()
        ax.plot(df['Humidity'])
        ax.set_xlabel('Time')
        ax.set_ylabel('Humidity(%)')

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
    