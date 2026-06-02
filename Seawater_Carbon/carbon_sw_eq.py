# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:34:49 2018

@author: Mario
"""

import numpy as np


# Constants for the equilibrium of the carbonate system in seawater
# Salinity 35 permil
# Temp 25
K0 = 10**-1.5468
K1 = 1.4626e-06
K2 = 1.1082e-09
Kw = 6.0628e-14
KB = 2.5266e-09
BT = 4.160e-04
# Values of pCO2 and Alk (can be changed)
pCO2 = 418   # ppm
Alk = 2300   # umol/kg



def carb_pH( pCO2, Alk ):
    H0 = 10**-8.2
    H = newton(H0, 1e-12, 30, alkalinity, pCO2, Alk)
    pH = -np.log10(H)
    return pH


def newton( y0, tol, n, f, *args ):
    '''
    Solver for non-linear equations by the Newton-Raphson method
    y0 - initial estimate
    tol - tolerance of the solution
    n - maximum number of iterations
    f - name of the non-linear function to solve
    *args - variable arguments (pCO2 and Alk)
    '''
    dif = tol*10
    i = 0
    while dif > tol and i < n:
        y = y0 - f(y0, *args)/derivative(y0,f, *args);
        dif = np.abs(y - y0)
        y0 = y
        i = i+1
    return y

def derivative( y,f, *args ):
    '''
    Function to calculate the numerical derivative of function f
    using the central finite diference
    '''
    delta = 1e-5*y
    dy = (f(y+delta, *args) - f(y-delta, *args))/(2*delta)
    return dy

def alkalinity( H, *args ):
    '''
    Equation of the alkalinity of the system, knowing pCO2 and Alk
    to calculate the pH of the solution
    '''
    pCO2 = args[0] * 1e-6
    Alk = args[1] * 1e-6
    y = pCO2*K0*K1/H + 2*pCO2*K0*K1*K2/H**2 + Kw/H - H + KB*BT/(KB + H) - Alk
    return y

pH = carb_pH(pCO2, Alk)  # call main function with pCO2 and Alk

# Calculate H+ and carbonate species concentration
H = 10**-pH
HCO3 = pCO2*K0*K1/H
CO32 = pCO2*K0*K1*K2/H**2
H2CO3 = pCO2*K0
DIC = HCO3 + CO32 + H2CO3

# Display the results
print('Distribution of carbon species (T = 25ºC and salinity = 35 permil):')
print('H2CO3: %3.0f umol/kg' % H2CO3)
print('HCO3: %3.0f umol/kg' % HCO3)
print('CO3: %3.0f umol/kg' % CO32)
print('DIC: %4.0f umol/kg' % DIC)
print('pH: %1.2f' % pH)
