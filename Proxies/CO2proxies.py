# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:09:39 2023

@author: Mario
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd

import os	
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

data = pd.read_csv("age_co2_plot_data.csv", usecols=list(range(1,10)))

# Convert ages and uncertainties from ka to Ma
data[['age', 'age_uncertainty_older', 'age_uncertainty_younger']] =\
    data[['age', 'age_uncertainty_older', 'age_uncertainty_younger']]/1e3

data = data.drop(labels='doi', axis=1)

data.columns = ['Name_site', 'Proxy', 'Age', 'Age_uncert_inf',\
                 'Age_uncert_sup', 'CO2', 'CO2_uncert_sup', 'CO2_uncert_inf']

#Descriptive statistics

estatistica = data.groupby('Proxy')[['Age', 'CO2']].describe()

estatistica.to_excel("desc_statistics.xlsx")

data.to_excel('data_co2.xlsx')

# Example Boron Proxy

plot_data = data[data['Proxy'] == 'Boron Proxies']

yerror = plot_data[['CO2_uncert_inf', 'CO2_uncert_sup']].to_numpy().T

plot_data.plot(x = 'Age', y = 'CO2', kind='scatter', yerr=yerror,\
               ylabel=r'CO$_2$ (ppm)', xlabel='Age (Ma)', label='Boron Proxies', \
               figsize=(8, 5))
plt.gca().invert_xaxis()
plt.savefig("boron.jpg", dpi=600, format="jpg", bbox_inches="tight")

#%%Complementary

# Extract the unique labels of each proxy into a list
proxies = list(data['Proxy'].unique())
label_proxy = ['Stomata', 'Phytoplankton', 'Leafs', 'Paleosols', 'Boron',\
               'Liverworts', r'$\delta^{13}$C Plants', 'Nacolite']
# Print the options (starting in 1. - sum 1)
print('Choose one or more of the following proxies:')
print('Example: 2 (if you choose proxy 2 from the list)')
print('         1 3 4 (if you choose more than one proxy, separated by a space)')
for i, k in enumerate(proxies):
    print(str(i+1) + '. ' + k)

op = list(input('>> ').split())   # separates each string of the input using spaces
op = [int(i)-1 for i in op]   # converts each string of the input to an integer
                              # subtracts 1 to match the indexes of the list

fig, ax = plt.subplots()

for i in op:    # scans each of the options
    plot_data = data[data['Proxy'] == proxies[i]] # extract proxy i data
    yerror = plot_data[['CO2_uncert_inf', 'CO2_uncert_sup']].to_numpy().T # error bars
    # Plot kind=plot (default) to assume each instruction as a different series
    # and attribute a distinct color; use linestyle='none' and define the
    # marker; doesn't work with kind='scatter'
    plot_data.plot(x = 'Age', y = 'CO2', marker='.', ms=10, linestyle='none',\
                   yerr=yerror, ax=ax, ylabel=r'CO$_2$ (ppm)',\
                   xlabel='Age (Ma)', label=label_proxy[i], figsize=(8, 5))
    
    # Alternative instructions using the scatter method from matplotlib:
    # x = plot_data['Age']
    # y = plot_data['CO2']
    # ax.scatter(x, y, s = 20, label=proxies[i])
    # ax.errorbar(x, y, yerr=yerror, fmt='o', markersize=1)
    # ax.legend()
    
    # Write data in the csv file with the name of the proxy
    plot_data[plot_data.columns[2:]].to_csv(proxies[i] + '.csv', sep=',')
    
# ax.set_xlabel('Age (Ma)')
# ax.set_ylabel(r'CO$_2$ (ppm)')
plt.gca().invert_xaxis()
ax.set_yscale('log')
plt.savefig("multi_proxies.jpg", dpi=600, format="jpg", bbox_inches="tight")