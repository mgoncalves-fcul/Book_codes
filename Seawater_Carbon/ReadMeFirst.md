
#Use of the Python functions:

These functions are required to compute the equilibrium distribution of carbon species and the pH of ocean waters given
a value of the alkalinity (as micro-mol/kg of seawater) and atmospheric concentration of CO2 (in ppm).

**carbon_sw_eq.py**

This is the main file. It can be edited to change the model conditions.

'# Constants for the equilibrium of the carbonate system in seawater
'# Salinity 35 permil
'# Temp 25
'K0 = 10**-1.5468
'K1 = 1.4626e-06
'K2 = 1.1082e-09
'Kw = 6.0628e-14
'KB = 2.5266e-09
'BT = 4.160e-04
'# Values of pCO2 and Alk (can be changed)
'pCO2 = 418   # ppm
'Alk = 2300   # umol/kg

The provided equilibrium constants are for a salinity of 35 permil and 25ºC temperature.
These values can be changed and replaced by other values at different temperature and salinity.
For that, use the function constant.py (description below).

Alter the values of pCO2 for other atmospheric concentrations and alkalinity (Alk) to compute the distribution
of carbon species and pH of the surface ocean.

Run the file in a command prompt:

python carbon_sw_eq.py

or, inside a python environment:

>>>from carbon_sw_eq import *

Or open with a IDE such as Spyder and run within it.

**constants.py**

This function computes the equilibrium constants necessary to solve the ocean carbonate system for different temperatures
and salinity.

To run the function in a Python environment:

>>>from constants import *
>>>constants(25, 35)

To show the help message inside the function:

>>>help(constants)

**constants_P.py**

Computes the constants for the carbonate system in the ocean, including calcite and aragonite solubility constant, for surface
and deep waters. The inputs are salinity, temperature and pressure.

To run the function in a Python environment:

>>>from constants_P import *
>>>constants_P(25, 35, 600)

To show the help message inside the function:

>>>help(constants_P)


