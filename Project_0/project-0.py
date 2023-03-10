#%%
import pandas as pd
import altair as alt

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

mpg.head()


#%%
# Question 1
# I did all the readings and asked my questions on the slack channel

# Question 2

#%%

chart = alt.Chart(mpg).mark_circle().encode(
    x='displ', 
    y='hwy'
)

chart
#%%

# Question 3
(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"]))
#%%