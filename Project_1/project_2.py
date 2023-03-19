import pandas as pd
import altair as alt
import numpy as np
import json

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

# read in the data
df = pd.read_json('https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json')

# Which airport has the worst delays?

worst_airport = df.groupby('minutes_delayed_total').mean()
print(worst_airport.head())
print(worst_airport.tail())

# What is the best month to fly if you want to avoid delays of any length? 

best_month = df.groupby('month').mean()
print(best_month.head())
month_rows = best_month.query('minutes_delayed_total > 0')
print(month_rows)
title1 = "Average delay by month"
best_month_chart1 = alt.Chart(best_month, title=title1).mark_line().encode(
    x = alt.X("month", title="Month", axis=alt.Axis(format="d")),
    y = alt.Y("month_rows", title="Average delay"),
)

best_month_chart1


# According to the BTS website, the “Weather” category only accounts for severe weather delays. Mild weather delays are not counted in the “Weather” category, but are actually included in both the “NAS” and “Late-Arriving Aircraft” categories. Your job is to create a new column that calculates the total number of flights delayed by weather (both severe and mild). You will need to replace all the missing values in the Late Aircraft variable with the mean. Show your work by printing the first 5 rows of data in a table. Use these three rules for your calculations:__

#     100% of delayed flights in the Weather category are due to weather
#     30% of all delayed flights in the Late-Arriving category are due to weather.
#     From April to August, 40% of delayed flights in the NAS category are due to weather. The rest of the months, the proportion rises to 65%.



# Using the new weather variable calculated above, create a barplot showing the proportion of all flights that are delayed by weather at each airport. Discuss what you learn from this graph.

# Fix all of the varied missing data types in the data to be consistent (all missing values should be displayed as “NaN”). 

# read in the data

# print the first 5 rows of data

