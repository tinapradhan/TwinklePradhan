import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("coviddata.csv")
print(df)

x=df['Total Cases']
y=df['Population']
plt.plot(x,y)
plt.title("covid 19 case study",loc="left")
plt.xlabel("No.of total case")
plt.ylabel("total population")
plt.show()
