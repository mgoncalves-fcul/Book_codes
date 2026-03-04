# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:52:19 2023

@author: Mario
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

import os	
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%

data = pd.read_csv('annual-co-emissions-by-region.csv', usecols=list(range(4)))
emissions = pd.read_excel('C_Emissions.xlsx', skiprows=2, usecols='A:C')
emissions = emissions.drop(0)

data.columns = ['Entity', 'Code', 'Year','Annual CO2']

world = data[data['Entity'] == 'World']

world.plot(x = 'Year', y = 'Annual CO2')

fig, ax = plt.subplots(figsize=(8,5))

world = world[world['Year']>=1959]

#plot_data2 = np.log10(world['Annual CO2'].cumsum()*1e-9)
plot_data2 = np.log10(emissions['Rate'].cumsum())

ax.plot(world['Year'], plot_data2, 'o')

def func(x, a, b, c):
    return a * x**b + c

def func2(x, a, b):
    return np.log10(x**a) + b

year = world['Year'].to_numpy()
x1 = np.arange(len(year))
x2 = np.arange(2,len(year))
y = plot_data2.to_numpy()

popt, pcov = curve_fit(func, x1, y)
popt2, pcov2 = curve_fit(func2, x2, y[2:])

# plt.plot(year, func(x, *popt), 'r-',\
#           label='fit: b=%5.3f, c=%5.3f' % tuple(popt))

x = np.arange(1959, 2700)
x1 = np.arange(len(x))
x2 = np.arange(2, len(x))
y1 = func(x1, *popt)
y2 = func2(x2, *popt2)

# ax.plot(x1, y1, 'r--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
ax.plot(x, y1, 'r--', label='model: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
ax.plot(x[2:], y2, 'g--', label='model: a=%5.3f, b=%5.3f' % tuple(popt2))
ax.legend()

# Limite mínimo e máximo do PETM Pg de C
y_min = np.log10(3000)
y_max = np.log10(7126)

ax.hlines(y=y_min, xmin=x[0], xmax=x[-1], color='k', ls='--')
ax.hlines(y=y_max, xmin=x[0], xmax=x[-1], color='k', ls='--')
ax.fill_between([x[0], x[-1]], [y_max, y_max], [y_min, y_min], alpha=0.3)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel(r'$\log_{10}$ Total Emissions (Pg C)', fontsize=14)
ax.grid()

plt.savefig("carbon_emissions.jpg", dpi=600, format="jpg", bbox_inches="tight")
plt.close()
