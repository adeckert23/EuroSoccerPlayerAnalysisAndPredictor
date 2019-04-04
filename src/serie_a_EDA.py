import numpy as np
import pandas as pd
import os
import re
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

os.chdir('..')
df = pd.read_csv('data/serie_a.csv')

'''Data from whoscored.com
All data as of April 3, 2019, 1pm Eastern (USA) time

player - player name
Age - years
position - main position
Rating - average rating per match
Team - team player plays for
CM - height (in cm)
KG - weight (in kg)
Apps - Appearances format- number of starts(appearances in parenthesis)
Mins - Minutes Played
Goals - number of goals
Assists - number of assists
Yel - yellow cards
Red - red cards
SpG - shots per game?
PS% - pass success %
AerialsWon - Aerial Duels Won per game
MotM - Man of the Match
KeyP - Key Passes per game
Drb - Dribbles past per game
Fouled - Fouled per game
Off - Offsides per game (as an attacker/bad)
Disp - Dispossessed per game
UnsTch - Bad Control per game
Tackles - Tackles per game
Inter - Interceptions per game
Fouls - Fouls per game
Offsides - Offsides won per game (as a defender/good)
Clear - Clearances per game
Blocks -Blocks per game
OwnG - Own Goals
AvgP - Passes per game
Crosses - Crosses per game
LongB - Long Balls per game
ThrB - Through Balls per game'''

#need to drop categories based on duplicates from scraped data
df = df.drop(labels=['Unnamed: 0','Goals.1', 'Assists.1', 'SpG.1', 'Drb.1',
            'Assists.2', 'KeyP.1', 'PS%.1'], axis=1)

#need to cleanup the data, first changing all columns from object to numerical
cols = ['Goals', 'Assists', 'Yel', 'Red', 'SpG', 'PS%', 'AerialsWon', 'MotM',
        'KeyP', 'Drb', 'Fouled', 'Off', 'Disp', 'UnsTch', 'Tackles', 'Inter',
        'Fouls', 'Offsides', 'Clear', 'Blocks', 'OwnG', 'AvgP', 'Crosses',
        'LongB', 'ThrB']

df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)

#need to fill NaN's with 0's
df.fillna(0, inplace=True)

#break appearances into 2 seperate columns
#THIS DOESN"T WORK FOR PLAYERS WITH NO SUB APPEARANCES.  NEEDS IF STATEMENT
def apps_columns(df):
    Apps = df['Apps']
    Apps = Apps.str.slice(stop=-1)
    subset = Apps.str.split('(', expand=True)
    df = pd.concat((df, subset), axis=1)
    df = df.drop('Apps', axis=1)
    df.rename({0:'starts', 1:'sub_apps'},axis=1, inplace=True)
    return df

apps_columns(df)

df.describe()



df['Apps'][0]
df.head()
df.info()
