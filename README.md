# Book_codes

Python scripts and data files for reproducing selected figures from **_The Earth, Carbon Dioxide, and Climate_** by **Mário A. Gonçalves**.

This repository accompanies the book and provides the code used to generate figures related to Earth’s carbon cycle, atmospheric carbon dioxide, greenhouse radiation, climate change indicators, ice-core records, proxy data, seawater carbonate chemistry, and related geoscience topics.

> **Branch note**
>
> The code is currently available on the `Python-Code` branch. If the repository opens on `main` and only `README.md` and `LICENSE` are visible, switch to the `Python-Code` branch.

## Repository contents

| Directory | Main script(s) | Description |
| --- | --- | --- |
| `BlackBody_Spectra/` | `BlackBody.py` | Generates blackbody spectra and compares atmospheric radiance curves for different CO₂ concentrations. |
| `CarbonDioxide_Emissions/` | `CO2Emissions.py` | Plots cumulative carbon emissions and simple extrapolations of total emissions. |
| `ClimateChange/` | `PlotsTemperatureForcingIce.py` | Generates plots of temperature anomaly, effective radiative forcing, and ice-mass loss from Greenland and Antarctica. |
| `Keeling_IceCores/` | `CO2_icecore_graphics.py` | Generates the Keeling Curve and ice-core plots for CO₂, CH₄, oxygen isotopes, deuterium, and temperature-related records. |
| `MiscellaneousGraphs/` | `CO2absorption.py`, `CarbonateSat.py`, `Normal_ExtremeEv.py`, `bulk_Earth_composition.py` | Generates miscellaneous supporting figures, including anthropogenic emissions, carbonate saturation, normal-distribution extremes, and bulk Earth composition. |
| `Proxies/` | `CO2proxies.py` | Processes and plots geological CO₂ proxy data. The script includes an interactive selection step for choosing one or more proxy types. |
| `Seawater_Carbon/` | `carbon_sw_eq.py` | Calculates carbonate-system equilibrium in seawater and prints pH and dissolved carbon species. |
| `Zachos_Data/` | `zachos_data.py` | Plots carbon-isotope data from the Zachos dataset included in the repository. |

Most scripts write figure files such as `.jpg`, `.png`, or `.eps` in the same directory as the script.

## Requirements

The scripts require Python 3 and the following Python packages:

```bash
numpy
pandas
matplotlib
scipy
openpyxl
```

`openpyxl` is needed because several scripts read `.xlsx` files through `pandas`.

## Installation

Clone the repository and switch to the branch containing the code:

```bash
git clone -b Python-Code https://github.com/mgoncalves-fcul/Book_codes.git
cd Book_codes
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib scipy openpyxl
```

## Running the scripts

Run each script from its own directory so that the local data files are found correctly.

Example:

```bash
cd BlackBody_Spectra
python BlackBody.py
```

This creates the output figure in the `BlackBody_Spectra/` directory.

Another example:

```bash
cd ClimateChange
python PlotsTemperatureForcingIce.py
```

This generates temperature, radiative-forcing, and ice-loss figures in the `ClimateChange/` directory.

For the proxy-data script:

```bash
cd Proxies
python CO2proxies.py
```

The script asks which proxy or proxies to plot. Enter one or more numbers separated by spaces when prompted.

## Data files

The scripts use data files stored in the same folders as the corresponding Python files. Do not rename or move these files unless the paths in the scripts are updated accordingly.

The repository includes data in several formats, including `.csv`, `.txt`, `.tab`, `.xlsx`, and image files. Some data files originate from external scientific datasets; cite the original data sources as appropriate when using generated figures or derived results.

## Output files

Typical generated outputs include:

- `spectra.jpg`
- `carbon_emissions.jpg`
- `temperature_anomaly.jpg`
- `Radiatve_forcing.jpg`
- `ice_loss.jpg`
- `keeling.jpg`
- `ice_cores.jpg`
- `AnthropogenicEmissions.png`
- `AnthropogenicEmissions.eps`
- `distribution_extremes.jpg`
- `Bulk_Earth_Composition.png`
- `boron.jpg`
- `multi_proxies.jpg`
- `zachos_data.jpg`

Existing output files may be overwritten when scripts are run again.

## Citation

If you use this repository, please cite the accompanying book:

> Gonçalves, M. A. (2026). *The Earth, Carbon Dioxide, and Climate*. Springer Cham.

Please also cite this repository when using or adapting the code:

> Gonçalves, M. A. *Book_codes: Python code for figures from The Earth, Carbon Dioxide, and Climate*. GitHub repository.

## License

This repository is distributed under the **GNU General Public License v3.0**. See the [`LICENSE`](LICENSE) file for details.

## Notes

The scripts are intended for figure reproduction, teaching, and exploratory calculations. They are not packaged as a Python library, and many scripts are designed to be run as standalone programs from their own folders.
