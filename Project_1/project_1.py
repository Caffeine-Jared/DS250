#%%
import pandas as pd
import altair as alt
import numpy as np
import datetime as dt
from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

dat = pd.read_csv("https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv")

# #| label: GQ1
# #| code-summary: Read and format data
# # Include and execute your code here


# # filter data to only include my name
# my_name = dat.query("name == 'Jared'")
# print(my_name.head())
# #create a line chart using altair
# # ensure that the X and Y axis are labeled correctly, and that the chart has a title
# # in labeling the x and Y axises, ensure that you type the correct case, otherwise there'll be an issue
# title = "Number of Jareds born in each year"
# my_name_chart1 = alt.Chart(my_name, title=title).mark_line().encode(
#     x = alt.X("year", title="Year", axis=alt.Axis(format="d")),
#     y = alt.Y("Total", title="Number of Jareds"),
# )
# # my_name_chart1

# # create a new rule to the chart
# new_rule = my_name.query("year == 1997")
# print(new_rule.head())
# my_name_chart2 = alt.Chart(new_rule).mark_circle(color="red", size=100).encode(
#     x = 'year',
#     y = 'Total',
# )
# my_name_chart1 + my_name_chart2

# # create a new chart showing the most popular date in which Jareds were born
# subrule1 = my_name.query("year == 1997 & Total")
# print(subrule1) # 6682 Jareds were born in 1997
# subrule1_1 = 6682
# new_rule1 = my_name.query(f"Total > {subrule1_1}")
# print(new_rule1)
# my_name_chart3 = alt.Chart(new_rule1).mark_circle(color="blue", size=80).encode(
#     x = 'year',
#     y = 'Total',
# )
# my_name_chart1 + my_name_chart2 + my_name_chart3
# # my_name_chart1 + my_name_chart2 + my_name_chart3
# #%%

# ## GRAND QUESTION 2
#__If you talked to someone named Brittany on the phone, what is your guess of his or her age? What ages would you not guess?__

# # what are some of the dates in which the name "Brittany" was popular?
# brittany = dat.query("name == 'Brittany'")
# print(brittany.head())

# # create a line chart using altair
# # ensure that the X and Y axis are labeled correctly, and that the chart has a title

# title = "Number of Brittanys born in each year"
# brittany_chart1 = alt.Chart(brittany, title=title).mark_line().encode(
#     x = alt.X("year", title="Year", axis=alt.Axis(format="d")),
#     y = alt.Y("Total", title="Number of Brittanys"),
# )
# brittany_chart1

# # create a new rule to the chart
# britt_rule = brittany.query("year > 1980 & year < 2005 & Total > 10000")
# print(britt_rule)
# britt_rule_1 = brittany.query("year == 1990")

# britt_rule_1_chart = alt.Chart(britt_rule_1).mark_circle(color="red", size=150).encode(
#     x = 'year',
#     y = 'Total',
# )

# britt_rule_2_chart = alt.Chart(britt_rule).mark_circle(color="blue", size=80).encode(
#     x = 'year',
#     y = 'Total',
# )
# brittany_chart1 + britt_rule_1_chart + britt_rule_2_chart

# britt_rule3 = brittany.query("year == 1999")

# britt_rule3_chart = alt.Chart(britt_rule3).mark_circle(color="green", size=80).encode(
#     x = 'year',
#     y = 'Total',
# )
# brittany_chart1 + britt_rule_1_chart + britt_rule_2_chart + britt_rule3_chart

# britt_rule_1
#%%


# # ## GRAND QUESTION 3
# # Mary, Martha, Peter, and Paul are all Christian names. From 1920 - 2000, compare the name usage of each of the four names. What trends do you notice?

# # Mary (1920 - 2000)
# mary_name = dat.query("name == 'Mary' & year > 1920 & year < 2000")

# mary_name_chart = alt.Chart(mary_name).mark_line().encode(
#     x = alt.X("year", title="Year", axis=alt.Axis(format="d")),
#     y = alt.Y("Total", title="Number of Marys"),
#     color = alt.value("#FF0005"),
# )

# # Mary name query 2, 1950 max value
# # find the max value of the mary_name dataframe
# subrule2 = mary_name.query("year > 1920 & year < 2000 & Total > 50000").max()
# # query the mary_name dataframe for the year 1950 (year with max value)
# subrule2_1 = mary_name.query("year == 1950")

# mary_name_chart2 = alt.Chart(subrule2_1).mark_circle(color="red", size=80).encode(
#     x = 'year',
#     y = 'Total',
#     color = alt.value("#85FF00"),
# )

# # Martha (1920 - 2000)
# martha_name = dat.query("name == 'Martha' & year > 1920 & year < 2000")

# martha_name_chart = alt.Chart(martha_name).mark_line().encode(
#     x = alt.X("year", title="Year", axis=alt.Axis(format="d")),
#     y = alt.Y("Total", title="Number of Marthas"),
#     color = alt.value("#85FF00"),
# )

# # Martha name query 2, 1947 max value
# # find the max value of the martha_name dataframe
# subrule3 = martha_name.query("year > 1920 & year < 2000 & Total > 10700").max()

# # query the martha_name dataframe for the year 1947 (year with max value)
# subrule3_1 = martha_name.query("year == 1947")

# martha_name_chart2 = alt.Chart(subrule3_1).mark_circle(color="red", size=80).encode(
#     x = 'year',
#     y = 'Total',
#     color = alt.value("#FF0005"),
# )

# # Peter (1920 - 2000)
# peter_name = dat.query("name == 'Peter' & year > 1920 & year < 2000")

# peter_name_chart = alt.Chart(peter_name).mark_line().encode(
#     x = alt.X("year", title="Year", axis=alt.Axis(format="d")),
#     y = alt.Y("Total", title="Number of Peters"),
#     color = alt.value("#00FFFA"),
# )

# # Peter name query 2, max value
# # find the max value of the peter_name dataframe
# subrule5 = peter_name.query("year > 1920 & year < 2000 & Total > 10000").max()

# # query the peter_name dataframe for the year 1956 (year with max value)
# subrule5_1 = peter_name.query("year == 1956")

# peter_name_chart2 = alt.Chart(subrule5_1).mark_circle(color="red", size=80).encode(
#     x = 'year',
#     y = 'Total',
#     color = alt.value("#7A00FF"),
# )



# # Paul (1920 - 2000)
# paul_name = dat.query("name == 'Paul' & year > 1920 & year < 2000")

# paul_name_chart = alt.Chart(paul_name).mark_line().encode(
#     x = alt.X("year", title="Year", axis=alt.Axis(format="d")),
#     y = alt.Y("Total", title="Number of Pauls"),
#     color = alt.value("#7A00FF"),
# ).interactive()

# # Paul name query 2, max value
# # find the max value of the paul_name dataframe
# subrule4 = paul_name.query("year > 1920 & year < 2000 & Total > 25000").max()

# # query the paul_name dataframe for the year 1981 (year with max value)
# subrule4_1 = paul_name.query("year == 1954")

# paul_name_chart2 = alt.Chart(subrule4_1).mark_circle(color="red", size=80).encode(
#     x = 'year',
#     y = 'Total',
#     color = alt.value("#00FFFA"),
# )

# #%%

# #%%

# #%%

# mary_name_chart + mary_name_chart2 + martha_name_chart + martha_name_chart2 + peter_name_chart + peter_name_chart2 + paul_name_chart + paul_name_chart2

# #%%

## GRAND QUESTION 4

# __Think of a unique name from a famous movie. Plot the usage of that name and see how changes line up with the movie release. Does it look like the movie had an effect on usage?__

movie_name = dat.query("name == 'Leia' & year > 1920")

movie_name_chart = alt.Chart(movie_name).mark_line().encode(
    x = alt.X("year", title="Year", axis=alt.Axis(format="d")),
    y = alt.Y("Total", title="Number of Leias"),
    color = alt.value("#FF0005"),
).interactive()

movie_name_chart

#%%