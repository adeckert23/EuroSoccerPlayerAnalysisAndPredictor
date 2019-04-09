import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

import funcs
from importlib import reload
import dataframe_cleaner
reload(radar1_class)
import radar1_class
from radar1_class import Radar1
#final list of columns to choose from
cols2 = ['Player', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
        'Crosses', 'Fouled', 'mis_cont', 'AerialsWon', 'Tackles', 'Inter',
        'Fouls', 'Clear', 'Blocks']

off_cats = ['Player', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
            'Crosses', 'Fouled', 'mis_cont','Tackles', 'Inter']

#Defensive currently has 13, need to take out 1 of them
def_cats = ['Player', 'Rating', 'Goals', 'Assists', 'Drb', 'KeyP','PS%', 'Crosses',
            'mis_cont', 'AerialsWon', 'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']

#-------------------------------------------------------------------------------

#Need imported clean DF
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
from dataframe_cleaner import df_cleaner
df = df_cleaner(df)

from funcs import league_seperator
Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)

#--------------------------------------
#Sending in the Bundesliga to the scaler
from funcs import DF_Scaler
scaled_df = DF_Scaler(Bundesliga)

#--------------------------------------
bundesliga_chart_df = scaled_df[off_cats]
#--------------------------------------
Bundesliga.head()
Bundesliga.sort_values(by=['Assists'], ascending=False)


#Playmakers to radar plot
Sancho = bundesliga_chart_df.loc[1924].values
Gnabry = bundesliga_chart_df.loc[1716].values
Brandt = bundesliga_chart_df.loc[1654].values
Muller = bundesliga_chart_df.loc[1719].values
Hazard = bundesliga_chart_df.loc[1959].values

#Figure
fig.clear()
fig = plt.figure(figsize=(10, 10))
#Name to appear
titles = ['Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
        'Crosses', 'Fouled', 'mis_cont','Tackles', 'Inter']
#Numerical labels to be displayed along each axis
labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,19,6),2),
    np.around(np.linspace(0,13,6),2), np.around(np.linspace(0,4.3,6),2),
    np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,3,6),2),
    np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,2.7,6),2),
    np.around(np.linspace(0,2.8,6),2), np.around(np.linspace(0,5.8,6),2),
    np.around(np.linspace(0,4,6),2), np.around(np.linspace(0,3,6),2)]

radar = Radar1(fig, titles, labels)
radar.plot(Sancho[1:], '-', lw=3, color='y', alpha=0.4, label=Sancho[0])
radar.plot(Gnabry[1:], '-', lw=3, color='r', alpha=0.4, label=Gnabry[0])
radar.plot(Brandt[1:], '-', lw=3, color='c', alpha=0.4, label=Brandt[0])
radar.plot(Muller[1:], '-', lw=3, color='k', alpha=0.4, label=Muller[0])
radar.plot(Hazard[1:], '-', lw=3, color='g', alpha=0.4, label=Hazard[0])

radar.ax.legend()
fig.savefig('Bund_Playmakers.png')
# plt.show('<matplotlib.legend.legend at 0x1a29501048>')


#-------------------------------------------------------------------------------
#For future multiple players on the same plot
# radar.plot([3, 4, 3, 1, 2, 2, 4, 3, 1, 2, 3, 3], '-', lw=2, color='g', alpha=0.4, label='third')
# radar.ax.legend()
#
# fig.savefig('result.png')







#I need a figure, title, labels, ylimits
