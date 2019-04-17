import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
import funcs as f
from importlib import reload
import dataframe_cleaner
reload(unidecode)
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

#Defensive currently has 13, need to take out 1 of them
center_def_cats = ['Player', 'Rating', 'AvgP','PS%', 'mis_cont', 'AerialsWon',
                    'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']
outside_def_cats = ['Player', 'Rating', 'AvgP', 'Assists', 'Drb','PS%', 'Crosses',
            'mis_cont', 'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']

#-------------------------------------------------------------------------------

#Need imported clean DF
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
from dataframe_cleaner import df_cleaner
df = df_cleaner(df)

from funcs import league_seperator
Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)


from funcs import accent_stripper
Prem['Player'] = f.accent_stripper(Prem['Player'].values)
#--------------------------------------
#Sending in the Premier League to the scaler
from funcs import DF_Scaler
scaled_df = DF_Scaler(df)

#--------------------------------------
OBchart_prep = df[outside_def_cats]
#--------------------------------------

df[df['Player']=='Achraf Hakimi']
# Prem.columns
# Prem['Blocks'].describe()

#Playmakers to radar plot
Mendy = OBchart_prep.loc[2775].values
Gaya = OBchart_prep.loc[1429].values
Chilwell = OBchart_prep.loc[103].values
Hakimi = OBchart_prep.loc[1919].values
Henrichs = OBchart_prep.loc[2266].values
Wan_Bissaka = OBchart_prep.loc[77].values


#Figure
fig.clear()

fig = plt.figure(figsize=(10, 10))
#Name to appear
titles = ['Rating', 'AvgP', 'Assists', 'Drb','PS%', 'Crosses',
            'mis_cont', 'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']
#Numerical labels to be displayed along each axis
labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,91,6),2),
    np.around(np.linspace(0,11,6),2), np.around(np.linspace(0,3.2,6),2),
    np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,2.3,6),2),
    np.around(np.linspace(0,8.8,6),2), np.around(np.linspace(0,4.3,6),2),
    np.around(np.linspace(0,2.9,6),2), np.around(np.linspace(0,2.3,6),2),
    np.around(np.linspace(0,11,6),2), np.around(np.linspace(0,1.6,6),2)]

radar = Radar1(fig, titles, labels)
# radar.plot(Mendy[1:], '-', lw=3, color='r', alpha=0.4, label=Mendy[0])
# radar.plot(Gaya[1:], '-', lw=3, color='#F0770A', alpha=0.4, label=Gaya[0])
# radar.plot(Chilwell[1:], '-', lw=3, color='b', alpha=0.4, label=Chilwell[0])
radar.plot(Hakimi[1:], '-', lw=3, color='#E9E405', alpha=0.4, label=Hakimi[0])
radar.plot(Henrichs[1:], '-', lw=3, color='#0A1190', alpha=0.4, label=Henrichs[0])
radar.plot(Wan_Bissaka[1:], '-', lw=3, color='k', alpha=0.4, label=Wan_Bissaka[0])


radar.ax.legend()
fig.suptitle('RB replacements', fontsize=16)
fig.savefig('RB_replacements.png')


#-------------------------------------------------------------------------------
