import pandas as pd
import datetime
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

    # pd.set_option('colheader_justify', 'center')

    try:
        # 로그파일 불러오기
        df = pd.read_csv(data_dic+".log", sep=' ', \
                names=['날짜', '시간','로그레벨', '프로세스ID', '일치여부'], \
                header=None)
        # '날짜', '시간', '일치여부' 컬럼만 output
        finger_df = df.loc[:, ['날짜', '시간', '일치여부']]

        return finger_df.to_html(classes="mystle")
        
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
    
        # 로그의 일치여부 중 ReadyCapture, CaptureSuccess만 output
        df_cond = df[(df['촬영여부'] == 'ReadyCapture') | (df['촬영여부'] == 'CaptureSuccess')]

        # '날짜', '시간', '일치여부' 컬럼만 output
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
    
        # 로그의 일치여부 중 LedOn, LedOff만 output
        df_cond = df[(df['점등여부'] == 'LedOn') | (df['점등여부'] == 'LedOff')]

        # '날짜', '시간', '일치여부' 컬럼만 output
        led_df = df_cond.loc[:, ['날짜', '시간', '점등여부']]

        return led_df.to_html(justify='center')
        
    except:
        return "Error"


if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
