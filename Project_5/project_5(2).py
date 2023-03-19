#%%
import pandas as pd
import altair as alt
import numpy as np
alt.themes.enable('fivethirtyeight')

#%%
url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/star-wars-survey/StarWars.csv'
df = pd.read_csv(url, encoding='ISO-8859-1')

df.head(15)


# %%
column_df = pd.DataFrame({'header1': df.columns, "header2": df.iloc[0, :]}).reset_index(drop=True)
column_df




# %%
column_df.header1[1] = "star_wars_watched"
column_df.header1[2] = "star_wars_fan"
column_df.header1[3] = "have_you_seen_"
column_df.header1[9] = "rank_movie_"
column_df.header1[15] = "favorable_character_"
column_df.header1[29] = "shot_first"
column_df.header1[30] = "expanded_universe_familiar"
column_df.header1[31] = "expanded_universe_fan"
column_df.header1[32] = "star_trek_fan"
column_df.header1[35] = "household_income"
column_df.header1[37] = "location"

column_df.header2[3] = "episode_1"
column_df.header2[4] = "episode_2"
column_df.header2[5] = "episode_3"
column_df.header2[6] = "episode_4"
column_df.header2[7] = "episode_5"
column_df.header2[8] = "episode_6"
column_df.header2[9] = "episode_1"
column_df.header2[10] = "episode_2"
column_df.header2[11] = "episode_3"
column_df.header2[12] = "episode_4"
column_df.header2[13] = "episode_5"
column_df.header2[14] = "episode_6"
column_df.header2[15] = "Han_Solo"
column_df.header2[16] = "Luke_Skywalker"
column_df.header2[17] = "Princess_Leia"
column_df.header2[18] = "Anakin_Skywalker"
column_df.header2[19] = "Obi_Wan_Kenobi"
column_df.header2[20] = "Emperor_Palpatine"
column_df.header2[21] = "Darth_Vader"
column_df.header2[22] = "Lando_Calrissian"
column_df.header2[23] = "Boba_Fett"
column_df.header2[24] = "C_3P0"
column_df.header2[25] = "R2_D2"
column_df.header2[26] = "Jar_Jar_Binks"
column_df.header2[27] = "Padme_Amidala"





column_df


# %%
column_df.replace(["Unnamed:", "Response"], np.nan, regex=True, inplace=True)
column_df.header2.fillna("", inplace=True)

column_df



# %%
column_df.ffill(inplace=True)
column_df
# %%
header = column_df.header1 + column_df.header2
header
# %%
df = pd.read_csv(url, encoding='ISO-8859-1', header=None, skiprows=2, names=header)
df.head()

# %%
df.head(10)
# %%
columns_to_convert = ['star_wars_watched', 'star_wars_fan', 'expanded_universe_familiar', 'expanded_universe_fan', 'star_trek_fan']
for col in columns_to_convert:
    df[col] = df[col].replace({'Yes': 1, 'No': 0})


# df[columns_to_convert] = df[columns_to_convert].fillna(-1).astype(int)

# %%

df.head(10)

# %%

columns_to_mean = ['star_wars_watched', 'star_wars_fan', 'expanded_universe_familiar', 'expanded_universe_fan', 'star_trek_fan']
mean_values = df[columns_to_mean].mean()

df[columns_to_mean] = df[columns_to_mean].fillna(mean_values)

# %%
# %%
df = df[df['star_wars_watched'] == 1]
print(len(df))

# %%

episodes_seen = ['have_you_seen_episode_1', 'have_you_seen_episode_2', 'have_you_seen_episode_3', 'have_you_seen_episode_4', 'have_you_seen_episode_5', 'have_you_seen_episode_6']
for col in episodes_seen:
    df[col] = df[col].replace({'^.*Star Wars.*$': 1}, regex=True)
    df[col] = df[col].fillna(0)
df.head(10)
print(len(df))


# %%
df['Gender'] = df['Gender'].replace({'^.*Male.*$': 1, '^.*Female.*$': 0}, regex=True)
df_movies = df[episodes_seen]
df_movies = df_movies.loc[~(df_movies == 0).all(axis=1)]
print(len(df_movies))


# Select the desired columns from df
df_movies = df[['RespondentID'] + episodes_seen + ['Gender']]

# Filter out rows where all episode columns are 0
# df_movies = df_movies.loc[~(df_movies[episodes_seen] == 0).all(axis=1)]

# Merge df_movies with df on the RespondentID column
df_movies = pd.merge(df_movies, df[['RespondentID', 'Age']], on='RespondentID')

# Print the updated DataFrame
df_movies['Gender'].fillna(0, inplace=True)
print(df_movies.head(10))
df_movies.to_csv('star_wars_movies.csv', index=False)
# Assuming df is the name of your DataFrame
gender_sum = df_movies['Gender'].sum()

# Print the sum
print(gender_sum)


# # Calculate the sum of each column
# episodes_sum = {col: df_movies[col].sum() for col in episodes_seen}

# # Calculate the percentage of respondents who watched each episode
# episodes_percentages = {episode: count / len(df_movies) * 100 for episode, count in episodes_sum.items()}

# # Create the chart
# chart_data = pd.DataFrame({'Episode': list(episodes_percentages.keys()), 'Percentage': list(episodes_percentages.values())})

# chart = alt.Chart(chart_data).mark_bar().encode(
#     x=alt.X('Percentage:Q', title='Percentage of Respondents who Watched'),
#     y=alt.Y('Episode:N', title=None, sort=episodes_seen),
#     tooltip=[alt.Tooltip('Percentage:Q', format='.2f')]
# ).properties(title="Which 'Star Wars' Episodes Have You Seen?")

# chart
# film_names = {
#     1: 'The Phantom Menace',
#     2: 'Attack of the Clones',
#     3: 'Revenge of the Sith',
#     4: 'A New Hope',
#     5: 'The Empire Strikes Back',
#     6: 'Return of the Jedi'
# }

# # Calculate the sum of each column
# episodes_sum = {col: df_movies[col].sum() for col in episodes_seen}

# # Calculate the percentage of respondents who watched each episode
# episodes_percentages = {film_names[int(episode[-1])]: count / len(df_movies) * 100 for episode, count in episodes_sum.items()}

# # Create the chart
# chart_data = pd.DataFrame({'Film': list(episodes_percentages.keys()), 'Percentage': list(episodes_percentages.values())})

# chart = alt.Chart(chart_data).mark_bar().encode(
#     x=alt.X('Percentage:Q', title='Percentage of Respondents who Watched'),
#     y=alt.Y('Film:N', title=None, sort=list(film_names.values())),
#     tooltip=[alt.Tooltip('Percentage:Q', format='.2f')]
# ).properties(title="Which 'Star Wars' Films Have You Seen?")

# chart

# %%
# calculate percentages
# total_count = len(df_movies)
# print(total_count)

# # Define the list of movies to include in the chart
# bars = ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi']

# # create chart
# title = "Which 'Star Wars' Movies Have You Seen?"

# alt.Chart(df_movies).mark_bar().encode(
#     x=alt.X('percentage:Q', title='Percentage'),
#     y=alt.Y('bars:N', sort=bars, title=None),
#     tooltip=[alt.Tooltip('percentage:Q', format='.1f')],
# ).properties(
#     title=title,
# )
# %%

# create new DataFrame with non-null values for shot_first
df_shot_first = df[df['shot_first'].notnull()]

# %%
df.head(30)

# %%
print(pd.unique(df['location']))
# unique_values = pd.unique(df['favorable_character_Yoda'])
#  ['Very favorably' nan 'Unfamiliar (N/A)' 'Somewhat favorably'
#  'Very unfavorably' 'Neither favorably nor unfavorably (neutral)'
#  'Somewhat unfavorably']
# unique_values = pd.unique(df['favorable_character_Han_Solo'])
# ['Very favorably' nan 'Somewhat favorably'
#  'Neither favorably nor unfavorably (neutral)' 'Somewhat unfavorably'
#  'Unfamiliar (N/A)' 'Very unfavorably']

# %%

# convert age to numeric
df['Age'] = df['Age'].replace({'^.*18-29.*$': 1, '^.*30-44.*$': 2, '^.*45-60.*$': 3, '^.*> 60.*$': 4}, regex=True)

# %%
df.head(30)

# %%
df.head(30)
# %%

# convert education to numeric
df['Education'] = df['Education'].replace({
    '^Bachelor degree$': 1,
    '^High school degree$': 2,
    '^Some college or Associate degree$': 3,
    '^Graduate degree$': 4,
    '^Less than high school degree$': 5
}, regex=True)

# %%
df.head(30)


# %%
dummies = pd.get_dummies(df['location'], prefix='Location_')
# Concatenate the original DataFrame with the one-hot encoded columns
df = pd.concat([df, dummies], axis=1)

# Drop the original 'locations' column
df.drop('location', axis=1, inplace=True)

# Print the resulting DataFrame
print(df)
# %%

# %%
# convert favorite character to numeric
for column in df.columns:
    # Check if the column name contains "favorable_character"
    if 'favorable_character' in column:
        # Apply the regex pattern to the matching column
        df[column] = df[column].replace({
            '^.*Very favorably.*$': 6,
            '^.*Somewhat favorably.*$': 5,
            '^.*Neither favorably nor unfavorably \(neutral\)\.*$': 3,
            '^.*Somewhat unfavorably.*$': 2,
            '^.*Very unfavorably.*$': 1,
            '^.*Unfamiliar \(N/A\)\.*$': 4
        }, regex=True)
df.head(30)


# %%
df['household_income'].fillna(0, inplace=True)

# df['household_income'].replace({
#     '$0 - $24,999': 1,
#     '$25,000 - $49,999': 2,
#     '$50,000 - $99,999': 3,
#     '$100,000 - $149,999': 4,
#     '$150,000+': 5,
# })

# df['target'] = (df['household_income'] >= 3).astype(int)

df.to_csv('star_wars.csv', index=False)
df.head(15)

# %%


# %%

df['Gender'] = df['Gender'].replace({'^.*Male.*$': 1, '^.*Female.*$': 0}, regex=True)

# %%
# calculate counts and percentages
total_count = len(df_shot_first)
print()
df_count = df_shot_first.groupby('shot_first').size().reset_index(name='count')
df_count['shot_first'] = df_count['shot_first'].replace({0: "I don't understand this question", 1: "Han Solo", 2: "Greedo"})
df_count['percentage'] = df_count['count'] / total_count * 100

# create chart
title = "Who Shot First?"
bars = ['Han Solo', 'Greedo', "I don't understand this question"]

alt.Chart(df_count).mark_bar().encode(
    x=alt.X('percentage:Q', title='Percentage'),
    y=alt.Y('shot_first:N', sort=bars, title=None),
    tooltip=[alt.Tooltip('percentage:Q', format='.1f')],
).properties(
    title=title,
)
# %%
