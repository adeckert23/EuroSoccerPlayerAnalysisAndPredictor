import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
import funcs as f
from importlib import reload
import dataframe_cleaner
reload(radar1_class)
import radar1_class
from radar1_class import Radar1
import unidecode
from unidecode import unidecode
#final list of columns to choose from
cols2 = ['Player', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
        'Crosses', 'Fouled', 'mis_cont', 'AerialsWon', 'Tackles', 'Inter',
        'Fouls', 'Clear', 'Blocks']

off_cats = ['Player', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
            'Crosses', 'Fouled', 'mis_cont','Tackles', 'Inter']
cats = ['Player', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
        'Fouled', 'mis_cont']
#Defensive currently has 13, need to take out 1 of them
center_def_cats = ['Player', 'Rating', 'AvgP','PS%', 'mis_cont', 'AerialsWon',
                    'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']
outside_def_cats = ['Player', 'Rating', 'Assists', 'Drb','PS%', 'Crosses',
            'mis_cont', 'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']

#-------------------------------------------------------------------------------

#Need imported clean DF
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
from dataframe_cleaner import df_cleaner
df = df_cleaner(df)

from funcs import league_seperator
Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)


from funcs import accent_stripper
df['Player'] = f.accent_stripper(df['Player'].values)
#--------------------------------------
#Sending in the Premier League to the scaler
from funcs import DF_Scaler
scaled_df = DF_Scaler(Prem)

#--------------------------------------
chart_prep = scaled_df[outside_def_cats]
#--------------------------------------
Prem[Prem['Player']=='Trent Alexander-Arnold']

#Playmakers to radar plot
Walker = chart_prep.loc[139].values
Young = chart_prep.loc[177].values
Tripp = chart_prep.loc[403].values
TAE = chart_prep.loc[435].values
Bellerin = chart_prep.loc[502].values
AWB = chart_prep.loc[77].values
#Figure
fig.clear()

fig = plt.figure(figsize=(10, 10))
#Name to appear
titles =['Rating', 'Assists', 'Drb','PS%', 'Crosses', 'mis_cont', 'Tackles',
        'Inter', 'Fouls', 'Clear', 'Blocks']
#Numerical labels to be displayed along each axis
labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,9,6),2),
    np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,100,6),2),
    np.around(np.linspace(0,3,6),2), np.around(np.linspace(0,6,6),2),
    np.around(np.linspace(0,5,6),2), np.around(np.linspace(0,3.2,6),2),
    np.around(np.linspace(0,4,6),2),np.around(np.linspace(0,6,6),2), np.around(np.linspace(0,1.6,6),2)]

radar = Radar1(fig, titles, labels)
radar.plot(Young[1:], '-', lw=5, color='r', alpha=0.4, label=Young[0])
radar.plot(AWB[1:], '-', lw=5, color='#FF00FF', alpha=0.4, label=AWB[0])

radar.ax.legend()
fig.suptitle('Premier League Right Backs', fontsize=22)
fig.savefig('Prem_RB_Replacement.png')
