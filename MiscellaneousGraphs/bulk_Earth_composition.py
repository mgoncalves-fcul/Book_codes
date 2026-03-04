# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 14:30:43 2026

@author: Mario
"""

import matplotlib.pyplot as plt

# Bulk Earth composition (mass %)
data = {
    "Iron (Fe)": 32.0,
    "Oxygen (O)": 29.7,
    "Silicon (Si)": 16.1,
    "Magnesium (Mg)": 15.4,
    "Nickel (Ni)": 1.82,
    "Calcium (Ca)": 1.71,
    "Aluminum (Al)": 1.59,
    "Sulfur (S)": 0.64,
    "Chromium (Cr)": 0.47,
    "Sodium (Na)": 0.18,
    "Manganese (Mn)": 0.08,
    "Phosphorus (P)": 0.07,
    "Carbon (C)": 0.07,
}

# Main pie chart (show Fe, O, Si, Mg; group the rest into "Others")
main_labels = ["Iron (Fe)", "Oxygen (O)", "Silicon (Si)", "Magnesium (Mg)", "Others"]
main_values = [
    data["Iron (Fe)"],
    data["Oxygen (O)"],
    data["Silicon (Si)"],
    data["Magnesium (Mg)"],
]

others_elements = [
    "Nickel (Ni)", "Calcium (Ca)", "Aluminum (Al)", "Sulfur (S)",
    "Chromium (Cr)", "Sodium (Na)", "Manganese (Mn)",
    "Phosphorus (P)", "Carbon (C)"
]
others_values = [data[k] for k in others_elements]
others_total = sum(others_values)
main_values.append(others_total)

# Create a 2-panel layout so the breakdown doesn't overlap the main pie labels
fig, (ax_main, ax_inset) = plt.subplots(
    1, 2,
    figsize=(12, 6),
    gridspec_kw={"width_ratios": [1.35, 1]},
    constrained_layout=True
)

# Main pie
ax_main.pie(
    main_values,
    labels=main_labels,
    autopct="%1.1f%%",
    startangle=140,
    textprops={"fontsize": 11},
)
ax_main.set_title("Bulk Earth Composition by Mass\n(Main Elements + Others)", fontsize=13)

# "Inset" (shown as a separate panel for readability): breakdown of Others
wedges, _ = ax_inset.pie(
    others_values,
    labels=None,          # labels go in legend instead
    startangle=140,
)
ax_inset.set_title("Breakdown of 'Others'\n(absolute % of Earth's mass)", fontsize=13)

# Legend with absolute % values
legend_labels = [f"{el}  {val:.2f}%" for el, val in zip(others_elements, others_values)]
ax_inset.legend(
    wedges,
    legend_labels,
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    frameon=False,
    fontsize=11
)

# Save at 600 dpi (change filename/path as desired)
plt.savefig("Bulk_Earth_Composition.png", dpi=600)
plt.show()

