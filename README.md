# "How Can Canada Contribute to more Sustainable E-Waste Management Globally?": the Code

This project contains 3 Jupyter notebooks for processing 2 Statistics Canada datasets on the practices of Montrealers 
in regard to e-waste and hazardous waste, and a dataset on lead in the air in Guiyu, China. 

## Requirements

1. An environment capable of running Jupyter
2. `pandas==2.1.4`
3. `numpy==1.24.3`
4. `matplotlib==3.8.0`

Requirements are available in `requirements.txt`.

## Project Overview

- `data/`: Folder containing the 2 datasets used in this project.
- `images/`: Folder where plots are exported to. Contains 2 subfolders:
  - `e_waste`: Folder where plots from the `e_waste.ipynb` are exported to.
  - `hazardous_waste`: Folder where plots from the `hazardous_waste.ipynb` are exported to.
- `README.md`: This README.
- `requirements.txt`: The set of dependencies that this project requires. It is recommended to create a virtual
                      environment for them.
- `e_waste.ipynb`: Notebook processing data from the [1] dataset.
- `hazardous_waste.ipynb`: Notebook processing data from the [2] dataset.
- `lead_in_china.ipynb`: Notebook for processing data from [3]-[6].

## Bibliography

[1] Statistics Canada, “Table 38-10-0154-01  Electronic waste.” Statistics Canada, Jul. 18, 2022. 
doi: https://doi.org/10.25318/3810015401-eng.

[2] Statistics Canada, “Table 38-10-0155-01  Household hazardous waste.” Statistics Canada, Jul. 18, 2022.
doi: https://doi.org/10.25318/3810015501-eng.

[3] W. J. Deng, P. K. K. Louie, W. K. Liu, X. H. Bi, J. M. Fu, and M. H. Wong, “Atmospheric levels and cytotoxicity
of PAHs and heavy metals in TSP and PM2.5 at an electronic waste recycling site in southeast China,”
Atmospheric Environment, vol. 40, no. 36, pp. 6945–6955, Nov. 2006, doi: 10.1016/j.atmosenv.2006.06.032.

[4] World Health Organization Regional Office for Europe, Air quality guidelines for Europe, 2nd ed. in European Series,
no. 91. Copenhagen: WHO Regional Publications, 2000.

[5] F. Var, Y. Narita, and S. Tanaka, “The concentration, trend and seasonal variation of metals in the atmosphere in
16 Japanese cities shown by the results of National Air Surveillance Network (NASN) from 1974 to 1996,”
Atmospheric Environment, vol. 34, no. 17, pp. 2755–2770, Jan. 2000, doi: 10.1016/S1352-2310(99)00353-2.

[6] K.-H. Kim et al., “The chemical composition of fine and coarse particles in relation with the Asian Dust events,”
Atmospheric Environment, vol. 37, no. 6, pp. 753–765, Feb. 2003, doi: 10.1016/S1352-2310(02)00954-8.

[7] KostisPar, “Answer to ‘Pandas plot bar without NaN values spaces,’” Stack Overflow. Accessed: Jun. 08, 2024.
[Online]. Available: https://stackoverflow.com/a/70019779
