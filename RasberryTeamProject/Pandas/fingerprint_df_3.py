import pandas as pd
from pandas import DataFrame, read_csv
import datetime
from IPython.display import display

df = pd.read_csv("Pandas/2020-03-11.log", sep=' ', \
                 names=['Date', 'Time','LogLevel', 'ProcessID', 'Message', ''], \
                 header=None)

df_no_nan = df.fillna('')

display(df_no_nan)


# date = str(datetime.date.today())

# df = pd.read_csv(date+".log", names=['Time', 'LogLevel', 'ProcessID', 'Message'],header=None)

# df = pd.read_csv("Pandas/2020-03-11.log", sep=' ', \
#                  names=['Date', 'Time','LogLevel', 'ProcessID', 'Message', ''], \
#                  header=None)

# df_no_nan = df.fillna('')

# # print(df_no_nan)
# display(df_no_nan)