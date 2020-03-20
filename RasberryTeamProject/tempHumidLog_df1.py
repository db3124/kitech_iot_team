import pandas as pd
import datetime
from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/log/<thDate>", methods =['GET'])
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

if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)