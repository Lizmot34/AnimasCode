# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:33:35 2022

@author: Lizmot34
"""
###Has Continuous Values and Graphs, and only Annual Values
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
plt.close("all")
###Define Model Pathways
Model1 = 'C:/Users/Lizmot34/Desktop/IDW_PSG_0G/EM_IDW_v03_Ani/Salinity/salt.output.channels.txt'
Model2 = 'C:/Users/Lizmot34/Desktop/KRIGG_PSG_0G/EM_KRIGG_vo3_Ani/Salinity/salt.output.channels.txt'
Model3 = 'C:/Users/Lizmot34/Desktop/RBF-PSG-0G/EM_RBF_v03_Ani/EM_RBF_v03_Ani/SALINITY/salt.output.channels.txt'
GraphName = "Predicted Soils and Geology"
FigurePath = 'C:/Users/Lizmot34/Desktop/FinishedFigures/031122_3Models'
FigureSuffix = '3 Models'

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

###Pull in Model 1 Data
Mod1 = pd.read_csv(Model1, skiprows = 4, delim_whitespace = True)
Mod1.drop(Mod1.index[0:136950],0,inplace=True)
datestart1 = np.array('1992-01-01', dtype=np.datetime64)
dates1 = datestart1 + np.arange(7305)
years1 = Mod1.year
##Subarea 75
#Continuous
Sub75_1 = Mod1[Mod1.subarea == 75]
SO4_75L1 = Sub75_1.load_so4
Ca_75L1 = Sub75_1.load_ca
Mg_75L1 = Sub75_1.load_mg
Na_75L1 = Sub75_1.load_na
K_75L1 = Sub75_1.load_k
Cl_75L1 = Sub75_1.load_cl
CO3_75L1 = Sub75_1.load_co3
HCO3_75L1 = Sub75_1.load_hco3
#Annual
years1_75 = years1.unique()
Sub75Annual_1 = Sub75_1.groupby("year").mean()
SO4_75LAnn1 = Sub75Annual_1.load_so4
Ca_75LAnn1 = Sub75Annual_1.load_ca
Mg_75LAnn1 = Sub75Annual_1.load_mg
Na_75LAnn1 = Sub75Annual_1.load_na
K_75LAnn1 = Sub75Annual_1.load_k
Cl_75LAnn1 = Sub75Annual_1.load_cl
CO3_75LAnn1 = Sub75Annual_1.load_co3
HCO3_75LAnn1 = Sub75Annual_1.load_hco3
##Subarea 41
#Continuous
Sub41_1 = Mod1[Mod1.subarea == 41]
SO4_41L1 = Sub41_1.load_so4
Ca_41L1 = Sub41_1.load_ca
Mg_41L1 = Sub41_1.load_mg
Na_41L1 = Sub41_1.load_na
K_41L1 = Sub41_1.load_k
Cl_41L1 = Sub41_1.load_cl
HCO3_41L1 = Sub41_1.load_hco3
CO3_41L1 = Sub41_1.load_co3
#Annual
years1_41 = years1.unique()
Sub41Annual_1 = Sub41_1.groupby("year").mean()
SO4_41LAnn1 = Sub41Annual_1.load_so4
Ca_41LAnn1 = Sub41Annual_1.load_ca
Mg_41LAnn1 = Sub41Annual_1.load_mg
Na_41LAnn1 = Sub41Annual_1.load_na
K_41LAnn1 = Sub41Annual_1.load_k
Cl_41LAnn1 = Sub41Annual_1.load_cl
CO3_41LAnn1 = Sub41Annual_1.load_co3
HCO3_41LAnn1 = Sub41Annual_1.load_hco3
##Subarea 12
#Continuous
Sub12_1 = Mod1[Mod1.subarea == 12]
SO4_12L1 = Sub12_1.load_so4
Ca_12L1 = Sub12_1.load_ca
Mg_12L1 = Sub12_1.load_mg
Na_12L1 = Sub12_1.load_na
K_12L1 = Sub12_1.load_k
Cl_12L1 = Sub12_1.load_cl
CO3_12L1 = Sub12_1.load_co3
HCO3_12L1 = Sub12_1.load_hco3
#Annual
years1_12 = years1.unique()
Sub12Annual_1 = Sub12_1.groupby("year").mean()
SO4_12LAnn1 = Sub12Annual_1.load_so4
Ca_12LAnn1 = Sub12Annual_1.load_ca
Mg_12LAnn1 = Sub12Annual_1.load_mg
Na_12LAnn1 = Sub12Annual_1.load_na
K_12LAnn1 = Sub12Annual_1.load_k
Cl_12LAnn1 = Sub12Annual_1.load_cl
CO3_12LAnn1 = Sub12Annual_1.load_co3
HCO3_12LAnn1 = Sub12Annual_1.load_hco3
##Subarea 9
#Continuous
Sub9_1 = Mod1[Mod1.subarea == 9]
SO4_9L1 = Sub9_1.load_so4
Ca_9L1 = Sub9_1.load_ca
Mg_9L1 = Sub9_1.load_mg
Na_9L1 = Sub9_1.load_na
K_9L1 = Sub9_1.load_k
Cl_9L1 = Sub9_1.load_cl
CO3_9L1 = Sub9_1.load_co3
HCO3_9L1 = Sub9_1.load_hco3
#Annual
years1_9 = years1.unique()
Sub9Annual_1 = Sub9_1.groupby("year").mean()
SO4_9LAnn1 = Sub9Annual_1.load_so4
Ca_9LAnn1 = Sub9Annual_1.load_ca
Mg_9LAnn1 = Sub9Annual_1.load_mg
Na_9LAnn1 = Sub9Annual_1.load_na
K_9LAnn1 = Sub9Annual_1.load_k
Cl_9LAnn1 = Sub9Annual_1.load_cl
CO3_9LAnn1 = Sub9Annual_1.load_co3
HCO3_9LAnn1 = Sub9Annual_1.load_hco3

###Pull in Model 2 Data
Mod2 = pd.read_csv(Model2, skiprows = 4, delim_whitespace = True)
Mod2.drop(Mod2.index[0:136950], 0, inplace=True)
datestart2 = np.array('1992-01-01', dtype=np.datetime64)
dates2 = datestart2 + np.arange(7305)
years2 = Mod2.year
##Subarea 75
#Continuous
Sub75_2 = Mod2[Mod2.subarea == 75]
SO4_75L2 = Sub75_2.load_so4
Ca_75L2 = Sub75_2.load_ca
Mg_75L2 = Sub75_2.load_mg
Na_75L2 = Sub75_2.load_na
K_75L2 = Sub75_2.load_k
Cl_75L2 = Sub75_2.load_cl
CO3_75L2 = Sub75_2.load_co3
HCO3_75L2 = Sub75_2.load_hco3
#Annual
years2_75 = years2.unique()
Sub75Annual_2 = Sub75_2.groupby("year").mean()
SO4_75LAnn2 = Sub75Annual_2.load_so4
Ca_75LAnn2 = Sub75Annual_2.load_ca
Mg_75LAnn2 = Sub75Annual_2.load_mg
Na_75LAnn2 = Sub75Annual_2.load_na
K_75LAnn2 = Sub75Annual_2.load_k
Cl_75LAnn2 = Sub75Annual_2.load_cl
CO3_75LAnn2 = Sub75Annual_2.load_co3
HCO3_75LAnn2 = Sub75Annual_2.load_hco3
##Subarea 41
#Continuous
Sub41_2 = Mod2[Mod2.subarea == 41]
SO4_41L2 = Sub41_2.load_so4
Ca_41L2 = Sub41_2.load_ca
Mg_41L2 = Sub41_2.load_mg
Na_41L2 = Sub41_2.load_na
K_41L2 = Sub41_2.load_k
Cl_41L2 = Sub41_2.load_cl
HCO3_41L2 = Sub41_2.load_hco3
CO3_41L2 = Sub41_2.load_co3
#Annual
years2_41 = years2.unique()
Sub41Annual_2 = Sub41_2.groupby("year").mean()
SO4_41LAnn2 = Sub41Annual_2.load_so4
Ca_41LAnn2 = Sub41Annual_2.load_ca
Mg_41LAnn2 = Sub41Annual_2.load_mg
Na_41LAnn2 = Sub41Annual_2.load_na
K_41LAnn2 = Sub41Annual_2.load_k
Cl_41LAnn2 = Sub41Annual_2.load_cl
CO3_41LAnn2 = Sub41Annual_2.load_co3
HCO3_41LAnn2 = Sub41Annual_2.load_hco3
##Subarea 12
#Continuous
Sub12_2 = Mod2[Mod2.subarea == 12]
SO4_12L2 = Sub12_2.load_so4
Ca_12L2 = Sub12_2.load_ca
Mg_12L2 = Sub12_2.load_mg
Na_12L2 = Sub12_2.load_na
K_12L2 = Sub12_2.load_k
Cl_12L2 = Sub12_2.load_cl
CO3_12L2 = Sub12_2.load_co3
HCO3_12L2 = Sub12_2.load_hco3
#Annual
years2_12 = years2.unique()
Sub12Annual_2 = Sub12_2.groupby("year").mean()
SO4_12LAnn2 = Sub12Annual_2.load_so4
Ca_12LAnn2 = Sub12Annual_2.load_ca
Mg_12LAnn2 = Sub12Annual_2.load_mg
Na_12LAnn2 = Sub12Annual_2.load_na
K_12LAnn2 = Sub12Annual_2.load_k
Cl_12LAnn2 = Sub12Annual_2.load_cl
CO3_12LAnn2 = Sub12Annual_2.load_co3
HCO3_12LAnn2 = Sub12Annual_2.load_hco3
##Subarea 9
#Continuous
Sub9_2 = Mod2[Mod2.subarea == 9]
SO4_9L2 = Sub9_2.load_so4
Ca_9L2 = Sub9_2.load_ca
Mg_9L2 = Sub9_2.load_mg
Na_9L2 = Sub9_2.load_na
K_9L2 = Sub9_2.load_k
Cl_9L2 = Sub9_2.load_cl
CO3_9L2 = Sub9_2.load_co3
HCO3_9L2 = Sub9_2.load_hco3
#Annual
years2_9 = years2.unique()
Sub9Annual_2 = Sub9_2.groupby("year").mean()
SO4_9LAnn2 = Sub9Annual_2.load_so4
Ca_9LAnn2 = Sub9Annual_2.load_ca
Mg_9LAnn2 = Sub9Annual_2.load_mg
Na_9LAnn2 = Sub9Annual_2.load_na
K_9LAnn2 = Sub9Annual_2.load_k
Cl_9LAnn2 = Sub9Annual_2.load_cl
CO3_9LAnn2 = Sub9Annual_2.load_co3
HCO3_9LAnn2 = Sub9Annual_2.load_hco3

###Pull in Model 3 Data
Mod3 = pd.read_csv(Model3, skiprows = 4, delim_whitespace = True)
Mod3.drop(Mod3.index[0:136950],0,inplace=True)
datestart3 = np.array('1992-01-01', dtype=np.datetime64)
dates3 = datestart3 + np.arange(7305)
years3 = Mod3.year
##Subarea 75
#Continuous
Sub75_3 = Mod3[Mod3.subarea == 75]
SO4_75L3 = Sub75_3.load_so4
Ca_75L3 = Sub75_3.load_ca
Mg_75L3 = Sub75_3.load_mg
Na_75L3 = Sub75_3.load_na
K_75L3 = Sub75_3.load_k
Cl_75L3 = Sub75_3.load_cl
CO3_75L3 = Sub75_3.load_co3
HCO3_75L3 = Sub75_3.load_hco3
#Annual
years3_75 = years3.unique()
Sub75Annual_3 = Sub75_3.groupby("year").mean()
SO4_75LAnn3 = Sub75Annual_3.load_so4
Ca_75LAnn3 = Sub75Annual_3.load_ca
Mg_75LAnn3 = Sub75Annual_3.load_mg
Na_75LAnn3 = Sub75Annual_3.load_na
K_75LAnn3 = Sub75Annual_3.load_k
Cl_75LAnn3 = Sub75Annual_3.load_cl
CO3_75LAnn3 = Sub75Annual_3.load_co3
HCO3_75LAnn3 = Sub75Annual_3.load_hco3
##Subarea 41
#Continuous
Sub41_3 = Mod3[Mod3.subarea == 41]
SO4_41L3 = Sub41_3.load_so4
Ca_41L3 = Sub41_3.load_ca
Mg_41L3 = Sub41_3.load_mg
Na_41L3 = Sub41_3.load_na
K_41L3 = Sub41_3.load_k
Cl_41L3 = Sub41_3.load_cl
HCO3_41L3 = Sub41_3.load_hco3
CO3_41L3 = Sub41_3.load_co3
#Annual
years3_41 = years3.unique()
Sub41Annual_3 = Sub41_3.groupby("year").mean()
SO4_41LAnn3 = Sub41Annual_3.load_so4
Ca_41LAnn3 = Sub41Annual_3.load_ca
Mg_41LAnn3 = Sub41Annual_3.load_mg
Na_41LAnn3 = Sub41Annual_3.load_na
K_41LAnn3 = Sub41Annual_3.load_k
Cl_41LAnn3 = Sub41Annual_3.load_cl
CO3_41LAnn3 = Sub41Annual_3.load_co3
HCO3_41LAnn3 = Sub41Annual_3.load_hco3
##Subarea 12
#Continuous
Sub12_3 = Mod3[Mod3.subarea == 12]
SO4_12L3 = Sub12_3.load_so4
Ca_12L3 = Sub12_3.load_ca
Mg_12L3 = Sub12_3.load_mg
Na_12L3 = Sub12_3.load_na
K_12L3 = Sub12_3.load_k
Cl_12L3 = Sub12_3.load_cl
CO3_12L3 = Sub12_3.load_co3
HCO3_12L3 = Sub12_3.load_hco3
#Annual
years3_12 = years3.unique()
Sub12Annual_3 = Sub12_3.groupby("year").mean()
SO4_12LAnn3 = Sub12Annual_3.load_so4
Ca_12LAnn3 = Sub12Annual_3.load_ca
Mg_12LAnn3 = Sub12Annual_3.load_mg
Na_12LAnn3 = Sub12Annual_3.load_na
K_12LAnn3 = Sub12Annual_3.load_k
Cl_12LAnn3 = Sub12Annual_3.load_cl
CO3_12LAnn3 = Sub12Annual_3.load_co3
HCO3_12LAnn3 = Sub12Annual_3.load_hco3
##Subarea 9
#Continuous
Sub9_3 = Mod3[Mod3.subarea == 9]
SO4_9L3 = Sub9_3.load_so4
Ca_9L3 = Sub9_3.load_ca
Mg_9L3 = Sub9_3.load_mg
Na_9L3 = Sub9_3.load_na
K_9L3 = Sub9_3.load_k
Cl_9L3 = Sub9_3.load_cl
CO3_9L3 = Sub9_3.load_co3
HCO3_9L3 = Sub9_3.load_hco3
#Annual
years3_9 = years3.unique()
Sub9Annual_3 = Sub9_3.groupby("year").mean()
SO4_9LAnn3 = Sub9Annual_3.load_so4
Ca_9LAnn3 = Sub9Annual_3.load_ca
Mg_9LAnn3 = Sub9Annual_3.load_mg
Na_9LAnn3 = Sub9Annual_3.load_na
K_9LAnn3 = Sub9Annual_3.load_k
Cl_9LAnn3 = Sub9Annual_3.load_cl
CO3_9LAnn3 = Sub9Annual_3.load_co3
HCO3_9LAnn3 = Sub9Annual_3.load_hco3
###Make some Graphs 
##Subarea 75
#Sulfate 
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, SO4_75L1, color='blue', label='IDW')
ax.plot(dates2, SO4_75L2, color='green', label='Krigg')
ax.plot(dates3, SO4_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutSO4, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/SO4_75_3models_{}.png'.format(FigurePath, FigureSuffix))
#Carbonate 
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, CO3_75L1, color='blue', label='IDW')
ax.plot(dates2, CO3_75L2, color='green', label='Krigg')
ax.plot(dates3, CO3_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutCO3, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 CO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/CO3_75_3models_{}.png'.format(FigurePath, FigureSuffix))
#Bicarbonate 
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, HCO3_75L1, color='blue', label='IDW')
ax.plot(dates2, HCO3_75L2, color='green', label='KRIGG')
ax.plot(dates3, HCO3_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutHCO3, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 HCO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/HCO3_75_3models_{}.png'.format(FigurePath, FigureSuffix))
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Ca_75L1, color='blue', label='IDW')
ax.plot(dates2, Ca_75L2, color='green', label='KRIGG')
ax.plot(dates3, Ca_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutCa, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Ca_75_3models_{}.png'.format(FigurePath, FigureSuffix))
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Mg_75L1, color='blue', label='IDW')
ax.plot(dates2, Mg_75L2, color='green', label='KRIGG')
ax.plot(dates3, Mg_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutMg, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Mg Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Mg_75_3models_{}.png'.format(FigurePath, FigureSuffix))
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Na_75L1, color='blue', label='IDW')
ax.plot(dates2, Na_75L2, color='green', label='KRIGG')
ax.plot(dates3, Na_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutNa, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Na Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Na_75_3models_{}.png'.format(FigurePath, FigureSuffix))
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, K_75L1, color='blue', label='IDW')
ax.plot(dates2, K_75L2, color='green', label='KRIGG')
ax.plot(dates3, K_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutK, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 K Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/K_75_3models_{}.png'.format(FigurePath, FigureSuffix))
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Cl_75L1, color='blue', label='IDW')
ax.plot(dates2, Cl_75L2, color='green', label='KRIGG')
ax.plot(dates3, Cl_75L3, color='yellow', label='RBF')
ax.scatter(Outletdates, LoadOutCl, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("75 Cl Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Cl_75_3models_{}.png'.format(FigurePath, FigureSuffix))

## Subarea 41 - Has no CO3 or HCO3 Observed data
#Sulfate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, SO4_41L1, color='blue', label='IDW')
ax.plot(dates2, SO4_41L2, color='green', label='Krigg')
ax.plot(dates3, SO4_41L3, color='yellow', label='RBF')
ax.scatter(Observeddates41, LoadOb41SO4, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/SO4_41_3models_{}.png'.format(FigurePath, FigureSuffix))
#Carbonate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, CO3_41L1, color='blue', label='IDW')
ax.plot(dates2, CO3_41L2, color='green', label='Krigg')
ax.plot(dates3, CO3_41L3, color='yellow', label='RBF')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 CO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/CO3_41_3models_{}.png'.format(FigurePath, FigureSuffix))
#Bicarbonate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, HCO3_41L1, color='blue', label='IDW')
ax.plot(dates2, HCO3_41L2, color='green', label='KRIGG')
ax.plot(dates3, HCO3_41L3, color='yellow', label='RBF')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 HCO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/HCO3_41_3models_{}.png'.format(FigurePath, FigureSuffix))
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Ca_41L1, color='blue', label='IDW')
ax.plot(dates2, Ca_41L2, color='green', label='KRIGG')
ax.plot(dates3, Ca_41L3, color='yellow', label='RBF')
ax.scatter(Observeddates41, LoadOb41Ca, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Ca_41_3models_{}.png'.format(FigurePath, FigureSuffix))
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Mg_41L1, color='blue', label='IDW')
ax.plot(dates2, Mg_41L2, color='green', label='KRIGG')
ax.plot(dates3, Mg_41L3, color='yellow', label='RBF')
ax.scatter(Observeddates41, LoadOb41Mg, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Mg Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Mg_41_3models_{}.png'.format(FigurePath, FigureSuffix))
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Na_41L1, color='blue', label='IDW')
ax.plot(dates2, Na_41L2, color='green', label='KRIGG')
ax.plot(dates3, Na_41L3, color='yellow', label='RBF')
ax.scatter(Observeddates41, LoadOb41Na, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Na Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Na_41_3models_{}.png'.format(FigurePath, FigureSuffix))
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, K_41L1, color='blue', label='IDW')
ax.plot(dates2, K_41L2, color='green', label='KRIGG')
ax.plot(dates3, K_41L3, color='yellow', label='RBF')
ax.scatter(Observeddates41, LoadOb41K, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 K Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/K_41_3models_{}.png'.format(FigurePath, FigureSuffix))
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Cl_41L1, color='blue', label='IDW')
ax.plot(dates2, Cl_41L2, color='green', label='KRIGG')
ax.plot(dates3, Cl_41L3, color='yellow', label='RBF')
ax.scatter(Observeddates41, LoadOb41Cl, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("41 Cl Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Cl_41_3models_{}.png'.format(FigurePath, FigureSuffix))

##Subarea 12 - No CO3 Observed Data
#Sulfate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, SO4_12L1, color='blue', label='IDW')
ax.plot(dates2, SO4_12L2, color='green', label='Krigg')
ax.plot(dates3, SO4_12L3, color='yellow', label='RBF')
ax.scatter(Observeddates12, LoadOb12SO4, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/SO4_12_3models_{}.png'.format(FigurePath, FigureSuffix))
#Carbonate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, CO3_12L1, color='blue', label='IDW')
ax.plot(dates2, CO3_12L2, color='green', label='Krigg')
ax.plot(dates3, CO3_12L3, color='yellow', label='RBF')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 CO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/CO3_12_3models_{}.png'.format(FigurePath, FigureSuffix))
#Bicarbonate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, HCO3_12L1, color='blue', label='IDW')
ax.plot(dates2, HCO3_12L2, color='green', label='KRIGG')
ax.plot(dates3, HCO3_12L3, color='yellow', label='RBF')
ax.scatter(Observeddates12, LoadOb12HCO3, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("12 CO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/HCO3_12_3models_{}.png'.format(FigurePath, FigureSuffix))
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Ca_12L1, color='blue', label='IDW')
ax.plot(dates2, Ca_12L2, color='green', label='KRIGG')
ax.plot(dates3, Ca_12L3, color='yellow', label='RBF')
ax.scatter(Observeddates12, LoadOb12Ca, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}Ca_12_3models_{}.png'.format(FigurePath, FigureSuffix))
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Mg_12L1, color='blue', label='IDW')
ax.plot(dates2, Mg_12L2, color='green', label='KRIGG')
ax.plot(dates3, Mg_12L3, color='yellow', label='RBF')
ax.scatter(Observeddates12, LoadOb12Mg, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 Mg Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Mg_12_3models_{}.png'.format(FigurePath, FigureSuffix))
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Na_12L1, color='blue', label='IDW')
ax.plot(dates2, Na_12L2, color='green', label='KRIGG')
ax.plot(dates3, Na_12L3, color='yellow', label='RBF')
ax.scatter(Observeddates12, LoadOb12Na, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("12 Na Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Na_12_3models_{}.png'.format(FigurePath, FigureSuffix))
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, K_12L1, color='blue', label='IDW')
ax.plot(dates2, K_12L2, color='green', label='KRIGG')
ax.plot(dates3, K_12L3, color='yellow', label='RBF')
ax.scatter(Observeddates12, LoadOb12K, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("12 K Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/K_12_3models_{}.png'.format(FigurePath, FigureSuffix))
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Cl_12L1, color='blue', label='IDW')
ax.plot(dates2, Cl_12L2, color='green', label='KRIGG')
ax.plot(dates3, Cl_12L3, color='yellow', label='RBF')
ax.scatter(Observeddates12, LoadOb12Cl, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("12 Cl Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Cl_12_3models_{}.png'.format(FigurePath, FigureSuffix))

##Subarea 9 - Doesn't have CO3, HCO3, or Cl Observed data
#Sulfate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, SO4_9L1, color='blue', label='IDW')
ax.plot(dates2, SO4_9L2, color='green', label='Krigg')
ax.plot(dates3, SO4_9L3, color='yellow', label='RBF')
ax.scatter(Observeddates9, LoadOb9SO4, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 SO4 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/SO4_9_3models_{}.png'.format(FigurePath, FigureSuffix))
#Carbonate
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, CO3_9L1, color='blue', label='IDW')
ax.plot(dates2, CO3_9L2, color='green', label='Krigg')
ax.plot(dates3, CO3_9L3, color='yellow', label='RBF')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 CO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/CO3_9_3models_{}.png'.format(FigurePath, FigureSuffix))
#Bicarbonate 
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, HCO3_9L1, color='blue', label='IDW')
ax.plot(dates2, HCO3_9L2, color='green', label='KRIGG')
ax.plot(dates3, HCO3_9L3, color='yellow', label='RBF')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 HCO3 Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/HCO3_9_3models_{}.png'.format(FigurePath, FigureSuffix))
#Calcium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Ca_9L1, color='blue', label='IDW')
ax.plot(dates2, Ca_9L2, color='green', label='KRIGG')
ax.plot(dates3, Ca_9L3, color='yellow', label='RBF')
ax.scatter(Observeddates9, LoadOb9Ca, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 Ca Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Ca_9_3models_{}.png'.format(FigurePath, FigureSuffix))
#Magnesium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Mg_9L1, color='blue', label='IDW')
ax.plot(dates2, Mg_9L2, color='green', label='KRIGG')
ax.plot(dates3, Mg_9L3, color='yellow', label='RBF')
ax.scatter(Observeddates9, LoadOb9Mg, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 Mg Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Mg_9_3models_{}.png'.format(FigurePath, FigureSuffix))
#Sodium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Na_9L1, color='blue', label='IDW')
ax.plot(dates2, Na_9L2, color='green', label='KRIGG')
ax.plot(dates3, Na_9L3, color='yellow', label='RBF')
ax.scatter(Observeddates9, LoadOb9Na, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Loading [kg/d]')
ax.set_title("9 Na Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Na_9_3models_{}.png'.format(FigurePath, FigureSuffix))
#Potassium
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, K_9L1, color='blue', label='IDW')
ax.plot(dates2, K_75L2, color='green', label='KRIGG')
ax.plot(dates3, K_75L3, color='yellow', label='RBF')
ax.scatter(Observeddates9, LoadOb9K, color='red', label='observed')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("9 K Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/K_9_3models_{}.png'.format(FigurePath, FigureSuffix))
#Chlorine
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
ax.plot(dates1, Cl_9L1, color='blue', label='IDW')
ax.plot(dates2, Cl_9L2, color='green', label='KRIGG')
ax.plot(dates3, Cl_9L3, color='yellow', label='RBF')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration [mg/L]')
ax.set_title("9 Cl Loading {}".format(GraphName))
ax.legend()
fig.savefig('{}/Cl_9_3models_{}.png'.format(FigurePath, FigureSuffix))