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
            'Crosses', 'Fouled', 'mis_cont']
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
Bundesliga['Player'] = f.accent_stripper(Bundesliga['Player'].values)
#--------------------------------------
#Sending in the Premier League to the scaler
from funcs import DF_Scaler
scaled_df = DF_Scaler(Ligue_1)

Ligue_1[Ligue_1['Team']=='Paris Saint-Germain']

#--------------------------------------
chart_prep = scaled_df[off_cats]
#--------------------------------------
Prem[Prem['Player']=='Benjamin Mendy']
#Playmakers to radar plot
Mbappe = chart_prep.loc[2343].values
Cavani = chart_prep.loc[2336].values
Neymar = chart_prep.loc[2350].values
Pepe = chart_prep.loc[2427].values

#Figure
fig.clear()

fig = plt.figure(figsize=(10, 10))
#Name to appear
titles =['Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
            'Crosses', 'Fouled', 'mis_cont']
#Numerical labels to be displayed along each axis
labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,27,6),2),
    np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,4.3,6),2),
    np.around(np.linspace(0,4.8,6),2), np.around(np.linspace(0,3.2,6),2),
    np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,2.8,6),2),
    np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,8.5,6),2)]


radar = Radar1(fig, titles, labels)
radar.plot(Mbappe[1:], '-', lw=5, color='r', alpha=0.4, label=Mbappe[0])
radar.plot(Neymar[1:], '-', lw=5, color='b', alpha=0.4, label=Neymar[0])
radar.plot(Cavani[1:], '-', lw=5, color='g', alpha=0.4, label=Cavani[0])
#radar.plot(Pepe[1:], '-', lw=5, color='m', alpha=0.4, label=Pepe[0])

radar.ax.legend()
fig.suptitle('PSG Front Three', fontsize=22)
fig.savefig('PSG_Front_Three.png')
