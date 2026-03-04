# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:25:02 2023

@author: Mario
"""

import matplotlib.pyplot as plt
import pandas as pd

import os	
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%
#Read the data
dados = pd.read_excel('CO2Consumption.xlsx', skiprows=3, usecols='A:C')

#%%

#Create Figure
fig, ax = plt.subplots(figsize=(10, 6))
#Draw vertical dashed line from the first observation of 2005
ax.vlines(x=dados['CO2'][0], ymax=dados['D O2'][0], ymin = -225,\
           lw = 2, linestyle='--', color = 'k')

# Plot data
dados.plot(ax=ax, x='CO2', y='D O2', kind='scatter', grid='on')

# Read data and plot the stoichiometric line of the fossil fuel emissions
rectaFFuel = pd.read_excel('CO2Consumption.xlsx', skiprows=3, usecols='G:H')
rectaFFuel.plot(ax=ax, x='CO2.1', y='D O2.1', style='-o', color='c',\
                alpha=0.6, legend=False, markersize=4)

# Read data and plot the stoichiometric line of the land use change emissions
rectaLUC = pd.read_excel('CO2Consumption.xlsx', skiprows=3, usecols='J:K')
rectaLUC.plot(ax=ax, x='CO2.2', y='D O2.2', color='m', legend=False)

# Read data and plot the stoichiometric line of ocean absorption
# Blue horizontal line
rectaO = pd.read_excel('CO2Consumption.xlsx', skiprows=3, usecols='M:N')
rectaO.plot(ax=ax, x='CO2.3', y='D O2.3', style='-', color='b', grid='on', legend=False)
# Trace the vertical dashed line on the right
ax.vlines(x=rectaO['CO2.3'][0], ymax=rectaO['D O2.3'][0], ymin = -225,\
           lw = 2, linestyle='--', color = 'k')

    
# Read data and plot the stoichiometric line of absorption by the biosphere
# Green oblique line
rectaB = pd.read_excel('CO2Consumption.xlsx', skiprows=3, usecols='P:Q')
rectaB.plot(ax=ax, x='CO2.4', y='D O2.4', style='-', color='g', grid='on', legend=False)

# Trace the vertical dashed line between the ocean and the biosphere
ax.vlines(x=rectaB['CO2.4'][0], ymax=rectaB['D O2.4'][0], ymin = -225,\
           lw = 2, linestyle='--', color = 'k')

# Trace the vertical dashed line to the left of the biosphere
ax.vlines(x=rectaB['CO2.4'][1], ymax=rectaB['D O2.4'][1], ymin = -225,\
           lw = 2, linestyle='--', color = 'k')

# Trace the horizontal and vertical green lines of the CO2 and O2 components
# of the absorption by the biosphere
ax.vlines(x=rectaB['CO2.4'][1], ymax=rectaB['D O2.4'][1], ymin = rectaB['D O2.4'][0],\
           lw = 2, linestyle='-', color = 'g')
ax.hlines(y=rectaB['D O2.4'][0], xmax=rectaB['CO2.4'][0], xmin = rectaB['CO2.4'][1],\
           lw = 2, linestyle='-', color = 'g')
# Trace the horizontal dashed line of the maximum consumption of O2
ax.hlines(y=rectaB['D O2.4'][0], xmax=rectaB['CO2.4'][1], xmin = 360,\
           lw = 2, linestyle='--', color = 'k')

# Trace the horizontal dashed line of the final point of the absorption by the biosphere
ax.hlines(y=rectaB['D O2.4'][1], xmax=rectaB['CO2.4'][1], xmin = 360,\
           lw = 2, linestyle='--', color = 'k')
# Trace the horizontal dashed line of the last point of the observations in 2020
ax.hlines(y=dados['D O2'][len(dados)-1], xmax=dados['CO2'][len(dados)-1], xmin = 360,\
           lw = 2, linestyle='--', color = 'k')


# Filling of the areas
# Absoprtion by the Ocean
ax.fill_between(rectaO['CO2.3'][:2], rectaO['D O2.3'][:2], [-225, -225],\
                alpha=0.3)
y1 = [rectaB['D O2.4'][0], rectaB['D O2.4'][0]]

# Absorption by the Biosphere
ax.fill_between(rectaB['CO2.4'][:2], y1, [-225, -225],\
                alpha=0.3)
x = [360, rectaB['CO2.4'][1]]
y1 = [rectaB['D O2.4'][1], rectaB['D O2.4'][1]]
y2 = [rectaB['D O2.4'][0], rectaB['D O2.4'][0]]

# O2 emission by the Biosphere
ax.fill_between(x, y1, y2,\
                alpha=0.3)
x = [360, dados['CO2'][len(dados)-1]]
y1 = [dados['D O2'][len(dados)-1], dados['D O2'][len(dados)-1]]
y2 = [rectaB['D O2.4'][1], rectaB['D O2.4'][1]]

# O2 emission by the Ocean
ax.fill_between(x, y1, y2,\
                alpha=0.3)

ax.set_xlabel(r'CO$_2$ Mole Fraction (ppm)')
ax.set_ylabel(r'Deviation of O$_2$ Mole Fraction (ppm)')
ax.set_xlim([360, 480])
ax.set_ylim([-225, -45])

plt.savefig('AnthropogenicEmissions.png', dpi=600)
plt.savefig('AnthropogenicEmissions.eps', dpi=600)
