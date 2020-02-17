import pandas as pd

data = pd.read_csv("Us_Accidents_Dec19.csv")

print(data.info())

medianTemp = data["Temperature(F)"].median()
print(data["Temperature(F)"].median())

newData = data.loc[data['Temperature(F)'] == medianTemp]
print(newData["City"], newData["Temperature(F)"])