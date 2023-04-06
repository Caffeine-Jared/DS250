#%%
from matplotlib import pyplot as plt
import pandas as pd 
import altair as alt 
import numpy as np 
import altair as alt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.calibration import LabelEncoder



#%%
from sklearn.model_selection import train_test_split
from sklearn import tree

from sklearn import metrics
from sklearn.metrics import roc_curve, auc, RocCurveDisplay
from sklearn.ensemble import RandomForestClassifier

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



# %%

df.head(10)

# %%

columns_to_mean = ['star_wars_watched', 'star_wars_fan', 'expanded_universe_familiar', 'expanded_universe_fan', 'star_trek_fan']
mean_values = df[columns_to_mean].mean()

df[columns_to_mean] = df[columns_to_mean].fillna(mean_values)


# %%
df = df[df['star_wars_watched'] == 1]
df.to_csv('star_wars_cleaned.csv')
print(df['shot_first'].value_counts())


# %%
episodes_seen = ['have_you_seen_episode_1', 'have_you_seen_episode_2', 'have_you_seen_episode_3', 'have_you_seen_episode_4', 'have_you_seen_episode_5', 'have_you_seen_episode_6']
for col in episodes_seen:
    df[col] = df[col].replace({'^.*Star Wars.*$': 1}, regex=True)
    df[col] = df[col].fillna(0)


# %%
df = df.dropna(subset=['Gender'])
df['Gender'] = df['Gender'].replace({'^.*Male.*$': 1, '^.*Female.*$': 0}, regex=True)
# %%

male_df = df[df['Gender'] == 1] 
seen_any_df = male_df[(male_df[episodes_seen] == 1).any(axis=1)] # Filter for respondents who have seen at least one film
percent_male_seen_any = len(seen_any_df) / len(male_df) * 100 # Calculate percentage
print(f"{percent_male_seen_any:.4f}% of males have seen at least one film.")


# %%



df.head(30)



# %%
df.head(30)

# %%
print(pd.unique(df['location']))


# %%


df['Age'] = df['Age'].replace({'^.*18-29.*$': 1, '^.*30-44.*$': 2, '^.*45-60.*$': 3, '^.*> 60.*$': 4}, regex=True)

# %%
df.head(30)

# %%
df.head(30)
# %%


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

df = pd.concat([df, dummies], axis=1)


df.drop('location', axis=1, inplace=True)

print(df)
# %%
df['shot_first'].replace({'^.*I don\'t understand this question.*$': 0, '^.*Han.*$': 1, '^.*Greedo.*$': 2}, regex=True)
df.head(30)

# %%
for column in df.columns:
    if 'favorable_character' in column:
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

df['household_income'] = df['household_income'].replace({
    '$0 - $24,999': 1,
    '$25,000 - $49,999': 2,
    '$50,000 - $99,999': 3,
    '$100,000 - $149,999': 4,
    '$150,000+': 5,
})

df['household_income'] = df['household_income'].astype(float)

df['target'] = (df['household_income'] >= 3).astype(int)

# %%

#%%
df.fillna(df.median(), inplace=True)
X = df.drop(['household_income', 'target', 'shot_first'], axis=1)
y = df.filter(regex = 'target')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=24, stratify=y)

rf = RandomForestClassifier(random_state=24)

#%%
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)


#%% 
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

#%%
print(metrics.classification_report(y_pred, y_test))



#%% 
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

# %%
df_features = pd.DataFrame(
    {'f_names': X_train.columns, 
    'f_values': rf.feature_importances_}).sort_values('f_values', ascending = False)

# %%
(alt.Chart(df_features.query('f_values > .011'))
    .encode(
        alt.X('f_values'),
        alt.Y('f_names', sort = '-x'))
    .mark_bar())
# %%

y_probs = rf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_probs)

roc_auc = auc(fpr, tpr)

roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='Random Forest Classifier')
roc_display.plot()
plt.show()

