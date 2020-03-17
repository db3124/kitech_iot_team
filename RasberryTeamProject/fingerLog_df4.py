import pandas as pd
import datetime
from flask import Flask, request, Response
from flask_cors import CORS
from IPython.display import display

app = Flask(__name__)
CORS(app)

@app.route("/")
def print():
    # 로그파일 불러오기
    df = pd.read_csv("Pandas/2020-03-11.log", sep=' ', \
                 names=['Date', 'Time','LogLevel', 'ProcessID', 'Message', ''], \
                 header=None)
    
    # NaN값 채우기
    df_no_nan = df.fillna('')

    return df_no_nan.to_html()
    

if __name__ == "__main__":              
    app.run()

# date = str(datetime.date.today())

# df = pd.read_csv(date+".log", names=['Time', 'LogLevel', 'ProcessID', 'Message'],header=None)

# df = pd.read_csv("Pandas/2020-03-11.log", sep=' ', \
#                  names=['Date', 'Time','LogLevel', 'ProcessID', 'Message', ''], \
#                  header=None)

# df_no_nan = df.fillna('')

# # print(df_no_nan)
# display(df_no_nan)