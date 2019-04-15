#Merging 2 dataframes to make predictions on fifa data player stats
import numpy as np
import pandas as pd
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


fifa = pd.read_csv('data/fifa19_data.csv')
fifa = fc.fifa_df_cleaner(fifa)
#Scraped data of top 5 leagues
df = pd.read_csv('/Users/alexdeckwork/Galvanize/Galvrepos/soccer-proj/data/top5.csv')
df = df_cleaner(df)

#drop club values that have NA
fifa = fifa.dropna(subset=['Club'])
# df = df.dropna(subset=['Team'])

def accent_stripper(series):
    a=[]
    for item in series:
        a.append(unidecode.unidecode(item))
    return a

#strip accents from name from both datasets
fifa['Name'] = accent_stripper(fifa['Name'].values)
df['Player'] = accent_stripper(df['Player'].values)
fifa['Club'] = accent_stripper(fifa['Club'].values)
df['Team'] = accent_stripper(df['Team'].values)


#map team names so they match both databases
fifa['Club'] = fifa['Club'].map(fifa_names)
df['Team'] = df['Team'].map(scraped_names)

# THIS IS MY UNIQUE ID FOR THE FIFA DATASET
fifa['UniqueID'] = fifa['Name'].str.split(' ')
fifa['UniqueID'] = fifa['UniqueID'].str[-1]
fifa['UniqueID'] = fifa['UniqueID']+fifa['Club']


#UniqueID creation for scraped dataset
df['UniqueID'] = df['Player'].str.split(' ')
df['UniqueID'] = df['UniqueID'].str[-1]
df['UniqueID'] = df['UniqueID'] + df['Team']


master = df.merge(fifa, how='inner', on='UniqueID')
#dropping duplicates, unclean rows, and fake data/mis-information
master.drop(axis=0,index=index_td, inplace=True)
master.columns
#-------------------------------------------------------------------------------
#master[master['UniqueID']=='MurphyCardiff']

Neymar = df[df['Player']=='Neymar']
Neymar2 = fifa[fifa['Name']=='Neymar Jr']
Neymar2['UniqueID'] = 'NeymarPSG'

neymar = Neymar.merge(Neymar2, how='outer', on='UniqueID')
neymar.shape
master.shape
master = master.append(neymar)

master

#-------------------------------------------------------------------------------

def accent_stripper(series):
    a=[]
    for item in series:
        a.append(unidecode.unidecode(item))
    return a


#Seperating the leagues to test on?
Bundesliga, Prem, La_liga, Ligue_1, Serie_a = league_seperator(df)
#-------------------------------------------------------------------------------
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

 fifa_names = {'Milan':'ACMilan', 'Amiens SC': 'Amiens', 'Angers SCO': 'Angers',
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
