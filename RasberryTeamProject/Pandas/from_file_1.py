import pandas as pd

# csv 파일 읽어오기
# df = pd.read_csv('data/friend_list.csv')
# print(df)
# print(df.head(3))
# print(df.tail(3))

df2 = pd.read_csv('data/friend_list.txt')
print(df2)
print(df2.head(2))
print(df2.tail(2))

# df3_1 = pd.read_csv('data/friend_list_tab.txt')
# print(df3_1)
df3_2 = pd.read_csv('data/friend_list_tab.txt', delimiter='\t')
print(df3_2)