import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

dat = pd.read_csv("https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv")

#| label: GQ1
#| code-summary: Read and format data
# Include and execute your code here

#| label: GQ1 chart
#| code-summary: plot example
#| fig-cap: "My useless chart"
#| fig-align: center
# Include and execute your code here
alt.Chart(dat.head(200))\
    .encode(x="name", y="AK")\
    .mark_bar()\
    .properties(
        width=800,
        height=300
    )
#| label: GQ1 table
#| code-summary: table example
#| tbl-cap: "Not much of a table"
#| tbl-cap-location: top
# Include and execute your code here
mydat = dat.head(1000)\
    .groupby('year')\
    .sum()\
    .reset_index()\
    .tail(10)\
    .filter(["year", "AK","AR"])

display(mydat)

#| label: GQ2
#| code-summary: Read and format data
# Include and execute your code here


#| label: GQ2 chart
#| code-summary: plot example
#| fig-cap: "My useless chart"
#| fig-align: center
# Include and execute your code here
alt.Chart(dat.head(200))\
    .encode(x = "name", y = "AK")\
    .mark_bar()

#| label: GQ2 table
#| code-summary: table example
#| tbl-cap: "Not much of a table"
#| tbl-cap-location: top
# Include and execute your code here
mydat = dat.head(1000)\
    .groupby('year')\
    .sum()\
    .reset_index()\
    .tail(10)\
    .filter(["year", "AK","AR"])

display(mydat)

#| label: GQ3
#| code-summary: Read and format data
# Include and execute your code here


#| label: GQ3 chart
#| code-summary: plot example
#| fig-cap: "My useless chart"
#| fig-align: center
# Include and execute your code here
alt.Chart(dat.head(200))\
    .encode(x = "name", y = "AK")\
    .mark_bar()

#| label: GQ3 table
#| code-summary: table example
#| tbl-cap: "Not much of a table"
#| tbl-cap-location: top
# Include and execute your code here
mydat = dat.head(1000)\
    .groupby('year')\
    .sum()\
    .reset_index()\
    .tail(10)\
    .filter(["year", "AK","AR"])

display(mydat)