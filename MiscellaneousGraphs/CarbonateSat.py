# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 22:55:36 2021

@author: Mario
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('CaCO3_sat.xlsx', header = None, skiprows=1)
dados = np.asarray(data)

plt.plot(dados[:,1], dados[:,0], dados[:,2], dados[:,0], dados[:,3], dados[:,0])
plt.gca().invert_yaxis()
plt.xlabel('Concentration (mmol/kg)')
plt.ylabel('Depth (m)')
plt.legend(['Calcite', 'Aragonite', r'CO$_3^{2-}$'])
plt.grid(axis='both')
