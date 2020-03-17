import pandas as pd
import datetime
from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS
from IPython.display import display

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/stylerDate/<stylerDate>", methods =['GET'])
def date(stylerDate):
    data_dic = stylerDate

    # 로그파일 불러오기
    df = pd.read_csv("styler-"+data_dic+".log", sep=' ', \
                 names=['날짜', '시간','로그레벨', '프로세스ID', '일치여부'], \
                 header=None)
    
    # 로그의 일치여부 중 ReadyCapture, CaptureSuccess만 output
    condition = df[(df['일치여부'] == 'ReadyCapture') | (df['일치여부'] == 'CaptureSuccess')]

    # '날짜', '시간', '일치여부' 컬럼만 output
    styler_df = condition.loc[:, ['날짜', '시간', '일치여부']]

    if df is None:
        return 'Error'  

    if styler_df is None:
        return "Error"
    else:
        return styler_df.to_html(justify='center')

if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
