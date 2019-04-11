#functions folder
import numpy as np
import pandas as pd
import os
import re
# os.chdir('..')

#pass in main clean dataframe
def league_seperator(df):
     #seperate all the leagues
    Bundesliga = df[df['Bundesliga']==1]
    Bundesliga.drop(labels=['English_Prem', 'Ligue_1', 'Serie_A', 'Bundesliga',
                    'La_Liga'], axis=1, inplace=True)
    Prem = df[df['English_Prem']==1]
    Prem.drop(labels=['English_Prem', 'Ligue_1', 'Serie_A', 'Bundesliga',
                    'La_Liga'], axis=1, inplace=True)
    La_liga = df[df['La_Liga']==1]
    La_liga.drop(labels=['English_Prem', 'Ligue_1', 'Serie_A', 'Bundesliga',
                    'La_Liga'], axis=1, inplace=True)
    Ligue_1 = df[df['Ligue_1']==1]
    Ligue_1.drop(labels=['English_Prem', 'Ligue_1', 'Serie_A', 'Bundesliga',
                    'La_Liga'], axis=1, inplace=True)
    Serie_a = df[df['Serie_A']==1]
    Serie_a.drop(labels=['English_Prem', 'Ligue_1', 'Serie_A', 'Bundesliga',
                    'La_Liga'], axis=1, inplace=True)
    return Bundesliga, Prem, La_liga, Ligue_1, Serie_a

#pass in a league dataframe, output scaled features
def DF_Scaler(df):
    cols = ['Goals', 'Assists', 'SpG', 'PS%','KeyP', 'Drb', 'AvgP', 'Fouled',
    'mis_cont', 'Tackles', 'Inter', 'Crosses', 'Fouls', 'Clear', 'Blocks']
    df['Rating'] = (df['Rating']*5)/10
    for item in cols:
        Max = df[item].max()
        df[item] = (df[item]*5)/Max
    return df

#ideally pass in seperate leagues, but can work with full dataframe also
def MVP_calculator(df):
    #columns used to compute MVP
    col2s = ['Goals', 'Assists', 'Yel', 'Red', 'PS%', 'AerialsWon', 'KeyP', 'Drb',
            'Off', 'mis_cont', 'Tackles', 'Inter', 'Clear', 'Blocks', 'OwnG']
    #Weights used to figure out MVP
    MVP_weights = np.array([1, .5, -.15, -2, 1/100, .25, .2, .15, -.15, -.25,
                            .25, .33, .25, .2, -.4])
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

#fifa player names cleaner
def fifa_data_cleaner(df):
    df.drop(labels=['Unnamed: 0', 'Photo', 'Nationality', 'Flag', 'Potential',
    'Club Logo', 'Value', 'Wage', 'Special', 'International Reputation', 'Weak Foot',
    'Skill Moves', 'Real Face', 'Jersey Number', 'Joined', 'Loaned From',
    'Contract Valid Until', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning',
    'GKReflexes', 'Release Clause'],inplace=True, axis=1)
    return df
