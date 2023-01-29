import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

# Which airport has the worst delays?

# What is the best month to fly if you want to avoid delays of any length? 



# According to the BTS website, the “Weather” category only accounts for severe weather delays. Mild weather delays are not counted in the “Weather” category, but are actually included in both the “NAS” and “Late-Arriving Aircraft” categories. Your job is to create a new column that calculates the total number of flights delayed by weather (both severe and mild). You will need to replace all the missing values in the Late Aircraft variable with the mean. Show your work by printing the first 5 rows of data in a table. Use these three rules for your calculations:__

#     100% of delayed flights in the Weather category are due to weather
#     30% of all delayed flights in the Late-Arriving category are due to weather.
#     From April to August, 40% of delayed flights in the NAS category are due to weather. The rest of the months, the proportion rises to 65%.



# Using the new weather variable calculated above, create a barplot showing the proportion of all flights that are delayed by weather at each airport. Discuss what you learn from this graph.

# Fix all of the varied missing data types in the data to be consistent (all missing values should be displayed as “NaN”). 

# read in the data
df = pd.read_json('https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json')

# print the first 5 rows of data
print(df.head())

