# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:21:19 2020

@author: Mario
"""

import numpy as np

def constants (S, T):
    
    '''
        Compute the equilibrium constants of CO2, H2O,
        B(OH)3 and total concentration of boron as a function of
        salinity (S, in permil) and temperature (T, in ºC).
        
        Equilibrium constants shown as exponential and pK format
     
        Use: constants(S, T)
     
        Example: constants(35, 25) or constants(30, 5)
     
     
    '''
    TK = 273.15 + T
    lnK0 = 9345.17/TK - 60.2409 + 23.3585 * np.log(TK/100) + S *\
        (0.023517 - 0.00023656 * TK + 0.0047036 * (TK/100)**2)
    K0 = np.exp(lnK0)
    pK0 = -np.log10(K0)

    pK1 = -62.008 + 3670/TK + 9.7944 * np.log(TK) - 0.0118 * S + 0.000116 * S**2
    K1 = 10**(-pK1)
    
    pK2 = 4.777 + 1394.7/TK - 0.0184 * S + 0.000118 * S**2
    K2 = 10**(-pK2)
    
    lnKw = 148.96502 - 13847.26/TK - 23.6521 * np.log(TK) +  S**(1/2) *\
        (-5.977 + 118.67/TK + 1.0495 * np.log(TK)) - 0.01615 * S
    Kw = np.exp(lnKw)
    pKw = -np.log10(Kw)
    
    lnKb = 1/TK * (-8966.9 - 2890.53 * S**(0.5) - 77.942 * S + 1.728 * S**(1.5) -\
                   0.0996 * S**2) + 148.0248 + 137.1942 * S**(0.5) + 1.62142 *\
        S + 0.053105 * S**(0.5) * TK + np.log(TK) * \
            (-24.4344 - 25.085 * S**(0.5) - 0.2474 * S)
    Kb = np.exp(lnKb)
    pKb = -np.log10(Kb)
    
    T_Boron = 4.16e-4 * S/35   # in moles/kg of solution
    
    #   print the results

    print('')
    print('Results for %i ºC and %2.1f permil' % (T, S))
    print('')
    print('Dissolution of CO2: K0 = %1.4e; pK0 = %2.2f' % (K0, pK0))
    print('Dissociation of CO2: K1 = %1.4e; pK1 = %2.2f' % (K1, pK1))
    print('                   : K2 = %1.4e; pK2 = %2.2f' % (K2, pK2))
    print('Dissociation of water: Kw = %1.4e; pKw = %2.2f' % (Kw, pKw))
    print('Dissociation of boric acid: Kb = %1.4e; pKb = %2.2f' % (Kb, pKb))
    print('Total concentration of boron: %1.3e moles/kg' % (T_Boron))
    return K1, K2, Kw, Kb, T_Boron