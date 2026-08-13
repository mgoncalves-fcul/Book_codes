# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:01:51 2020

@author: Mario
"""

import numpy as np

def constants_P (S, T, P):
    
    '''
    Compute the equilibrium constants of CO2, H2O,
    B(OH)3, and solubility product of calcite and aragonite as a
    function of salinity (S, in permil), temperature (T, in ºC)
    and pressure (P, in bar). P = 0 gives the constants at the
    ocean surface
 
    Use: constants_P(S, T, P)
 
    Example: constants_P(35, 25, 0) or constants_P(30, 5, 900)
    '''

    TK = 273.15 + T
    
    pK1 = -62.008 + 3670/TK + 9.7944 * np.log(TK) - 0.0118 * S + 0.000116 * S**2
    K1 = 10**(-pK1)
    
    pK2 = 4.777 + 1394.7/TK - 0.0184 * S + 0.000118 * S**2
    K2 = 10**(-pK2)
    
    lnKw = 148.96502 - 13847.26/TK - 23.6521 * np.log(TK) +  S**(1/2) * \
        (-5.977 + 118.67/TK + 1.0495 * np.log(TK)) - 0.01615 * S
    Kw = np.exp(lnKw)
    
    lnKb = 1/TK * (-8966.9 - 2890.53 * S**(0.5) - 77.942 * S + 1.728 * S**(1.5) -\
                   0.0996 * S**2) + 148.0248 + 137.1942 * S**(0.5) + 1.62142 *\
        S + 0.053105 * S**(0.5) * TK + np.log(TK) *\
            (-24.4344 - 25.085 * S**(0.5) - 0.2474 * S)
    Kb = np.exp(lnKb)

    logKsp_c = -171.9065 - 0.077993 * TK + 2839.319/TK + 71.595 * np.log10(TK) +\
        (-0.77712 + 0.0028426 * TK + 178.34/TK) * S**(1/2) - 0.07711 * S +\
            0.0041249 * S**(1.5)
    Ksp_c = 10**(logKsp_c)

    logKsp_a = -171.945 - 0.077993 * TK + 2903.293/TK + 71.595 * np.log10(TK) +\
        (-0.068393 + 0.0017276 * TK + 88.135/TK) * S**(1/2) - 0.10018 * S +\
            0.0059415 * S**(1.5)
    Ksp_a = 10**(logKsp_a)


    K = np.array([K1, K2, Kw, Kb, Ksp_c, Ksp_a])
    
    if P != 0:       #  Constants correction for pressure
        R = 83.131      # perfect gases constant - cm3⋅bar/(mol⋅K)
        a0 = (-1) * np.array([25.50, 15.82, 25.60, 29.48, 48.76, 46.00])
        a1 = np.array([0.1271, -0.0219, 0.2324, 0.1622, 0.5304, 0.5304])
        a2 = 1e-3 * np.array([0.0, 0.0, -3.6246, 2.6080, 0.0, 0.0])
        b0 = -1e-3 * np.array([3.08, -1.13, 5.13, 2.84, 11.76, 11.76])
        b1 = 1e-3 * np.array([0.0877, -0.1475, 0.0794, 0.0, 0.3962, 0.3962])
        DeltaV = a0 + a1 * T + a2 * T**2
        Deltak = b0 + b1 * T
        lnK_P = np.log(K) - DeltaV/(R*TK)*P + 0.5*Deltak/(R*TK) * P**2
        K_P = np.exp(lnK_P)
        pK_P = -np.log10(K_P)
    else:
        K_P = K
        pK_P = -np.log10(K_P)

    #   Print the results
    
    print('')
    print('Results for %i ºC, %2.1f permil e %4.1f bar:' % (T, S, P))
    print('')
    print('Dissociation of CO2: K1 = %1.4e; pK1 = %2.2f' % (K_P[0], pK_P[0]))
    print('                   : K2 = %1.4e; pK2 = %2.2f' % (K_P[1], pK_P[1]))
    print('Dissociation of water: Kw = %1.4e; pKw = %2.2f' % (K_P[2], pK_P[2]))
    print('Dissociation of boric acid: Kb = %1.4e; pKb = %2.2f' % (K_P[3], pK_P[3]))
    print('Calcite solubility constant: Ksp_c = %1.4e; pKsp_c = %2.2f' % (K_P[4], pK_P[4]))
    print('Aragonite solubility constant: Ksp_a = %1.4e; pKsp_a = %2.2f' % (K_P[5], pK_P[5]))
    return K_P

