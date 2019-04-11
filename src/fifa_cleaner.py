#Fifa DF Cleaner
import numpy as np
import pandas as pd

def fifa_df_cleaner(df):
    #dropping columns I don't think are important currently
    df.drop(labels=['Unnamed: 0', 'Photo', 'Nationality', 'Flag', 'Potential',
    'Club Logo', 'Value', 'Wage', 'Special', 'International Reputation', 'Weak Foot',
    'Skill Moves', 'Real Face', 'Jersey Number', 'Joined', 'Loaned From',
    'Contract Valid Until', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning',
    'GKReflexes', 'Release Clause', 'Body Type', 'RB', 'RCB', 'CB', 'LCB', 'LB',
    'RWB','RDM','CDM','LDM','LWB', 'RM', 'RCM', 'CM', 'LCM', 'LM', 'RAM', 'CAM',
    'LAM', 'RW', 'RF', 'CF', 'LF', 'LW', 'RS', 'ST', 'LS', 'Preferred Foot'],inplace=True, axis=1)

    #splitting work rate into offensive/defensive
    subset = df['Work Rate'].str.split('/',expand=True)
    df = pd.concat((df, subset), axis=1)
    df.drop('Work Rate', axis=1, inplace=True)
    df.rename({0:'Attacking Work Rate', 1:'Defensive Work Rate'},axis=1, inplace=True)

    #dummy the work rate columns
    df = pd.get_dummies(df, columns=['Attacking Work Rate', 'Defensive Work Rate'])
    df.drop('Attacking Work Rate_Low', axis=1, inplace=True)
    df.drop('Defensive Work Rate_ Low', axis=1, inplace=True)

    return df
