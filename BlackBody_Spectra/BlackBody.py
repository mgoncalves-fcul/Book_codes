# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:58:00 2023

@author: Mario
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants: c - light speed; h - Plank; k - Boltzmann
#const = (3e8, 6.62e-34, 1.38e-23)  # Constants: (c, h, k)
c = 299792458;
h = 6.62606957e-34
kB = 1.3806488e-23


def funcPlankl(T, wvl):
    term1 = 2 * h * c**2 / wvl**5 
    pot = h * c / ( wvl * kB * T)
    term2 =  np.exp(pot) - 1
    spectra = term1 * 1 / term2
    return spectra

def funcPlankn(T, wvn):
    '''
    function with wavenumber in cm-1
    '''
    term1 = 2e8 * h * c**2 * wvn**3 
    pot = 100 * h * c * wvn / (kB * T)
    term2 =  np.exp(pot) - 1
    spectra = term1 * 1 / term2
    return spectra


def plotSpectra(T, wvl, wvn):
    fig, ax = plt.subplots(figsize=(10, 6))
    #ax.invert_xaxis()
    if hasattr(T, "__len__"):
        for k in T:
            y = funcPlankl(k, wvl)
            y2 = funcPlankn(k, wvn)
            #ax[0].semilogx(wvl, y, 'k--')
            ax.plot(wvn, y2, '--', label=str(k) + ' K')
            ax.set_xlabel(r'Wavenumber in cm$^{-1}$', fontsize=14)
            ax.set_ylabel(r'Radiance (W m$^{-2}$ sr$^{-1}$ (cm$^{-1}$)$^{-1}$)',\
                          fontsize=14)
            ax.legend()
            secax = ax.secondary_xaxis('top', functions=(wvl2wvn, wvn2wvl))
            secax.set_xticks(np.array([7, 8, 10, 15, 20, 25]))
            secax.set_xlabel(r'Wavelength ($\mu$m)', fontsize=12)
    else:
        y = funcPlankn(T, wvn)
        ax.plot(wvn, y, 'k--')
    return ax, fig

def wvl2wvn(x):
    "\mu m to cm-1"
    return 1 / (x * 1e2) * 1e6

def wvn2wvl(x):
    "cm-1 to \mu m"
    return 1 / (x * 1e2) * 1e6

## Call functions
# Data

T = np.arange(220, 340, 20)   # in kelvin
#T = 300
wavelen = np.linspace(6.25, 25, 10000) * 1e-6 # Wavelengths in meters

wavenumb = 1 / (wavelen * 100) # in cm-1
#wavenumb = 1e2 /wavelen # in cm-1
#T = 310
# y = funcPlank(T, lamb)
# fig,ax = plt.subplots()
# ax.semilogx(lamb,y)
#ax.invert_xaxis()

ax, fig = plotSpectra(T, wavelen, wavenumb)

#%%

import pandas as pd

import os	
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%

rad400 = pd.read_excel("RadianceAtmosphere400ppm.xlsx").to_numpy()
rad1000 = pd.read_excel("RadianceAtmosphere1000ppm.xlsx").to_numpy()

rad400[:,1] = rad400[:,1] * 1e4
rad1000[:,1] = rad1000[:,1] * 1e4

#fig, ax = plt.subplots()
ax.plot(rad400[:,0], rad400[:,1], '-b', label = r'400 ppm CO$_2$')
ax.plot(rad1000[:,0], rad1000[:,1], '-r', label = r'1000 ppm CO$_2$')
ax.legend()
fig.savefig("spectra.jpg", dpi=600, format="jpg", bbox_inches="tight")