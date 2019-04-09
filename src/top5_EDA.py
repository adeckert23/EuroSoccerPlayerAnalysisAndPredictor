import numpy as np
import pandas as pd
import os
import re
import matplotlib.pyplot as plt
from importlib import reload
import dataframe_cleaner
from dataframe_cleaner import df_cleaner
import funcs
reload(funcs)
from funcs import DF_Scaler
#os.chdir('..')


df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')

from funcs import league_seperator, MVP_calculator, ratings_grabber

df = df_cleaner(df)

Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)

# MVP_calculator(Bundesliga)
# ratings_grabber(Bundesliga)

#-------------------------------------------------------------------------------





#-------------------------------------------------------------------------------
#Bundesliga.describe()#50% min percentile = 963
# Prem.describe()     #50% min percentile = 1217
# La_liga.describe()  #50% min percentile = 1116
# Ligue_1.describe()  #50% min percentile = 964
# Serie_a.describe()  #50% min percentile = 967

Germ_median = Bundesliga[Bundesliga['Mins']>963]
Prem_median = Prem[Prem['Mins']>1217]
La_liga_median = La_liga[La_liga['Mins']>1116]
Ligue_1_median = Ligue_1[Ligue_1['Mins']>964]
Serie_a_median = Serie_a[Serie_a['Mins']>967]
#create a new dataframe with the first column
League_means = pd.DataFrame(data=Germ_median.mean(), columns=['Bundesliga'])
#adding each league column after that
League_means['Prem'] = Prem_median.mean()
League_means['La_liga'] = La_liga_median.mean()
League_means['Ligue_1'] = Ligue_1_median.mean()
League_means['Serie_a'] = Serie_a_median.mean()

#transpose for better format for graphing, better shape to compare leagues
League_means = League_means.transpose()
League_means

#Weights used to figure out MVP
MVP_weights = np.array([1,.5,-.15,-2,1/100, .25, .2, .15, -.15, -.25, -.25, .25, .33,
                        .25, .2, -.4])
#Columns in dataframe to compute MVP
col2s = ['Goals', 'Assists', 'Yel', 'Red', 'PS%', 'AerialsWon', 'KeyP', 'Drb',
        'Off', 'Disp', 'UnsTch', 'Tackles', 'Inter', 'Clear', 'Blocks', 'OwnG']
