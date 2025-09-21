# Greenhouse Gas Emissions Analysis Dashboard

## Overview

This project presents an interactive Power BI dashboard that provides insights into CO₂ emissions by country and continent, and their relationship with various socioeconomic factors such as GDP, population, etc. The goal is to help explore how emissions correlate with development, population growth, and other macro indicators, and to highlight regional and global trends.

---

## Contents

| File | Description |
|------|-------------|
| `co2_emissions_report.pbix` | Power BI report/dashboard file. |
| `Data_cleaning.ipynb` | Jupyter notebook used for cleaning, transforming, and preparing raw datasets. |
| `web_scrap.py` | Python script used to scrape / retrieve emission or related data from web sources (if applicable). |
| `countries_by_continent.csv` | Lookup file mapping countries to continents. Needed for grouping/filtering. |

---

## Data Sources

- Raw emissions data (CO₂ per country over time) — source(s) you used (e.g., *Our World in Data*, World Bank, etc.).  
- Socioeconomic metrics: GDP, population, possibly others.  
- Country-to-continent mapping from `countries_by_continent.csv`.  
- Any scraped sources via `web_scrap.py` (list specific URLs if possible).  

---

## Key Features & Insights

The dashboard allows you to:

- View CO₂ emission trends over time for ​countries and continents.  
- Compare emission levels against population size, GDP, or GDP per capita.  
- Identify which countries or regions are diverging from global trends (e.g. increasing emissions despite GDP growth slowing, or per-capita emissions decreasing).  
- Filter, drill down / slice by country, continent, and time period.  
- Visualize correlation (scatter plots, line charts, etc.) between CO₂ emissions and other factors.

---

## How it works / Data Flow

1. **Data collection**  
   - Emissions and related indicators are gathered (via direct download or scraping).  
   - The `web_scrap.py` script handles any web-scraping needed, if some indicators are not available in standard datasets.

2. **Data cleaning & transformation**  
   - With `Data_cleaning.ipynb` you preprocess the data: handling missing values, aligning time ranges, standardizing country names, merging datasets, etc.  
   - Prepare the `countries_by_continent.csv` lookup to enable continent grouping in the visuals.

3. **Report / Dashboard building in Power BI**  
   - Import cleaned datasets.  
   - Build visuals (time series, bar charts, scatter / correlation plots, maps, etc.).  
   - Add filters / slicers for usability: by year, country, continent, etc.

---

## How to Use the Dashboard

- **Interacting with the visuals**: Use filters or slicers to select the time period, continent(s), or country(ies) you want to focus on.  
- **Comparing metrics**: Switch between emissions per capita, total emissions, or emissions growth to see different perspectives.  
- **Exploring relationships**: Use scatter plots to see how emissions relate to population growth, GDP, etc.  
- **Geographic insights**: If map visuals are included, you can see which regions are contributing more, and how that shifts over time.

---

## Setup & Requirements

- **Power BI Desktop / Power BI Service** — to open and view the `.pbix` report.  
- **Python** environment, with libraries such as `pandas`, `numpy`, and possibly `requests` / `beautifulsoup4` if scraping.  
- **Jupyter Notebook** to run `Data_cleaning.ipynb`.  

---

## Limitations & Assumptions

- Some countries have missing or irregular data; interpolation or dropping of entries may have been necessary.  
- Data sources may have different update frequencies or reporting standards.  
- Causation versus correlation: dashboard shows associations but not necessarily causality.  
- Emission values might not account for all sectors (e.g., only CO₂, not other greenhouse gases, depending on source).

---

## Future Work

Here are some ideas you might want to incorporate later:

- Add more socioeconomic variables (energy consumption, industrialization, renewable energy adoption).  
- Include forecasts / projections for CO₂ emissions.  
- Allow export of filtered data / visuals.  
- Add more geographic detail (sub-national regions, if data available).  
- More sophisticated statistical analysis (e.g. regression, clustering) embedded or linked.

---

## Screenshots

> *Insert screenshots of the dashboard here (e.g. Home overview, country/continent comparison, correlation plots etc.)*

---

## License & Contact

- **License**: *Specify license here (e.g., MIT, CC-BY, etc.)*  
- **Contact**: *Your name / email / GitHub handle*  
