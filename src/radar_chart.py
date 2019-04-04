import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
df = df.drop(labels=['Unnamed: 0','Goals.1', 'Assists.1', 'SpG.1', 'Drb.1',
            'Assists.2', 'KeyP.1', 'PS%.1'], axis=1)
cols = ['Goals', 'Assists', 'Yel', 'Red', 'SpG', 'PS%', 'AerialsWon', 'MotM',
        'KeyP', 'Drb', 'Fouled', 'Off', 'Disp', 'UnsTch', 'Tackles', 'Inter',
        'Fouls', 'Offsides', 'Clear', 'Blocks', 'OwnG', 'AvgP', 'Crosses',
        'LongB', 'ThrB']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
#need to fill NaN's with 0's
df.fillna(0, inplace=True)
df.drop_duplicates(keep='first', inplace=True)
df.columns
#final list of columns to choose from
cols2 = ['player', 'position', 'Team', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb',
        'KeyP','PS%', 'Crosses', 'Fouled', 'Disp','UnsTch', 'AerialsWon', 'Tackles', 'Inter',
        'Fouls', 'Clear', 'Blocks']

#offensive radar chart
off_cats = ['player', 'position', 'Team', 'Rating', 'Goals', 'Assists', 'SpG', 'Drb',
        'KeyP','PS%', 'Crosses', 'Fouled', 'Disp','UnsTch','Tackles', 'Inter']
#defensive radar chart
def_cats = ['player', 'position', 'Team', 'Rating', 'Goals', 'Assists', 'Drb',
        'KeyP','PS%', 'Crosses', 'Disp','UnsTch', 'AerialsWon', 'Tackles', 'Inter',
        'Fouls', 'Clear', 'Blocks']
# number of variable
categories=list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1)
