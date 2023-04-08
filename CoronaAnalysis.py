import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from datetime import date, datetime, time, timezone

df = pd.read_csv("covid-vaccination-doses-per-capita.csv")

# df.info()

df['Date'] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace=True)
df.drop(['Day'], axis=1, inplace=True)

# print(df.head())
# print(len(df['Entity'].unique()))
covid_c = df.groupby(['Entity'])

# for key, group in covid_c:
#     print('+key', key)
#     print('+number:', len(group))
#     print(group.head())
#     print('\n')

total_df = covid_c.sum()
print(total_df.head())
