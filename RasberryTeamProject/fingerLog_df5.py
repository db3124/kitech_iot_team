import pandas as pd
import datetime
from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/fingerDate/<fDate>", methods =['GET'])
def date(fDate):
    data_dic = fDate

    # pd.set_option('colheader_justify', 'center')

    # 로그파일 불러오기
    df = pd.read_csv(data_dic+".log", sep=' ', \
                 names=['날짜', '시간','로그레벨', '프로세스ID', '일치여부'], \
                 header=None)

    # 로그의 일치여부 중 (  )만 output
    # condition = df[df['일치여부'] == 'match']

    # '날짜', '시간', '일치여부' 컬럼만 output
    finger_df = df.loc[:, ['날짜', '시간', '일치여부']]

    # NaN값 채우기
    # df_no_nan = df.fillna('')

    if df is None:
        return 'Error'  
    
    if finger_df is None:
        return "Error"
    else:
        return finger_df.to_html(justify='center')

    # url = 'http://192.168.0.23:8080/smarthome/fingerprint/userFingerprintLog'

    # files = {'fingerprint':open(df_no_nan.to_html(), 'rb')}
    # data = {'fingerprint':df_no_nan.to_html()}
    # r = requests.post(url, data=data)
    # r.text
    # print(r.text)

    

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error':'not used date'}))
    

if __name__ == "__main__":              
    app.run(host="192.168.0.24", port=5000, debug=False)
