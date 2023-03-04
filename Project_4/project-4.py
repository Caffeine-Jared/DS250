# Create 2-3 charts that evaluate potential relationships between the home variables and before1980.
# chart 1: home value vs. before1980
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()
dwellings_ml_df = pd.read_csv('Project_4\dwellings_ml.csv')
dwellings_ml_df.head()
dwellings_ml_df.shape
alt.Chart(dwellings_ml_df).mark_circle().encode(
    x='sprice:Q',
    y='before1980:N',
    color='before1980:N'
).interactive()

# # chart 2: home age vs. before1980
# alt.Chart(dwellings_ml_df).mark_circle().encode(
#     x='home_age',
#     y='before1980',
#     color='before1980'
# ).interactive()

# # chart 3: home size vs. before1980
# alt.Chart(dwellings_ml_df).mark_circle().encode(
#     x='home_size',
#     y='before1980',
#     color='before1980'
# ).interactive()

# # chart 4: home size vs. home value
# alt.Chart(dwellings_ml_df).mark_circle().encode(
#     x='home_size',
#     y='home_value',
#     color='before1980'
# ).interactive()


#uild a classification model labeling houses as being built “before 1980” or “during or after 1980”. Your goal is to reach or exceed 90% accuracy. Explain your final model choice (algorithm, tuning parameters, etc) and describe what other models you tried.

#Justify your classification model by discussing the most important features selected by your model. This discussion should include a chart and a description of the features.

#Describe the quality of your classification model using 2-3 different evaluation metrics. You also need to explain how to interpret each of the evaluation metrics you use.