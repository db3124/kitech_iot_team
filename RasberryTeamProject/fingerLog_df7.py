import pandas as pd
import datetime
from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/log/<fDate>", methods =['GET'])
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

if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
    