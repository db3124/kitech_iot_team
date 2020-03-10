import pandas as pd

df = pd.read_csv('data/friend_list_no_head.txt', header=None)
print(df)

df.columns = ['name', 'age', 'job']
print(df)

df = pd.read_csv(
    'data/friend_list_no_head.txt',
     header=None, 
     names=['name', 'age', 'job'])
print(df)