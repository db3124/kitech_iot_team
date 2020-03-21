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

# 홈
@app.route("/")
def index():
    return "<h1>HOME</h1>"


# 지문인식 로그 읽는 함수
@app.route("/log/fingerprint/<fDate>", methods =['GET'])
def finger_log(fDate):

    data_dic = fDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("finger-"+data_dic+".log", sep=' ', \
                names=['날짜', '시간','로그레벨', '프로세스ID', '일치여부'], \
                header=None)

        # '날짜', '시간', '일치여부' 컬럼만 output
        finger_df = df.loc[:, ['날짜', '시간', '일치여부']]

        return finger_df.to_html(justify='center')
        
    except:
        return "Error"


# 스타일러 로그 읽는 함수
@app.route("/log/styler/<stylerDate>", methods =['GET'])
def styler_log(stylerDate):

    data_dic = stylerDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("styler-"+data_dic+".log", sep=' ', \
                    names=['날짜', '시간','로그레벨', '프로세스ID', '촬영여부'], \
                    header=None)
    
        # '촬영여부' 중 ReadyCapture, CaptureSuccess만 output / Capture, SaveCapture, exit 제외
        df_cond = df[(df['촬영여부'] == 'ReadyCapture') | (df['촬영여부'] == 'CaptureSuccess')]

        # '날짜', '시간', '촬영여부' 컬럼만 output
        styler_df = df_cond.loc[:, ['날짜', '시간', '촬영여부']]

        return styler_df.to_html(justify='center')

    except:
        return "Error"


# 현관문 led 로그 읽는 함수
@app.route("/log/led/<ledDate>", methods =['GET'])
def led_log(ledDate):

    data_dic = ledDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("buttonLed-"+data_dic+".log", sep=' ', \
                    names=['날짜', '시간','로그레벨', '프로세스ID', '점등여부'], \
                    header=None)
    
        # '점등여부' 중 LedOn, LedOff만 output / ReadyLed 제외
        df_cond = df[(df['점등여부'] == 'LedOn') | (df['점등여부'] == 'LedOff')]

        # '날짜', '시간', '점등여부' 컬럼만 output
        led_df = df_cond.loc[:, ['날짜', '시간', '점등여부']]

        return led_df.to_html(justify='center')
        
    except:
        return "Error"  


# CCTV 로그 잆는 함수
@app.route("/log/cctv/<cctvDate>", methods =['GET'])
def cctv_log(cctvDate):

    data_dic = cctvDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("cctv-"+data_dic+".log", sep=' ', \
                    names=['날짜', '시간','로그레벨', '프로세스ID', '라벨', '사진/동영상', '거리', ''], \
                    header=None)
        
        df['사진/동영상'] = df['사진/동영상'].str.replace(
            pat='cheking(', repl='', regex=False)
        df['사진/동영상'] = df['사진/동영상'].str.replace(
            pat='):', repl='', regex=False)

        # '날짜', '시간', '사진/동영상' 컬럼만 output
        cctv_df = df.loc[:, ['날짜', '시간', '사진/동영상']]

        # def color_negative_red(val):
        #     color = 'red' if val == 'Video' else 'black'
        #     return 'color: %s' % color
 
        # cctv_df.style.applymap(color_negative_red)

        return cctv_df.to_html(justify='center')

    except:
        return "Error"


# 온습도 로그 읽는 함수
@app.route("/log/temphumid/<thDate>", methods =['GET'])
def th_log(thDate):

    data_dic = thDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("tempHumid-"+data_dic+".log", sep=' ', \
                    names=['날짜', '시간','로그레벨', '프로세스ID', '온도(℃)', '습도(%)'], \
                    header=None)

        # 온도 컬럼에서 숫자만 빼오기
        df['온도(℃)'] = df['온도(℃)'].str.slice(start=5, stop=-1)

        # 습도 컬럼에서 숫자만 빼오기
        df['습도(%)'] = df['습도(%)'].str.slice(start=9, stop=-1)

        # '날짜', '시간', '온도(℃)', '습도(%)' 컬럼만 output
        th_df = df.loc[:, ['날짜', '시간', '온도(℃)', '습도(%)']]

        return th_df.to_html(justify='center')
        
    except:
        return "Error" 


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