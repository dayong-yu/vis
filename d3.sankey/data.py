import pandas as pd


df = pd.read_csv('d3.chrod.adp.csv')

df_country = pd.read_csv('CountryCode.txt', encoding="ISO-8859-1")


df_country = df_country[df_country['G20']=='Y'][['Name','G20']]


df = pd.merge(df,df_country,left_on='reporter',right_on='Name')
df = pd.merge(df,df_country,left_on='partner',right_on='Name')

df = df[['reporter','partner','value']]
df = df.rename(columns={'reporter':'source','partner':'target'})
df['target'] = ' ' + df['target']
df.to_csv('sankey.csv')
