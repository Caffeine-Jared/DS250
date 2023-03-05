# Create 2-3 charts that evaluate potential relationships between the home variables and before1980.
#%%
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import seaborn as sns


#%%
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

#%%
dwellings_ml = pd.read_csv('dwellings_ml.csv')
dwellings_denver = pd.read_csv('dwellings_denver.csv')
dwellings_neighborhoods_ml = pd.read_csv('dwellings_neighborhoods_ml.csv')

#%%
alt.data_transformers.disable_max_rows()
alt.data_transformers.enable('json')


#%%
h_subset = dwellings_ml.filter(['livearea', 'finbsmnt', 'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 'before1980','stories', 'yrbuilt']).sample(500)

sns.pairplot(h_subset, hue = 'before1980')

#%%

corr = h_subset.drop(columns='before1980').corr()
sns.heatmap(corr)


#%%
dwellings_ml_df = pd.read_csv('dwellings_ml.csv')
dwellings_ml_df.head()
#%%
dwellings_ml_df.shape
# chart 1: home value vs. before1980
alt.Chart(dwellings_ml_df, title="Homes w/ One Story are most likely to be built before 1980").mark_bar().encode(
    alt.X('before1980:N', title="Before 1980"),
    alt.Y('count(stories)', title="Count of Homes"),
    alt.Color('before1980:N', title="Built Before 1980?"),
    alt.Column('stories')
)


#uild a classification model labeling houses as being built “before 1980” or “during or after 1980”. Your goal is to reach or exceed 90% accuracy. Explain your final model choice (algorithm, tuning parameters, etc) and describe what other models you tried.

#Justify your classification model by discussing the most important features selected by your model. This discussion should include a chart and a description of the features.

#Describe the quality of your classification model using 2-3 different evaluation metrics. You also need to explain how to interpret each of the evaluation metrics you use.

# %%
