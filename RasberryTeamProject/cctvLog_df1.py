import pandas as pd
import datetime
from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/log/<cctvDate>", methods =['GET'])
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

if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
