import pandas as pd
import datetime
from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS
from IPython.display import display

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/ledDate/<ledDate>", methods =['GET'])
def date(ledDate):
    data_dic = ledDate

    # 로그파일 불러오기
    df = pd.read_csv("buttonLed-"+data_dic+".log", sep=' ', \
                 names=['날짜', '시간','로그레벨', '프로세스ID', '일치여부'], \
                 header=None)
    
    # 로그의 일치여부 중 LedOn, LedOff만 output
    led_df = df[(df['일치여부'] == 'LedOn') | (df['일치여부'] == 'LedOff')]
    # condition2 = df[df['일치여부']=='LedOff']
    # led_df = df[condition1]

    # led_df = df[df['일치여부']=='LedOn']

    if df is None:
        return 'Error'  
    
    # url = 'http://192.168.0.23:8080/smarthome/fingerprint/userFingerprintLog'

    # files = {'fingerprint':open(df_no_nan.to_html(), 'rb')}
    # data = {'fingerprint':df_no_nan.to_html()}
    # r = requests.post(url, data=data)
    # r.text
    # print(r.text)

    if led_df is None:
        return "Error"
    else:
        return led_df.to_html(justify='center')

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error':'not used date'}))
    

if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
