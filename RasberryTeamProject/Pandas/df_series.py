import pandas as pd

# 시리즈(열)생성, 데이터프레임=시리즈의 집합
s1 = pd.core.series.Series([1,2,3])
s2 = pd.core.series.Series([4,5,6])
# print(s1)
# print(s2)

df = pd.DataFrame(data=dict(num=s1, word=s2))
print(df)
