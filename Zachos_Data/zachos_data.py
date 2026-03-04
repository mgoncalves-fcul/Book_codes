# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:25:21 2024

@author: Mario
"""

import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')

import os	
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

data = pd.read_table('Zachos_2008.txt')
columns = data.columns

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(data[columns[0]]/1000, data[columns[2]], 'o')
plt.gca().invert_xaxis()
ax.set_xlabel('Age [Ma]')
ax.set_ylabel(r'$\delta^{13}$C [$^o/_{oo}$]')
#ax.set_title(r'$\delta^{13}$C data from Zachos et al. (2008)')
plt.savefig("zachos_data.jpg", dpi=600, format="jpg", bbox_inches="tight")