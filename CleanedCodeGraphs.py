# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:33:35 2022

@author: Lizmot34
"""
### Has Continous Loading and Graphs, Needs Annual Valuse and Graphs for each Subbasin
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.close("all")
Model1 = 'C:/Users/Lizmot34/Desktop/EM_RBF_Ani_PSG/EM_RBF_v03_Ani/Salinity/salt.output.channels.txt'
GraphName = "Predicted Soils and Geology RBF"


###Pull in Observed Data
##Site 09364500 = Outlet = Subarea 75
OutletData = pd.read_excel('C:/Users/Lizmot34/Desktop/ObservedSaltData.xlsx', 
                     sheet_name='09364500Salts', skiprows = 1)
OutletData.drop(OutletData.index[0:36],0, inplace=True)
Outletdates = OutletData.Start_date
Discharge=OutletData.Discharge
ConcOutSO4 = OutletData.SO4
LoadOutSO4 = (Discharge * 28.3168) * (ConcOutSO4 / 1000) * (86400  / 1000)
ConcOutCO3 = OutletData.CO3
LoadOutCO3 = (Discharge * 28.3168) * (ConcOutCO3 / 1000) * (86400  / 1000)
ConcOutHCO3 = OutletData.HCO3
LoadOutHCO3 = (Discharge * 28.3168) * (ConcOutHCO3 / 1000) * (86400  / 1000)
ConcOutCa = OutletData.Ca
LoadOutCa = (Discharge * 28.3168) * (ConcOutCa / 1000) * (86400  / 1000)
ConcOutMg = OutletData.Mg
LoadOutMg = (Discharge * 28.3168) * (ConcOutMg / 1000) * (86400  / 1000)
ConcOutNa = OutletData.Na
LoadOutNa = (Discharge * 28.3168) * (ConcOutNa / 1000) * (86400  / 1000)
ConcOutK = OutletData.K
LoadOutK = (Discharge * 28.3168) * (ConcOutK / 1000) * (86400  / 1000)
ConcOutCl = OutletData.Cl
LoadOutCl = (Discharge * 28.3168) * (ConcOutCl / 1000) * (86400  / 1000)


##Site 09361500 = Site 41
ObservedData41 = pd.read_excel('C:/Users/Lizmot34/Desktop/ObservedSaltData.xlsx',
                     sheet_name='09361500Salts', skiprows = 1)
ObservedData41.drop(ObservedData41.index[0:64],0,inplace=True)
Observeddates41 = ObservedData41.Start_date
Discharge41=ObservedData41.Discharge
ConcOb41SO4 = ObservedData41.SO4
LoadOb41SO4 = (Discharge41 * 28.3168) * (ConcOb41SO4 / 1000) * (86400  / 1000)
ConcOb41Ca = ObservedData41.Ca
LoadOb41Ca = (Discharge41 * 28.3168) * (ConcOb41Ca / 1000) * (86400  / 1000)
ConcOb41Mg = ObservedData41.Mg
LoadOb41Mg = (Discharge41 * 28.3168) * (ConcOb41Mg / 1000) * (86400  / 1000)
ConcOb41Na = ObservedData41.Na
LoadOb41Na = (Discharge41 * 28.3168) * (ConcOb41Na / 1000) * (86400  / 1000)
ConcOb41K = ObservedData41.K
LoadOb41K = (Discharge41 * 28.3168) * (ConcOb41K / 1000) * (86400  / 1000)
ConcOb41Cl = ObservedData41.Cl
LoadOb41Cl = (Discharge41 * 28.3168) * (ConcOb41Cl / 1000) * (86400  / 1000)


##Site 09359020 = Subarea 12
ObservedData12 = pd.read_excel('C:/Users/Lizmot34/Desktop/ObservedSaltData.xlsx', 
                     sheet_name='09359020Salts',skiprows = 1)
ObservedData12.drop(ObservedData12.index[0:3],0,inplace=True)
Observeddates12 = ObservedData12.Start_date
Discharge12=ObservedData12.Discharge
ConcOb12SO4 = ObservedData12.SO4
LoadOb12SO4 = (Discharge12 * 28.3168) * (ConcOb12SO4 / 1000) * (86400  / 1000)
ConcOb12Ca = ObservedData12.Ca
LoadOb12Ca = (Discharge12 * 28.3168) * (ConcOb12Ca / 1000) * (86400  / 1000)
ConcOb12Mg = ObservedData12.Mg
LoadOb12Mg = (Discharge12 * 28.3168) * (ConcOb12Mg / 1000) * (86400  / 1000)
ConcOb12Na = ObservedData12.Na
LoadOb12Na = (Discharge12 * 28.3168) * (ConcOb12Na / 1000) * (86400  / 1000)
ConcOb12K = ObservedData12.K
LoadOb12K = (Discharge12 * 28.3168) * (ConcOb12K / 1000) * (86400  / 1000)
ConcOb12Cl = ObservedData12.Cl
LoadOb12Cl = (Discharge12 * 28.3168) * (ConcOb12Cl / 1000) * (86400  / 1000)
ConcOb12HCO3 = ObservedData12.HCO3
LoadOb12HCO3 = (Discharge12 * 28.3168) * (ConcOb12HCO3 / 1000) * (86400  / 1000)

##Site 09358000 = Subarea 9
ObservedData9 = pd.read_excel('C:/Users/Lizmot34/Desktop/ObservedSaltData.xlsx', 
                     sheet_name='09358000Salts', skiprows = 1)
ObservedData9.drop(ObservedData9.index[0:3],0,inplace=True)
Observeddates9 = ObservedData9.Start_date
Discharge9 = ObservedData9.Discharge
ConcOb9SO4 = ObservedData9.SO4
LoadOb9SO4 = (Discharge9 * 28.3168) * (ConcOb9SO4 / 1000) * (86400  / 1000)
ConcOb9Ca = ObservedData9.Ca
LoadOb9Ca = (Discharge9 * 28.3168) * (ConcOb9Ca / 1000) * (86400  / 1000)
ConcOb9Mg = ObservedData9.Mg
LoadOb9Mg = (Discharge9 * 28.3168) * (ConcOb9Mg / 1000) * (86400  / 1000)
ConcOb9Na = ObservedData9.Na
LoadOb9Na = (Discharge9 * 28.3168) * (ConcOb9Na / 1000) * (86400  / 1000)
ConcOb9K = ObservedData9.K
LoadOb9K = (Discharge9 * 28.3168) * (ConcOb9K / 1000) * (86400  / 1000)

#
####Pull in Model 1 Data
Mod1 = pd.read_csv(Model1 ,skiprows = 4, delim_whitespace = True)
#Drop Data till the End of Warmup
Mod1.drop(Mod1.index[0:136950],0,inplace=True)
datestart = np.array('1992-01-01', dtype=np.datetime64)
dates = datestart + np.arange(7305)
years = Mod1.year

###Subarea 75 
##Continuous
Sub75 = Mod1[Mod1.subarea == 75]
SO4_75L = Sub75.load_so4
Ca_75L = Sub75.load_ca
Mg_75L = Sub75.load_mg
Na_75L = Sub75.load_na
K_75L = Sub75.load_k
Cl_75L = Sub75.load_cl
CO3_75L = Sub75.load_co3
HCO3_75L = Sub75.load_hco3
##Annual
years75 = years.unique()
Sub75Annual = Sub75.groupby("year").mean()
SO4_75LAnn = Sub75Annual.load_so4
Ca_75LAnn = Sub75Annual.load_ca
Mg_75LAnn = Sub75Annual.load_mg
Na_75LAnn = Sub75Annual.load_na
K_75LAnn = Sub75Annual.load_k
Cl_75LAnn = Sub75Annual.load_cl
CO3_75LAnn = Sub75Annual.load_co3
HCO3_75LAnn = Sub75Annual.load_hco3

##Subarea 41
#Continuous
Sub41 = Mod1[Mod1.subarea == 41]
SO4_41L = Sub41.load_so4
Ca_41L = Sub41.load_ca
Mg_41L = Sub41.load_mg
Na_41L = Sub41.load_na
K_41L = Sub41.load_k
Cl_41L = Sub41.load_cl
HCO3_41L = Sub41.load_hco3
CO3_41L = Sub41.load_co3
#Annual
years41 = years.unique()
Sub41Annual = Sub41.groupby("year").mean()
SO4_41LAnn = Sub41Annual.load_so4
Ca_41LAnn = Sub41Annual.load_ca
Mg_41LAnn = Sub41Annual.load_mg
Na_41LAnn = Sub41Annual.load_na
K_41LAnn = Sub41Annual.load_k
Cl_41LAnn = Sub41Annual.load_cl
CO3_41LAnn = Sub41Annual.load_co3
HCO3_41LAnn = Sub41Annual.load_hco3
##Subarea 12
#Continuous
Sub12 = Mod1[Mod1.subarea == 12]
SO4_12L = Sub12.load_so4
Ca_12L = Sub12.load_ca
Mg_12L = Sub12.load_mg
Na_12L = Sub12.load_na
K_12L = Sub12.load_k
Cl_12L = Sub12.load_cl
CO3_12L = Sub12.load_co3
HCO3_12L = Sub12.load_hco3
#Annual
years12 = years.unique()
Sub12Annual = Sub12.groupby("year").mean()
SO4_12LAnn = Sub12Annual.load_so4
Ca_12LAnn = Sub12Annual.load_ca
Mg_12LAnn = Sub12Annual.load_mg
Na_12LAnn = Sub12Annual.load_na
K_12LAnn = Sub12Annual.load_k
Cl_12LAnn = Sub12Annual.load_cl
CO3_12LAnn = Sub12Annual.load_co3
HCO3_12LAnn = Sub12Annual.load_hco3
##Subarea 9
#Continuous
Sub9 = Mod1[Mod1.subarea == 9]
SO4_9L = Sub9.load_so4
Ca_9L = Sub9.load_ca
Mg_9L = Sub9.load_mg
Na_9L = Sub9.load_na
K_9L = Sub9.load_k
Cl_9L = Sub9.load_cl
CO3_9L = Sub9.load_co3
HCO3_9L = Sub9.load_hco3
#Annual
years9 = years.unique()
Sub9Annual = Sub9.groupby("year").mean()
SO4_9LAnn = Sub9Annual.load_so4
Ca_9LAnn = Sub9Annual.load_ca
Mg_9LAnn = Sub9Annual.load_mg
Na_9LAnn = Sub9Annual.load_na
K_9LAnn = Sub9Annual.load_k
Cl_9LAnn = Sub9Annual.load_cl
CO3_9LAnn = Sub9Annual.load_co3
HCO3_9LAnn = Sub9Annual.load_hco3


#####Make some Graphs
####Annual
###Sulfate
fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
ax.plot(years75, SO4_75LAnn, color='blue', label='75')
ax.plot(years41, SO4_41LAnn, color='red', label='41')
ax.plot(years12, SO4_12LAnn, color='green', label='12')
ax.plot(years9, SO4_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("SO4 Annual Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4AnnualAll.png')
###Carbonate 
fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
ax.plot(years75, CO3_75LAnn, color='blue', label='75')
ax.plot(years41, CO3_41LAnn, color='red', label='41')
ax.plot(years12, CO3_12LAnn, color='green', label='12')
ax.plot(years9, CO3_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("CO3 Annual Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/CO3AnnualAll.png')
###Bicarbonate
fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
ax.plot(years75, HCO3_75LAnn, color='blue', label='75')
ax.plot(years41, HCO3_41LAnn, color='red', label='41')
ax.plot(years12, HCO3_12LAnn, color='green', label='12')
ax.plot(years9, HCO3_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("HCO3 Annual Loading {}".format(GraphName))
ax.legend()
###Calcium
fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
ax.plot(years75, Ca_75LAnn, color='blue', label='75')
ax.plot(years41, Ca_41LAnn, color='red', label='41')
ax.plot(years12, Ca_12LAnn, color='green', label='12')
ax.plot(years9, Ca_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("Ca Annual Loading {}".format(GraphName))
ax.legend()
###Magnesiums
fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
ax.plot(years75, Mg_75LAnn, color='blue', label='75')
ax.plot(years41, Mg_41LAnn, color='red', label='41')
ax.plot(years12, Mg_12LAnn, color='green', label='12')
ax.plot(years9, Mg_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("Mg Annual Loading")
ax.legend()
###Sodium
fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
ax.plot(years75, Na_75LAnn, color='blue', label='75')
ax.plot(years41, Na_41LAnn, color='red', label='41')
ax.plot(years12, Na_12LAnn, color='green', label='12')
ax.plot(years9, Na_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("Na Annual Loading {}".format(GraphName))
ax.legend()
###Potassium
fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
ax.plot(years75, K_75LAnn, color='blue', label='75')
ax.plot(years41, K_41LAnn, color='red', label='41')
ax.plot(years12, K_12LAnn, color='green', label='12')
ax.plot(years9, K_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("K Annual Loading {}".format(GraphName))
ax.legend()
###Cholrine
fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
ax.plot(years75, Cl_75LAnn, color='blue', label='75')
ax.plot(years41, Cl_41LAnn, color='red', label='41')
ax.plot(years12, Cl_12LAnn, color='green', label='12')
ax.plot(years9, Cl_9LAnn, color='yellow', label='9')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("Cl Annual Loading {}".format(GraphName))
ax.legend()
###Subarea 75
##Continuous 
#Sulfate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutSO4, color='red', label='observed')
ax.plot(dates, SO4_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_75_Contin.png')
#Carbonate 
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutCO3, color='red', label='observed')
ax.plot(dates, CO3_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 CO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/CO3_75_Contin.png')
#Bicarbonate 
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutHCO3, color='red', label='observed')
ax.plot(dates, HCO3_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 HCO3 Loading {}".format(GraphName))
ax.legend()
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutCa, color='red', label='observed')
ax.plot(dates, Ca_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_75_Contin.png')
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutMg, color='red', label='observed')
ax.plot(dates, Mg_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Mg Loading {}".format(GraphName))
ax.legend()
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutNa, color='red', label='observed')
ax.plot(dates, Na_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Na Loading {}".format(GraphName))
ax.legend()
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutK, color='red', label='observed')
ax.plot(dates, K_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 K Loading {}".format(GraphName))
ax.legend()
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Outletdates, LoadOutCl, color='red', label='observed')
ax.plot(dates, Cl_75L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Cl Loading {}".format(GraphName))
ax.legend()

## Subarea 41 - Has no CO3 or HCO3 Observed data
##Continuous
#Sulfate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates41, LoadOb41SO4, color='red', label='observed')
ax.plot(dates, SO4_41L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_41_Contin.png')
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates41, LoadOb41Ca, color='red', label='observed')
ax.plot(dates, Ca_41L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_41_Contin.png')
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates41, LoadOb41Mg, color='red', label='observed')
ax.plot(dates, Mg_41L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Mg Loading {}".format(GraphName))
ax.legend()
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates41, LoadOb41Na, color='red', label='observed')
ax.plot(dates, Na_41L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Na Loading {}".format(GraphName))
ax.legend()
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates41, LoadOb41K, color='red', label='observed')
ax.plot(dates, K_41L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 K Loading {}".format(GraphName))
ax.legend()
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates41, LoadOb41Cl, color='red', label='observed')
ax.plot(dates, Cl_41L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Cl Loading {}".format(GraphName))
ax.legend()

##Subarea 12 - No CO3 Observed Data
#Sulfate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates12, LoadOb12SO4, color='red', label='observed')
ax.plot(dates, SO4_12L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_12_Contin.png')
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates12, LoadOb12Ca, color='red', label='observed')
ax.plot(dates, Ca_12L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_12_Contin.png')
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates12, LoadOb12Mg, color='red', label='observed')
ax.plot(dates, Mg_12L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 Mg Loading {}".format(GraphName))
ax.legend()
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates12, LoadOb12Na, color='red', label='observed')
ax.plot(dates, Na_12L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 Na Loading {}".format(GraphName))
ax.legend()
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates12, LoadOb12K, color='red', label='observed')
ax.plot(dates, K_12L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("12 K Loading {}".format(GraphName))
ax.legend()
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates12, LoadOb12Cl, color='red', label='observed')
ax.plot(dates, Cl_12L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("12 Cl Loading {}".format(GraphName))
ax.legend()
#Bicarbonate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates12, LoadOb12HCO3, color='red', label='observed')
ax.plot(dates, HCO3_12L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("12 CO3 Loading {}".format(GraphName))
ax.legend()

##Subarea 9 - Doesn't have CO3, HCO3, or Cl Observed data
#Sulfate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates9, LoadOb9SO4, color='red', label='observed')
ax.plot(dates, SO4_9L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_9_Contin.png')
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates9, LoadOb9Ca, color='red', label='observed')
ax.plot(dates, Ca_9L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_9_Contin.png')
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates9, LoadOb9Mg, color='red', label='observed')
ax.plot(dates, Mg_9L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 Mg Loading {}".format(GraphName))
ax.legend()
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates9, LoadOb9Na, color='red', label='observed')
ax.plot(dates, Na_9L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 Na Loading {}".format(GraphName))
ax.legend()
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.scatter(Observeddates9, LoadOb9K, color='red', label='observed')
ax.plot(dates, K_9L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("9 K Loading {}".format(GraphName))
ax.legend()
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates, Cl_9L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("9 Cl Loading {}".format(GraphName))
ax.legend()
#Bicarbonate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates, HCO3_9L, color='blue', label='modeled')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("9 HCO3 Loading {}".format(GraphName))
ax.legend()