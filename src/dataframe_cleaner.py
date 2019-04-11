#DF CLEANER
import numpy as np
import pandas as pd

#should run df = df_cleaner(df) to return all changes inplace=True
def df_cleaner(df):
    #need to drop categories based on duplicates from scraped data
    df = df.drop(labels=['Unnamed: 0','Goals.1', 'Assists.1', 'SpG.1', 'Drb.1',
                'Assists.2', 'KeyP.1', 'PS%.1'], axis=1)
    #need to cleanup the data, first changing all columns from object to numerical
    cols = ['Goals', 'Assists', 'Yel', 'Red', 'SpG', 'PS%', 'AerialsWon', 'MotM',
            'KeyP', 'Drb', 'Fouled', 'Off', 'Disp', 'UnsTch', 'Tackles', 'Inter',
            'Fouls', 'Offsides', 'Clear', 'Blocks', 'OwnG', 'AvgP', 'Crosses',
            'LongB', 'ThrB']
    #changing columns to numeric from object/strings
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
    #need to fill NaN's with 0's
    df.fillna(0, inplace=True)
    #feature engineering 2 bad touch/miscontrolled column to one cumulative column
    df['mis_cont'] = round(df['Disp']+df['UnsTch'],3)
    #Duplicate players, originally 2798, now down to 2546
    df.drop_duplicates(keep='first', inplace=True)
    #Dummy the league names
    df = pd.get_dummies(df, columns=['league'])
    #rename the dummied columns
    df.rename({'league_England-Premier-League':'English_Prem',
     'league_France-Ligue-1':'Ligue_1', 'league_Germany-Bundesliga':'Bundesliga',
     'league_Italy-Serie-A': 'Serie_A', 'league_Spain-La-Liga':'La_Liga'},axis=1, inplace=True)
    #player column has whitespace at the end of the name, create new column to remove
    df['Player'] = df['player'].str.strip()
    #drop original player column
    #drop Disp and Unstch now that they are combined in mis_cont
    df.drop(labels=['player', 'Disp', 'UnsTch'], axis=1, inplace=True)

    def clean_apps_col(df):
        subset = df['Apps'].str.split('(', expand=True)
        df = pd.concat((df, subset), axis=1)
        df = df.drop('Apps', axis=1)
        df.rename({0:'starts', 1:'sub_apps'},axis=1, inplace=True)
        df['starts']=df['starts'].apply(pd.to_numeric, errors='coerce')
        return df

    def clean_sub_apps_col(df):
        df['sub_apps'].fillna(0, inplace=True)
        df['sub_apps'] = df['sub_apps'].str.strip(')')
        df['sub_apps'].fillna(0, inplace=True)
        df['sub_apps']=df['sub_apps'].apply(pd.to_numeric, errors='coerce')
        return df

    df = clean_apps_col(df)
    df = clean_sub_apps_col(df)
    #columns and order I want the dataframe to end up as
    cs = ['Player', 'age', 'position', 'Mins','starts', 'sub_apps', 'Rating',
        'Goals', 'Assists','SpG', 'PS%', 'MotM', 'KeyP', 'Drb','Fouled', 'Off',
        'mis_cont', 'AerialsWon','Tackles','Inter','Fouls', 'Offsides','Clear', 'Blocks',
        'OwnG', 'AvgP', 'Crosses','LongB','ThrB', 'Yel','Red','KG','CM',
        'English_Prem', 'Ligue_1', 'Bundesliga','Serie_A', 'La_Liga', 'Team']
    df = df[cs]

    return df
