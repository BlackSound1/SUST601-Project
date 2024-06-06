# My code for the SUST601 Project

This project contains 2 Jupyter notebooks for processing 2 Statistics Canada datasets on the practices of Montrealers 
in regard to e-waste and hazardous waste. 

# Requirements

1. An environment capable of running Jupyter
2. `pandas==2.1.4`
3. `numpy==1.24.3`
4. `matplotlib==3.8.0`

Requirements are available in `requirements.txt`.

# Project Overview

- `data/`: Folder containing the 2 datasets used in this project.
- `images/`: Folder where plots are exported to. Contains 2 subfolders:
  - `e_waste`: Folder where plots from the `e-waste_notebook` are exported to.
  - `hazardous_waste`: Folder where plots from the `house_hazard_waste_notebook` are exported to.
- `utilities.py`: A Python module containing utility function(s).
- `README.md`: This README.
- `requirements.txt`: The set of dependencies that this project requires. It is recommended to create a virtual
                      environment for them.
- `e-waste_notebook.ipynb`: Notebook processing data from the `Electronic Waste.csv` dataset.
- `house_hazard_waste_notebook.ipynb`: Notebook processing data from the `Household Hazardous Waste.csv` dataset.

# Bibliography

[1] Statistics Canada, “Table 38-10-0154-01  Electronic waste.” Statistics Canada, Jul. 18, 2022. 
doi: https://doi.org/10.25318/3810015401-eng.

[2] Statistics Canada, “Table 38-10-0155-01  Household hazardous waste.” Statistics Canada, Jul. 18, 2022.
doi: https://doi.org/10.25318/3810015501-eng.
