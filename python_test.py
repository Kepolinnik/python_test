import pandas as pd

df1 = pd.read_csv('Data_part_1.csv', sep=';', header=None)
df2 = pd.read_csv('Data_part_2.csv', sep=';', header=None)
df3 = pd.read_csv('Data_part_3.csv', sep=';', header=None)

datas = pd.concat([df1, df2, df3])
datas.columns = datas.iloc[0]
datas = datas.drop(index=0)

datas.to_csv('Datas.csv', sep=';', index=False)

df = pd.read_csv("Datas.csv", sep=';')
df['Domain Share'] = df['email'].str.split('@').str[1]
people_count = df.groupby('company_name')['first_name'].count()

print("Результати:")
print(df)
print("Кількість людей для кожної компанії:")
print(people_count)