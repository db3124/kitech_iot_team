import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime

from flask import Flask, request, Response, jsonify, make_response
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return "HOME"


@app.route("/ts/<thDate>", methods=['GET'])
def tempHumid_ts(thDate):

    data_dic = thDate

    try:
        df = pd.read_csv("tempHumid-"+data_dic+".log",
                    names=['Datetime', 'etc'],
                    header=None, index_col='Datetime')

        df[['etc1', 'etc2', 'etc3', 'Temp', 'Humid']] = \
            df['etc'].str.split(' ', n=5, expand=True)

        del df['etc']
        del df['etc1']
        del df['etc2']
        del df['etc3']

        df['Temp'] = df['Temp'].str.slice(start=5, stop=-1)
        df['Temp'] = df['Temp'].apply(pd.to_numeric)

        df['Humid'] = df['Humid'].str.slice(start=9, stop=-1)
        df['Humid'] = df['Humid'].apply(pd.to_numeric)

        df.index = pd.to_datetime(df.index)

        return df
    except:
        return "Error"

if __name__ == "__main__":              
    # app.run(host="192.168.0.24", port=5000, debug=False)
    app.run()