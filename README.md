# Assignment A7: Bias in Data

This repository contains data sources, code and documentation to support the analysis and results in the project report for Assignment 7 of the course DATA 512 of the 2021 fall quarter in MSDS at UW.

## Files

This repository contains 3 jupyter notebooks, 1 python script, 1 Tableau workbook and 10 data files.

### hcds-a4-mask-mandates.ipynb
This notebook creates a visualization of the number of confirmed COVID-19 cases, along with trends of the rate of infection and the periods of mask mandates.

### hcds-a7-data-processing.ipynb
This notebook contains the data aggregations, clean up and pre-processing to support all the remaining analysis and visualizations.

### hcds-a7-regressions.ipynb
This notebook uses the output of hcds-a7-data-processing.ipynb to display visualizations of linear regressions on all metrics and predictors.

### hcds-a7-stats.py
This python script uses the output of hcds-a7-data-processing.ipynb to fit a linear regression model and display the statistical properties of the model, including p-values.

### visualizations.twbx
This Tableau workbook uses the output of hcds-a7-data-processing.ipynb and displays visualizations of the mortality rate metrics per state and per county.

### cases/RAW_us_confirmed_cases.csv
A record of COVID-19 confirmed cases by county [1] in the United States.

*Schema*

- Province_State: The name of the state.
- Admin2: The name of the county.
- UID: Unique Identifier for each row entry.
- iso3: Officialy assigned country code identifiers.
- FIPS: Federal Information Processing Standards code that uniquely identifies counties within the USA
- Country_Region: Country, region or sovereignty name. 
- Lat: Latitude.
- Long_: Longitude.
- Dates: Multiple columns. Each row contains a time series of the number of confirmed cases on that date.

### cases/RAW_us_deaths.csv
A record of COVID-19 deaths by county [1] in the United States.

*Schema*

(same schema as RAW_us_confirmed_cases.csv plus a Population column)

- Province_State: The name of the state.
- Admin2: The name of the county.
- UID: Unique Identifier for each row entry.
- iso3: Officialy assigned country code identifiers.
- FIPS: Federal Information Processing Standards code that uniquely identifies counties within the USA
- Country_Region: Country, region or sovereignty name. 
- Lat: Latitude.
- Long_: Longitude.
- Population: Population of the county/region.
- Dates: Multiple columns. Each row contains a time series of the number of deaths on that date.

### masks_mandate/US_State_and_Territorial_Public_Mask_Mandates.csv
Record of the "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through August 15, 2021 by County by Day" [2], filtered to include only the assignment county.

*Schema*

- State_Tribe_Territory: U.S. state, tribe, and territory names.
- County_Name: U.S. county names.
- FIPS_State: U.S. state FIPS codes
- FIPS_County: U.S. county FIPS codes.
- date: Daily date in dataset.
- order_code: (1) for mandate anywhere outside the home or (2) both in retail businesses and in restaurants/food establishments.
- Source_of_Action: Source where order was found.
- URL: URL of order language used to complete dataset.
- Citation: Citation for the order.

### masks_usage/mask-use-by-county.csv
Estimates of mask usage [3] by county.

*Schema*

- COUNTYFP: U.S. county code.
- NEVER: Percentage of the population who answered that 'never' used masks.
- RARELY: Percentage of the population who answered that 'rarely' used masks.
- SOMETIMES: Percentage of the population who answered that 'some times' used masks.
- FREQUENTLY: Percentage of the population who answered that 'frequently' used masks.
- ALWAYS: Percentage of the population who answered that 'always' used masks.

### health_infrastructure/community_health_centers.csv
Number of community health centers per state [5].

*Schema*

- Location: Name of the state.
- Total CHCs: Total number of community health centers.
- Service Delivery Sites: Total number of service delivery sites.
- Clinical Visits: Total number of clinic visits.
- Virtual Visits: Total number of virtual visits.
- Total Visits: Total number of visits.

### health_infrastructure/hospital_beds_per_1000_people.csv
Number of hospital beds per state [6].

*Schema*

- Location: Name of the state.
- State/Local Government: Number of state or local government beds.
- Non-Profit: Number of non-profit beds.
- For-Profit: Number of for-profit beds.
- Total: Total number of beds.

### health_infrastructure/icu_beds.csv
Number of ICU beds per state [7].

*Schema*

- Location: Name of the state.
- ICU Beds: Total number of ICU beds
- ICU Beds per 10,000 Population: Number of ICU beds per 10,000 population.

### health_infrastructure/primary_care_shortage.csv
Health Professional Shortage Area (HPSA) designations are used to identify areas and population groups within the United States that are experiencing a shortage of health professionals [9].

*Schema*

- Location: Name of the state.
- Total Primary Care HPSA Designations: The number of additional primary care physicians needed to achieve a population-to-primary care physician ratio of 3,500 to 1 (3,000 to 1 where high needs are indicated) in all designated primary care HPSAs, resulting in their removal from designation. The formula used to designate primary care HPSAs does not take into account the availability of additional primary care services provided by nurse practitioners and physician assistants in an area."
- Population of Designated HPSAs: Population of the area.
- Percent of Need Met: Computed by dividing the number of physicians available to serve the population of the area, group, or facility by the number of physicians that would be necessary to eliminate the primary are HPSA (based on a ratio of 3,500 to 1 (3,000 to 1 where high needs are indicated)).
- Practitioners Needed to Remove HPSA Designation: Number of practitioners necessary to remove the designation.

### health_infrastructure/primary_care.csv
Number of active primary case physicians per state [8].

*Schema*

- Location: Name of the state.
- Internal Medicine: Number of physicians in internal medicine.
- Family Medicine/General Practice: Number of physicians in family/general practice.
- Pediatrics: Number of physicians in pediatrics.
- Obstetrics & Gynecology: Number of physicians in obstetrics/gynecology.
- Geriatrics: Number of physicians in geriatrics.
- Total Primary Care: Total number of active primary care physicians.

### health_infrastructure/total_hospitals.csv
Number of hospitals per state [4].

*Schema*

- Location: Name of the state.
- Total Hospitals: Total number of hospitals.

## How to Run

In order to obtain the results mentioned in the project report, the code should be executed as follows:

1) hcds-a4-mask-mandates.ipynb, the preliminary analysis
2) hcds-a7-data-processing.ipynb, this will output 3 cooked data files:

*all_metrics.csv*

- State: Name of the state.
- Cases: Number of cases.
- Deaths: Number of deaths.
- Population: Population of the state.
- Deaths by 1,000 Population: Ratio of deaths by 1,000 population.
- Deaths by 1,000 Case: Ratio of deaths by 1,000 cases.
- Hospitals per 1,000 Population: Number of hospitals per 1,000 population.
- Community Health Centers per 1,000 Population: Number of CHC per 1,000 population.
- Total beds per 1,000 Population: Total hospital beds per 1,000 population.
- ICU beds per 1,000 Population: Total ICU beds per 1,000 population.
- Primary Care Practitioners per 1,000 Population: Total primary care practitioners per 1,000 population.
- Percentage of Practitioners Needed Met: Percentage of practitioners met according to the HPSA metric.

*mortality_rates_by_state.csv*

- State: Name of the state.
- Cases: Number of cases.
- Deaths: Number of deaths.
- Population: Population of the state.
- Deaths by 1,000 Population: Ratio of deaths by 1,000 population.
- Deaths by 1,000 Case: Ratio of deaths by 1,000 cases.

*mortality_rates_by_county.csv*

- State: Name of the state.
- County: Name of the county.
- Cases: Number of cases.
- Deaths: Number of deaths.
- Population: Population of the county.
- Deaths by 1,000 Population: Ratio of deaths by 1,000 population.
- Deaths by 1,000 Case: Ratio of deaths by 1,000 cases.

3) Run hcds-a7-regressions.ipynb to plot the linear regressions.
4) Run hcds-a7-stats.py to obtain all the regression stats, including p-values.
5) Open visualizations.twbx in Tableau desktop.


## Licenses

The code provided in this repository is released under the MIT License.  

The data from [KFF](https://www.kff.org/statedata/) is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).

Other licenses are mentioned for each data source listed in the next section.

## Data Sources

[1] Record of COVID-19 confirmed cases and deaths by county, dataset from Johns Hopkins University and distributed through [Kaggle](https://www.kaggle.com/antgoldbloom/covid19-data-from-john-hopkins-university?select=CONVENIENT_us_metadata.csv) under CC BY 4.0 license.

[2] "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through August 15, 2021 by County by Day". Data Provided by Mara Howard-Williams, Public Health Law Program, Center for State, Tribal, Local, and Territorial Support, Centers for Disease Control and Prevention and available for download directly from the CDC at https://data.cdc.gov/Policy-Surveillance/U-S-State-and-Territorial-Public-Mask-Mandates-Fro/62d6-pm5i

[3] Mask Usage: Estimates are from The New York Times, based on roughly 250,000 interviews conducted by Dynata from July 2 to July 14 and available on a [GitHub repository](https://github.com/nytimes/covid-19-data/tree/master/mask-use) under a specific [copyright notice and attribution request](https://github.com/nytimes/covid-19-data/blob/master/LICENSE).

[4] “Total Hospitals”, 2019, AHA Annual Survey, Copyright 2020 by Health Forum, LLC, an affiliate of the American Hospital Association. Special data request, 2020. Available from KFF State Health Facts, https://www.kff.org/other/state-indicator/total-hospitals/

[5] “Community Health Center Delivery Sites and Patient Visits”, 2019, George Washington University analysis of the 2020 Uniform Data System, Health Resources and Services Administration. Special Data Request, September 2021. Available from KFF State Health Facts, https://www.kff.org/other/state-indicator/community-health-center-sites-and-visits/

[6] “Hospital Beds per 1,000 Population by Ownership Type”, 2019, AHA Annual Survey, Copyright 2020 by Health Forum, LLC, an affiliate of the American Hospital Association. Special data request, 2020. Available from KFF State Health Facts, https://www.kff.org/other/state-indicator/beds-by-ownership

[7] “ICU Beds”, 2018, KFF analysis of merged American Hospital Directory and 2018 AHA Annual Survey data. Available from KFF State Health Facts, https://www.kff.org/other/state-indicator/icu-beds/

[8] “Professionally Active Primary Care Physicians by Field”, 2021, Special data request on State Licensing Information from Redi-Data, Inc., June 202. Available from KFF State Health Facts, https://www.kff.org/other/state-indicator/primary-care-physicians-by-field/

[9] “Primary Care Health Professional Shortage Areas (HPSAs)”, 2021, Bureau of Health Workforce, Health Resources and Services Administration (HRSA), U.S. Department of Health & Human Services, Designated Health Professional Shortage Areas Statistics: Designated HPSA Quarterly Summary, as of September 30, 2021 available at https://data.hrsa.gov/topics/health-workforce/shortage-areas and obtained from KFF State Health Facts, https://www.kff.org/other/state-indicator/primary-care-health-professional-shortage-areas-hpsas/
