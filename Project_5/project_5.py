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
df.info()
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
df.head(30)
# %%
episodes_seen = ['have_you_seen_episode_1', 'have_you_seen_episode_2', 'have_you_seen_episode_3', 'have_you_seen_episode_4', 'have_you_seen_episode_5', 'have_you_seen_episode_6']
for col in episodes_seen:
    df[col] = df[col].replace({'^.*Star Wars.*$': 1}, regex=True)
    df[col] = df[col].fillna(0)

# %%

df.head(30)

# %%
df = df.dropna(subset=['Gender'])
df['Gender'] = df['Gender'].replace({'^.*Male.*$': 1, '^.*Female.*$': 0}, regex=True)

# %%
df.head(30)

# %%
print(pd.unique(df['Location (Census Region)']))
# unique_values = pd.unique(df['favorable_character_Yoda'])
#  ['Very favorably' nan 'Unfamiliar (N/A)' 'Somewhat favorably'
#  'Very unfavorably' 'Neither favorably nor unfavorably (neutral)'
#  'Somewhat unfavorably']
# unique_values = pd.unique(df['favorable_character_Han_Solo'])
# ['Very favorably' nan 'Somewhat favorably'
#  'Neither favorably nor unfavorably (neutral)' 'Somewhat unfavorably'
#  'Unfamiliar (N/A)' 'Very unfavorably']

# %%


df['Age'] = df['Age'].replace({'^.*18-29.*$': 1, '^.*30-44.*$': 2, '^.*45-60.*$': 3, '^.*> 60.*$': 4}, regex=True)

# %%
df.head(30)
# %%
df = df.fillna(0)
df['Household Income'] = df['Household Income'].replace({'^\\$0 - \\$24,999$': 1, '^\\$25,000 - \\$49,999$': 2, '^\\$50,000 - \\$99,999$': 3, '^\\$100,000 - \\$149,999$': 4, '^\\$150,000\\+$': 5}, regex=True)

# %%
df.head(30)
# %%

df = df.dropna(subset=['Education'])
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
df = df[df['star_wars_watched'] == 1]
df.head(30)

# %%
dummies = pd.get_dummies(df['Location (Census Region)'], prefix='Location')
# Concatenate the original DataFrame with the one-hot encoded columns
df = pd.concat([df, dummies], axis=1)

# Drop the original 'locations' column
df.drop('Location (Census Region)', axis=1, inplace=True)

# Print the resulting DataFrame
print(df)
# %%
df['shot_first'] = df['shot_first'].replace({'^.*I don\'t understand this question.*$': 0, '^.*Han.*$': 1, '^.*Greedo.*$': 2}, regex=True)
df.head(30)

# %%
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

threshold = 3  # Set this to the desired threshold
df['target'] = (df['Household_Income'] >= threshold).astype(int)

df.to_csv('star_wars5.csv', index=False)
# %%
