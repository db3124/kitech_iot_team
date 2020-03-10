import pandas as pd
from collections import OrderedDict

# 리스트를 이용하여 df 생성
friend_list = [
    ['john', 20, 'student'],
    ['katie', 40, 'teacher']
]

column_name = [
    'name', 'age', 'job'
]

df = pd.DataFrame.from_records(
    friend_list,
    columns=column_name)
print(df)


# 리스트를 이용하여 df 생성2
friend_list_2 = [
    ['name', ['john', 'katie']],
    ['age', [20, 40]],
    ['job', ['student', 'teacher']]
]

df2 = pd.DataFrame.from_items(friend_list_2)
print(df2)
