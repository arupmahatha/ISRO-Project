# Overview of Oceanographic Variables

    This table provides a comprehensive overview of various oceanographic variables, detailing their specific names, acronyms, the oceanic regions they pertain to, and the units of measurement used. The variables include physical parameters such as temperature and salinity, as well as chemical constituents like dissolved oxygen and nutrients. Understanding these variables is crucial for analyzing ocean dynamics and biogeochemical processes.

    | S.No. | Variable name | Specific variable name                                                               | Acronyms | Ocean       | Units   |
    |-------|---------------|--------------------------------------------------------------------------------------|----------|-------------|---------|
    | 1     | Temperature   | Sea water potential temperature                                                      | thetao   | Blue Ocean  | °C      |
    | 2     | Salinity      | Sea water salinity                                                                   | so       | Blue Ocean  | /10³    |
    | 3     | Velocity      | Eastward sea water velocity                                                          | uo       | Blue Ocean  | m/s     |
    | 4     | Velocity      | Northward sea water velocity                                                         | vo       | Blue Ocean  | m/s     |
    | 5     | Velocity      | Upward sea water velocity                                                            | wo       | Blue Ocean  | m/s     |
    | 6     | Light         | Volume attenuation coefficient of downwelling radiative flux in sea water            | kd       | Green Ocean | m⁻¹     |
    | 7     | pH            | Sea water ph reported on total scale                                                 | ph       | Green Ocean | -       |
    | 8     | SpCO2         | Surface partial pressure of carbon dioxide in sea water                              | spco2    | Green Ocean | Pa      |
    | 9     | O2            | Mole concentration of dissolved molecular oxygen in sea water                        | o2       | Green Ocean | mmol/m³ |
    | 10    | NO3           | Mole concentration of nitrate in sea water                                           | no3      | Green Ocean | mmol/m³ |
    | 11    | PO4           | Mole concentration of phosphate in sea water                                         | po4      | Green Ocean | mmol/m³ |
    | 12    | Si            | Mole concentration of silicate in sea water                                          | si       | Green Ocean | mmol/m³ |
    | 13    | Fe            | Mole concentration of dissolved iron in sea water                                    | fe       | Green Ocean | mmol/m³ |
    | 14    | Chl-a         | Mass concentration of chlorophyll a in sea water                                     | chl      | Green Ocean | mg/m³   |



# Oceanographic Types and Their Forecasting
    Blue Ocean: Global Ocean Physics Analysis and Forecast
    Green Ocean: Global Ocean Biogeochemistry Analysis and Forecast



# Location:
    Latitude: 20 to 23
    Longitude: 87 to 91



# Depth range:
    From 0.49 m to 0.49 m



# Time range:
    As of Now (cleaned_data.csv): 01/11/2023 → 01/11/2024
    Green Ocean: 01/06/2022, 00:00 → 08/01/2025, 00:00
    Blue Ocean: 01/11/2021 → 03/01/2025
    Blue Ocean (Chl-a): 01/10/2021, 00:00 → 01/11/2024, 00:00
    Blue Ocean (Light): 15/11/2023 → 03/01/2025



## Points in the Dataset:
    1) No depth in SpCO2



## Points of Interest: 
    1) o2 : More likely an effect rather than a cause of chlorophyll levels
    2) The combination of the neural network and random forest models is yielding satisfactory results as compared to incorporating additional methods such as ridge, lasso, robust linear and support vector regression.