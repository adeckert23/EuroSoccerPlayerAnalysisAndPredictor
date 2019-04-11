#Merging 2 dataframes to make predictions on fifa data player stats
import numpy as np
import pandas as pd
import sqlite3
import os
import re
import matplotlib.pyplot as plt
from importlib import reload
import dataframe_cleaner
from dataframe_cleaner import df_cleaner
import funcs as f
import unidecode
import fifa_cleaner as fc
reload(dataframe_cleaner)
os.chdir('..')

#establish connection to sql database
# cnx = sqlite3.connect('EuropeanSoccerDataProject/database.sqlite')
#
#
# #reading in player names and player attribute data
# player_data = pd.read_sql_query('SELECT * FROM Player_Attributes', cnx)
# player_names = pd.read_sql_query('SELECT * FROM Player', cnx)
# #clean up player data, so now both tables are the same legnth
# player_data = f.player_data_cleaner(player_data)
#drop id column that means nothing for both dataframes
# player_data.drop(labels='id',axis=1,inplace=True)
# player_names.drop(labels='id', axis=1, inplace=True)
#Merged player data with player names
#fifa = player_names.merge(player_data, how='outer', left_on=['player_fifa_api_id', 'player_api_id'])

fifa = pd.read_csv('data/fifa19_data.csv')
fifa = fc.fifa_df_cleaner(fifa)
fifa




df.columns







name_series = fifa['Name'].str.split(' ')
name_series[0][-1]

f.fifa_data_cleaner(fifa)




#Scraped data of top 5 leagues
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
df = df_cleaner(df)

df.tail(30)
# unidecode.unidecode(type(df['Player'].values)
# type(df['Player'].values

def accent_stripper(series):
    a=[]
    for item in series:
        a.append(unidecode.unidecode(item))
    return a

df['Player'] = accent_stripper(df['Player'].values)

master_df = df.merge(fifa, how='outer', left_on='Player', right_on='player_name')
master_df = master_df.dropna(subset=['Goals'])
master_df.sort_values('Player')
master_df.info()

fifa['player_name'].str.contains('')
fifa.tail(100)
#cleaning the data
df = df_cleaner(df)

#Seperating the leagues to test on?
Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)
