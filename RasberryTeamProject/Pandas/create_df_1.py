import pandas as pd
from collections import OrderedDict

# 딕셔너리 이용 df 만들기
friend_dict_list = [
    {'name' : 'john', 'age' : 40, 'job' : 'teacher'},
    {'name' : 'jane', 'age' : 25, 'job' : 'student'}
]

df = pd.DataFrame(friend_dict_list)
df = df[['name', 'age', 'job']]
print(df)

# 콜렉션의 OrderedDict 사용해서 df 만들기
friend_ordered_dict = OrderedDict(
    [
        ('name', ['john', 'jane']),
        ('age', [40, 25]),
        ('job', ['teacher', 'student'])
    ]
)

df2 = friend_ordered_dict
print(df2)