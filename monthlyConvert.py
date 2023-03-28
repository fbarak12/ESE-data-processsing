import pandas as pd

df = pd.read_csv(r"C:\Users\fbara\OneDrive - University at Albany - SUNY\EPA\Queens2000-2022Sorted.csv")
# print(df)
df.set_index('date_local',inplace=True)
# dfNew = df.resample('D', on='date_local').mean()
# dfNew = df.set_index('date_local').resample('1H').pad()

print(df)

# dfMonthly = df.apply(pd.to_numeric).resample('M').mean()
# print(dfMonthly)