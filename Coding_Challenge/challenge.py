#%%
import pandas as pd 
import altair as alt
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv'

dat_home = pd.read_csv(url).sample(n=4500, random_state=15)

dat_home.head()
#%%
arcstyle_colors = {style: color for style, color in zip(dat_home['arcstyle'].unique(), plt.cm.tab10.colors)}
rannge = [100,200,300,400,500,1000,2000,3000,4000,5000,10000]

keys = ['ONE-STORY','TWO-STORY','ONE AND HALF-STORY']
for style, color in arcstyle_colors.items():
    if style in keys:
        plt.scatter(dat_home[dat_home['arcstyle'] == style]['yrbuilt'],
                    dat_home[dat_home['arcstyle'] == style]['livearea'],
                    c=color,
                    alpha=0.5,
                    label=style)
       

plt.yticks(rannge)
plt.title('Thank goodness 21st Century homes are not split levels!')
plt.xlabel('Year Built')
plt.ylabel('Total Living Area')
plt.legend(title='Architectural Style', loc='best')

plt.show()

#%%
mister = pd.Series(["lost", 15, 22, 45, 31, "lost", 85, 38, 129, 80, 21, 2])

for i in range(len(mister)):
    if mister[i] == "lost":
        mister[i] = 125
plt.boxplot(mister)


plt.title('Box Plot of Mister Series')
plt.ylabel('Values')

plt.show()

#%%
mister = pd.Series(["lost", 15, 22, 45, 31, "lost", 85, 38, 129, 80, 21, 2])

for i in range(len(mister)):
    if mister[i] == "lost":
        mister[i] = 125


print(round(mister.mean(), 2))

#%%

url = 'https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/table1/table1.json'

# Read JSON data from the URL
df = pd.read_json(url)

df
# filter data to keep only cases column and 1999/2000 years
df = df[df['year'].isin([1999, 2000])]
df = df[['country', 'year', 'cases']]
df = df.pivot(index='country', columns='year', values='cases')

df.head(6)