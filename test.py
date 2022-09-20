import pandas as pd
technologies= {
    'Courses':["Spark","PySpark","Spark","Java","PySpark","PHP"],
    'Fee' :[22000,25000,23000,24000,26000,27000],
    'Duration':['30days','50days','30days','60days','35days','30days']
          }
df = pd.DataFrame(technologies)
print(df)
lista = [22000]

df = df.loc[df.Fee.isin(lista),:]
print(df)