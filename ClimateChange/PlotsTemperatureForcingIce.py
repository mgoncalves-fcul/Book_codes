# -*- coding: utf-8 -*-
"""
Created on Fri May 12 18:28:02 2023

@author: Mario
"""

import matplotlib.pyplot as plt
import pandas as pd

import os	
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%  Temperature Anomaly 1850 - 2022 NASA-GISS

temperatures = pd.read_csv("TemperatureNASA.txt", skiprows=3, sep='\s+')
temperatures = temperatures.drop(0)
temperatures.columns=['Year', 'Temp', 'Temp_smooth']

y1 = temperatures['Temp']
y2 = temperatures['Temp_smooth']
x = temperatures['Year'].astype('int')

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y1, '-o', x, y2, '-', markersize=4)
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly')
start = x.min()
end = x.max()
years = list(range(start, end, 20))
ax.set_xticks(years)
ax.legend(('Temperature data', 'Lowess Smoothing'))
fig.savefig("temperature_anomaly.jpg", dpi=600, format="jpg", bbox_inches="tight")

#%% Influence of natural and human factors
# Historical data + Miller et al (2021) model

factors = pd.read_csv("ERFs_SSP245_MillerFig10_2021.txt", skiprows=6,\
                       header=None, delim_whitespace=True)
factors.columns = ['Year', 'Combined', 'Greenhouse Gases', 'GHG (Smooth)',\
                    'Aerosols', 'Aerosols (Smooth)', 'Natural']

factors.plot(x='Year', y=['Combined', 'Greenhouse Gases', 'GHG (Smooth)',\
                    'Aerosols', 'Aerosols (Smooth)', 'Natural'],\
              ylabel=r'Efective Radiative Forcing (W/m$^2$)', figsize=(10,6))

plt.savefig("Radiatve_forcing.jpg", dpi=600, format="jpg", bbox_inches="tight")
    
#%%  Mass of ice loss in Antarctic and Greenland

ice_antarctica = pd.read_csv("antarctica_mass_200204_202302.txt", skiprows=31,\
                             header=None, delim_whitespace=True)
ice_antarctica.columns = ['Year', 'Mass Diff', 'Sigma']
x = ice_antarctica['Year'].to_numpy()
y = ice_antarctica['Mass Diff'].to_numpy()
erro = ice_antarctica['Sigma'].to_numpy()
fig, ax = plt.subplots(2,1, sharex=True, figsize=(10,8))
ice_antarctica.plot(ax=ax[0], x='Year', y='Mass Diff', legend=False,\
                    ylabel='Mass Antarctica (Gt)', grid=True)
ax[0].fill_between(x, y-2*erro, y+2*erro, alpha=0.35, color='g')

ice_greenland = pd.read_csv("greenland_mass_200204_202302.txt", skiprows=31,\
                             header=None, delim_whitespace=True)
ice_greenland.columns = ['Year', 'Mass Diff', 'Sigma']
x = ice_greenland['Year'].to_numpy()
y = ice_greenland['Mass Diff'].to_numpy()
erro = ice_greenland['Sigma'].to_numpy()
ice_greenland.plot(ax=ax[1], x='Year', y='Mass Diff', legend=False, xlabel = 'Year',\
                   ylabel='Mass Greenland (Gt)', grid=True)
ax[1].fill_between(x, y-2*erro, y+2*erro, alpha=0.35, color='g')

plt.savefig("ice_loss.jpg", dpi=600, format="jpg", bbox_inches="tight")
