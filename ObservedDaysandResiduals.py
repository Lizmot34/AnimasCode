# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 14:19:25 2022

@author: Lizmot34
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.close("all")

###Pull in Observed Data
##Site 09364500 = Outlet = Subarea 75
OutletData = pd.read_excel('C:/Users/Lizmot34/Desktop/ObservedSaltData.xlsx', 
                     sheet_name='09364500Salts', skiprows = 1)
OutletData.drop(OutletData.index[0:2],0, inplace=True)
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
#Combine loads with dates
LoadOutSO4.index = Outletdates
LoadOutCO3.index = Outletdates
LoadOutHCO3.index = Outletdates
LoadOutCa.index = Outletdates
LoadOutMg.index = Outletdates
LoadOutNa.index = Outletdates
LoadOutK.index = Outletdates
LoadOutCl.index = Outletdates

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

LoadOb41SO4.index = Observeddates41
LoadOb41Ca.index = Observeddates41
LoadOb41Mg.index = Observeddates41
LoadOb41Na.index = Observeddates41
LoadOb41K.index = Observeddates41
LoadOb41Cl.index = Observeddates41

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

LoadOb12SO4.index = Observeddates12
LoadOb12Ca.index = Observeddates12
LoadOb12Mg.index = Observeddates12
LoadOb12Na.index = Observeddates12
LoadOb12K.index = Observeddates12
LoadOb12Cl.index = Observeddates12
LoadOb12HCO3.index = Observeddates12

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

LoadOb9SO4.index = Observeddates9
LoadOb9Ca.index = Observeddates9
LoadOb9Mg.index = Observeddates9
LoadOb9Na.index = Observeddates9
LoadOb9K.index = Observeddates9


####Pull in Model Data#################################################################################################################
Mod1 = pd.read_csv('salt.txt',skiprows = 4, delim_whitespace = True)
#Drop Data till the End of Warmup
Mod1.drop(Mod1.index[0:136950],0,inplace=True)
datestart = np.array('1992-01-01', dtype=np.datetime64)
dates = datestart + np.arange(7305)
years = Mod1.year

####Subarea 75 ####################################################################################
###Continuous
Sub75 = Mod1[Mod1.subarea == 75]
SO4_75L = Sub75.load_so4
Ca_75L = Sub75.load_ca
Mg_75L = Sub75.load_mg
Na_75L = Sub75.load_na
K_75L = Sub75.load_k
Cl_75L = Sub75.load_cl
CO3_75L = Sub75.load_co3
HCO3_75L = Sub75.load_hco3
###Specific Data days
##Sulfate, Calcium, Magnesium, Sodium, Potassium, and Chloride all have same obsv. days
#Year: 1992 Days: 15, 78, 126, 216, 324
Year1992_75 = Sub75[Sub75.year == 1992]
Concentrations_92 = Year1992_75[(Year1992_75['day'] == 15) | (Year1992_75['day'] == 78) |
        (Year1992_75['day'] == 126) | (Year1992_75['day'] == 216) | (Year1992_75['day'] == 324)]
Dates_92_75 = pd.to_datetime(['1/15/1992', '3/18/1992', '5/5/1992', '8/3/1992',
                               '11/19/1992'])
SO4_92_75 = Concentrations_92.load_so4
Ca_92_75 = Concentrations_92.load_ca
Mg_92_75 = Concentrations_92.load_mg
Na_92_75 = Concentrations_92.load_na
K_92_75 = Concentrations_92.load_k
Cl_92_75 = Concentrations_92.load_cl
#Year: 1993 Days: 68, 125, 244
Year1993_75 = Sub75[Sub75.year == 1993]
Concentrations_93 = Year1993_75[(Year1993_75['day'] == 68) | (Year1993_75['day'] == 125) |
        (Year1993_75['day'] == 244)]
Dates_93_75 = pd.to_datetime(['3/9/1993', '5/5/1993', '9/1/1993'])
SO4_93_75 = Concentrations_93.load_so4
Ca_93_75 = Concentrations_93.load_ca
Mg_93_75 = Concentrations_93.load_mg
Na_93_75 = Concentrations_93.load_na
K_93_75 = Concentrations_93.load_k
Cl_93_75 = Concentrations_93.load_cl
#Year: 1994 Day: 322
Year1994_75 = Sub75[Sub75.year == 1994]
Concentrations_94 = Year1994_75[(Year1994_75['day'] == 322)]
Dates_94_75 = pd.to_datetime(['11/18/1994'])
SO4_94_75 = Concentrations_94.load_so4
Ca_94_75 = Concentrations_94.load_ca
Mg_94_75 = Concentrations_94.load_mg
Na_94_75 = Concentrations_94.load_na
K_94_75 = Concentrations_94.load_k
Cl_94_75 = Concentrations_94.load_cl
#Year: 1995 Day: 58, 124, 222, 340
Year1995_75 = Sub75[Sub75.year == 1995]
Concentrations_95 = Year1995_75[(Year1995_75['day'] == 58) | (Year1995_75['day'] == 124) | 
        (Year1995_75['day'] == 222) | (Year1995_75['day'] == 340)]
Dates_95_75 = pd.to_datetime(['2/27/1995', '5/4/1995', '8/10/1995', '12/6/1995'])
SO4_95_75 = Concentrations_95.load_so4
Ca_95_75 = Concentrations_95.load_ca
Mg_95_75 = Concentrations_95.load_mg
Na_95_75 = Concentrations_95.load_na
K_95_75 = Concentrations_95.load_k
Cl_95_75 = Concentrations_95.load_cl
#Year: 1996 Day: 16, 92, 248, 302
Year1996_75 = Sub75[Sub75.year == 1996]
Concentrations_96 = Year1996_75[(Year1996_75['day'] == 16) | (Year1996_75['day'] == 92) | 
        (Year1996_75['day'] == 248) | (Year1996_75['day'] == 302)]
Dates_96_75 = pd.to_datetime(['1/16/1996', '4/1/1996', '9/4/1996', '10/28/1996'])
SO4_96_75 = Concentrations_96.load_so4
Ca_96_75 = Concentrations_96.load_ca
Mg_96_75 = Concentrations_96.load_mg
Na_96_75 = Concentrations_96.load_na
K_96_75 = Concentrations_96.load_k
Cl_96_75 = Concentrations_96.load_cl
#Year: 1997 Day: 35, 343
Year1997_75 = Sub75[Sub75.year == 1997]
Concentrations_97 = Year1997_75[(Year1997_75['day'] == 35) | (Year1997_75['day'] == 343)]
Dates_97_75 = pd.to_datetime(['2/4/1997', '12/9/1997'])
SO4_97_75 = Concentrations_97.load_so4
Ca_97_75 = Concentrations_97.load_ca
Mg_97_75 = Concentrations_97.load_mg
Na_97_75 = Concentrations_97.load_na
K_97_75 = Concentrations_97.load_k
Cl_97_75 = Concentrations_97.load_cl
#Year: 1998 Days: 41, 125, 223
Year1998_75 = Sub75[Sub75.year == 1998]
Concentrations_98 = Year1998_75[(Year1998_75['day'] == 41) | (Year1998_75['day'] == 125) |
        (Year1998_75['day'] == 223)]
Dates_98_75 = pd.to_datetime(['2/10/1998', '5/5/1998' , '8/11/1998'])
SO4_98_75 = Concentrations_98.load_so4
Ca_98_75 = Concentrations_98.load_ca
Mg_98_75 = Concentrations_98.load_mg
Na_98_75 = Concentrations_98.load_na
K_98_75 = Concentrations_98.load_k
Cl_98_75 = Concentrations_98.load_cl
#Year: 1999 Days: 70, 153, 201, 217, 340
Year1999_75 = Sub75[Sub75.year == 1999]
Concentrations_99 = Year1999_75[(Year1999_75['day'] == 70) | (Year1999_75['day'] == 153) |
        (Year1999_75['day'] == 201) | (Year1999_75['day'] == 217) | (Year1999_75['day'] == 340)]
Dates_99_75 = pd.to_datetime(['3/11/1999', '6/2/1999', '7/20/1999', '8/5/1999', '12/6/1999'])
SO4_99_75 = Concentrations_99.load_so4
Ca_99_75 = Concentrations_99.load_ca
Mg_99_75 = Concentrations_99.load_mg
Na_99_75 = Concentrations_99.load_na
K_99_75 = Concentrations_99.load_k
Cl_99_75 = Concentrations_99.load_cl
#Year: 2000 Days: 20, 95, 202, 333
Year2000_75 = Sub75[Sub75.year == 2000]
Concentrations_00 = Year2000_75[(Year2000_75['day'] == 20) | (Year2000_75['day'] == 95) |
        (Year2000_75['day'] == 202) | (Year2000_75['day'] == 333)]
Dates_00_75 = pd.to_datetime(['1/20/2000', '4/4/2000', '7/20/2000', '11/28/2000'])
SO4_00_75 = Concentrations_00.load_so4
Ca_00_75 = Concentrations_00.load_ca
Mg_00_75 = Concentrations_00.load_mg
Na_00_75 = Concentrations_00.load_na
K_00_75 = Concentrations_00.load_k
Cl_00_75 = Concentrations_00.load_cl
#Year 2001 Days: 80, 114, 219,319
Year2001_75 = Sub75[Sub75.year == 2001]
Concentrations_01 = Year2001_75[(Year2001_75['day'] == 80) | (Year2001_75['day'] == 114) |
        (Year2001_75['day'] == 219) | (Year2001_75['day'] == 319)]
Dates_01_75 = pd.to_datetime(['3/21/2001', '4/25/2001', '8/7/2001', '11/15/2001'])
SO4_01_75 = Concentrations_01.load_so4
Ca_01_75 = Concentrations_01.load_ca
Mg_01_75 = Concentrations_01.load_mg
Na_01_75 = Concentrations_01.load_na
K_01_75 = Concentrations_01.load_k
Cl_01_75 = Concentrations_01.load_cl
#Year 2002 Days: 78, 134, 199
Year2002_75 = Sub75[Sub75.year == 2002]
Concentrations_02 = Year2002_75[(Year2002_75['day'] == 78) | (Year2002_75['day'] == 134) |
        (Year2002_75['day'] == 199)]
Dates_02_75 = pd.to_datetime(['3/19/2002', '4/14/2002', '7/18/2002'])
SO4_02_75 = Concentrations_02.load_so4
Ca_02_75 = Concentrations_02.load_ca
Mg_02_75 = Concentrations_02.load_mg
Na_02_75 = Concentrations_02.load_na
K_02_75 = Concentrations_02.load_k
Cl_02_75 = Concentrations_02.load_cl
#Year 2003 Days: 29, 78, 141, 190, 345
Year2003_75 = Sub75[Sub75.year == 2003]
Concentrations_03 = Year2003_75[(Year2003_75['day'] == 29) | (Year2003_75['day'] == 78) |
        (Year2003_75['day'] == 141) | (Year2003_75['day'] == 190) | (Year2003_75['day'] == 345)]
Dates_03_75 = pd.to_datetime(['1/29/2003', '3/19/2003', '5/21/2003', '7/9/2003', '12/11/2003'])
SO4_03_75 = Concentrations_03.load_so4
Ca_03_75 = Concentrations_03.load_ca
Mg_03_75 = Concentrations_03.load_mg
Na_03_75 = Concentrations_03.load_na
K_03_75 = Concentrations_03.load_k
Cl_03_75 = Concentrations_03.load_cl
#Year: 2004 Days: 72, 183, 224
Year2004_75 = Sub75[Sub75.year == 2004]
Concentrations_04 = Year2004_75[(Year2004_75['day'] == 72) | (Year2004_75['day'] == 183) |
        (Year2004_75['day'] == 224)]
Dates_04_75 = pd.to_datetime(['3/12/2004', '7/1/2004', '8/11/2004'])
SO4_04_75 = Concentrations_04.load_so4
Ca_04_75 = Concentrations_04.load_ca
Mg_04_75 = Concentrations_04.load_mg
Na_04_75 = Concentrations_04.load_na
K_04_75 = Concentrations_04.load_k
Cl_04_75 = Concentrations_04.load_cl
#Year: 2005 Days: 83, 216
Year2005_75 = Sub75[Sub75.year == 2005]
Concentrations_05 = Year2005_75[(Year2005_75['day'] == 83) | (Year2005_75['day'] == 216)]
Dates_05_75 = pd.to_datetime(['3/24/2005', '8/4/2005'])
SO4_05_75 = Concentrations_05.load_so4
Ca_05_75 = Concentrations_05.load_ca
Mg_05_75 = Concentrations_05.load_mg
Na_05_75 = Concentrations_05.load_na
K_05_75 = Concentrations_05.load_k
Cl_05_75 = Concentrations_05.load_cl
#Year: 2006 Days: 88, 208, 269, 325
Year2006_75 = Sub75[Sub75.year == 2006]
Concentrations_06 = Year2006_75[(Year2006_75['day'] == 88) | (Year2006_75['day'] == 208) |
        (Year2006_75['day'] == 269) | (Year2006_75['day'] == 325)]
Dates_06_75 = pd.to_datetime(['3/29/2006', '7/27/2006', '9/26/2006', '11/21/2006'])
SO4_06_75 = Concentrations_06.load_so4
Ca_06_75 = Concentrations_06.load_ca
Mg_06_75 = Concentrations_06.load_mg
Na_06_75 = Concentrations_06.load_na
K_06_75 = Concentrations_06.load_k
Cl_06_75 = Concentrations_06.load_cl
#Year: 2007 Days: 101, 199
Year2007_75 = Sub75[Sub75.year == 2007]
Concentrations_07 = Year2007_75[(Year2007_75['day'] == 101) | (Year2007_75['day'] == 199)]
Dates_07_75 = pd.to_datetime(['4/11/2007', '7/18/2007'])
SO4_07_75 = Concentrations_07.load_so4
Ca_07_75 = Concentrations_07.load_ca
Mg_07_75 = Concentrations_07.load_mg
Na_07_75 = Concentrations_07.load_na
K_07_75 = Concentrations_07.load_k
Cl_07_75 = Concentrations_07.load_cl
#Year 2008 Day: 344
Year2008_75 = Sub75[Sub75.year == 2008]
Concentrations_08 = Year2008_75[(Year2008_75['day'] == 344)]
Dates_08_75 = pd.to_datetime(['12/9/2008'])
SO4_08_75 = Concentrations_08.load_so4
Ca_08_75 = Concentrations_08.load_ca
Mg_08_75 = Concentrations_08.load_mg
Na_08_75 = Concentrations_08.load_na
K_08_75 = Concentrations_08.load_k
Cl_08_75 = Concentrations_08.load_cl
#Year 2009 Day 55, 119, 342
Year2009_75 = Sub75[Sub75.year == 2009]
Concentrations_09 = Year2009_75[(Year2009_75['day'] == 55) |(Year2009_75['day'] == 199) |
        (Year2009_75['day'] == 342)]
Dates_09_75 = pd.to_datetime(['2/24/2009', '4/29/2009', '12/8/2009'])
SO4_09_75 = Concentrations_09.load_so4
Ca_09_75 = Concentrations_09.load_ca
Mg_09_75 = Concentrations_09.load_mg
Na_09_75 = Concentrations_09.load_na
K_09_75 = Concentrations_09.load_k
Cl_09_75 = Concentrations_09.load_cl
#Year 2010 Day 138, 209,341
Year2010_75 = Sub75[Sub75.year == 2010]
Concentrations_10 = Year2010_75[(Year2010_75['day'] == 138) |(Year2010_75['day'] == 209)]
Dates_10_75 = pd.to_datetime(['5/18/2010', '7/28/2010'])
SO4_10_75 = Concentrations_10.load_so4
Ca_10_75 = Concentrations_10.load_ca
Mg_10_75 = Concentrations_10.load_mg
Na_10_75 = Concentrations_10.load_na
K_10_75 = Concentrations_10.load_k
Cl_10_75 = Concentrations_10.load_cl

#Combine

ObservedDays_75 = Dates_92_75.union_many([Dates_93_75, Dates_94_75, Dates_95_75, Dates_96_75,
                                 Dates_97_75, Dates_98_75, Dates_99_75, Dates_00_75, Dates_01_75,
                                 Dates_02_75, Dates_03_75, Dates_04_75, Dates_05_75, Dates_06_75,
                                 Dates_07_75, Dates_08_75, Dates_09_75, Dates_10_75])
SO4_Modeled_75 = pd.concat([SO4_92_75, SO4_93_75, SO4_94_75, SO4_95_75, SO4_96_75, SO4_97_75,
                                  SO4_98_75, SO4_99_75, SO4_00_75, SO4_01_75, SO4_02_75, SO4_03_75,
                                  SO4_04_75, SO4_05_75, SO4_06_75, SO4_07_75, SO4_08_75, SO4_09_75,
                                  SO4_10_75], axis=0)
Ca_Modeled_75 = pd.concat([Ca_92_75, Ca_93_75, Ca_94_75, Ca_95_75, Ca_96_75, Ca_97_75,Ca_98_75,
                                 Ca_99_75, Ca_00_75, Ca_01_75, Ca_02_75, Ca_03_75,Ca_04_75, Ca_05_75,
                                 Ca_06_75, Ca_07_75, Ca_08_75, Ca_09_75, Ca_10_75], axis=0)
Mg_Modeled_75 = pd.concat([Mg_92_75, Mg_93_75, Mg_94_75, Mg_95_75, Mg_96_75, Mg_97_75, Mg_98_75,
                                 Mg_99_75, Mg_00_75, Mg_01_75, Mg_02_75, Mg_03_75, Mg_04_75, Mg_05_75,
                                 Mg_06_75, Mg_07_75, Mg_08_75, Mg_09_75, Mg_10_75], axis=0)
Na_Modeled_75 = pd.concat([Na_92_75, Na_93_75, Na_94_75, Na_95_75, Na_96_75, Na_97_75, Na_98_75,
                                 Na_99_75, Na_00_75, Na_01_75, Na_02_75, Na_03_75, Na_04_75, Na_05_75,
                                 Na_06_75, Na_07_75, Na_08_75, Na_09_75, Na_10_75], axis=0)
K_Modeled_75 = pd.concat([K_92_75, K_93_75, K_94_75, K_95_75, K_96_75, K_97_75, K_98_75, K_99_75, K_00_75,
                                K_01_75, K_02_75, K_03_75, K_04_75, K_05_75, K_06_75, K_07_75, K_08_75, K_09_75,
                                K_10_75], axis=0)
Cl_Modeled_75 = pd.concat([Cl_92_75, Cl_93_75, Cl_94_75, Cl_95_75, Cl_96_75, Cl_97_75, Cl_98_75,
                                 Cl_99_75, Cl_00_75, Cl_01_75, Cl_02_75, Cl_03_75, Cl_04_75, Cl_05_75,
                                 Cl_06_75, Cl_07_75, Cl_08_75, Cl_09_75, Cl_10_75], axis=0)

##Carbonate
#Year: 1992 Days: 15, 78, 126, 216, 324
Year1992_75 = Sub75[Sub75.year == 1992]
Concentrations_92 = Year1992_75[(Year1992_75['day'] == 15) | (Year1992_75['day'] == 78) |
        (Year1992_75['day'] == 126) | (Year1992_75['day'] == 216) | (Year1992_75['day'] == 324)]
CO3Dates_92_75 = pd.to_datetime(['1/15/1992', '3/18/1992', '5/5/1992', '8/3/1992',
                               '11/19/1992'])
CO3_92_75 = Concentrations_92.load_co3
#Year: 1993 Days: 68, 125, 244
Year1993_75 = Sub75[Sub75.year == 1993]
Concentrations_93 = Year1993_75[(Year1993_75['day'] == 68) | (Year1993_75['day'] == 125) |
        (Year1993_75['day'] == 244)]
CO3Dates_93_75 = pd.to_datetime(['3/9/1993', '5/5/1993', '9/1/1993'])
CO3_93_75 = Concentrations_93.load_co3
#Year: 1994 Day: 322
Year1994_75 = Sub75[Sub75.year == 1994]
Concentrations_94 = Year1994_75[(Year1994_75['day'] == 322)]
CO3Dates_94_75 = pd.to_datetime(['11/18/1994'])
CO3_94_75 = Concentrations_94.load_co3
#Year: 1995 Day: 58, 124, 222, 340
Year1995_75 = Sub75[Sub75.year == 1995]
Concentrations_95 = Year1995_75[(Year1995_75['day'] == 58) | (Year1995_75['day'] == 124) | 
        (Year1995_75['day'] == 222) | (Year1995_75['day'] == 340)]
CO3Dates_95_75 = pd.to_datetime(['2/27/1995', '5/4/1995', '8/10/1995', '12/6/1995'])
CO3_95_75 = Concentrations_95.load_co3
#Year: 1996 Day: 16, 92, 248, 302
Year1996_75 = Sub75[Sub75.year == 1996]
Concentrations_96 = Year1996_75[(Year1996_75['day'] == 16) | (Year1996_75['day'] == 92) | 
        (Year1996_75['day'] == 248) | (Year1996_75['day'] == 302)]
CO3Dates_96_75 = pd.to_datetime(['1/16/1996', '4/1/1996', '9/4/1996', '10/28/1996'])
CO3_96_75 = Concentrations_96.load_co3
#Year: 1997 Day: 343
Year1997_75 = Sub75[Sub75.year == 1997]
Concentrations_97 = Year1997_75[(Year1997_75['day'] == 343)]
CO3Dates_97_75 = pd.to_datetime([ '12/9/1997'])
CO3_97_75 = Concentrations_97.load_co3
#Year: 1998 Days: 125, 223
Year1998_75 = Sub75[Sub75.year == 1998]
Concentrations_98 = Year1998_75[(Year1998_75['day'] == 125) | (Year1998_75['day'] == 223)]
CO3Dates_98_75 = pd.to_datetime(['5/5/1998' , '8/11/1998'])
CO3_98_75 = Concentrations_98.load_co3
#Year: 1999 Days: 70, 153, 201, 217, 340
Year1999_75 = Sub75[Sub75.year == 1999]
Concentrations_99 = Year1999_75[(Year1999_75['day'] == 70) | (Year1999_75['day'] == 153) |
        (Year1999_75['day'] == 201) | (Year1999_75['day'] == 217) | (Year1999_75['day'] == 340)]
CO3Dates_99_75 = pd.to_datetime(['3/11/1999', '6/2/1999', '7/20/1999', '8/5/1999', '12/6/1999'])
CO3_99_75 = Concentrations_99.load_co3
#Year: 2000 Days: 20, 95, 202, 333
Year2000_75 = Sub75[Sub75.year == 2000]
Concentrations_00 = Year2000_75[(Year2000_75['day'] == 20) | (Year2000_75['day'] == 95) |
        (Year2000_75['day'] == 202) | (Year2000_75['day'] == 333)]
CO3Dates_00_75 = pd.to_datetime(['1/20/2000', '4/4/2000', '7/20/2000', '11/28/2000'])
CO3_00_75 = Concentrations_00.load_co3
#Year 2001 Days: 80, 114, 219
Year2001_75 = Sub75[Sub75.year == 2001]
Concentrations_01 = Year2001_75[(Year2001_75['day'] == 80) | (Year2001_75['day'] == 114) |
        (Year2001_75['day'] == 219)]
CO3Dates_01_75 = pd.to_datetime(['3/21/2001', '4/25/2001', '8/7/2001'])
CO3_01_75 = Concentrations_01.load_co3
#Year 2002 Day:  134
Year2002_75 = Sub75[Sub75.year == 2002]
Concentrations_02 = Year2002_75[(Year2002_75['day'] == 134)]
CO3Dates_02_75 = pd.to_datetime(['4/14/2002'])
CO3_02_75 = Concentrations_02.load_co3
#Year 2003 Day:  345
Year2003_75 = Sub75[Sub75.year == 2003]
Concentrations_03 = Year2003_75[(Year2003_75['day'] == 345)]
CO3Dates_03_75 = pd.to_datetime(['12/11/2003'])
CO3_03_75 = Concentrations_03.load_co3
#Year: 2004 Days: 72
Year2004_75 = Sub75[Sub75.year == 2004]
Concentrations_04 = Year2004_75[(Year2004_75['day'] == 72)]
CO3Dates_04_75 = pd.to_datetime(['3/12/2004'])
CO3_04_75 = Concentrations_04.load_co3
#Year: 2005 Days: 83, 242
Year2005_75 = Sub75[Sub75.year == 2005]
Concentrations_05 = Year2005_75[(Year2005_75['day'] == 83) | (Year2005_75['day'] == 242)]
CO3Dates_05_75 = pd.to_datetime(['3/24/2005', '8/30/2005'])
CO3_05_75 = Concentrations_05.load_co3
#Year: 2006 Days: 88, 208, 269, 325
Year2006_75 = Sub75[Sub75.year == 2006]
Concentrations_06 = Year2006_75[(Year2006_75['day'] == 88) | (Year2006_75['day'] == 208) |
        (Year2006_75['day'] == 269) | (Year2006_75['day'] == 325)]
CO3Dates_06_75 = pd.to_datetime(['3/29/2006', '7/27/2006', '9/26/2006', '11/21/2006'])
CO3_06_75 = Concentrations_06.load_co3
#Year: 2007 Days: 101, 199
Year2007_75 = Sub75[Sub75.year == 2007]
Concentrations_07 = Year2007_75[(Year2007_75['day'] == 101) | (Year2007_75['day'] == 199)]
CO3Dates_07_75 = pd.to_datetime(['4/11/2007', '7/18/2007'])
CO3_07_75 = Concentrations_07.load_co3
#Year 2008 Day: 344
Year2008_75 = Sub75[Sub75.year == 2008]
Concentrations_08 = Year2008_75[(Year2008_75['day'] == 344)]
CO3Dates_08_75 = pd.to_datetime(['12/9/2008'])
CO3_08_75 = Concentrations_08.load_co3
#Year 2009 Day 55, 119, 342
Year2009_75 = Sub75[Sub75.year == 2009]
Concentrations_09 = Year2009_75[(Year2009_75['day'] == 55) |(Year2009_75['day'] == 199) |
        (Year2009_75['day'] == 342)]
CO3Dates_09_75 = pd.to_datetime(['2/24/2009', '4/29/2009', '12/8/2009'])
CO3_09_75 = Concentrations_09.load_co3
#Year 2010 Day 138, 209,341
Year2010_75 = Sub75[Sub75.year == 2010]
Concentrations_10 = Year2010_75[(Year2010_75['day'] == 138) |(Year2010_75['day'] == 209)]
CO3Dates_10_75 = pd.to_datetime(['5/18/2010', '7/28/2010'])
CO3_10_75 = Concentrations_10.load_co3

#Combine
CO3_Modeled_75 = pd.concat([CO3_92_75, CO3_93_75, CO3_94_75, CO3_95_75, CO3_96_75, CO3_97_75,
                                  CO3_98_75, CO3_99_75, CO3_00_75, CO3_01_75, CO3_02_75, CO3_03_75,
                                  CO3_04_75, CO3_05_75, CO3_06_75, CO3_07_75, CO3_08_75, CO3_09_75,
                                  CO3_10_75], axis=0)
CO3_ObservedDays_75 = CO3Dates_92_75.union_many([CO3Dates_93_75, CO3Dates_94_75, CO3Dates_95_75,
                                              CO3Dates_96_75, CO3Dates_97_75, CO3Dates_98_75, 
                                              CO3Dates_99_75, CO3Dates_00_75, CO3Dates_01_75,
                                              CO3Dates_02_75, CO3Dates_03_75, CO3Dates_04_75, 
                                              CO3Dates_05_75, CO3Dates_06_75, CO3Dates_07_75, 
                                              CO3Dates_08_75, CO3Dates_09_75, CO3Dates_10_75])

##Bicarbonate
#Year: 1992 Days: 15, 78, 126, 216, 324
Year1992_75 = Sub75[Sub75.year == 1992]
Concentrations_92 = Year1992_75[(Year1992_75['day'] == 15) | (Year1992_75['day'] == 78) |
        (Year1992_75['day'] == 126) | (Year1992_75['day'] == 216) | (Year1992_75['day'] == 324)]
HCO3Dates_92_75 = pd.to_datetime(['1/15/1992', '3/18/1992', '5/5/1992', '8/3/1992',
                               '11/19/1992'])
HCO3_92_75 = Concentrations_92.load_hco3
#Year: 1993 Days: 68, 125, 244
Year1993_75 = Sub75[Sub75.year == 1993]
Concentrations_93 = Year1993_75[(Year1993_75['day'] == 68) | (Year1993_75['day'] == 125) |
        (Year1993_75['day'] == 244)]
HCO3Dates_93_75 = pd.to_datetime(['3/9/1993', '5/5/1993', '9/1/1993'])
HCO3_93_75 = Concentrations_93.load_hco3
#Year: 1994 Day: 322
Year1994_75 = Sub75[Sub75.year == 1994]
Concentrations_94 = Year1994_75[(Year1994_75['day'] == 322)]
HCO3Dates_94_75 = pd.to_datetime(['11/18/1994'])
HCO3_94_75 = Concentrations_94.load_hco3
#Year: 1995 Day: 58, 124, 222, 340
Year1995_75 = Sub75[Sub75.year == 1995]
Concentrations_95 = Year1995_75[(Year1995_75['day'] == 58) | (Year1995_75['day'] == 124) | 
        (Year1995_75['day'] == 222) | (Year1995_75['day'] == 340)]
HCO3Dates_95_75 = pd.to_datetime(['2/27/1995', '5/4/1995', '8/10/1995', '12/6/1995'])
HCO3_95_75 = Concentrations_95.load_hco3
#Year: 1996 Day: 16, 92, 248, 302
Year1996_75 = Sub75[Sub75.year == 1996]
Concentrations_96 = Year1996_75[(Year1996_75['day'] == 16) | (Year1996_75['day'] == 92) | 
        (Year1996_75['day'] == 248) | (Year1996_75['day'] == 302)]
HCO3Dates_96_75 = pd.to_datetime(['1/16/1996', '4/1/1996', '9/4/1996', '10/28/1996'])
HCO3_96_75 = Concentrations_96.load_hco3
#Year: 1997 Day: 343
Year1997_75 = Sub75[Sub75.year == 1997]
Concentrations_97 = Year1997_75[(Year1997_75['day'] == 343)]
HCO3Dates_97_75 = pd.to_datetime([ '12/9/1997'])
HCO3_97_75 = Concentrations_97.load_hco3
#Year: 1998 Days: 125, 223
Year1998_75 = Sub75[Sub75.year == 1998]
Concentrations_98 = Year1998_75[(Year1998_75['day'] == 125) | (Year1998_75['day'] == 223)]
HCO3Dates_98_75 = pd.to_datetime(['5/5/1998' , '8/11/1998'])
HCO3_98_75 = Concentrations_98.load_hco3
#Year: 1999 Days: 70, 153, 201, 217, 340
Year1999_75 = Sub75[Sub75.year == 1999]
Concentrations_99 = Year1999_75[(Year1999_75['day'] == 70) | (Year1999_75['day'] == 153) |
        (Year1999_75['day'] == 201) | (Year1999_75['day'] == 217) | (Year1999_75['day'] == 340)]
HCO3Dates_99_75 = pd.to_datetime(['3/11/1999', '6/2/1999', '7/20/1999', '8/5/1999', '12/6/1999'])
HCO3_99_75 = Concentrations_99.load_hco3
#Year: 2000 Days: 20, 95, 202, 333
Year2000_75 = Sub75[Sub75.year == 2000]
Concentrations_00 = Year2000_75[(Year2000_75['day'] == 20) | (Year2000_75['day'] == 95) |
        (Year2000_75['day'] == 202) | (Year2000_75['day'] == 333)]
HCO3Dates_00_75 = pd.to_datetime(['1/20/2000', '4/4/2000', '7/20/2000', '11/28/2000'])
HCO3_00_75 = Concentrations_00.load_hco3
#Year 2001 Days: 80, 114, 219, 319
Year2001_75 = Sub75[Sub75.year == 2001]
Concentrations_01 = Year2001_75[(Year2001_75['day'] == 80) | (Year2001_75['day'] == 114) |
        (Year2001_75['day'] == 219) | (Year2001_75['day'] == 319)]
HCO3Dates_01_75 = pd.to_datetime(['3/21/2001', '4/25/2001', '8/7/2001', '11/15/2001'])
HCO3_01_75 = Concentrations_01.load_hco3
#Year 2002 Day: 78, 134, 199
Year2002_75 = Sub75[Sub75.year == 2002]
Concentrations_02 = Year2002_75[(Year2002_75['day'] == 78) | (Year2002_75['day'] == 134) |
        (Year2002_75['day'] == 199)]
HCO3Dates_02_75 = pd.to_datetime(['3/19/2002', '4/14/2002', '7/18/2002'])
HCO3_02_75 = Concentrations_02.load_hco3
#Year 2003 Day: 29, 78, 141, 190, 345
Year2003_75 = Sub75[Sub75.year == 2003]
Concentrations_03 = Year2003_75[(Year2003_75['day'] == 29) | (Year2003_75['day'] == 78) |
        (Year2003_75['day'] == 141) | (Year2003_75['day'] == 190) | (Year2003_75['day'] == 345)]
HCO3Dates_03_75 = pd.to_datetime(['1/29/2003', '3/19/2003', '5/21/2003', '7/9/2003', '12/11/2003'])
HCO3_03_75 = Concentrations_03.load_hco3
#Year: 2004 Days: 72, 183,224
Year2004_75 = Sub75[Sub75.year == 2004]
Concentrations_04 = Year2004_75[(Year2004_75['day'] == 72) | (Year2004_75['day'] == 183) |
        (Year2004_75['day'] == 224)]
HCO3Dates_04_75 = pd.to_datetime(['3/12/2004', '7/1/2004', '8/11/2004'])
HCO3_04_75 = Concentrations_04.load_hco3
#Year: 2005 Days: 19, 83, 216, 242
Year2005_75 = Sub75[Sub75.year == 2005]
Concentrations_05 = Year2005_75[(Year2005_75['day'] == 19) | (Year2005_75['day'] == 83) | 
        (Year2005_75['day'] == 216) | (Year2005_75['day'] == 242)]
HCO3Dates_05_75 = pd.to_datetime(['1/19/2005', '3/24/2005', '8/4/2005', '8/30/2005'])
HCO3_05_75 = Concentrations_05.load_hco3
#Year: 2006 Days: 88, 208, 269, 325
Year2006_75 = Sub75[Sub75.year == 2006]
Concentrations_06 = Year2006_75[(Year2006_75['day'] == 88) | (Year2006_75['day'] == 208) |
        (Year2006_75['day'] == 269) | (Year2006_75['day'] == 325)]
HCO3Dates_06_75 = pd.to_datetime(['3/29/2006', '7/27/2006', '9/26/2006', '11/21/2006'])
HCO3_06_75 = Concentrations_06.load_hco3
#Year: 2007 Days: 101, 199
Year2007_75 = Sub75[Sub75.year == 2007]
Concentrations_07 = Year2007_75[(Year2007_75['day'] == 101) | (Year2007_75['day'] == 199)]
HCO3Dates_07_75 = pd.to_datetime(['4/11/2007', '7/18/2007'])
HCO3_07_75 = Concentrations_07.load_hco3
#Year 2008 Day: 344
Year2008_75 = Sub75[Sub75.year == 2008]
Concentrations_08 = Year2008_75[(Year2008_75['day'] == 344)]
HCO3Dates_08_75 = pd.to_datetime(['12/9/2008'])
HCO3_08_75 = Concentrations_08.load_hco3
#Year 2009 Day 55, 119, 342
Year2009_75 = Sub75[Sub75.year == 2009]
Concentrations_09 = Year2009_75[(Year2009_75['day'] == 55) |(Year2009_75['day'] == 199) |
        (Year2009_75['day'] == 342)]
HCO3Dates_09_75 = pd.to_datetime(['2/24/2009', '4/29/2009', '12/8/2009'])
HCO3_09_75 = Concentrations_09.load_hco3
#Year 2010 Day 138, 209,341
Year2010_75 = Sub75[Sub75.year == 2010]
Concentrations_10 = Year2010_75[(Year2010_75['day'] == 138) |(Year2010_75['day'] == 209)]
HCO3Dates_10_75 = pd.to_datetime(['5/18/2010', '7/28/2010'])
HCO3_10_75 = Concentrations_10.load_hco3

#Combine
HCO3_Modeled_75 = pd.concat([HCO3_92_75, HCO3_93_75, HCO3_94_75, HCO3_95_75, HCO3_96_75,
                                   HCO3_97_75, HCO3_98_75, HCO3_99_75, HCO3_00_75, HCO3_01_75, 
                                   HCO3_02_75, HCO3_03_75, HCO3_04_75, HCO3_05_75, HCO3_06_75, 
                                   HCO3_07_75, HCO3_08_75, HCO3_09_75, HCO3_10_75], axis=0)
HCO3_ObservedDays_75 = HCO3Dates_92_75.union_many([HCO3Dates_93_75, HCO3Dates_94_75, HCO3Dates_95_75,
                                              HCO3Dates_96_75, HCO3Dates_97_75, HCO3Dates_98_75, 
                                              HCO3Dates_99_75, HCO3Dates_00_75, HCO3Dates_01_75,
                                              HCO3Dates_02_75, HCO3Dates_03_75, HCO3Dates_04_75, 
                                              HCO3Dates_05_75, HCO3Dates_06_75, HCO3Dates_07_75, 
                                              HCO3Dates_08_75, HCO3Dates_09_75, HCO3Dates_10_75])
###
SO4_Modeled_75.index = ObservedDays_75
Ca_Modeled_75.index = ObservedDays_75
Mg_Modeled_75.index = ObservedDays_75
Na_Modeled_75.index = ObservedDays_75
K_Modeled_75.index = ObservedDays_75
Cl_Modeled_75.index = ObservedDays_75
CO3_Modeled_75.index = CO3_ObservedDays_75
HCO3_Modeled_75.index = HCO3_ObservedDays_75
###Analysis of Observed and Model data
SO4_Residual_75 = SO4_Modeled_75 - LoadOutSO4
Ca_Residual_75 = Ca_Modeled_75 - LoadOutCa
Mg_Residual_75 = Mg_Modeled_75 - LoadOutMg
Na_Residual_75 = Na_Modeled_75 - LoadOutNa
K_Residual_75 = K_Modeled_75 - LoadOutK
Cl_Residual_75 = Cl_Modeled_75 - LoadOutCl
CO3_Residual_75 = CO3_Modeled_75 - LoadOutCO3
HCO3_Residual_75 = HCO3_Modeled_75 - LoadOutHCO3


###Subarea 41################################################################################################
##Continuous
Sub41 = Mod1[Mod1.subarea == 41]
SO4_41L = Sub41.load_so4
Ca_41L = Sub41.load_ca
Mg_41L = Sub41.load_mg
Na_41L = Sub41.load_na
K_41L = Sub41.load_k
Cl_41L = Sub41.load_cl
HCO3_41L = Sub41.load_hco3
CO3_41L = Sub41.load_co3
##Observed Data
##Sulfate, Calcium, Magnesium, Sodium, Potassium, and Chloride all have same obsv. days
#Year 2002 Days: 213, 246
Year2002_41 = Sub41[Sub41.year == 2002]
Concentrations_02_41 = Year2002_41[(Year2002_41['day'] == 213) | (Year2002_41['day'] == 246)]
Dates_02_41 = pd.to_datetime(['8/1/2002', '9/3/2002'])
SO4_02_41 = Concentrations_02_41.load_so4
Ca_02_41 = Concentrations_02_41.load_ca
Mg_02_41 = Concentrations_02_41.load_mg
Na_02_41 = Concentrations_02_41.load_na
K_02_41 = Concentrations_02_41.load_k
Cl_02_41 = Concentrations_02_41.load_cl

#Year 2010 Day 221
Year2010_41 = Sub41[Sub41.year == 2010]
Concentrations_10_41 = Year2010_41[(Year2010_41['day'] == 221)]
Dates_10_41 = pd.to_datetime(['8/9/2010'])
SO4_10_41 = Concentrations_10_41.load_so4
Ca_10_41 = Concentrations_10_41.load_ca
Mg_10_41 = Concentrations_10_41.load_mg
Na_10_41 = Concentrations_10_41.load_na
K_10_41 = Concentrations_10_41.load_k
Cl_10_41 = Concentrations_10_41.load_cl
#Year 2011 Day 133
Year2011_41 = Sub41[Sub41.year == 2011]
Concentrations_11_41 = Year2011_41[(Year2011_41['day'] == 133)]
Dates_11_41 = pd.to_datetime(['5/13/2011'])
SO4_11_41 = Concentrations_11_41.load_so4
Ca_11_41 = Concentrations_11_41.load_ca
Mg_11_41 = Concentrations_11_41.load_mg
Na_11_41 = Concentrations_11_41.load_na
K_11_41 = Concentrations_11_41.load_k
Cl_11_41 = Concentrations_11_41.load_cl

#Combine
ObservedDays_41 = Dates_02_41.union_many([Dates_10_41, Dates_11_41])
SO4_Modeled_41 = pd.concat([SO4_02_41, SO4_10_41, SO4_11_41], axis=0)
Ca_Modeled_41 = pd.concat([Ca_02_41, Ca_10_41, Ca_11_41], axis=0)
Mg_Modeled_41 = pd.concat([Mg_02_41, Mg_10_41, Mg_11_41], axis=0)
Na_Modeled_41 = pd.concat([Na_02_41, Na_10_41, Na_11_41], axis=0)
K_Modeled_41 = pd.concat([K_02_41, K_10_41, K_11_41], axis=0)
Cl_Modeled_41 = pd.concat([Cl_02_41, Cl_10_41, Cl_11_41], axis=0)

SO4_Modeled_41.index = ObservedDays_41
Ca_Modeled_41.index = ObservedDays_41
Mg_Modeled_41.index = ObservedDays_41
Na_Modeled_41.index = ObservedDays_41
K_Modeled_41.index = ObservedDays_41
Cl_Modeled_41.index = ObservedDays_41

###Analysis of Observed and Model data
SO4_Residual_41 = SO4_Modeled_41 - LoadOb41SO4
Ca_Residual_41 = Ca_Modeled_41 - LoadOb41Ca
Mg_Residual_41 = Mg_Modeled_41 - LoadOb41Mg
Na_Residual_41 = Na_Modeled_41 - LoadOb41Na
K_Residual_41 = K_Modeled_41 - LoadOb41K
Cl_Residual_41 = Cl_Modeled_41 - LoadOb41Cl

#####Subarea 12#######################################################################################
###Continuous
Sub12 = Mod1[Mod1.subarea == 12]
SO4_12L = Sub12.load_so4
Ca_12L = Sub12.load_ca
Mg_12L = Sub12.load_mg
Na_12L = Sub12.load_na
K_12L = Sub12.load_k
Cl_12L = Sub12.load_cl
CO3_12L = Sub12.load_co3
HCO3_12L = Sub12.load_hco3

###Specific Observed Dates
##Sulfate, Calcium, Magnesium, Sodium all have same obsv. days
#Year: 1993 Days: 314
Year1993_12 = Sub12[Sub12.year == 1993]
Concentrations_93_12 = Year1993_12[(Year1993_12['day'] == 314)]
Dates_93_12 = pd.to_datetime(['11/10/1993'])
SO4_93_12 = Concentrations_93_12.load_so4
Ca_93_12 = Concentrations_93_12.load_ca
Mg_93_12 = Concentrations_93_12.load_mg
Na_93_12 = Concentrations_93_12.load_na

#Year: 1994 Day: 138, 153, 207, 313
Year1994_12 = Sub12[Sub12.year == 1994]
Concentrations_94_12 = Year1994_12[(Year1994_12['day'] == 138) | (Year1994_12['day'] == 153) | 
        (Year1994_12['day'] ==207) | (Year1994_12['day'] == 313)]
Dates_94_12 = pd.to_datetime(['5/18/1994', '6/2/1994', '7/26/1994', '11/9/1994'])
SO4_94_12 = Concentrations_94_12.load_so4
Ca_94_12 = Concentrations_94_12.load_ca
Mg_94_12 = Concentrations_94_12.load_mg
Na_94_12 = Concentrations_94_12.load_na

#Year: 1995 Day: 102, 172, 249, 333
Year1995_12 = Sub12[Sub12.year == 1995]
Concentrations_95_12 = Year1995_12[(Year1995_12['day'] == 102) | (Year1995_12['day'] == 172) | 
        (Year1995_12['day'] == 249) | (Year1995_12['day'] == 333)]
Dates_95_12 = pd.to_datetime(['4/12/1995', '6/21/1995', '9/6/1995', '11/29/1995'])
SO4_95_12 = Concentrations_95_12.load_so4
Ca_95_12 = Concentrations_95_12.load_ca
Mg_95_12 = Concentrations_95_12.load_mg
Na_95_12 = Concentrations_95_12.load_na

#Year: 1996 Day: 100, 143, 227, 324, ###NOTE 324 has 2 data points
Year1996_12 = Sub12[Sub12.year == 1996]
Concentrations_96_12 = Year1996_12[(Year1996_12['day'] == 100) | (Year1996_12['day'] == 143) | 
        (Year1996_12['day'] == 227) | (Year1996_12['day'] == 324)]
Dates_96_12 = pd.to_datetime(['4/9/1996', '5/22/1996', '8/14/1996', '11/19/1996'])
SO4_96_12 = Concentrations_96_12.load_so4
Ca_96_12 = Concentrations_96_12.load_ca
Mg_96_12 = Concentrations_96_12.load_mg
Na_96_12 = Concentrations_96_12.load_na

#Year: 1997 Day: 8,31,57,85,118*,133,140,148,155,163,167*,176,182,195,212,225,268,295*,329,357
Year1997_12 = Sub12[Sub12.year == 1997]
Concentrations_97_12 = Year1997_12[(Year1997_12['day'] == 8) | (Year1997_12['day'] == 31) | 
        (Year1997_12['day'] == 57) | (Year1997_12['day'] == 85) | (Year1997_12['day'] == 118) |
        (Year1997_12['day'] == 133) | (Year1997_12['day'] == 140) | (Year1997_12['day'] == 148) |
        (Year1997_12['day'] == 155) | (Year1997_12['day'] == 163) | (Year1997_12['day'] == 167) |
        (Year1997_12['day'] == 176) | (Year1997_12['day'] == 182) | (Year1997_12['day'] == 195) | 
        (Year1997_12['day'] == 212) | (Year1997_12['day'] == 225) | (Year1997_12['day'] == 268) |
        (Year1997_12['day'] == 295) | (Year1997_12['day'] == 329) | (Year1997_12['day'] == 357)]
Dates_97_12 = pd.to_datetime(['1/8/1997', '1/31/1997', '2/26/1997', '3/26/1997', '4/28/1997', '5/13/1997',
                              '5/20/1997', '5/28/1997', '6/4/1997', '6/12/1997', '6/16/1997', '6/25/1997',
                              '7/1/1997', '7/14/1997', '7/31/1997', '8/13/1997', '9/25/1997', '10/22/1997',
                              '11/25/1997', '12/23/1997'])
SO4_97_12 = Concentrations_97_12.load_so4
Ca_97_12 = Concentrations_97_12.load_ca
Mg_97_12 = Concentrations_97_12.load_mg
Na_97_12 = Concentrations_97_12.load_na

#Year: 1998 Days: 44,75,113,125*,149,153*,161,176,190,203*,273,317
Year1998_12 = Sub12[Sub12.year == 1998]
Concentrations_98_12 = Year1998_12[(Year1998_12['day'] == 44) | (Year1998_12['day'] == 75) |
        (Year1998_12['day'] == 113) | (Year1998_12['day'] == 125) | (Year1998_12['day'] == 149) | 
        (Year1998_12['day'] == 153) | (Year1998_12['day'] == 161) | (Year1998_12['day'] == 176) |
        (Year1998_12['day'] == 190) | (Year1998_12['day'] == 203) | (Year1998_12['day'] == 273) |
        (Year1998_12['day'] == 317)]
Dates_98_12 = pd.to_datetime(['2/13/1998', '3/16/1998', '4/23/1998', '5/5/1998', '5/29/1998',
                              '6/2/1998', '6/10/1998', '6/25/1998', '7/9/1998', '7/22/1998',
                              '9/30/1998', '11/13/1998'])
SO4_98_12 = Concentrations_98_12.load_so4
Ca_98_12 = Concentrations_98_12.load_ca
Mg_98_12 = Concentrations_98_12.load_mg
Na_98_12 = Concentrations_98_12.load_na

#Year: 1999 Days: 50,98,120,154,231,238,334
Year1999_12 = Sub12[Sub12.year == 1999]
Concentrations_99_12 = Year1999_12[(Year1999_12['day'] == 50) | (Year1999_12['day'] == 98) |
        (Year1999_12['day'] == 120) | (Year1999_12['day'] == 154) | (Year1999_12['day'] == 231) |
        (Year1999_12['day'] == 238) | (Year1999_12['day'] == 334)]
Dates_99_12 = pd.to_datetime(['2/19/1999','4/8/1999', '4/20/1999', '6/3/1999', '8/19/1999',
                              '8/26/1999', '11/30/1999'])
SO4_99_12 = Concentrations_99_12.load_so4
Ca_99_12 = Concentrations_99_12.load_ca
Mg_99_12 = Concentrations_99_12.load_mg
Na_99_12 = Concentrations_99_12.load_na

#Year: 2000 Days: 104,115,145,152,180,200,222,230,259,312,336
Year2000_12 = Sub12[Sub12.year == 2000]
Concentrations_00_12 = Year2000_12[(Year2000_12['day'] == 104) | (Year2000_12['day'] == 115) |
        (Year2000_12['day'] == 145) | (Year2000_12['day'] == 152) | (Year2000_12['day'] == 180) |
        (Year2000_12['day'] == 200) | (Year2000_12['day'] == 222) | (Year2000_12['day'] == 230) |
        (Year2000_12['day'] == 259) | (Year2000_12['day'] == 312) | (Year2000_12['day'] == 336)]
Dates_00_12 = pd.to_datetime(['4/13/2000', '4/24/2000', '5/24/2000', '5/31/2000', '6/28/2000',
                              '7/18/2000', '8/9/2000', '8/17/2000', '9/15/2000', '11/7/2000',
                              '12/1/2000'])
SO4_00_12 = Concentrations_00_12.load_so4
Ca_00_12 = Concentrations_00_12.load_ca
Mg_00_12 = Concentrations_00_12.load_mg
Na_00_12 = Concentrations_00_12.load_na

#Year 2001 Days: 79,120,150,222,233,305
Year2001_12 = Sub12[Sub12.year == 2001]
Concentrations_01_12 = Year2001_12[(Year2001_12['day'] == 79) | (Year2001_12['day'] == 120) |
        (Year2001_12['day'] == 150) | (Year2001_12['day'] == 222) | (Year2001_12['day'] == 233) |
        (Year2001_12['day'] == 305)]
Dates_01_12 = pd.to_datetime(['3/20/2001', '4/30/2001', '5/30/2001', '8/10/2001', '8/21/2001', '11/1/2001'])
SO4_01_12 = Concentrations_01_12.load_so4
Ca_01_12 = Concentrations_01_12.load_ca
Mg_01_12 = Concentrations_01_12.load_mg
Na_01_12 = Concentrations_01_12.load_na

#Year 2002 Days: 106, 140, 212, 339
Year2002_12 = Sub12[Sub12.year == 2002]
Concentrations_02_12 = Year2002_12[(Year2002_12['day'] == 106) | (Year2002_12['day'] == 140) |
        (Year2002_12['day'] == 212) | (Year2002_12['day'] == 339)]
Dates_02_12 = pd.to_datetime(['4/16/2002', '5/20/2002', '7/31/2002', '12/5/2002'])
SO4_02_12 = Concentrations_02_12.load_so4
Ca_02_12 = Concentrations_02_12.load_ca
Mg_02_12 = Concentrations_02_12.load_mg
Na_02_12 = Concentrations_02_12.load_na

#Year 2003 Days: 122, 150, 192, 300
Year2003_12 = Sub12[Sub12.year == 2003]
Concentrations_03_12 = Year2003_12[(Year2003_12['day'] == 122) | (Year2003_12['day'] == 150) |
        (Year2003_12['day'] == 192) | (Year2003_12['day'] == 300)]
Dates_03_12 = pd.to_datetime(['5/11/2003', '5/30/2003', '7/11/2003', '10/27/2003'])
SO4_03_12 = Concentrations_03_12.load_so4
Ca_03_12 = Concentrations_03_12.load_ca
Mg_03_12 = Concentrations_03_12.load_mg
Na_03_12 = Concentrations_03_12.load_na

#Year: 2004 Days: 132, 160, 217, 313
Year2004_12 = Sub12[Sub12.year == 2004]
Concentrations_04_12 = Year2004_12[(Year2004_12['day'] == 132) | (Year2004_12['day'] == 160) |
        (Year2004_12['day'] == 217) | (Year2004_12['day'] == 313)]
Dates_04_12 = pd.to_datetime(['5/11/2004', '6/8/2004', '8/4/2004', '11/8/2004'])
SO4_04_12 = Concentrations_04_12.load_so4
Ca_04_12 = Concentrations_04_12.load_ca
Mg_04_12 = Concentrations_04_12.load_mg
Na_04_12 = Concentrations_04_12.load_na

#Year: 2005 Days: 130, 179, 220, 346
Year2005_12 = Sub12[Sub12.year == 2005]
Concentrations_05_12 = Year2005_12[(Year2005_12['day'] == 130) | (Year2005_12['day'] == 179) |
        (Year2005_12['day'] == 220) | (Year2005_12['day'] == 346)]
Dates_05_12 = pd.to_datetime(['5/10/2005', '6/28/2005', '8/8/2005', '12/12/2005'])
SO4_05_12 = Concentrations_05_12.load_so4
Ca_05_12 = Concentrations_05_12.load_ca
Mg_05_12 = Concentrations_05_12.load_mg
Na_05_12 = Concentrations_05_12.load_na

#Year: 2006 Days: 109, 144, 270, 304
Year2006_12 = Sub12[Sub12.year == 2006]
Concentrations_06_12 = Year2006_12[(Year2006_12['day'] == 109) | (Year2006_12['day'] == 144) |
        (Year2006_12['day'] == 270) | (Year2006_12['day'] == 304)]
Dates_06_12 = pd.to_datetime(['4/19/2006', '5/24/2006', '9/27/2006', '10/31/2006'])
SO4_06_12 = Concentrations_06_12.load_so4
Ca_06_12 = Concentrations_06_12.load_ca
Mg_06_12 = Concentrations_06_12.load_mg
Na_06_12 = Concentrations_06_12.load_na

#Year: 2007 Days: 106,136, 199,310
Year2007_12 = Sub12[Sub12.year == 2007]
Concentrations_07_12 = Year2007_12[(Year2007_12['day'] == 106) | (Year2007_12['day'] == 136) |
        (Year2007_12['day'] == 199) | (Year2007_12['day'] == 310)]
Dates_07_12 = pd.to_datetime(['4/16/2007', '5/15/2007', '7/18/2007', '11/6/2007'])
SO4_07_12 = Concentrations_07_12.load_so4
Ca_07_12 = Concentrations_07_12.load_ca
Mg_07_12 = Concentrations_07_12.load_mg
Na_07_12 = Concentrations_07_12.load_na

#Year 2008 Day: 135, 155, 227, 337
Year2008_12 = Sub12[Sub12.year == 2008]
Concentrations_08_12 = Year2008_12[(Year2008_12['day'] == 135) | (Year2008_12['day'] == 155) |
        (Year2008_12['day'] == 227) | (Year2008_12['day'] == 337)]
Dates_08_12 = pd.to_datetime(['5/14/2008', '6/3/2008', '8/14/2008', '12/2/2008'])
SO4_08_12 = Concentrations_08_12.load_so4
Ca_08_12 = Concentrations_08_12.load_ca
Mg_08_12 = Concentrations_08_12.load_mg
Na_08_12 = Concentrations_08_12.load_na
#Year 2009 Day 119, 202, 252, 317
Year2009_12 = Sub12[Sub12.year == 2009]
Concentrations_09_12 = Year2009_12[(Year2009_12['day'] == 119) |(Year2009_12['day'] == 202) |
        (Year2009_12['day'] == 252) | (Year2009_12['day'] == 317)]
Dates_09_12 = pd.to_datetime(['4/29/2009', '7/21/2009', '9/9/2009', '11/13/2009'])
SO4_09_12 = Concentrations_09_12.load_so4
Ca_09_12 = Concentrations_09_12.load_ca
Mg_09_12 = Concentrations_09_12.load_mg
Na_09_12 = Concentrations_09_12.load_na

#Year 2010 Day 124, 160, 222, 327
Year2010_12 = Sub12[Sub12.year == 2010]
Concentrations_10_12 = Year2010_12[(Year2010_12['day'] == 124) |(Year2010_12['day'] == 160) |
        (Year2010_12['day'] == 222) | (Year2010_12['day'] == 327)]
Dates_10_12 = pd.to_datetime(['5/4/2010', '6/9/2010', '8/10/2010', '11/23/2010'])
SO4_10_12 = Concentrations_10_12.load_so4
Ca_10_12 = Concentrations_10_12.load_ca
Mg_10_12 = Concentrations_10_12.load_mg
Na_10_12 = Concentrations_10_12.load_na

#Year 2011 Day 94, 158,243, 314
Year2011_12 = Sub12[Sub12.year == 2011]
Concentrations_11_12 = Year2011_12[(Year2011_12['day'] == 94) | (Year2011_12['day'] == 158) |
        (Year2011_12['day'] == 243) | (Year2011_12['day'] == 314)]
Dates_11_12 = pd.to_datetime(['4/4/2011', '6/7/2011', '8/31/2011', '11/10/2011'])
SO4_11_12 = Concentrations_11_12.load_so4
Ca_11_12 = Concentrations_11_12.load_ca
Mg_11_12 = Concentrations_11_12.load_mg
Na_11_12 = Concentrations_11_12.load_na

#Combine

ObservedDays_12 = Dates_93_12.union_many([Dates_94_12, Dates_95_12, Dates_96_12, Dates_97_12, 
                                          Dates_98_12, Dates_99_12, Dates_00_12, Dates_01_12,
                                          Dates_02_12, Dates_03_12, Dates_04_12, Dates_05_12, 
                                          Dates_06_12, Dates_07_12, Dates_08_12, Dates_09_12, 
                                          Dates_10_12, Dates_11_12])
SO4_Modeled_12 = pd.concat([SO4_93_12, SO4_94_12, SO4_95_12, SO4_96_12, SO4_97_12,
                                  SO4_98_12, SO4_99_12, SO4_00_12, SO4_01_12, SO4_02_12, SO4_03_12,
                                  SO4_04_12, SO4_05_12, SO4_06_12, SO4_07_12, SO4_08_12, SO4_09_12,
                                  SO4_10_12, SO4_11_12], axis=0)
Ca_Modeled_12 = pd.concat([Ca_93_12, Ca_94_12, Ca_95_12, Ca_96_12, Ca_97_12, Ca_98_12,
                                 Ca_99_12, Ca_00_12, Ca_01_12, Ca_02_12, Ca_03_12, Ca_04_12, Ca_05_12,
                                 Ca_06_12, Ca_07_12, Ca_08_12, Ca_09_12, Ca_10_12, Ca_11_12], axis=0)
Mg_Modeled_12 = pd.concat([Mg_93_12, Mg_94_12, Mg_95_12, Mg_96_12, Mg_97_12, Mg_98_12,
                                 Mg_99_12, Mg_00_12, Mg_01_12, Mg_02_12, Mg_03_12, Mg_04_12, Mg_05_12,
                                 Mg_06_12, Mg_07_12, Mg_08_12, Mg_09_12, Mg_10_12, Mg_11_12], axis=0)
Na_Modeled_12 = pd.concat([Na_93_12, Na_94_12, Na_95_12, Na_96_12, Na_97_12, Na_98_12,
                                 Na_99_12, Na_00_12, Na_01_12, Na_02_12, Na_03_12, Na_04_12, Na_05_12,
                                 Na_06_12, Na_07_12, Na_08_12, Na_09_12, Na_10_12, Na_11_12], axis=0)

##Potassium
#Year: 1993 Days: 314
Year1993_12 = Sub12[Sub12.year == 1993]
Concentrations_93_12 = Year1993_12[(Year1993_12['day'] == 314)]
K_Dates_93_12 = pd.to_datetime(['11/10/1993'])
K_93_12 = Concentrations_93_12.load_k
#Year: 1994 Day: 138, 153, 207, 313
Year1994_12 = Sub12[Sub12.year == 1994]
Concentrations_94_12 = Year1994_12[(Year1994_12['day'] == 138) | (Year1994_12['day'] == 153) | 
        (Year1994_12['day'] == 207) | (Year1994_12['day'] == 313)]
K_Dates_94_12 = pd.to_datetime(['5/18/1994', '6/2/1994', '7/26/1994', '11/9/1994'])
K_94_12 = Concentrations_94_12.load_k
#Year: 1995 Day: 102, 172, 249, 333
Year1995_12 = Sub12[Sub12.year == 1995]
Concentrations_95_12 = Year1995_12[(Year1995_12['day'] == 102) | (Year1995_12['day'] == 172) | 
        (Year1995_12['day'] == 249) | (Year1995_12['day'] == 333)]
K_Dates_95_12 = pd.to_datetime(['4/12/1995', '6/21/1995', '9/6/1995', '11/29/1995'])
K_95_12 = Concentrations_95_12.load_co3
#Year: 1996 Day: 100, 143, 227, 324
Year1996_12 = Sub12[Sub12.year == 1996]
Concentrations_96_12 = Year1996_12[(Year1996_12['day'] == 100) | (Year1996_12['day'] == 143) | 
        (Year1996_12['day'] == 227) | (Year1996_12['day'] == 324)]
K_Dates_96_12 = pd.to_datetime(['4/9/1996', '5/22/1996', '8/14/1996', '11/19/1996'])
K_96_12 = Concentrations_96_12.load_k
#Year: 1997 Day: 118, 167, 225, 295, 357
Year1997_12 = Sub12[Sub12.year == 1997]
Concentrations_97_12 = Year1997_12[(Year1997_12['day'] == 118) | (Year1997_12['day'] == 167) |
        (Year1997_12['day'] == 225) | (Year1997_12['day'] == 295) | (Year1997_12['day'] == 357)]
K_Dates_97_12 = pd.to_datetime([ '4/28/1997', '6/16/1997', '8/13/1997', '10/22/1997', '12/23/1997'])
K_97_12 = Concentrations_97_12.load_k
#Year: 1998 Days: 44, 75, 113, 125, 149, 153, 161, 176, 190, 203, 273, 317
Year1998_12 = Sub12[Sub12.year == 1998]
Concentrations_98_12 = Year1998_12[(Year1998_12['day'] == 44) | (Year1998_12['day'] == 75) |
        (Year1998_12['day'] == 113) | (Year1998_12['day'] == 125) | (Year1998_12['day'] == 149) | 
        (Year1998_12['day'] == 153) | (Year1998_12['day'] == 161) | (Year1998_12['day'] == 176) |
        (Year1998_12['day'] == 190) | (Year1998_12['day'] == 203) | (Year1998_12['day'] == 273) |
        (Year1998_12['day'] == 317)]
K_Dates_98_12 = pd.to_datetime(['2/13/1998', '3/16/1998', '4/23/1998', '5/5/1998', '5/29/1998', 
                                '6/2/1998', '6/10/1998', '6/25/1998', '7/9/1998', '7/22/1998',
                                '9/30/1998', '11/13/1998'])
K_98_12 = Concentrations_98_12.load_k
#Year: 1999 Days: 50, 98, 120, 154, 231, 238, 334
Year1999_12 = Sub12[Sub12.year == 1999]
Concentrations_99_12 = Year1999_12[(Year1999_12['day'] == 50) | (Year1999_12['day'] == 98) |
        (Year1999_12['day'] == 120) | (Year1999_12['day'] == 154) | (Year1999_12['day'] == 231) |
        (Year1999_12['day'] == 238) | (Year1999_12['day'] == 334)]
K_Dates_99_12 = pd.to_datetime(['2/19/1999', '4/8/1999', '4/30/1999', '6/3/1999', '8/19/1999',
                                 '8/26/1999', '11/30/1999'])
K_99_12 = Concentrations_99_12.load_k
#Year: 2000 Days: 104, 115, 145, 152, 180, 200, 222, 230, 259, 312, 336
Year2000_12 = Sub12[Sub12.year == 2000]
Concentrations_00_12 = Year2000_12[(Year2000_12['day'] == 104) | (Year2000_12['day'] == 115) |
        (Year2000_12['day'] == 145) | (Year2000_12['day'] == 152) | (Year2000_12['day'] == 180) | 
        (Year2000_12['day'] == 200) | (Year2000_12['day'] == 222) | (Year2000_12['day'] == 230) |
        (Year2000_12['day'] == 259) | (Year2000_12['day'] == 312) | (Year2000_12['day'] == 336)]
K_Dates_00_12 = pd.to_datetime(['4/13/2000', '4/24/2000', '5/24/2000', '5/31/2000', '6/28/2000', 
                                 '7/18/2000', '8/9/2000', '8/17/2000', '9/15/2000', '11/7/2000',
                                 '12/1/2000'])
K_00_12 = Concentrations_00_12.load_k
#Year 2001 Days: 79, 120, 150, 222, 233, 305
Year2001_12 = Sub12[Sub12.year == 2001]
Concentrations_01_12 = Year2001_12[(Year2001_12['day'] == 79) | (Year2001_12['day'] == 120) |
        (Year2001_12['day'] == 150) | (Year2001_12['day'] == 222) | (Year2001_12['day'] == 233) |
        (Year2001_12['day'] == 305)]
K_Dates_01_12 = pd.to_datetime(['3/20/2001', '4/30/2001', '5/30/2001', '8/10/2001', '8/21/2001',
                                '11/1/2001'])
K_01_12 = Concentrations_01_12.load_k
#Year 2002 Day:  106, 140, 212, 339
Year2002_12 = Sub12[Sub12.year == 2002]
Concentrations_02_12 = Year2002_12[(Year2002_12['day'] == 106) | (Year2002_12['day'] == 140) |
        (Year2002_12['day'] == 212) | (Year2002_12['day'] == 339)]
K_Dates_02_12 = pd.to_datetime(['4/19/2002', '5/20/2002', '7/31/2002', '12/5/2002'])
K_02_12 = Concentrations_02_12.load_k
#Year 2003 Day: 122, 150, 192, 300
Year2003_12 = Sub12[Sub12.year == 2003]
Concentrations_03_12 = Year2003_12[(Year2003_12['day'] == 122) | (Year2003_12['day'] == 150) |
        (Year2003_12['day'] == 192) | (Year2003_12['day'] == 300)]
K_Dates_03_12 = pd.to_datetime(['5/2/2003', '5/30/2003', '7/11/2003', '10/27/2003'])
K_03_12 = Concentrations_03_12.load_k
#Year: 2004 Days: 132, 160, 217, 313
Year2004_12 = Sub12[Sub12.year == 2004]
Concentrations_04_12 = Year2004_12[(Year2004_12['day'] == 132) | (Year2004_12['day'] == 160) |
        (Year2004_12['day'] == 217) | (Year2004_12['day'] == 313)]
K_Dates_04_12 = pd.to_datetime(['5/11/2004', '6/8/2004', '8/4/2004', '11/8/2004'])
K_04_12 = Concentrations_04_12.load_k
#Year: 2005 Days: 130, 179, 220, 346
Year2005_12 = Sub12[Sub12.year == 2005]
Concentrations_05_12 = Year2005_12[(Year2005_12['day'] == 130) | (Year2005_12['day'] == 179) |
        (Year2005_12['day'] == 220) | (Year2005_12['day'] == 346)]
K_Dates_05_12 = pd.to_datetime(['5/10/2005', '6/28/2005', '8/8/2005', '12/12/2005'])
K_05_12 = Concentrations_05_12.load_k
#Year: 2006 Days: 109, 144, 270, 304
Year2006_12 = Sub12[Sub12.year == 2006]
Concentrations_06_12 = Year2006_12[(Year2006_12['day'] == 109) | (Year2006_12['day'] == 144) |
        (Year2006_12['day'] == 270) | (Year2006_12['day'] == 304)]
K_Dates_06_12 = pd.to_datetime(['4/19/2006', '5/24/2006', '9/27/2006', '10/31/2006'])
K_06_12 = Concentrations_06_12.load_k
#Year: 2007 Days: 106, 136, 199, 310
Year2007_12 = Sub12[Sub12.year == 2007]
Concentrations_07_12 = Year2007_12[(Year2007_12['day'] == 106) | (Year2007_12['day'] == 136) |
        (Year2007_12['day'] == 199) | (Year2007_12['day'] == 310)]
K_Dates_07_12 = pd.to_datetime(['4/16/2007', '5/16/2007', '7/18/2007', '11/6/2007'])
K_07_12 = Concentrations_07_12.load_k
#Year 2008 Day: 135, 155, 227, 337
Year2008_12 = Sub12[Sub12.year == 2008]
Concentrations_08_12 = Year2008_12[(Year2008_12['day'] == 135) | (Year2008_12['day'] == 155) | 
        (Year2008_12['day'] == 227) | (Year2008_12['day'] == 337)]
K_Dates_08_12 = pd.to_datetime(['5/14/2008', '6/3/2008', '8/14/2008', '12/2/2008'])
K_08_12 = Concentrations_08_12.load_k
#Year 2009 Day 119, 202, 252, 317
Year2009_12 = Sub12[Sub12.year == 2009]
Concentrations_09_12 = Year2009_12[(Year2009_12['day'] == 119) |(Year2009_12['day'] == 202) |
        (Year2009_12['day'] == 252) | (Year2009_12['day'] == 317)]
K_Dates_09_12 = pd.to_datetime(['4/29/2009', '7/21/2009', '9/9/2009', '11/13/2009'])
K_09_12 = Concentrations_09_12.load_k
#Year 2010 Day 124, 160, 222, 327
Year2010_12 = Sub12[Sub12.year == 2010]
Concentrations_10_12 = Year2010_12[(Year2010_12['day'] == 124) |(Year2010_12['day'] == 160) |
        (Year2010_12['day'] == 222) | (Year2010_12['day'] == 327)]
K_Dates_10_12 = pd.to_datetime(['5/4/2010', '6/9/2010', '8/10/2010', '11/23/2010'])
K_10_12 = Concentrations_10_12.load_k
#Year 2011 Day 94, 158, 243, 314
Year2011_12 = Sub12[Sub12.year == 2011]
Concentrations_11_12 = Year2011_12[(Year2011_12['day'] == 94) | (Year2011_12['day'] == 158) |
        (Year2011_12['day'] == 243) | (Year2011_12['day'] == 314)]
K_Dates_11_12 = pd.to_datetime(['4/4/2011', '6/7/2011', '8/31/2011', '11/10/2011'])
K_11_12 = Concentrations_11_12.load_k
#Combine
K_Modeled_12 = pd.concat([K_93_12, K_94_12, K_95_12, K_96_12, K_97_12,
                                  K_98_12, K_99_12, K_00_12, K_01_12, K_02_12, K_03_12,
                                  K_04_12, K_05_12, K_06_12, K_07_12, K_08_12, K_09_12,
                                  K_10_12, K_11_12], axis=0)
K_ObservedDays_12 = K_Dates_93_12.union_many([K_Dates_94_12, K_Dates_95_12, K_Dates_96_12, 
                                              K_Dates_97_12, K_Dates_98_12, K_Dates_99_12, 
                                              K_Dates_00_12, K_Dates_01_12, K_Dates_02_12, 
                                              K_Dates_03_12, K_Dates_04_12, K_Dates_05_12, 
                                              K_Dates_06_12, K_Dates_07_12, K_Dates_08_12, 
                                              K_Dates_09_12, K_Dates_10_12, K_Dates_11_12])

##Chloride
#Year: 1993 Days: 314
Year1993_12 = Sub12[Sub12.year == 1993]
Concentrations_93_12 = Year1993_12[(Year1993_12['day'] == 314)]
Cl_Dates_93_12 = pd.to_datetime(['11/10/1993'])
Cl_93_12 = Concentrations_93_12.load_cl
#Year: 1994 Day: 138, 153, 207, 313
Year1994_12 = Sub12[Sub12.year == 1994]
Concentrations_94_12 = Year1994_12[(Year1994_12['day'] == 138) | (Year1994_12['day'] == 153) | 
        (Year1994_12['day'] == 207) | (Year1994_12['day'] == 313)]
Cl_Dates_94_12 = pd.to_datetime(['5/18/1994', '6/2/1994', '7/26/1994', '11/9/1994'])
Cl_94_12 = Concentrations_94_12.load_cl
#Year: 1995 Day: 102, 172, 249, 333
Year1995_12 = Sub12[Sub12.year == 1995]
Concentrations_95_12 = Year1995_12[(Year1995_12['day'] == 102) | (Year1995_12['day'] == 172) | 
        (Year1995_12['day'] == 249) | (Year1995_12['day'] == 333)]
Cl_Dates_95_12 = pd.to_datetime(['4/12/1995', '6/21/1995', '9/6/1995', '11/29/1995'])
Cl_95_12 = Concentrations_95_12.load_cl
#Year: 1996 Day: 100, 143, 227, 324
Year1996_12 = Sub12[Sub12.year == 1996]
Concentrations_96_12 = Year1996_12[(Year1996_12['day'] == 100) | (Year1996_12['day'] == 143) | 
        (Year1996_12['day'] == 227) | (Year1996_12['day'] == 324)]
Cl_Dates_96_12 = pd.to_datetime(['4/9/1996', '5/22/1996', '8/14/1996', '11/19/1996'])
Cl_96_12 = Concentrations_96_12.load_cl
#Year: 1997 Day: 118, 167, 225, 295,
Year1997_12 = Sub12[Sub12.year == 1997]
Concentrations_97_12 = Year1997_12[(Year1997_12['day'] == 118) | (Year1997_12['day'] == 167) |
        (Year1997_12['day'] == 225) | (Year1997_12['day'] == 295)]
Cl_Dates_97_12 = pd.to_datetime([ '4/28/1997', '6/16/1997', '8/13/1997', '10/22/1997'])
Cl_97_12 = Concentrations_97_12.load_cl
#Year: 1998 Days: 125, 153, 203, 317
Year1998_12 = Sub12[Sub12.year == 1998]
Concentrations_98_12 = Year1998_12[(Year1998_12['day'] == 125) | (Year1998_12['day'] == 153) | 
        (Year1998_12['day'] == 203) | (Year1998_12['day'] == 317)]
Cl_Dates_98_12 = pd.to_datetime(['5/5/1998', '6/2/1998', '7/22/1998', '11/13/1998'])
Cl_98_12 = Concentrations_98_12.load_cl
#Year: 1999 Days: 98, 154,  238, 334
Year1999_12 = Sub12[Sub12.year == 1999]
Concentrations_99_12 = Year1999_12[(Year1999_12['day'] == 98) | (Year1999_12['day'] == 154) | 
        (Year1999_12['day'] == 238) | (Year1999_12['day'] == 334)]
Cl_Dates_99_12 = pd.to_datetime(['4/8/1999', '6/3/1999', '8/26/1999', '11/30/1999'])
Cl_99_12 = Concentrations_99_12.load_cl
#Year: 2000 Days: 104, 115, 145, 222,  312, 
Year2000_12 = Sub12[Sub12.year == 2000]
Concentrations_00_12 = Year2000_12[(Year2000_12['day'] == 104) | (Year2000_12['day'] == 115) |
        (Year2000_12['day'] == 145) | (Year2000_12['day'] == 222) | (Year2000_12['day'] == 312)]
Cl_Dates_00_12 = pd.to_datetime(['4/13/2000', '4/24/2000', '5/24/2000', '8/9/2000', '11/7/2000'])
Cl_00_12 = Concentrations_00_12.load_cl
#Year 2001 Days: 120, 150, 222, 305
Year2001_12 = Sub12[Sub12.year == 2001]
Concentrations_01_12 = Year2001_12[(Year2001_12['day'] == 120) | (Year2001_12['day'] == 150) | 
        (Year2001_12['day'] == 222) | (Year2001_12['day'] == 305)]
Cl_Dates_01_12 = pd.to_datetime(['4/30/2001', '5/30/2001', '8/10/2001', '11/1/2001'])
Cl_01_12 = Concentrations_01_12.load_cl
#Year 2002 Day:  106, 140, 212, 339
Year2002_12 = Sub12[Sub12.year == 2002]
Concentrations_02_12 = Year2002_12[(Year2002_12['day'] == 106) | (Year2002_12['day'] == 140) |
        (Year2002_12['day'] == 212) | (Year2002_12['day'] == 339)]
Cl_Dates_02_12 = pd.to_datetime(['4/19/2002', '5/20/2002', '7/31/2002', '12/5/2002'])
Cl_02_12 = Concentrations_02_12.load_cl
#Year 2003 Day: 122, 150, 192, 300
Year2003_12 = Sub12[Sub12.year == 2003]
Concentrations_03_12 = Year2003_12[(Year2003_12['day'] == 122) | (Year2003_12['day'] == 150) |
        (Year2003_12['day'] == 192) | (Year2003_12['day'] == 300)]
Cl_Dates_03_12 = pd.to_datetime(['5/2/2003', '5/30/2003', '7/11/2003', '10/27/2003'])
Cl_03_12 = Concentrations_03_12.load_cl
#Year: 2004 Days: 132, 160, 217, 313
Year2004_12 = Sub12[Sub12.year == 2004]
Concentrations_04_12 = Year2004_12[(Year2004_12['day'] == 132) | (Year2004_12['day'] == 160) |
        (Year2004_12['day'] == 217) | (Year2004_12['day'] == 313)]
Cl_Dates_04_12 = pd.to_datetime(['5/11/2004', '6/8/2004', '8/4/2004', '11/8/2004'])
Cl_04_12 = Concentrations_04_12.load_cl
#Year: 2005 Days: 130, 179, 220, 346
Year2005_12 = Sub12[Sub12.year == 2005]
Concentrations_05_12 = Year2005_12[(Year2005_12['day'] == 130) | (Year2005_12['day'] == 179) |
        (Year2005_12['day'] == 220) | (Year2005_12['day'] == 346)]
Cl_Dates_05_12 = pd.to_datetime(['5/10/2005', '6/28/2005', '8/8/2005', '12/12/2005'])
Cl_05_12 = Concentrations_05_12.load_cl
#Year: 2006 Days: 109, 144, 270, 304
Year2006_12 = Sub12[Sub12.year == 2006]
Concentrations_06_12 = Year2006_12[(Year2006_12['day'] == 109) | (Year2006_12['day'] == 144) |
        (Year2006_12['day'] == 270) | (Year2006_12['day'] == 304)]
Cl_Dates_06_12 = pd.to_datetime(['4/19/2006', '5/24/2006', '9/27/2006', '10/31/2006'])
Cl_06_12 = Concentrations_06_12.load_cl
#Year: 2007 Days: 106, 136, 199, 310
Year2007_12 = Sub12[Sub12.year == 2007]
Concentrations_07_12 = Year2007_12[(Year2007_12['day'] == 106) | (Year2007_12['day'] == 136) |
        (Year2007_12['day'] == 199) | (Year2007_12['day'] == 310)]
Cl_Dates_07_12 = pd.to_datetime(['4/16/2007', '5/16/2007', '7/18/2007', '11/6/2007'])
Cl_07_12 = Concentrations_07_12.load_cl
#Year 2008 Day: 135, 155, 227, 337
Year2008_12 = Sub12[Sub12.year == 2008]
Concentrations_08_12 = Year2008_12[(Year2008_12['day'] == 135) | (Year2008_12['day'] == 155) | 
        (Year2008_12['day'] == 227) | (Year2008_12['day'] == 337)]
Cl_Dates_08_12 = pd.to_datetime(['5/14/2008', '6/3/2008', '8/14/2008', '12/2/2008'])
Cl_08_12 = Concentrations_08_12.load_cl
#Year 2009 Day 119, 202, 252, 317
Year2009_12 = Sub12[Sub12.year == 2009]
Concentrations_09_12 = Year2009_12[(Year2009_12['day'] == 119) |(Year2009_12['day'] == 202) |
        (Year2009_12['day'] == 252) | (Year2009_12['day'] == 317)]
Cl_Dates_09_12 = pd.to_datetime(['4/29/2009', '7/21/2009', '9/9/2009', '11/13/2009'])
Cl_09_12 = Concentrations_09_12.load_cl
#Year 2010 Day 124, 160, 222, 327
Year2010_12 = Sub12[Sub12.year == 2010]
Concentrations_10_12 = Year2010_12[(Year2010_12['day'] == 124) |(Year2010_12['day'] == 160) |
        (Year2010_12['day'] == 222) | (Year2010_12['day'] == 327)]
Cl_Dates_10_12 = pd.to_datetime(['5/4/2010', '6/9/2010', '8/10/2010', '11/23/2010'])
Cl_10_12 = Concentrations_10_12.load_cl
#Year 2011 Day 94, 158, 243, 314
Year2011_12 = Sub12[Sub12.year == 2011]
Concentrations_11_12 = Year2011_12[(Year2011_12['day'] == 94) | (Year2011_12['day'] == 158) |
        (Year2011_12['day'] == 243) | (Year2011_12['day'] == 314)]
Cl_Dates_11_12 = pd.to_datetime(['4/4/2011', '6/7/2011', '8/31/2011', '11/10/2011'])
Cl_11_12 = Concentrations_11_12.load_cl
#Combine
Cl_Modeled_12 = pd.concat([Cl_93_12, Cl_94_12, Cl_95_12, Cl_96_12, Cl_97_12,
                                  Cl_98_12, Cl_99_12, Cl_00_12, Cl_01_12, Cl_02_12, Cl_03_12,
                                  Cl_04_12, Cl_05_12, Cl_06_12, Cl_07_12, Cl_08_12, Cl_09_12,
                                  Cl_10_12, Cl_11_12], axis=0)
Cl_ObservedDays_12 = Cl_Dates_93_12.union_many([Cl_Dates_94_12, Cl_Dates_95_12, Cl_Dates_96_12, 
                                              Cl_Dates_97_12, Cl_Dates_98_12, Cl_Dates_99_12, 
                                              Cl_Dates_00_12, Cl_Dates_01_12, Cl_Dates_02_12, 
                                              Cl_Dates_03_12, Cl_Dates_04_12, Cl_Dates_05_12, 
                                              Cl_Dates_06_12, Cl_Dates_07_12, Cl_Dates_08_12, 
                                              Cl_Dates_09_12, Cl_Dates_10_12, Cl_Dates_11_12])

##Bicarbonate
#Year: 1996 Day: 324
Year1996_12 = Sub12[Sub12.year == 1996]
Concentrations_96_12 = Year1996_12[(Year1996_12['day'] == 324)]
HCO3Dates_96_12 = pd.to_datetime(['11/19/1996'])
HCO3_96_12 = Concentrations_96_12.load_hco3
#Year: 1997 Day: 118, 167, 295
Year1997_12 = Sub12[Sub12.year == 1997]
Concentrations_97_12 = Year1997_12[(Year1997_12['day'] == 118) | (Year1997_12['day'] == 167) |
        (Year1997_12['day'] == 295)]
HCO3Dates_97_12 = pd.to_datetime([ '4/28/1997', '6/16/1997', '10/22/1997'])
HCO3_97_12 = Concentrations_97_12.load_hco3
#Year: 1998 Days: 125, 153, 203, 317
Year1998_125 = Sub12[Sub12.year == 1998]
Concentrations_98_12 = Year1998_12[(Year1998_12['day'] == 125) | (Year1998_12['day'] == 153) |
        (Year1998_12['day'] == 203) | (Year1998_12['day'] == 317)]
HCO3Dates_98_12 = pd.to_datetime(['5/5/1998' , '6//2/1998', '7/22/1998', '11/13/1998'])
HCO3_98_12 = Concentrations_98_12.load_hco3
#Year: 1999 Days: 98, 154, 238, 334
Year1999_12 = Sub12[Sub12.year == 1999]
Concentrations_99_12 = Year1999_12[(Year1999_12['day'] == 98) | (Year1999_12['day'] == 154) |
        (Year1999_12['day'] == 238) | (Year1999_12['day'] == 334)]
HCO3Dates_99_12 = pd.to_datetime(['4/8/1999', '6/3/1999', '8/26/1999', '11/30/1999'])
HCO3_99_12 = Concentrations_99_12.load_hco3
#Year: 2000 Days: 104, 145, 222, 312
Year2000_12 = Sub12[Sub12.year == 2000]
Concentrations_00_12 = Year2000_12[(Year2000_12['day'] == 104) | (Year2000_12['day'] == 145) |
        (Year2000_12['day'] == 222) | (Year2000_12['day'] == 312)]
HCO3Dates_00_12 = pd.to_datetime(['4/13/2000', '5/24/2000', '8/9/2000', '11/7/2000'])
HCO3_00_12 = Concentrations_00_12.load_hco3
#Year 2001 Days: 120, 150, 222, 305
Year2001_12 = Sub12[Sub12.year == 2001]
Concentrations_01_12 = Year2001_12[(Year2001_12['day'] == 120) | (Year2001_12['day'] == 150) |
        (Year2001_12['day'] == 222) | (Year2001_12['day'] == 305)]
HCO3Dates_01_12 = pd.to_datetime(['4/30/2001', '5/30/2001', '8/19/2001', '11/1/2001'])
HCO3_01_12 = Concentrations_01_12.load_hco3
#Year 2002 Day: 106, 140, 212, 339
Year2002_12 = Sub12[Sub12.year == 2002]
Concentrations_02_12 = Year2002_12[(Year2002_12['day'] == 106) | (Year2002_12['day'] == 140) |
        (Year2002_12['day'] == 212) | (Year2002_12['day'] == 339)]
HCO3Dates_02_12 = pd.to_datetime(['4/16/2002', '5/20/2002', '7/31/2002', '12/5/2002'])
HCO3_02_12 = Concentrations_02_12.load_hco3
#Year 2003 Day: 122, 150, 192, 300
Year2003_12 = Sub12[Sub12.year == 2003]
Concentrations_03_12 = Year2003_12[(Year2003_12['day'] == 122) | (Year2003_12['day'] == 150) |
        (Year2003_12['day'] == 192) | (Year2003_12['day'] == 300)]
HCO3Dates_03_12 = pd.to_datetime(['5/2/2003', '5/30/2003', '7/11/2003', '10/27/2003'])
HCO3_03_12 = Concentrations_03_12.load_hco3
#Year: 2004 Days: 132, 160, 217, 313
Year2004_12 = Sub12[Sub12.year == 2004]
Concentrations_04_12 = Year2004_12[(Year2004_12['day'] == 132) | (Year2004_12['day'] == 160) |
        (Year2004_12['day'] == 217) | (Year2004_12['day'] == 313)]
HCO3Dates_04_12 = pd.to_datetime(['5/11/2004', '6/8/2004', '8/4/2004', '11/8/2004'])
HCO3_04_12 = Concentrations_04_12.load_hco3
#Year: 2005 Days: 130, 179, 220, 346
Year2005_12 = Sub12[Sub12.year == 2005]
Concentrations_05_12 = Year2005_12[(Year2005_12['day'] == 130) | (Year2005_12['day'] == 179) | 
        (Year2005_12['day'] == 220) | (Year2005_12['day'] == 346)]
HCO3Dates_05_12 = pd.to_datetime(['5/10/2005', '6/28/2005', '8/8/2005', '12/12/2005'])
HCO3_05_12 = Concentrations_05_12.load_hco3
#Year: 2006 Days: 109, 144
Year2006_12 = Sub12[Sub12.year == 2006]
Concentrations_06_12 = Year2006_12[(Year2006_12['day'] == 109) | (Year2006_12['day'] == 144)]
HCO3Dates_06_12 = pd.to_datetime(['4/19/2006', '5/24/2006'])
HCO3_06_12 = Concentrations_06_12.load_hco3

#Combine
HCO3_Modeled_12 = pd.concat([HCO3_96_12, HCO3_97_12, HCO3_98_12, HCO3_99_12, HCO3_00_12, HCO3_01_12, 
                                   HCO3_02_12, HCO3_03_12, HCO3_04_12, HCO3_05_12, HCO3_06_12], axis=0)
HCO3_ObservedDays_12 = HCO3Dates_96_12.union_many([ HCO3Dates_97_12, HCO3Dates_98_12, HCO3Dates_99_12, 
                                                   HCO3Dates_00_12, HCO3Dates_01_12, HCO3Dates_02_12, 
                                                   HCO3Dates_03_12, HCO3Dates_04_12, HCO3Dates_05_12, 
                                                   HCO3Dates_06_12])

####Index
SO4_Modeled_12.index = ObservedDays_12
Ca_Modeled_12.index = ObservedDays_12
Mg_Modeled_12.index = ObservedDays_12
Na_Modeled_12.index = ObservedDays_12
K_Modeled_12.index = K_ObservedDays_12
Cl_Modeled_12.index = Cl_ObservedDays_12
HCO3_Modeled_12.index = HCO3_ObservedDays_12


####Analyze
SO4_Residual_12 = SO4_Modeled_12 - LoadOb12SO4
Ca_Residual_12 = Ca_Modeled_12 - LoadOb12Ca
Mg_Residual_12 = Mg_Modeled_12 - LoadOb12Mg
Na_Residual_12 = Na_Modeled_12 - LoadOb12Na
K_Residual_12 = K_Modeled_12 - LoadOb12K
Cl_Residual_12 = Cl_Modeled_12 - LoadOb12Cl
HCO3_Residual_12 = HCO3_Modeled_12 - LoadOb12HCO3

###Subarea 9######################################################################################################################################
##Continuous
Sub9 = Mod1[Mod1.subarea == 9]
SO4_9L = Sub9.load_so4
Ca_9L = Sub9.load_ca
Mg_9L = Sub9.load_mg
Na_9L = Sub9.load_na
K_9L = Sub9.load_k
Cl_9L = Sub9.load_cl
CO3_9L = Sub9.load_co3
HCO3_9L = Sub9.load_hco3

##Specific Dates
## Calcium, Magnesium, Sodium all have same obsv. days
#Year: 1996 Day: 324
Year1996_9 = Sub9[Sub9.year == 1996]
Concentrations_96_9 = Year1996_9[(Year1996_9['day'] == 324)]
Dates_96_9 = pd.to_datetime(['11/19/1996'])
Ca_96_9 = Concentrations_96_9.load_ca
Mg_96_9 = Concentrations_96_9.load_mg
Na_96_9 = Concentrations_96_9.load_na
#Year: 1997 Day: 8,30,56,84,119,134,141,149,156,162,167,177,182,196,211,224,268,295,329,357
Year1997_9 = Sub9[Sub9.year == 1997]
Concentrations_97_9 = Year1997_9[(Year1997_9['day'] == 8) | (Year1997_9['day'] == 30) | 
        (Year1997_9['day'] == 56) | (Year1997_9['day'] == 84) | (Year1997_9['day'] == 119) |
        (Year1997_9['day'] == 134) | (Year1997_9['day'] == 141) | (Year1997_9['day'] == 149) |
        (Year1997_9['day'] == 156) | (Year1997_9['day'] == 162) | (Year1997_9['day'] == 167) |
        (Year1997_9['day'] == 177) | (Year1997_9['day'] == 182) | (Year1997_9['day'] == 196) | 
        (Year1997_9['day'] == 211) | (Year1997_9['day'] == 224) | (Year1997_9['day'] == 268) |
        (Year1997_9['day'] == 295) | (Year1997_9['day'] == 329) | (Year1997_9['day'] == 357)]
Dates_97_9 = pd.to_datetime(['1/8/1997', '1/30/1997', '2/25/1997', '3/25/1997', '4/29/1997', '5/14/1997',
                              '5/21/1997', '5/29/1997', '6/5/1997', '6/11/1997', '6/16/1997', '6/26/1997',
                              '7/1/1997', '7/15/1997', '7/30/1997', '8/12/1997', '9/25/1997', '10/22/1997',
                              '11/25/1997', '12/23/1997'])
Ca_97_9 = Concentrations_97_9.load_ca
Mg_97_9 = Concentrations_97_9.load_mg
Na_97_9 = Concentrations_97_9.load_na
#Year: 1998 Days: 43,75,113,126,149,153,160,175,190,203,273
Year1998_9 = Sub9[Sub9.year == 1998]
Concentrations_98_9 = Year1998_9[(Year1998_9['day'] == 43) | (Year1998_9['day'] == 75) |
        (Year1998_9['day'] == 113) | (Year1998_9['day'] == 126) | (Year1998_9['day'] == 149) | 
        (Year1998_9['day'] == 153) | (Year1998_9['day'] == 160) | (Year1998_9['day'] == 175) |
        (Year1998_9['day'] == 190) | (Year1998_9['day'] == 203) | (Year1998_9['day'] == 273)]
Dates_98_9 = pd.to_datetime(['2/12/1998', '3/16/1998', '4/23/1998', '5/6/1998', '5/29/1998',
                              '6/2/1998', '6/9/1998', '6/24/1998', '7/9/1998', '7/22/1998',
                              '9/30/1998'])
Ca_98_9 = Concentrations_98_9.load_ca
Mg_98_9 = Concentrations_98_9.load_mg
Na_98_9 = Concentrations_98_9.load_na
#Year: 1999 Days: 48,119,231
Year1999_9 = Sub9[Sub9.year == 1999]
Concentrations_99_9 = Year1999_9[(Year1999_9['day'] == 48) | (Year1999_9['day'] == 119) |
        (Year1999_9['day'] == 231)]
Dates_99_9 = pd.to_datetime(['2/17/1999', '4/29/1999', '8/19/1999'])
Ca_99_9 = Concentrations_99_9.load_ca
Mg_99_9 = Concentrations_99_9.load_mg
Na_99_9 = Concentrations_99_9.load_na
#Year: 2000 Days: 89,115,137,152,164,180,200,235,259,340
Year2000_9 = Sub9[Sub9.year == 2000]
Concentrations_00_9 = Year2000_9[(Year2000_9['day'] == 89) | (Year2000_9['day'] == 115) |
        (Year2000_9['day'] == 137) | (Year2000_9['day'] == 152) | (Year2000_9['day'] == 164) |
        (Year2000_9['day'] == 180) | (Year2000_9['day'] == 200) | (Year2000_9['day'] == 235) |
        (Year2000_9['day'] == 259) | (Year2000_9['day'] == 340)]
Dates_00_9 = pd.to_datetime(['3/29/2000', '4/24/2000', '5/16/2000', '5/31/2000', '6/12/2000',
                              '6/28/2000', '7/18/2000', '8/22/2000', '9/15/2000', '12/5/2000'])
Ca_00_9 = Concentrations_00_9.load_ca
Mg_00_9 = Concentrations_00_9.load_mg
Na_00_9 = Concentrations_00_9.load_na
#Year 2001 Days: 8,71,120,150,233
Year2001_9 = Sub9[Sub9.year == 2001]
Concentrations_01_9 = Year2001_9[(Year2001_9['day'] == 8) | (Year2001_9['day'] == 71) |
        (Year2001_9['day'] == 120) | (Year2001_9['day'] == 150) | (Year2001_9['day'] == 233)]
Dates_01_9 = pd.to_datetime(['1/8/2001', '3/12/2001', '4/30/2001', '5/30/2001', '8/21/2001'])
Ca_01_9 = Concentrations_01_9.load_ca
Mg_01_9 = Concentrations_01_9.load_mg
Na_01_9 = Concentrations_01_9.load_na
#Combine
ObservedDays_9 = Dates_96_9.union_many([Dates_97_9, Dates_98_9, Dates_99_9, Dates_00_9, Dates_01_9])
Ca_Modeled_9 = pd.concat([Ca_96_9, Ca_97_9, Ca_98_9, Ca_99_9, Ca_00_9, Ca_01_9], axis=0)
Mg_Modeled_9 = pd.concat([Mg_96_9, Mg_97_9, Mg_98_9, Mg_99_9, Mg_00_9, Mg_01_9], axis=0)
Na_Modeled_9 = pd.concat([Na_96_9, Na_97_9, Na_98_9, Na_99_9, Na_00_9, Na_01_9], axis=0)
##Sulfate
#Year: 1996 Day: 324
Year1996_9 = Sub9[Sub9.year == 1996]
Concentrations_96_9 = Year1996_9[(Year1996_9['day'] == 324)]
SO4_Dates_96_9 = pd.to_datetime(['11/19/1996'])
SO4_96_9 = Concentrations_96_9.load_so4
#Year: 1997 Day: 8,30,56,84,119,134,141,149,156,162,167,177,182,196,211,224,268,295,329,357
Year1997_9 = Sub9[Sub9.year == 1997]
Concentrations_97_9 = Year1997_9[(Year1997_9['day'] == 8) | (Year1997_9['day'] == 30) | 
        (Year1997_9['day'] == 56) | (Year1997_9['day'] == 84) | (Year1997_9['day'] == 119) |
        (Year1997_9['day'] == 134) | (Year1997_9['day'] == 141) | (Year1997_9['day'] == 149) |
        (Year1997_9['day'] == 156) | (Year1997_9['day'] == 162) | (Year1997_9['day'] == 167) |
        (Year1997_9['day'] == 177) | (Year1997_9['day'] == 182) | (Year1997_9['day'] == 196) | 
        (Year1997_9['day'] == 211) | (Year1997_9['day'] == 224) | (Year1997_9['day'] == 268) |
        (Year1997_9['day'] == 295) | (Year1997_9['day'] == 329) | (Year1997_9['day'] == 357)]
SO4_Dates_97_9 = pd.to_datetime(['1/8/1997', '1/30/1997', '2/25/1997', '3/25/1997', '4/29/1997', '5/14/1997',
                              '5/21/1997', '5/29/1997', '6/5/1997', '6/11/1997', '6/16/1997', '6/26/1997',
                              '7/1/1997', '7/15/1997', '7/30/1997', '8/12/1997', '9/25/1997', '10/22/1997',
                              '11/25/1997', '12/23/1997'])
SO4_97_9 = Concentrations_97_9.load_so4
#Year: 1998 Days: 43,75,113,126,149,153,160,175,190,203,273
Year1998_9 = Sub9[Sub9.year == 1998]
Concentrations_98_9 = Year1998_9[(Year1998_9['day'] == 43) | (Year1998_9['day'] == 75) |
        (Year1998_9['day'] == 113) | (Year1998_9['day'] == 126) | (Year1998_9['day'] == 149) | 
        (Year1998_9['day'] == 153) | (Year1998_9['day'] == 160) | (Year1998_9['day'] == 175) |
        (Year1998_9['day'] == 190) | (Year1998_9['day'] == 203) | (Year1998_9['day'] == 273)]
SO4_Dates_98_9 = pd.to_datetime(['2/12/1998', '3/16/1998', '4/23/1998', '5/6/1998', '5/29/1998',
                              '6/2/1998', '6/9/1998', '6/24/1998', '7/9/1998', '7/22/1998',
                              '9/30/1998'])
SO4_98_9 = Concentrations_98_9.load_so4
#Year: 1999 Days: 48,119,231
Year1999_9 = Sub9[Sub9.year == 1999]
Concentrations_99_9 = Year1999_9[(Year1999_9['day'] == 48) | (Year1999_9['day'] == 119) |
        (Year1999_9['day'] == 231)]
SO4_Dates_99_9 = pd.to_datetime(['2/17/1999', '4/29/1999', '8/19/1999'])
SO4_99_9 = Concentrations_99_9.load_so4
#Year: 2000 Days: 89,115,137,152,164,180,200,259,340
Year2000_9 = Sub9[Sub9.year == 2000]
Concentrations_00_9 = Year2000_9[(Year2000_9['day'] == 89) | (Year2000_9['day'] == 115) |
        (Year2000_9['day'] == 137) | (Year2000_9['day'] == 152) | (Year2000_9['day'] == 164) |
        (Year2000_9['day'] == 180) | (Year2000_9['day'] == 200) | (Year2000_9['day'] == 259) | 
        (Year2000_9['day'] == 340)]
SO4_Dates_00_9 = pd.to_datetime(['3/29/2000', '4/24/2000', '5/16/2000', '5/31/2000', '6/12/2000',
                              '6/28/2000', '7/18/2000', '9/15/2000', '12/5/2000'])
SO4_00_9 = Concentrations_00_9.load_so4
#Year 2001 Days: 8,71,120,150,233
Year2001_9 = Sub9[Sub9.year == 2001]
Concentrations_01_9 = Year2001_9[(Year2001_9['day'] == 8) | (Year2001_9['day'] == 71) |
        (Year2001_9['day'] == 120) | (Year2001_9['day'] == 150) | (Year2001_9['day'] == 233)]
SO4_Dates_01_9 = pd.to_datetime(['1/8/2001', '3/12/2001', '4/30/2001', '5/30/2001', '8/21/2001'])
SO4_01_9 = Concentrations_01_9.load_so4
#Combine
SO4_ObservedDays_9 = SO4_Dates_96_9.union_many([SO4_Dates_97_9, SO4_Dates_98_9, SO4_Dates_99_9,
                                            SO4_Dates_00_9, SO4_Dates_01_9])
SO4_Modeled_9 = pd.concat([SO4_96_9, SO4_97_9, SO4_98_9, SO4_99_9, SO4_00_9, SO4_01_9], axis=0)
##Potassium
#Year: 1997 Day: 357
Year1997_9 = Sub9[Sub9.year == 1997]
Concentrations_97_9 = Year1997_9[(Year1997_9['day'] == 357)]
K_Dates_97_9 = pd.to_datetime([ '12/23/1997'])
K_97_9 = Concentrations_97_9.load_k
#Year: 1998 Days: 43,75,113,126,149,153,160,175,190,203,273
Year1998_9 = Sub9[Sub9.year == 1998]
Concentrations_98_9 = Year1998_9[(Year1998_9['day'] == 43) | (Year1998_9['day'] == 75) |
        (Year1998_9['day'] == 113) | (Year1998_9['day'] == 126) | (Year1998_9['day'] == 149) | 
        (Year1998_9['day'] == 153) | (Year1998_9['day'] == 160) | (Year1998_9['day'] == 175) |
        (Year1998_9['day'] == 190) | (Year1998_9['day'] == 203) | (Year1998_9['day'] == 273)]
K_Dates_98_9 = pd.to_datetime(['2/12/1998', '3/16/1998', '4/23/1998', '5/6/1998', '5/29/1998',
                              '6/2/1998', '6/9/1998', '6/24/1998', '7/9/1998', '7/22/1998',
                              '9/30/1998'])
K_98_9 = Concentrations_98_9.load_k
#Year: 1999 Days: 48,119,231
Year1999_9 = Sub9[Sub9.year == 1999]
Concentrations_99_9 = Year1999_9[(Year1999_9['day'] == 48) | (Year1999_9['day'] == 119) |
        (Year1999_9['day'] == 231)]
K_Dates_99_9 = pd.to_datetime(['2/17/1999', '4/29/1999', '8/19/1999'])
K_99_9 = Concentrations_99_9.load_k
#Year: 2000 Days: 89,115,137,152,164,180,200,235,259,340
Year2000_9 = Sub9[Sub9.year == 2000]
Concentrations_00_9 = Year2000_9[(Year2000_9['day'] == 89) | (Year2000_9['day'] == 115) |
        (Year2000_9['day'] == 137) | (Year2000_9['day'] == 152) | (Year2000_9['day'] == 164) |
        (Year2000_9['day'] == 180) | (Year2000_9['day'] == 200) | (Year2000_9['day'] == 235) |
        (Year2000_9['day'] == 259) | (Year2000_9['day'] == 340)]
K_Dates_00_9 = pd.to_datetime(['3/29/2000', '4/24/2000', '5/16/2000', '5/31/2000', '6/12/2000',
                              '6/28/2000', '7/18/2000', '8/22/2000', '9/15/2000', '12/5/2000'])
K_00_9 = Concentrations_00_9.load_k
#Year 2001 Days:  8,71,120,150,233
Year2001_9 = Sub9[Sub9.year == 2001]
Concentrations_01_9 = Year2001_9[(Year2001_9['day'] == 8) | (Year2001_9['day'] == 71) |
        (Year2001_9['day'] == 120) | (Year2001_9['day'] == 150) | (Year2001_9['day'] == 233)]
K_Dates_01_9 = pd.to_datetime(['1/8/2001', '3/12/2001', '4/30/2001', '5/30/2001', '8/21/2001'])
K_01_9 = Concentrations_01_9.load_k
#Combine
K_Modeled_9 = pd.concat([K_97_9, K_98_9, K_99_9, K_00_9, K_01_9], axis=0)
K_ObservedDays_9 = K_Dates_97_9.union_many([K_Dates_98_9, K_Dates_99_9, K_Dates_00_9, K_Dates_01_9])

####Index
SO4_Modeled_9.index = SO4_ObservedDays_9
Ca_Modeled_9.index = ObservedDays_9
Mg_Modeled_9.index = ObservedDays_9
Na_Modeled_9.index = ObservedDays_9
K_Modeled_9.index = K_ObservedDays_9


####Analyze
SO4_Residual_9 = SO4_Modeled_9 - LoadOb9SO4
Ca_Residual_9 = Ca_Modeled_9 - LoadOb9Ca
Mg_Residual_9 = Mg_Modeled_9 - LoadOb9Mg
Na_Residual_9 = Na_Modeled_9 - LoadOb9Na
K_Residual_9 = K_Modeled_9 - LoadOb9K


####Plots##############################################################################################################################
##Subarea 75########################################################################################
##SO4
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_75, SO4_Modeled_75, color='blue', label='75 Model')
#ax.scatter(Outletdates, LoadOutSO4, color='red', label='75 Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("SO4 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(SO4_Residual_75.index, SO4_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('SO4 at 75 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_75_Residual.png')

##Ca
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_75, Ca_Modeled_75, color='blue', label='Model')
#ax.scatter(Outletdates, LoadOutCa, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Ca Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Ca_Residual_75.index, Ca_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Ca at 75 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_75_Residual.png')
##Mg
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_75, Mg_Modeled_75, color='blue', label='Model')
#ax.scatter(Outletdates, LoadOutMg, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Mg Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Mg_Residual_75.index, Mg_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Mg at 75 Residual between Modeled and Observed')
##Na
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_75, Na_Modeled_75, color='blue', label='Model')
#ax.scatter(Outletdates, LoadOutNa, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Na Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Na_Residual_75.index, Na_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Na at 75 Residual between Modeled and Observed')
##K
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_75, K_Modeled_75, color='blue', label='Model')
#ax.scatter(Outletdates, LoadOutK, color='red', label='gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("K Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(K_Residual_75.index, K_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('K at 75 Residual between Modeled and Observed')
##Cl
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_75, Cl_Modeled_75, color='blue', label='Model')
#ax.scatter(Outletdates, LoadOutCl, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Cl Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Cl_Residual_75.index, Cl_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Cl at 75 Residual between Modeled and Observed')
##CO3
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(CO3_ObservedDays_75, CO3_Modeled_75, color='blue', label='Model')
#ax.scatter(Outletdates, LoadOutCO3, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("CO3 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(CO3_Residual_75.index, CO3_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Co3 at 75 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/CO3_75_Residual.png')
##HCO3
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(HCO3_ObservedDays_75, HCO3_Modeled_75, color='blue', label='Model')
#ax.scatter(Outletdates, LoadOutHCO3, color='red', label='Model')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("HCO3 75 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(HCO3_Residual_75.index, HCO3_Residual_75)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('HCO3 at 75 Residual between Modeled and Observed')

###Subarea 41######################################################################################################################
##SO4
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_41, SO4_Modeled_41, color='blue', label='Model')
#ax.scatter(Observeddates41, LoadOb41SO4, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("SO4 at 41 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(SO4_Residual_41.index, SO4_Residual_41)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('SO4 at 41 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_41_Residual.png')

##Ca
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_41, Ca_Modeled_41, color='blue', label='Model')
#ax.scatter(Observeddates41, LoadOb41Ca, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Ca 41 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Ca_Residual_41.index, Ca_Residual_41)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Ca at 41 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_41_Residual.png')
##Mg
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_41, Mg_Modeled_41, color='blue', label='Model')
#ax.scatter(Observeddates41, LoadOb41Mg, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Mg 41 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Mg_Residual_41.index, Mg_Residual_41)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Mg at 41 Residual between Modeled and Observed')
##Na
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_41, Na_Modeled_41, color='blue', label='Model')
#ax.scatter(Observeddates41, LoadOb41Na, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Na 41 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Na_Residual_41.index, Na_Residual_41)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Na at 41 Residual between Modeled and Observed')
##K
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_41, K_Modeled_41, color='blue', label='Model')
#ax.scatter(Observeddates41, LoadOb41K, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("K 41 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(K_Residual_41.index, K_Residual_41)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('K at 41 Residual between Modeled and Observed')
##Cl
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_41, Cl_Modeled_41, color='blue', label='Model')
#ax.scatter(Observeddates41, LoadOb41Cl, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Cl 41 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Cl_Residual_41.index, Cl_Residual_41)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Cl at 41 Residual between Modeled and Observed')

###Subarea 12################################################################################################################################
##SO4
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_12, SO4_Modeled_12, color='blue', label='Model')
#ax.scatter(Observeddates12, LoadOb12SO4, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("SO4 12 Annual Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(SO4_Residual_12.index, SO4_Residual_12)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('SO4 at 12 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_12_Residual.png')

##Ca
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_12, Ca_Modeled_12, color='blue', label='Model')
#ax.scatter(Observeddates12, LoadOb12Ca, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Ca 12 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Ca_Residual_12.index, Ca_Residual_12)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Ca at 12 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_12_Residual.png')
##Mg
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_12, Mg_Modeled_12, color='blue', label='Model')
#ax.scatter(Observeddates12, LoadOb12Mg, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Mg 12 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Mg_Residual_12.index, Mg_Residual_12)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Mg at 12 Residual between Modeled and Observed')
##Na
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_12, Na_Modeled_12, color='blue', label='Model')
#ax.scatter(Observeddates12, LoadOb12Na, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Na 12 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Na_Residual_12.index, Na_Residual_12)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Na at 12 Residual between Modeled and Observed')
##K
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(K_ObservedDays_12, K_Modeled_12, color='blue', label='Model')
#ax.scatter(Observeddates12, LoadOb12K, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("K 12 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(K_Residual_12.index, K_Residual_12)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('K at 12 Residual between Modeled and Observed')
##Cl
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(Cl_ObservedDays_12, Cl_Modeled_12, color='blue', label='Model')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Cl Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Cl_Residual_12.index, Cl_Residual_12)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Cl at 12 Residual between Modeled and Observed')
##HCO3
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(HCO3_ObservedDays_12, HCO3_Modeled_12, color='blue', label='Model')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("HCO3 12 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(HCO3_Residual_12.index, HCO3_Residual_12)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('HCO3 at 12 Residual between Modeled and Observed')

###Subarea 9#############################################################################################################
##Ca
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_9, Ca_Modeled_9, color='blue', label='Model')
#ax.scatter(Observeddates9, LoadOb9Ca, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Ca 9 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Ca_Residual_9.index, Ca_Residual_9)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Ca at 9 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/Ca_9_Residual.png')
##Mg
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_9, Mg_Modeled_9, color='blue', label='Model')
#ax.scatter(Observeddates9, LoadOb9Mg, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Mg 9 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Mg_Residual_9.index, Mg_Residual_9)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Mg at 9 Residual between Modeled and Observed')
##Na
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(ObservedDays_9, Na_Modeled_9, color='blue', label='Model')
#ax.scatter(Observeddates9, LoadOb9Na, color='red', label='Ggae')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("Na Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(Na_Residual_9.index, Na_Residual_9)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('Na at 9 Residual between Modeled and Observed')
##SO4
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(SO4_ObservedDays_9, SO4_Modeled_9, color='blue', label='Model')
#ax.scatter(Observeddates9, LoadOb9SO4, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("SO4 9 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(SO4_Residual_9.index, SO4_Residual_9)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('SO4 at 9 Residual between Modeled and Observed')
fig.savefig('C:/Users/Lizmot34/Desktop/FinishedFigures/SO4_9_Residual.png')

##K
#fig, ax = plt.subplots(figsize=(5, 2.7), constrained_layout=True)
#ax.scatter(K_ObservedDays_9, K_Modeled_9, color='blue', label='Model')
#ax.scatter(Observeddates9, LoadOb9K, color='red', label='Gage')
#ax.set_xlabel('Time')
#ax.set_ylabel('Loading [kg/d]')
#ax.set_title("K 9 Observed Loading")
#ax.legend()
fig, ax = plt.subplots(figsize=(7,4), constrained_layout=True)
ax.scatter(K_Residual_9.index, K_Residual_9)
ax.set_xlabel('Time')
ax.set_ylabel('Residual')
ax.set_title('K at 9 Residual between Modeled and Observed')