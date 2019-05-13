#Saved information for generating plots:
#-------------------------------------------------------------------------------
# #Figure
# fig.clear()
# fig = plt.figure(figsize=(10, 10))
#Name to appear on each axis for offensive categories
# titles = ['Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
#         'Crosses', 'Fouled', 'mis_cont','Tackles', 'Inter']
#-------------------------------------------------------------------------------
#Bund Playmakers:
# Sancho = bundesliga_chart_df.loc[1924].values
# Gnabry = bundesliga_chart_df.loc[1716].values
# Brandt = bundesliga_chart_df.loc[1654].values
# Muller = bundesliga_chart_df.loc[1719].values
# Hazard = bundesliga_chart_df.loc[1959].values
# Kostic = bundesliga_chart_df.loc[1677].values

# labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,19,6),2),
#     np.around(np.linspace(0,13,6),2), np.around(np.linspace(0,4.3,6),2),
#     np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,3,6),2),
#     np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,2.7,6),2),
#     np.around(np.linspace(0,2.8,6),2), np.around(np.linspace(0,5.8,6),2),
#     np.around(np.linspace(0,4,6),2), np.around(np.linspace(0,3,6),2)]

# radar = Radar1(fig, titles, labels)
# radar.plot(Sancho[1:], '-', lw=3, color='#FFFF00', alpha=0.4, label=Sancho[0])
# radar.plot(Gnabry[1:], '-', lw=3, color='r', alpha=0.4, label=Gnabry[0])
# radar.plot(Brandt[1:], '-', lw=3, color='k', alpha=0.4, label=Brandt[0])
# radar.plot(Muller[1:], '-', lw=3, color='m', alpha=0.4, label=Muller[0])
# radar.plot(Hazard[1:], '-', lw=3, color= '#0000FF', alpha=0.4, label=Hazard[0])
# radar.plot(Kostic[1:], '-', lw=3, color='#008080', alpha=0.4, label=Kostic[0])

# radar.ax.legend()
# fig.suptitle('Bundesliga Playmakers', fontsize=16)
# fig.savefig('Bund_Playmakers.png')

#-------------------------------------------------------------------------------
#Premier League Playmakers
# Hazard = Prem_chart_df.loc[285].values
# Eriksen = Prem_chart_df.loc[390].values
# Sane = Prem_chart_df.loc[140].values
# Sterling = Prem_chart_df.loc[144].values
# Salah = Prem_chart_df.loc[429].values


# labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,19,6),2),
#     np.around(np.linspace(0,11,6),2), np.around(np.linspace(0,3.9,6),2),
#     np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,3,6),2),
#     np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,2.3,6),2),
#     np.around(np.linspace(0,3,6),2), np.around(np.linspace(0,8.8,6),2),
#     np.around(np.linspace(0,4.3,6),2), np.around(np.linspace(0,2.9,6),2)]

# radar = Radar1(fig, titles, labels)
# radar.plot(Hazard[1:], '-', lw=3, color='#FFFF00', alpha=0.4, label=Hazard[0])
# radar.plot(Eriksen[1:], '-', lw=3, color='#000080', alpha=0.4, label=Eriksen[0])
# radar.plot(Sane[1:], '-', lw=3, color='m', alpha=0.4, label=Sane[0])
# radar.plot(Sterling[1:], '-', lw=3, color='#00FFFF', alpha=0.4, label=Sterling[0])
# radar.plot(Salah[1:], '-', lw=3, color= 'r', alpha=0.4, label=Salah[0])
# radar.plot(Pogba[1:], '-', lw=3, color='k', alpha=0.4, label=Pogba[0])

# radar.ax.legend()
# fig.suptitle('Premier League Playmakers', fontsize=16)
# fig.savefig('Prem_Playmakers.png')
#-------------------------------------------------------------------------------
#FIFA PLAYER OF THE YEAR COMPARISON FOLLOW UP
#Messi vs Ronaldo

# Modric = df_chart_df.loc[1504].values
# Ronaldo= df_chart_df.loc[729].values
# Salah = df_chart_df.loc[429].values
# Mbappe = df_chart_df.loc[2343].values
# Messi = df_chart_df.loc[1241].values

# labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,32,6),2),
#     np.around(np.linspace(0,13,6),2), np.around(np.linspace(0,6.1,6),2),
#     np.around(np.linspace(0,4.8,6),2), np.around(np.linspace(0,3.2,6),2),
#     np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,3,6),2),
#     np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,8.8,6),2),
#     np.around(np.linspace(0,6.5,6),2), np.around(np.linspace(0,3.2,6),2)]

# radar = Radar1(fig, titles, labels)
# radar.plot(Modric[1:], '-', lw=3, color='#000000', alpha=0.4, label=Modric[0])
# radar.plot(Ronaldo[1:], '-', lw=3, color='#800000', alpha=0.4, label=Ronaldo[0])
# radar.plot(Salah[1:], '-', lw=3, color='#FF0000', alpha=0.4, label=Salah[0])
# radar.plot(Mbappe[1:], '-', lw=3, color='#0000FF', alpha=0.4, label=Mbappe[0])
# radar.plot(Messi[1:], '-', lw=3, color='#00FFFF', alpha=0.4, label=Messi[0])
#
# radar.ax.legend()
# fig.suptitle('FIFA Player of the Year follow up', fontsize=16)
# fig.savefig('Fifa_POY.png')
#-------------------------------------------------------------------------------
#Serie A STRIKERS storeyline

# Ronaldo= serie_a_chart.loc[729].values
# Quag = serie_a_chart.loc[1004].values
# Icardi = serie_a_chart.loc[664].values
# PiatekG = serie_a_chart.loc[608].values
# PiatekM = serie_a_chart.loc[961].values

# labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,21,6),2),
#     np.around(np.linspace(0,9,6),2), np.around(np.linspace(0,6.1,6),2),
#     np.around(np.linspace(0,2.9,6),2), np.around(np.linspace(0,3.2,6),2),
#     np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,2.9,6),2),
#     np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,6.3,6),2),
#     np.around(np.linspace(0,4.2,6),2), np.around(np.linspace(0,3.2,6),2)]

# radar = Radar1(fig, titles, labels)
# radar.plot(Ronaldo[1:], '-', lw=3, color='#FF00FF', alpha=0.4, label=Ronaldo[0])
# radar.plot(Quag[1:], '-', lw=3, color='b', alpha=0.4, label=Quag[0])
# radar.plot(Icardi[1:], '-', lw=3, color='k', alpha=0.4, label=Icardi[0])
# radar.plot(PiatekG[1:], '-', lw=3, color='#00FFFF', alpha=0.4, label=PiatekG[0])
# radar.plot(PiatekM[1:], '-', lw=3, color='r', alpha=0.4, label=PiatekM[0])
#-------------------------------------------------------------------------------
#Piatek on Genoa vs Piatek on Milan

# PiatekG = serie_a_chart.loc[608].values
# PiatekM = serie_a_chart.loc[961].values
#
#labels/linspace from serie_a above

# radar = Radar1(fig, titles, labels)
# radar.plot(PiatekG[1:], '-', lw=3, color='#0000FF', alpha=0.4, label='Piatek Genoa')
# radar.plot(PiatekM[1:], '-', lw=3, color='r', alpha=0.4, label='Piatek Milan')
#
# radar.ax.legend()
# fig.suptitle('Piatek Before and After the Transfer', fontsize=16)
# fig.savefig('Piatek.png')

#-------------------------------------------------------------------------------
#Identifying young defenders to scout further.
#Under 20 years old, compared to possibly best young CB in the world Varane

# Ndicka = young_center_backs_chart.loc[1676].values
# Zag = young_center_backs_chart.loc[1922].values
# Konate = young_center_backs_chart.loc[1806].values
# Muki = young_center_backs_chart.loc[2267].values
# Bastoni = young_center_backs_chart.loc[779].values
# Varane = young_center_backs_chart.loc[1510].values

# titles = ['Rating', 'AvgP','PS%', 'mis_cont','AerialsWon', 'Tackles', 'Inter',
#             'Fouls', 'Clear', 'Blocks']
#
# labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,91,6),2),
#     np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,8.8,6),2),
#     np.around(np.linspace(0,7.8,6),2), np.around(np.linspace(0,4.4,6),2),
#     np.around(np.linspace(0,3,6),2), np.around(np.linspace(0,2.7,6),2),
#     np.around(np.linspace(0,7.4,6),2), np.around(np.linspace(0,1.6,6),2)]
#
# radar = Radar1(fig, titles, labels)
# radar.plot(Varane[1:], '-', lw=3, color='#00FFFF', alpha=0.4, label=Varane[0])
# radar.plot(Ndicka[1:], '-', lw=3, color='r', alpha=0.4, label=Ndicka[0])
# radar.plot(Zag[1:], '-', lw=3, color='#FFFF00', alpha=0.4, label=Zag[0])
# radar.plot(Konate[1:], '-', lw=3, color='#FF00FF', alpha=0.4, label=Konate[0])
# radar.plot(Muki[1:], '-', lw=3, color='b', alpha=0.4, label=Muki[0])
# radar.plot(Bastoni[1:], '-', lw=3, color='g', alpha=0.4, label=Bastoni[0])
#
# radar.ax.legend()
# fig.suptitle('Young Defenders', fontsize=16)
# fig.savefig('Young_Defenders.png')

#-------------------------------------------------------------------------------
# Robertson = chart_prep.loc[419].values
# Shaw = chart_prep.loc[186].values
# Alonso = chart_prep.loc[291].values
# Rose = chart_prep.loc[391].values
# Kolasinac = chart_prep.loc[514].values
# Mendy = chart_prep.loc[128].values
#
# #Figure
# fig.clear()
#
# fig = plt.figure(figsize=(10, 10))
# #Name to appear
# titles =['Rating', 'Assists', 'Drb','PS%', 'Crosses', 'mis_cont', 'Tackles', 'Inter', 'Fouls', 'Clear', 'Blocks']
# #Numerical labels to be displayed along each axis
# labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,11,6),2),
#     np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,100,6),2),
#     np.around(np.linspace(0,2.3,6),2), np.around(np.linspace(0,8.8,6),2),
#     np.around(np.linspace(0,4.3,6),2), np.around(np.linspace(0,2.9,6),2),
#     np.around(np.linspace(0,2.3,6),2), np.around(np.linspace(0,5,6),2),
#     np.around(np.linspace(0,1,6),2)]
#
#
# radar = Radar1(fig, titles, labels)
# radar.plot(Robertson[1:], '-', lw=5, color='r', alpha=0.4, label=Robertson[0])
# radar.plot(Shaw[1:], '-', lw=5, color='k', alpha=0.4, label=Shaw[0])
# radar.plot(Alonso[1:], '-', lw=5, color='b', alpha=0.4, label=Alonso[0])
# radar.plot(Rose[1:], '-', lw=5, color='m', alpha=0.4, label=Rose[0])
# radar.plot(Kolasinac[1:], '-', lw=5, color= 'g', alpha=0.4, label=Kolasinac[0])
# radar.plot(Mendy[1:], '-', lw=5, color= 'c', alpha=0.4, label=Mendy[0])
#
# radar.ax.legend()
# fig.suptitle('Premier League LB', fontsize=22)
# fig.savefig('Prem_LB.png')
#-------------------------------------------------------------------------------
# Bale = chart_prep.loc[1496].values
# Benzema = chart_prep.loc[1500].values
# Asensio = chart_prep.loc[1506].values
#
# #Figure
# fig.clear()
#
# fig = plt.figure(figsize=(10, 10))
# #Name to appear
# titles =['Rating', 'Goals', 'Assists', 'SpG', 'Drb', 'KeyP','PS%',
#             'Crosses', 'Fouled', 'mis_cont']
# #Numerical labels to be displayed along each axis
# labels = [np.around(np.linspace(0,10,6),2), np.around(np.linspace(0,32,6),2),
#     np.around(np.linspace(0,12,6),2), np.around(np.linspace(0,5.2,6),2),
#     np.around(np.linspace(0,4.1,6),2), np.around(np.linspace(0,2.9,6),2),
#     np.around(np.linspace(0,100,6),2), np.around(np.linspace(0,3,6),2),
#     np.around(np.linspace(0,3.2,6),2), np.around(np.linspace(0,7,6),2)]
#
#
# radar = Radar1(fig, titles, labels)
# radar.plot(Bale[1:], '-', lw=5, color='r', alpha=0.4, label=Bale[0])
# radar.plot(Benzema[1:], '-', lw=5, color='b', alpha=0.4, label=Benzema[0])
# radar.plot(Asensio[1:], '-', lw=5, color='g', alpha=0.4, label=Asensio[0])
#
# radar.ax.legend()
# fig.suptitle('Ronaldos Replacement', fontsize=22)
# fig.savefig('Madrid_front_three.png')
#-------------------------------------------------------------------------------
