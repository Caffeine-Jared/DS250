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
sns.scatterplot(x='finbsmnt', y='basement', hue='before1980', data=dwellings_ml)
# %%
#%% 
sns.scatterplot(x='livearea', y='sprice', hue='before1980', data=dwellings_ml)

# %%
sns.scatterplot(x='livearea', y='totunits', hue='before1980', data=dwellings_ml)

