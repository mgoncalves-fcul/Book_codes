# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 19:13:35 2021

@author: Mario
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
''' Keeling Curve '''

data = pd.read_csv('monthly_in_situ_co2_mlo.csv', header = None, skiprows=64)
curve = np.asarray(data[[3,4]])
curve[:,1] = np.where(curve[:,1]==-99.99, np.nan, curve[:,1])

plt.plot(curve[:,0], curve[:,1],'-')
plt.xlabel('Year')
plt.ylabel(r'CO$_2$ (ppm)')
plt.grid(axis='both')
plt.savefig("keeling.jpg", dpi=600, format="jpg", bbox_inches="tight")

#%%
''' Ice-core EPICA DOME C and Vostok delta18O'''
# EPICA DOME C data starts at 100 kyr and Vostok goes from 0 to 400 kyr

delta18 = pd.read_csv('DomeC_d18O.tab', header=None, skiprows=18, sep='\t')
delta18_v = pd.read_table('o18nat_vostok.txt', header=None, skiprows=155,\
                          skipinitialspace=True, sep='\t', encoding='latin-1')
d18O = np.asarray(delta18[[1,2]])
n = np.where(delta18_v[0] < 100000)
d18O_v = np.asarray(delta18_v)
d18O_v = d18O_v[n]
fig, ax = plt.subplots()
ax.plot(d18O[:,0], d18O[:,1],'-')
ax.plot(d18O_v[:,0]*1e-3, d18O_v[:,1], '#1f77b4')
ax.set_xlabel('Time (ka)')
ax.set_ylabel(u'$\delta^{18}$O ‰')
#plt.xlim(0, plt.xlim()[1])  # second limit set to maximum of data
ax.invert_xaxis()
ax.grid(axis='both')

#%%
''' delta H and Temperature'''

deltaH = pd.read_table('edc3deuttemp2007.txt', header=None, skiprows=104, \
                     skipinitialspace=True, sep=' ', encoding='latin-1')
dD = np.asarray(deltaH[[2,3,4]])

# plt.figure()
# plt.plot(dD[:,0]*1e-3, dD[:,1],'-')

fig,(ax1, ax2) = plt.subplots(2,1)

ax1.plot(dD[:,0]*1e-3, dD[:,1])
# ax1.set_xlabel('Time (years)')
ax1.set_ylabel(u'$\delta$D ‰')
ax1.invert_xaxis()
ax1.grid()

ax2.plot(dD[:,0]*1e-3, dD[:,2])
ax2.set_xlabel('Time (ka)')
ax2.set_ylabel('Temperature')
ax2.invert_xaxis()
ax2.grid()

#%%
''' CO2 in EPICA DOME C'''

CO2_Epica = pd.read_excel('antarctica2015co2.xlsx', sheet_name='CO2 Composite',\
                          header=None, skiprows=15)
Curve_CO2 = np.asarray(CO2_Epica[[0,1]])
fig, ax = plt.subplots()
ax.plot(Curve_CO2[:,0]*1e-3, Curve_CO2[:,1], '-')
ax.set_xlabel('Time (ka)')
ax.set_ylabel(r'CO$_{2}$ (ppm)')
ax.invert_xaxis()
ax.grid()

#%%
''' Methane in EPICA DOME C'''

CH4_Epica = pd.read_table('edc-ch4-2008.txt', header=None, skiprows=154, \
                     skipinitialspace=True, sep=' ', encoding='latin-1')
Curve_CH4 = np.asarray(CH4_Epica[[1,2]])
fig, ax = plt.subplots()
ax.plot(Curve_CH4[:,0]*1e-3, Curve_CH4[:,1], '-')
ax.set_xlabel('Time (ka)')
ax.set_ylabel(r'CH$_{4}$ (ppbv)')
ax.invert_xaxis()
ax.grid()

#%%

''' Composite plot'''

fig, ax = plt.subplots(4,1, sharex=True, figsize=(10, 8))
fig.subplots_adjust(hspace=0)

ax[0].plot(Curve_CO2[:,0]*1e-3, Curve_CO2[:,1])
ax[0].set_ylabel(r'CO$_2$ (ppmv)')
# start, end = ax[0].get_ylim()
# ax[0].yaxis.set_ticks(np.arange(start, end, 50))
ax[0].grid()

ax2 = ax[1].twinx()
ax2.plot(Curve_CH4[:,0]*1e-3, Curve_CH4[:,1])
# start, end = ax2.get_ylim()
# ax2.yaxis.set_ticks(np.arange(start, end, 100))
ax[1].set_yticklabels([])
ax2.set_ylabel(r'CH$_4$ (ppbv)')
ax2.grid()
ax[1].grid(axis='x')

ax[2].plot(d18O[:,0], d18O[:,1])
ax[2].plot(d18O_v[:,0]*1e-3, d18O_v[:,1], '#1f77b4')
ax[2].set_ylabel(u'$\delta^{18}$O (‰)')
ax[2].grid()

ax2 = ax[3].twinx()
ax2.plot(dD[:,0]*1e-3, dD[:,1])
ax[3].set_yticklabels([])
ax[3].set_xlabel('Time (ka)')
ax[3].invert_xaxis()
ax2.set_ylabel(u'$\delta$D (‰)')
ax2.grid(axis='both')
ax[3].grid(axis='x')

plt.savefig("ice_cores.jpg", dpi=600, format="jpg", bbox_inches="tight")