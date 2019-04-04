import numpy as np
import pandas as pd
import os
import re
import matplotlib.pyplot as plt

#os.chdir('..')
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')

#need to drop categories based on duplicates from scraped data
df = df.drop(labels=['Unnamed: 0','Goals.1', 'Assists.1', 'SpG.1', 'Drb.1',
            'Assists.2', 'KeyP.1', 'PS%.1'], axis=1)

#need to cleanup the data, first changing all columns from object to numerical
cols = ['Goals', 'Assists', 'Yel', 'Red', 'SpG', 'PS%', 'AerialsWon', 'MotM',
        'KeyP', 'Drb', 'Fouled', 'Off', 'Disp', 'UnsTch', 'Tackles', 'Inter',
        'Fouls', 'Offsides', 'Clear', 'Blocks', 'OwnG', 'AvgP', 'Crosses',
        'LongB', 'ThrB']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
df
#need to fill NaN's with 0's
df.fillna(0, inplace=True)
#French is the youngest league.
df.groupby('league').mean()

#Found bug, what if player only starts and has no subs (NEED IF STATEMENT)
# def apps_columns(df):
#     Apps = df['Apps']
#     Apps = Apps.str.slice(stop=-1)
#     subset = Apps.str.split('(', expand=True)
#     df = pd.concat((df, subset), axis=1)
#     df = df.drop('Apps', axis=1)
#     df.rename({0:'starts', 1:'sub_apps'},axis=1, inplace=True)
#     return df
#
# apps_columns(df)
##FOUND BUG
#Duplicate players, originally 2798, now down to 2546
df.drop_duplicates(keep='first', inplace=True)

#should i use dropfirst=True?
#Dummy the league names
df = pd.get_dummies(df, columns=['league'])

df.rename({'league_England-Premier-League':'English_Prem',
 'league_France-Ligue-1':'Ligue_1', 'league_Germany-Bundesliga':'Bundesliga',
 'league_Italy-Serie-A': 'Serie_A', 'league_Spain-La-Liga':'La_Liga'},axis=1, inplace=True)

#seperate all the leagues
Bundesliga = df[df['Bundesliga']==1]
Prem = df[df['English_Prem']==1]
La_liga = df[df['La_Liga']==1]
Ligue_1 = df[df['Ligue_1']==1]
Serie_a = df[df['Serie_A']==1]

#Bundesliga.describe()#50% min percentile = 963
# Prem.describe()     #50% min percentile = 1217
# La_liga.describe()  #50% min percentile = 1116
# Ligue_1.describe()  #50% min percentile = 964
# Serie_a.describe()  #50% min percentile = 967

Germ_median = Bundesliga[Bundesliga['Mins']>963]
Prem_median = Prem[Prem['Mins']>1217]
La_liga_median = La_liga[La_liga['Mins']>1116]
Ligue_1_median = Ligue_1[Ligue_1['Mins']>964]
Serie_a_median = Serie_a[Serie_a['Mins']>967]
#create a new dataframe with the first column
League_means = pd.DataFrame(data=Germ_median.mean(), columns=['Bundesliga'])
#adding each league column after that
League_means['Prem'] = Prem_median.mean()
League_means['La_liga'] = La_liga_median.mean()
League_means['Ligue_1'] = Ligue_1_median.mean()
League_means['Serie_a'] = Serie_a_median.mean()

#transpose for better format for graphing, better shape to compare leagues
League_means = League_means.transpose()
League_means

#Weights used to figure out MVP
MVP_weights = np.array([1,.5,-.15,-2,1/100, .25, .2, .15, -.15, -.25, -.25, .25, .33,
                        .25, .2, -.4])
#Columns in dataframe to compute MVP
col2s = ['Goals', 'Assists', 'Yel', 'Red', 'PS%', 'AerialsWon', 'KeyP', 'Drb',
        'Off', 'Disp', 'UnsTch', 'Tackles', 'Inter', 'Clear', 'Blocks', 'OwnG']

#pass in dataframe per league, not full
def MVP_calculator(df):
    #columns used to compute MVP
    col2s = ['Goals', 'Assists', 'Yel', 'Red', 'PS%', 'AerialsWon', 'KeyP', 'Drb',
            'Off', 'Disp', 'UnsTch', 'Tackles', 'Inter', 'Clear', 'Blocks', 'OwnG']
    #Weights used to figure out MVP
    MVP_weights = np.array([1,.5,-.15,-2,1/100, .25, .2, .15, -.15, -.25, -.25, .25, .33,
                            .25, .2, -.4])
    uniform_df = df.loc[:,col2s]
    MVP_score = np.dot(uniform_df.values, MVP_weights)
    top_10 = MVP_score.argsort()[-10:]
    #flip so most valuble is on top
    top_10 = np.flip(top_10)
    MVPs = df.iloc[top_10,:]
    return MVPs

#pass in each individual league dataframe
def ratings_grabber(df):
    #want to filter out players who have good ratings in only a few app's
    df = df[df['Mins']>600]
    vals = df['Rating'].values
    idx = np.argsort(vals)[-10:]
    idx = np.flip(idx)
    top_ratings = df.iloc[idx,:]
    return top_ratings

MVP_calculator(Prem)
ratings_grabber(Prem)
