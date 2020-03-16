import pandas as pd
import datetime
from flask import Flask, request, Response
from flask_cors import CORS
from IPython.display import display

app = Flask(__name__)
CORS(app)

@app.route("/<fingerDate>")
def print(fingerDate):
    data_dic = {'fd':fingerDate} 

    # 로그파일 불러오기
    df = pd.read_csv("Pandas/"+data_dic+".log", sep=' ', \
                 names=['Date', 'Time','LogLevel', 'ProcessID', 'Message', ''], \
                 header=None)
    
    # NaN값 채우기
    df_no_nan = df.fillna('')

    return df_no_nan.to_html()

if __name__ == "__main__":              
    app.run()
