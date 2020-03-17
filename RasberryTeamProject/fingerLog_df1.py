import fingerprintreal4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col_name = ['Time']
values = fingerprintreal4.printLog(fingerprintreal4.formatter)

df = pd.Dataframe(values, columns=col_name)

df.Time = pd.to_datetime(df.Time)


