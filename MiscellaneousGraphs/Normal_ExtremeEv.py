# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:53:44 2024

@author: Mario
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = np.linspace(-3, 3, 101)
y = 1/(np.sqrt(2*np.pi)) * np.exp(-1/2*x**2)

x2 = np.linspace(-2, 4, 101)
y2 = 1/(np.sqrt(2*np.pi)) * np.exp(-1/2*(x2-1)**2)


fig, ax = plt.subplots()
ax.plot(x, y, x2, y2)
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())

x_plus = x[x > 1.645]
y_plus = y[x > 1.645]

x_minus = x[x < -1.645]
y_minus = y[x < -1.645]

x2_plus = x2[x2 > 1.645]
y2_plus = y2[x2 > 1.645]

ax.fill_between(x_plus, y_plus, color="g")
ax.fill_between(x_minus, y_minus, color="g")
ax.fill_between(x2_plus, y2_plus, color="none", hatch="/", edgecolor="k")

ax.set_xlabel('Variable', size=15)
ax.set_ylabel('Probability', size=15)

ax.annotate('5%', xy=(1.77, 0.011), color="w", size=12)
ax.annotate('26%', xy=(2.00, 0.106), color="b", size=12)

ax.vlines(0, min(y), max(y), linestyle='--')
ax.vlines(1, min(y), max(y), linestyle='--', color='g')

plt.savefig("distribution_extremes.jpg", dpi=600, format="jpg", bbox_inches="tight")
