#Merging 2 dataframes to make predictions on fifa data player stats
import numpy as np
import pandas as pd
import os
import re
from importlib import reload
import dataframe_cleaner
from dataframe_cleaner import df_cleaner
import funcs as f
import fifa_cleaner as fc
from funcs import accent_stripper
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
reload(f)
os.chdir('..')


fifa = pd.read_csv('data/fifa19_data.csv')
fifa = fc.fifa_df_cleaner(fifa)
fifa.info()
#Scraped data of top 5 leagues
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
df = df_cleaner(df)

#scraped df as df1, fifa df as df2
def join_tables(scraped, feef):

    scraped_names = {'AC Milan': 'ACMilan', 'Amiens': 'Amiens', 'Angers':'Angers',
     'Arsenal':'Arsenal','Atalanta':'Atalanta', 'Athletic Bilbao': 'AthleticBilbao',
     'Atletico Madrid': 'AtleticoMadrid', 'Augsburg':'Augsburg', 'Barcelona':'Barcelona',
     'Bayer Leverkusen': 'BayerLeverkusen', 'Bayern Munich':'BayernMunich',
     'Bologna':'Bologna', 'Bordeaux':'Bordeaux', 'Borussia Dortmund':'BorussiaDortmund',
     'Borussia M.Gladbach': 'BorussiaMonchengladbach', 'Bournemouth':'Bournemouth',
     'Brighton':'Brighton', 'Burnley':'Burnley', 'Caen':'Caen', 'Cagliari':'Cagliari',
     'Cardiff':'Cardiff', 'Celta Vigo':'CeltaVigo', 'Chelsea':'Chelsea','Chievo':'Chievo',
     'Crystal Palace':'CrystalPalace','Deportivo Alaves':'DeportivoAlaves',
     'Dijon':'Dijon', 'Eibar':'Eibar', 'Eintracht Frankfurt':'EintrachtFrankfurt',
     'Empoli':'Empoli', 'Espanyol':'Espanyol', 'Everton':'Everton', 'Fiorentina':'Fiorentina',
     'Fortuna Duesseldorf':'FortunaDuesseldorf', 'Freiburg':'Freiburg', 'Frosinone':'Frosinone',
     'Fulham':'Fulham', 'Genoa':'Genoa','Getafe':'Getafe', 'Girona':'Girona',
     'Guingamp':'Guingamp', 'Hannover 96':'Hannover96', 'Hertha Berlin':'HerthaBerlin',
     'Hoffenheim':'Hoffenheim', 'Huddersfield':'Huddersfield', 'Inter':'InterMilan',
     'Juventus':'Juventus', 'Lazio':'Lazio', 'Leganes':'Leganes', 'Leicester':'Leicester',
     'Levante':'Levante', 'Lille':'Lille','Liverpool':'Liverpool','Lyon':'Lyon',
     'Mainz 05': 'Mainz05','Manchester City':'ManchesterCity','Manchester United':'ManchesterUnited',
     'Marseille':'Marseille','Monaco':'Monaco','Montpellier':'Montpellier','Nantes':'Nantes',
     'Napoli':'Napoli', 'Newcastle United':'NewcastleUnited','Nice':'Nice','Nimes':'Nimes',
     'Nuernberg':'Nuernberg','Paris Saint-Germain':'PSG', 'Parma Calcio 1913':'Parma',
     'RasenBallsport Leipzig':'RBLeipzig', 'Rayo Vallecano':'RayoVallecano',
     'Real Betis':'RealBetis', 'Real Madrid':'RealMadrid','Real Sociedad':'RealSociedad',
     'Real Valladolid':'Real Valladolid', 'Reims':'Reims','Rennes':'Rennes','Roma':'Roma',
     'SD Huesca':'Huesca','SPAL 2013':'SPAL', 'Saint-Etienne':'SaintEtienne',
     'Sampdoria':'Sampdoria','Sassuolo':'Sassuolo','Schalke 04':'Schalke',
     'Sevilla':'Sevilla', 'Southampton':'Southampton', 'Strasbourg':'Strasbourg',
     'Torino':'Torino','Tottenham':'Tottenham','Toulouse':'Toulouse','Udinese':'Udinese',
     'Valencia':'Valencia', 'VfB Stuttgart':'Stuttgart','Villarreal':'Villarreal',
     'Watford':'Watford','Werder Bremen':'WerderBremen','West Ham':'WestHam',
     'Wolfsburg':'Wolfsburg','Wolverhampton Wanderers':'Wolves'}

    feef_names = {'Milan':'ACMilan', 'Amiens SC': 'Amiens', 'Angers SCO': 'Angers',
     'Arsenal':'Arsenal','Atalanta':'Atalanta', 'Athletic Club de Bilbao': 'AthleticBilbao',
     'Atletico Madrid': 'AtleticoMadrid', 'FC Augsburg':'Augsburg', 'FC Barcelona':'Barcelona',
     'Bayer 04 Leverkusen': 'BayerLeverkusen', 'FC Bayern Munchen':'BayernMunich',
     'Bologna':'Bologna', 'FC Girondins de Bordeaux':'Bordeaux', 'Borussia Dortmund':'BorussiaDortmund',
     'Borussia Monchengladbach':'BorussiaMonchengladbach', 'Bournemouth':'Bournemouth',
     'Brighton & Hove Albion':'Brighton', 'Burnley':'Burnley', 'Stade Malherbe Caen':'Caen',
     'Cagliari':'Cagliari', 'Cardiff City':'Cardiff', 'RC Celta':'CeltaVigo','Chelsea':'Chelsea',
     'Chievo Verona':'Chievo', 'Crystal Palace':'CrystalPalace', 'Deportivo Alaves':'DeportivoAlaves',
     'Dijon FCO':'Dijon', 'SD Eibar':'Eibar', 'Eintracht Frankfurt':'EintrachtFrankfurt',
     'Empoli':'Empoli', 'RCD Espanyol':'Espanyol', 'Everton':'Everton', 'Fiorentina':'Fiorentina',
     'Fortuna Duesseldorf':'FortunaDuesseldorf', 'SC Freiburg':'Freiburg', 'Frosinone':'Frosinone',
     'Fulham':'Fulham','Genoa':'Genoa', 'Getafe CF':'Getafe', 'Girona FC':'Girona',
     'En Avant de Guingamp':'Guingamp', 'Hannover 96':'Hannover96', 'Hertha BSC':'HerthaBerlin',
     'TSG 1899 Hoffenheim':'Hoffenheim', 'Huddersfield Town':'Huddersfield', 'Inter':'InterMilan',
     'Juventus':'Juventus', 'Lazio':'Lazio', 'CD Leganes':'Leganes', 'Leicester City':'Leicester',
     'Levante UD':'Levante', 'LOSC Lille':'Lille', 'Liverpool':'Liverpool', 'Olympique Lyonnais':'Lyon',
     '1. FSV Mainz 05': 'Mainz05', 'Manchester City':'ManchesterCity', 'Manchester United':'ManchesterUnited',
     'Olympique de Marseille':'Marseille', 'AS Monaco':'Monaco', 'Montpellier HSC':'Montpellier',
     'FC Nantes':'Nantes', 'Napoli':'Napoli', 'Newcastle United':'NewcastleUnited', 'OGC Nice':'Nice',
     'Nimes Olympique':'Nimes','1. FC Nurnberg':'Nuernberg', 'Paris Saint-Germain':'PSG',
     'Parma':'Parma', 'RB Leipzig':'RBLeipzig','Rayo Vallecano':'RayoVallecano',
     'Real Betis':'RealBetis', 'Real Madrid':'RealMadrid','Real Sociedad':'RealSociedad',
     'Real Valladolid CF':'Real Valladolid', 'Stade de Reims':'Reims', 'Stade Rennais FC':'Rennes',
     'Roma':'Roma','SD Huesca':'Huesca','SPAL':'SPAL', 'AS Saint-Etienne':'SaintEtienne',
     'Sampdoria':'Sampdoria','Sassuolo':'Sassuolo','FC Schalke 04':'Schalke',
     'Sevilla FC':'Sevilla', 'Southampton':'Southampton','RC Strasbourg Alsace':'Strasbourg',
     'Torino':'Torino','Tottenham Hotspur':'Tottenham','Toulouse Football Club':'Toulouse',
     'Udinese':'Udinese','Valencia CF':'Valencia', 'VfB Stuttgart':'Stuttgart','Villarreal CF':'Villarreal',
     'Watford':'Watford','SV Werder Bremen':'WerderBremen','West Ham United':'WestHam',
     'VfL Wolfsburg':'Wolfsburg','Wolverhampton Wanderers':'Wolves'}

    #index to drop
    index_td = [444,1929,925,926,1668,1670,778,779,117,120,2227,2228,1035,1038,246,249,1353,1356,1398,
                1399,1553,1552,1337,958,1205,1318,1317,2122,2123,192,361,794,795,1051,1363,1364,1365,
                1366,1367,1368,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,
                1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192]

    #strip accents from name from both datasets
    feef['Name'] = f.accent_stripper(feef['Name'].values)
    feef['Club'] = f.accent_stripper(feef['Club'].values)
    scraped['Player'] = f.accent_stripper(scraped['Player'].values)
    scraped['Team'] = f.accent_stripper(scraped['Team'].values)

    #map team names so they match both databases
    feef['Club'] = feef['Club'].map(feef_names)
    scraped['Team'] = scraped['Team'].map(scraped_names)

    # THIS IS MY UNIQUE ID FOR THE FIFA DATASET
    feef['UniqueID'] = feef['Name'].str.split(' ')
    feef['UniqueID'] = feef['UniqueID'].str[-1]
    feef['UniqueID'] = feef['UniqueID']+feef['Club']

    #UniqueID creation for scraped dataset
    scraped['UniqueID'] = scraped['Player'].str.split(' ')
    scraped['UniqueID'] = scraped['UniqueID'].str[-1]
    scraped['UniqueID'] = scraped['UniqueID'] + scraped['Team']


    master = scraped.merge(feef, how='inner', on='UniqueID')
    #dropping duplicates, unclean rows, and fake data/mis-information
    master.drop(axis=0,index=index_td, inplace=True)

    Neymar = scraped[scraped['Player']=='Neymar']
    Neymar2 = feef[feef['Name']=='Neymar Jr']
    Neymar2['UniqueID'] = 'NeymarPSG'
    neymar = Neymar.merge(Neymar2, how='outer', on='UniqueID')
    master = master.append(neymar)

    master.drop(labels=['Name', 'Age', 'ID', 'Club', 'position',
                        'KG','CM'],axis=1, inplace=True)

    return master
#-------------------------------------------------------------------------------
#Tables are now joined above
#First, let's predict overall
#Second, let's go granular and predict a player profile
#()
join_tables(df, fifa)
#-------------------------------------------------------------------------------

master.head()
master.columns
master.info()
X = master.loc[:,['Mins', 'Rating', 'Goals', 'Assists','SpG', 'PS%', 'MotM',
'KeyP','Drb','Fouled','mis_cont','AerialsWon','Tackles','Inter','Fouls',
'Offsides', 'Clear','Blocks', 'AvgP', 'LongB', 'ThrB']]
y= master.loc[:,['Overall']].values
y = np.ravel(y)

from sklearn.preprocessing import StandardScaler
model = StandardScaler()
X_scaled = model.fit_transform(X)
X_scaled

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25)

GBmodel = GradientBoostingRegressor(learning_rate=.01, n_estimators=1200, subsample=.75)
GBmodel.fit(X_train, y_train)

GBmodel.score(X_test, y_test)
GBmodel.feature_importances_


master2 = master.copy()
#-------------------------------------------------------------------------------
#predicting granular columns
#FINISHING
master.columns
master = master.dropna(subset=['Finishing'])
X_shooting = master.loc[:,['Mins', 'Rating', 'Goals','SpG', 'PS%',
'KeyP','mis_cont','Tackles','Inter','Blocks']]
y_shooting= master.loc[:,['Finishing']].values
y = np.ravel(y)

master.info()

model = StandardScaler()
X_scaled_shooting = model.fit_transform(X_shooting)
X_train, X_test, y_train, y_test = train_test_split(X_shooting, y_shooting, test_size=0.25)
GBmodel.fit(X_train, y_train)
GBmodel.score(X_test, y_test)
GBmodel.feature_importances_
a = GBmodel.predict(X_shooting)
master2['Predicted_Finishing'] = a
#--------------------first attribute above-----------------------------
#SHORT PASSING
#LONG PASSING
X_passing = master.loc[:,['Mins', 'Rating','Assists', 'SpG', 'PS%',
'KeyP','mis_cont', 'Clear','Blocks', 'AvgP','ThrB','LongB']]
y_pass1 = master.loc[:,['ShortPassing']].values
y_pass2 = master.loc[:,['LongPassing']].values
y_pass1 = np.ravel(y_pass1)
y_pass2 = np.ravel(y_pass2)

X_train, X_test, y_train, y_test = train_test_split(X_passing, y_pass2, test_size=0.25)
GBmodel.fit(X_train, y_train)
GBmodel.score(X_test, y_test)
GBmodel.feature_importances_

master2['Predicted_long_passing'] = GBmodel.predict(X_passing)
#-------------------------------------------------------------------------------
master.columns
master2.tail()
#DRIBBLING
#BALL CONTROL
X_dribbling = master.loc[:,['Mins', 'Rating','SpG', 'PS%','KeyP','Drb',
'mis_cont','Fouls','Clear','Blocks', 'AvgP', 'LongB']]
y_drb = master.loc[:,['Dribbling']].values
y_bc = master.loc[:,['BallControl']].values
y_drb = np.ravel(y_drb)
y_bc = np.ravel(y_bc)

X_train, X_test, y_train, y_test = train_test_split(X_dribbling, y_bc, test_size=0.25)
GBmodel.fit(X_train, y_train)
GBmodel.score(X_test, y_test)
GBmodel.feature_importances_

master2['Predicted_Dribbling'] = GBmodel.predict(X_dribbling)
master2['Predicted_Ball_Control'] = GBmodel.predict(X_dribbling)
#-------------------------------------------------------------------------------
#Predicting Interceptions, Marking, STD tackle, SLIDE Tackle
X_defense = master.loc[:,['Mins', 'Rating', 'PS%','mis_cont',
'AerialsWon','Tackles','Inter','Fouls','Clear','Blocks','LongB']]
y_inter = master.loc[:,['Interceptions']].values
y_inter = np.ravel(y_inter)
y_mark = master.loc[:,['Marking']].values
y_mark = np.ravel(y_mark)
y_tackle = master.loc[:,['StandingTackle']].values
y_tackle = np.ravel(y_tackle)
y_slide = master.loc[:,['SlidingTackle']].values
y_slide = np.ravel(y_slide)

X_train, X_test, y_train, y_test = train_test_split(X_defense, y_slide, test_size=0.25)
GBmodel.fit(X_train, y_train)
GBmodel.score(X_test, y_test)
GBmodel.feature_importances_

master2['Predicted_Interceptions'] = GBmodel.predict(X_defense)
master2['Predicted_Marking'] = GBmodel.predict(X_defense)
master2['Predicted_Std_Tackle'] = GBmodel.predict(X_defense)
master2['Predicted_Sliding_Tackle'] = GBmodel.predict(X_defense)
#-------------------------------------------------------------------------------
#Predicting Overall based on generated predicted attributes
X_overall = master2.loc[:,['Predicted_Dribbling', 'Predicted_Marking', 'Predicted_Finishing',
'Predicted_Std_Tackle', 'Predicted_Ball_Control','Predicted_long_passing',
'Predicted_Interceptions', 'Predicted_Sliding_Tackle']]
y_overall = master.loc[:,['Overall']].values
y_overall = np.ravel(y_overall)

X_train, X_test, y_train, y_test = train_test_split(X_overall, y_overall, test_size=0.25)
GBmodel.fit(X_train, y_train)
GBmodel.score(X_test, y_test)
GBmodel.feature_importances_

master2['Predicted_Overall'] = GBmodel.predict(X_overall)
#-------------------------------------------------------------------------------
master2[master2['Player']=='Neymar']
master2.columns
master3 = master2.loc[:,['Player', 'Finishing', 'Predicted_Finishing', 'Dribbling',
'Predicted_Dribbling', 'ShortPassing','Predicted_short_passing', 'LongPassing',
'Predicted_long_passing', 'BallControl', 'Predicted_Ball_Control', 'Interceptions',
'Predicted_Interceptions', 'Marking','Predicted_Marking', 'StandingTackle',
'Predicted_Std_Tackle', 'SlidingTackle','Predicted_Sliding_Tackle', 'Overall','Predicted_Overall']]

master3[master3['Player']=='Luka Modric']
pd.set_option('display.max_columns', 500)

#-------------------------------------------------------------------------------

Player_Profile = master2.loc[:,['Player', 'age', 'Team','UniqueID',]]
#-------------------------------------------------------------------------------
master2.columns

#Seperating the leagues to test on?
Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)


#-------------------------------------------------------------------------------
