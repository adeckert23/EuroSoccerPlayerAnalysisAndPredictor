import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
#link for info https://www.kaggle.com/hugomathien/soccer

#establish connection to sql database
cnx = sqlite3.connect('database.sqlite')

player_data = pd.read_sql_query('SELECT * FROM Player_Attributes', cnx)
player_names = pd.read_sql_query('SELECT * FROM Player', cnx)

#change player birthdays (string) to datetime object that can be iterable
player_names['birthday'] = pd.to_datetime(player_names['birthday'], format='%Y-%m-%d')

#change date column to datetime format
player_data['date'] = pd.to_datetime(player_data['date'], format='%Y-%m-%d')

player_data = player_data.sort_values('date').drop_duplicates('player_api_id',keep='last')
#set it equal to itself, instead of using inplace (which isn't working)
#because of multiple methods

#I wanted to dummy the below columns, but got many unexpected values, so I had
#to do some feature engineering to still be able to work with them.

#Below code to show unique values for each column
# player_data['attacking_work_rate'].unique()
# player_data['defensive_work_rate'].unique()
# player_data['preferred_foot'].unique()

#build a function to manually create the dummy columns for preferred right foot
def preferred_foot_dummy(df):
    for idx, row in df.iterrows():
        if row['preferred_foot'] == 'right':
            df.at[idx,'preferred_foot'] = 1
        else:
            df.at[idx,'preferred_foot'] = 0

def attk_work_rate(df):
    for idx, row in df.iterrows():
        if row['attacking_work_rate'] == 'high':
            df.at[idx,'attacking_work_rate'] = 1
            df.at[idx,'attacking_medium_rate'] = 0
        elif row['attacking_work_rate'] == 'medium':
            df.at[idx,'attacking_work_rate'] = 0
            df.at[idx,'attacking_medium_rate'] = 1
        else:
            df.at[idx,'attacking_work_rate'] = 0
            df.at[idx,'attacking_medium_rate'] = 0

def def_work_rate(df):
    for idx, row in df.iterrows():
        if row['defensive_work_rate'] == 'high':
            df.at[idx,'defensive_work_rate'] = 1
            df.at[idx,'defensive_medium_rate'] = 0
        elif row['defensive_work_rate'] == 'medium':
            df.at[idx,'defensive_work_rate'] = 0
            df.at[idx,'defensive_medium_rate'] = 1
        else:
            df.at[idx,'defensive_work_rate'] = 0
            df.at[idx,'defensive_medium_rate'] = 0

preferred_foot_dummy(player_data)
attk_work_rate(player_data)
def_work_rate(player_data)

#changing dummy columns dtype to numeric
player_data['preferred_foot'] = pd.to_numeric(player_data['preferred_foot'])
player_data['attacking_work_rate'] = pd.to_numeric(player_data['attacking_work_rate'])
player_data['defensive_work_rate'] = pd.to_numeric(player_data['defensive_work_rate'])

#create a function to fill the na's with the means of each column
def mean_filler(df):
    for col in df:
        df[col].fillna((df[col].mean()), inplace=True)
    return df

#create an X and a y
X = player_data.iloc[:,4:]

mean_filler(player_data)

#X still has 40 columns, this will need to be reduced
#I don't need y (target) for clustering... creating for regression in near future

#Using a scaler from -1 --> 1 where 0 is the mean
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=5, random_state=7)
X_pca = pca.fit_transform(X_scaled)
kmeans = KMeans(n_clusters=40, random_state=7, n_jobs=-1)
kmeans.fit_transform(X_pca)
labels = kmeans.labels_



#start of regression
#taking out overall_rating, since that is my y (target) instantiated above
new_x = X.iloc[:,1:]
y = X.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size=.2, random_state=7)

gbr = GradientBoostingRegressor(n_estimators=350)
model = gbr.fit(X_train, y_train)
# preds = model.predict(X_test)
#takes X_test not preds
score = model.score(X_test, y_test)
score
