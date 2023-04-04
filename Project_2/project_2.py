#%%
import pandas as pd
import altair as alt
import numpy as np
from IPython.display import display, HTML

#%%
url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json"
df = pd.read_json(url)
df.to_csv("flights_missing_original.csv", index=False)

#%%
df = df.replace({
    'airport_name': '',
    'minutes_delayed_carrier': '',
    'num_of_delays_carrier': '1500+',
    'num_of_delays_late_aircraft': -999,
    'minutes_delayed_nas': [-999, ''],
    'year': '',
    'month': 'n/a'
}, np.nan)

airport_dict = {
    'ATL': 'Atlanta, GA: Hartsfield-Jackson Atlanta International',
    'DEN': 'Denver, CO: Denver International',
    'IAD': 'Washington, DC: Washington Dulles International',
    'ORD': "Chicago, IL: Chicago O'Hare International",
    'SAN': 'San Diego, CA: San Diego International',
    'SFO': 'San Francisco, CA: San Francisco International',
    'SLC': 'Salt Lake City, UT: Salt Lake City International'
}

df['airport_name'] = df['airport_name'].fillna(df['airport_code'].map(airport_dict))

df.to_csv("flights_missing.csv", index=False)



#%%
df = df.assign(average_delay_time = df.minutes_delayed_total / df.num_of_delays_total)
title = 'Average Delay Time per Flight by Airport'
alt.Chart(df).mark_boxplot().encode(
    x=alt.X("average_delay_time:Q", title='Average Delay Time (minutes)'),
    y=alt.Y("airport_code:N", sort=alt.EncodingSortField(field='average_delay_time', order='descending'), axis=alt.Axis(title='Airport Code')),
    color=alt.Color('airport_code:N'),
)
# %%
df = df.assign(hours_delayed_total = df.minutes_delayed_total / 60)

summary_table = df.groupby("airport_code").agg(
    total_num_flights = ('num_of_flights_total', 'sum'),
    total_delay_flights = ('num_of_delays_total', 'sum'),
    avg_delay_hours = ('hours_delayed_total', 'mean'),
).assign(
    prop_delayed_flights = lambda x: x.total_delay_flights / x.total_num_flights
).sort_values('prop_delayed_flights', ascending=False)
display(HTML(summary_table.to_html()))

#%%
df['month'] = df['month'].replace('Febuary', 'February') 
month_df = df.dropna(subset=['month']) 

#%%

monthly_avg_delay = month_df.groupby('month')['minutes_delayed_total', 'num_of_delays_total'].sum()

#%%
monthly_avg_delay['avg_delay_time'] = monthly_avg_delay['minutes_delayed_total'] / monthly_avg_delay['num_of_delays_total']

#%%

chart = alt.Chart(monthly_avg_delay.reset_index()).mark_bar().encode(
    x=alt.X('month:O', sort=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], axis=alt.Axis(title='Month')),
    y=alt.Y('avg_delay_time:Q', axis=alt.Axis(title='Average Delay Time (minutes)')),
    color=alt.Color('month:N'),
)

chart.title = 'Average Delay Time per Flight by Month'
chart


# %%

monthly_avg_delay = monthly_avg_delay.sort_values(by=['avg_delay_time'], ascending=False)
display(HTML(monthly_avg_delay.to_html()))



#%%
mean_late_aircraft = df['num_of_delays_late_aircraft'].mean()
df['num_of_delays_late_aircraft'] = df['num_of_delays_late_aircraft'].replace(np.nan, mean_late_aircraft)

#%%


df['weather_delay'] = 0



nas_weather = np.where(df['month'].isin(['April', 'May', 'June', 'July', 'August']), df['num_of_delays_nas'] * 0.4, df['num_of_delays_nas'] * 0.65)

df['weather_delay'] += nas_weather + df['num_of_delays_weather'] + df['num_of_delays_late_aircraft'] * .3

df['weather_delay'].head(5)

df.to_csv("flights_missing.csv", index=False)

df[['weather_delay', 'month', 'num_of_delays_weather', 'num_of_delays_late_aircraft', 'num_of_delays_nas']].head(5)



#%%

weather_delay_prop = df.groupby('airport_code')['weather_delay', 'num_of_delays_total'].sum()
weather_delay_prop['prop_weather_delay'] = weather_delay_prop['weather_delay'] / weather_delay_prop['num_of_delays_total']
weather_delay_prop.reset_index(inplace=True)

bars = alt.Chart(weather_delay_prop).mark_bar().encode(
    x=alt.X('airport_code:N', title='Airport Code', sort=alt.EncodingSortField(field='prop_weather_delay', order='descending')),
    y=alt.Y('prop_weather_delay:Q', axis=alt.Axis(format='%', title='Proportion of Delayed Flights Due to Weather')),
    color=alt.Color('airport_code:N', legend=None)
).properties(title='Proportion of Delayed Flights Due to Weather by Airport')

bars

weather_delay_prop.sort_values(by=['prop_weather_delay'], ascending=False)



#%%

df.head(1)

#%%
nan_year_rows = df.loc[df['year'].isna()]
nan_year_rows.head(1)
# %%
#missing/incorrect values however: airport_name(''), minutes_delayed_carrier(''), num_of_delays_carrier('1500+'), num_of_delays_late_aircraft(-999), minutes_delayed_nas(-999 and ''), year(''), and month('n/a').