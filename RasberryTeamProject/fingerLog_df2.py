# import fingerprintreal4
import pandas as pd
from pandas import DataFrame
from IPython.display import display

# col_names = ['Time', 'Message']
# values = fingerprintreal4.printLog(fingerprintreal4.formatter)
col_names = ['Time']
values = ['2020-03-11 14:12:51,432 WARNING 13165 no match']

df = pd.DataFrame(data=values, columns = col_names)

display(pd.Dataframe(df))



