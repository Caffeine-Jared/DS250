# Create 2-3 charts that evaluate potential relationships between the home variables and before1980.
# chart 1: home value vs. before1980

#%%
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()
dwellings_ml_df = pd.read_csv('dwellings_ml.csv')
#%%
dwellings_ml_df.head()
#%%
dwellings_ml_df.shape

#%%
# chart 1: stories vs before1980
alt.Chart(dwellings_ml_df, title="Homes w/ One Story are most likely to be built before 1980").mark_bar().encode(
    alt.X('before1980:N', title=""),
    alt.Y('count(stories)', title="Count of Homes"),
    alt.Color('before1980:N', title="Built Before 1980?"),
    alt.Column('stories')
).interactive()

# live area
#%%
alt.Chart(dwellings_ml_df).transform_density(
    'livearea',
    as_=['livearea', 'density'],
    groupby=['before1980']
).mark_area(opacity=.5).encode(
    x="livearea",
    y="density:Q",
    color="before1980:N"
).interactive()






# # query sprice > 0 and before1980 == 1 and before1980 == 0
# # chart 2: home size vs. before1980

# dwellings_ml_df = pd.read_csv('Project_4\dwellings_ml.csv')
# dwellings_ml_df.head()
# dwellings_ml_df.shape
# alt.Chart(dwellings_ml_df).mark_circle().encode(
#     x='sqft:Q',
#     y='before1980:N',
#     color='before1980:N'
# ).interactive()



#uild a classification model labeling houses as being built “before 1980” or “during or after 1980”. Your goal is to reach or exceed 90% accuracy. Explain your final model choice (algorithm, tuning parameters, etc) and describe what other models you tried.

#Justify your classification model by discussing the most important features selected by your model. This discussion should include a chart and a description of the features.

#Describe the quality of your classification model using 2-3 different evaluation metrics. You also need to explain how to interpret each of the evaluation metrics you use.
# %%
