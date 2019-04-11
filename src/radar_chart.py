import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
import funcs
from importlib import reload
import dataframe_cleaner
reload(funcs)
import radar1_class
from radar1_class import Radar1
#final list of columns to choose from
cols2 = ['Player', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
        'Crosses', 'Fouled', 'mis_cont', 'AerialsWon', 'Tackles', 'Inter',
        'Fouls', 'Clear', 'Blocks']

off_cats = ['Player', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
            'Crosses', 'Fouled', 'mis_cont','Tackles', 'Inter']

#Defensive currently has 13, need to take out 1 of them
center_def_cats = ['Player', 'Rating', 'AvgP','PS%', 'mis_cont', 'AerialsWon',
                    'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']
outside_def_cats = ['Player', 'Rating', 'AvgP', 'Assists', 'Drb', 'KeyP','PS%', 'Crosses',
            'mis_cont', 'AerialsWon', 'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']

#-------------------------------------------------------------------------------

#Need imported clean DF
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
from dataframe_cleaner import df_cleaner
df = df_cleaner(df)

from funcs import league_seperator
Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)

# df = df[df['age']<22]
# df = df[df['Mins']>1000]
# df.sort_values(by=['Rating'])

#--------------------------------------
#Sending in the Bundesliga to the scaler first
from funcs import DF_Scaler
scaled_df = DF_Scaler(df)

#--------------------------------------
young_center_backs_chart = scaled_df[center_def_cats]
#--------------------------------------
# df = df[df['Mins']>500]
# df['Blocks'].describe()
# df[df['Player']=='Raphael Varane']

#Playmakers to radar plot
Ndicka = young_center_backs_chart.loc[1676].values
Zag = young_center_backs_chart.loc[1922].values
Konate = young_center_backs_chart.loc[1806].values
Muki = young_center_backs_chart.loc[2267].values
Bastoni = young_center_backs_chart.loc[779].values
Varane = young_center_backs_chart.loc[1510].values


#Figure
fig.clear()

fig = plt.figure(figsize=(10, 10))
#Name to appear
titles = ['Rating', 'AvgP','PS%', 'mis_cont','AerialsWon', 'Tackles', 'Inter',
            'Fouls', 'Clear', 'Blocks']
#Numerical labels to be displayed along each axis
labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,91,6),2),
    np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,8.8,6),2),
    np.around(np.linspace(0,7.8,6),2), np.around(np.linspace(0,4.4,6),2),
    np.around(np.linspace(0,3,6),2), np.around(np.linspace(0,2.7,6),2),
    np.around(np.linspace(0,7.4,6),2), np.around(np.linspace(0,1.6,6),2)]

radar = Radar1(fig, titles, labels)
radar.plot(Varane[1:], '-', lw=3, color='#00FFFF', alpha=0.4, label=Varane[0])
radar.plot(Ndicka[1:], '-', lw=3, color='r', alpha=0.4, label=Ndicka[0])
radar.plot(Zag[1:], '-', lw=3, color='#FFFF00', alpha=0.4, label=Zag[0])
radar.plot(Konate[1:], '-', lw=3, color='#FF00FF', alpha=0.4, label=Konate[0])
radar.plot(Muki[1:], '-', lw=3, color='b', alpha=0.4, label=Muki[0])
radar.plot(Bastoni[1:], '-', lw=3, color='g', alpha=0.4, label=Bastoni[0])

radar.ax.legend()
fig.suptitle('Young Defenders', fontsize=16)
fig.savefig('Young_Defenders.png')


#-------------------------------------------------------------------------------
