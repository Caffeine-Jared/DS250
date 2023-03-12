#%%
import pandas as pd
import altair as alt
import numpy as np


df = pd.read_csv('https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv', encoding='ISO-8859-1')
print(df.columns)
#%%
pd.DataFrame.rename(df,columns={'RespondentID':'respondent_id'}, inplace=True)
#%%
print(df.columns)
#%%
pd.DataFrame.rename(columns={'Have you seen any of the 6 films in the Star Wars franchise?':'seen_any'}, inplace=True)
pd.DataFrame.rename(columns={'Do you consider yourself to be a fan of the Star Wars film franchise?':'fan'}, inplace=True)
pd.DataFrame.rename(columns={'Do you consider yourself to be a fan of the Star Trek franchise?':'trek_fan'}, inplace=True)
pd.DataFrame.rename(columns={'Do you consider yourself to be a fan of the Expanded Universe?æ':'expanded_universe'}, inplace=True)
pd.DataFrame.rename(columns={'Which character shot first?':'shot_first'}, inplace=True)
pd.DataFrame.rename(columns={'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.':'film_ranking'}, inplace=True)