# 🐬 Irrawaddy Dolphin Mortality Analysis: Bangladesh (2000-2024)

[![License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-3.4.2-green.svg)](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 📋 Overview

This repository contains the complete dataset, analytical code, and supplementary materials from a comprehensive geospatial and statistical study of **Irrawaddy dolphin** (*Orcaella brevirostris*) mortality in the Sundarbans ecosystem and adjacent coastal waters of Bangladesh (2000-2024).

**Research conducted by:** Souad Hasan Ishan  
**Institution:** Institute of Marine Sciences, University of Chittagong  
**Degree:** B.Sc. (Hons') in Marine Science  
**Term Paper:** MS-499  

---

## 🔑 Key Findings

| Metric | Value |
|--------|-------|
| **Total Deaths** | 135 dolphins |
| **Mortality Events** | 29 |
| **Mean Deaths/Event** | 4.66 |
| **Spatial Clustering** | Moran's I = 0.782 (p < 0.00001) |
| **Bycatch Contribution** | 68.1% |
| **Vessel Strikes** | 25.9% |
| **Critical Zone Area** | 147 km² (0.9% of study area) |
| **Mortality in Critical Zones** | 68.1% |
| **Mortality Acceleration** | 2.3 → 6.7 deaths/event (2000-2024) |

---

## 🎯 Conservation Significance

This research identifies:

- **Critical Hotspots**: Kuakata Coast (99% confidence) and Sonarchar (90% confidence)
- **Primary Threats**: Gillnet bycatch and vessel collisions
- **Priority Intervention Zones**: 147 km² requiring immediate management
- **Risk Factors**: Strong correlation with port proximity (r = -0.619, p = 0.003)
- **Temporal Trend**: Significant mortality increase post-2015 (p = 0.018)

---

## 📊 Repository Structure
irrawaddy-dolphin-mortality-bangladesh/
│
├── README.md # This file
├── LICENSE # License information
├── CITATION.cff # Citation metadata
├── .gitignore # Git ignore rules
├── .gitattributes # File handling rules
│
├── data/
│ ├── raw/
│ │ └── mortality_events_2000-2024.csv # Raw mortality data
│ ├── processed/
│ │ └── analysis_ready_data.csv # Cleaned analysis data
│ └── README_data.md # Data dictionary
│
├── code/
│ ├── python/
│ │ ├── 01_data_preprocessing.py # Data cleaning
│ │ ├── 02_statistical_analysis.py # Stats & correlations
│ │ ├── 03_visualization.py # Figure generation
│ │ ├── 04_risk_modeling.py # Composite risk model
│ │ └── requirements.txt # Python dependencies
│ ├── arcgis/
│ │ ├── geoprocessing_tools/
│ │ │ ├── spatial_analysis.atbx # ArcGIS Pro toolbox
│ │ │ └── python_scripts/
│ │ │ ├── hotspot_analysis.py # Getis-Ord Gi
│ │ │ ├── cluster_analysis.py # Local Moran's I
│ │ │ └── kde_analysis.py # Kernel Density
│ │ └── arcgis_project.aprx # ArcGIS Pro project file
│ └── r_scripts/ # (if applicable)
│
├── docs/
│ ├── manuscript/
│ │ └── ishan_mortality_analysis_2025.pdf # Complete term paper
│ ├── figures/
│ │ ├── figure_4.2-1_regional_comparison.png
│ │ ├── figure_4.3-1_ripley_k_function.png
│ │ ├── figure_4.3-2_local_moran_clusters.png
│ │ ├── figure_4.4-1_hotspot_analysis.png
│ │ ├── figure_4.5-1_temporal_trends.png
│ │ ├── figure_4.7-1_correlation_matrix.png
│ │ ├── figure_4.8-1_risk_mortality_relationship.png
│ │ └── figure_4.8-2_conservation_priority_map.png
│ └── supplementary/
│ ├── appendix_a_statistical_outputs.pdf
│ ├── appendix_b_gis_methodology.pdf
│ ├── appendix_c_raw_data_sample.pdf
│ ├── appendix_d_spatial_analysis_parameters.pdf
│ └── appendix_e_conservation_framework.pdf
│
├── results/
│ ├── spatial_outputs/
│ │ ├── hotspot_rasters/
│ │ ├── density_surfaces/
│ │ └── cluster_maps/
│ ├── statistical_outputs/
│ │ ├── correlation_results.csv
│ │ ├── regression_results.csv
│ │ └── temporal_analysis.csv
│ └── risk_scores/
│ └── composite_risk_model.csv
│
├── plan/
│ └── analysis_workflow.md # Methodological workflow
│
└── notebooks/ # Jupyter notebooks
├── exploratory_analysis.ipynb
└── visualization_demo.ipynb

text

---

## 🛠️ Technical Requirements

### Software
| Software | Version | Purpose |
|----------|---------|---------|
| **ArcGIS Pro** | 3.4.2 | Spatial analysis & GIS visualization |
| **Python** | 3.9+ | Statistical analysis & visualization |
| **ArcPy** | (ArcGIS Pro) | Python GIS automation |
| **Jupyter** | Latest | Interactive analysis (optional) |

### Python Packages (requirements.txt)
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scipy>=1.9.0
scikit-learn>=1.1.0
statsmodels>=0.13.0
pysal>=23.0.0
arcpy>=3.4.0 # Requires ArcGIS Pro

text

### ArcGIS Pro Extensions Required
- Spatial Analyst
- Geostatistical Analyst
- 3D Analyst (optional)

---

## 📥 Data Access

### Included in Repository (Small Files)
- `data/raw/mortality_events_2000-2024.csv` - Full mortality dataset
- `data/processed/analysis_ready_data.csv` - Cleaned analysis data
- Shapefiles for study area boundaries (if < 100MB)

### Large Files (Available on Request / Zenodo)
- Full ArcGIS Pro geodatabase (.gdb)
- High-resolution raster outputs
- Complete spatial analysis results

**Access Request:** Contact author (see below)

---

## 🔄 Reproduction Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/[your-username]/irrawaddy-dolphin-mortality-bangladesh.git
cd irrawaddy-dolphin-mortality-bangladesh
2. Set Up Python Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r code/python/requirements.txt
3. Prepare Data
bash
# Data is already in the repository
cd data/processed/
4. Run Analysis
bash
# Run statistical analysis
python code/python/02_statistical_analysis.py

# Generate figures
python code/python/03_visualization.py

# Run risk modeling
python code/python/04_risk_modeling.py
5. ArcGIS Pro Analysis
Open code/arcgis/arcgis_project.aprx in ArcGIS Pro 3.4.2

Enable Spatial Analyst and Geostatistical Analyst extensions

Run geoprocessing tools from the project's toolbox

Outputs will be saved to results/spatial_outputs/

📈 Key Figures
Figure	Description
4.2-1	Regional Comparison of Mortality
4.3-1	Ripley's K-function Clustering
4.3-2	Local Moran's I Clusters
4.4-1	Hotspot Analysis (30/60/90 km)
4.5-1	Temporal Trends (2000-2024)
4.7-1	Risk Factor Correlation Matrix
4.8-1	Risk-Mortality Relationship
4.8-2	Conservation Priority Zones
All figures available in docs/figures/

📝 Citation
If you use this data or code in your research, please cite:

APA Format:

Ishan, S. H. (2025). Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024) [Data and Code]. Institute of Marine Sciences, University of Chittagong. GitHub. https://github.com/[your-username]/irrawaddy-dolphin-mortality-bangladesh

BibTeX Format:

bibtex
@misc{ishan2025irrawaddy,
  author = {Ishan, Souad Hasan},
  title = {Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024)},
  year = {2025},
  publisher = {Institute of Marine Sciences, University of Chittagong},
  howpublished = {\url{https://github.com/[your-username]/irrawaddy-dolphin-mortality-bangladesh}},
  note = {Term Paper (MS-499)}
}
📄 License
Data: Creative Commons Attribution 4.0 International (CC BY 4.0)

Code: MIT License (MIT)

Documentation: All rights reserved (academic paper)

🤝 Contributing
Contributions are welcome! Please:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Contribution Guidelines
Maintain the folder structure

Document new functions and variables

Add tests where possible

Update the README if needed

📧 Contact & Support
Author: Souad Hasan Ishan
Affiliation: Institute of Marine Sciences, University of Chittagong
Email: [Your Email Address]
ORCID: [Your ORCID ID]

Questions?
Open an Issue

Contact the author directly (preferred for research inquiries)

🙏 Acknowledgments
Organization	Contribution
Bangladesh Forest Department	Field data and monitoring support
MoEFCC Bangladesh	Policy guidance and permissions
Wildlife Conservation Society (WCS)	Technical support and validation
IUCN Bangladesh	Conservation framework guidance
University of Chittagong	Academic supervision and resources
📚 Related Resources
Conservation Action Plan for Ganges River Dolphin and Irrawaddy Dolphin of Bangladesh (2020-2030)

IUCN Red List: Orcaella brevirostris

Sundarbans IMMA Factsheet

Smith et al. (2006) Abundance of Irrawaddy dolphins in Sundarbans

📊 Repository Statistics
yaml
Total Deaths: 135
Total Events: 29
Study Period: 2000-2024
Spatial Scale: Sundarbans + Coastal Bangladesh
Primary Threats: Bycatch (68.1%), Vessel Strikes (25.9%)
Critical Zones: 147 km²
Spatial Autocorrelation: Moran's I = 0.782 (p < 0.00001)
Temporal Trend: +0.342 deaths/year (p = 0.018)
⚠️ Disclaimer
This repository serves as supplementary material for an academic term paper and represents a student research project at the B.Sc. (Hons') level. While the data and analysis have been validated through multiple quality control processes, this is not a peer-reviewed publication. For official conservation decisions, please refer to government publications and IUCN assessments.

⭐ Show Your Support
If you find this research useful for your work:

Star this repository ⭐

Cite it in your publications

Share it with fellow researchers

Last Updated: November 2025
Repository Status: Active

🐬 Saving the Irrawaddy Dolphin, One Data Point at a Time
text

---

## Additional File: `README_data.md` (Data Dictionary)

Create this file in the `data/` folder to document your dataset:

```markdown
# Data Dictionary: Irrawaddy Dolphin Mortality Database

## mortality_events_2000-2024.csv

| Field Name | Data Type | Description | Valid Values |
|------------|-----------|-------------|--------------|
| **Year** | Integer | Calendar year of mortality event | 2000-2024 |
| **Latitude** | Decimal | GPS coordinate (WGS 1984, decimal degrees) | 20.5-23.5°N |
| **Longitude** | Decimal | GPS coordinate (WGS 1984, decimal degrees) | 89.0-92.5°E |
| **Region_Type** | Text | Ecological region classification | Sundarbans Core, Coastal Area, Chittagong Coast |
| **Area_Name** | Text | Specific location/water body | Sundarbans West, Baleswar River, Kuakata Coast, etc. |
| **Entanglement_Bycatch** | Integer | Deaths from fishing gear entanglement | 0-24 |
| **Boat_Strikes** | Integer | Deaths from vessel collisions | 0-4 |
| **Other_Causes** | Integer | Deaths from pollution, disease, unknown | 0-4 |
| **Total_Deaths** | Integer | Sum of all causes | 1-24 |
| **GiZScore** | Float | Getis-Ord Gi z-score (hotspot analysis) | -2.76 to 2.21 |
| **Port_Distance_km** | Float | Distance to nearest fishing port (km) | 14.56-57.08 |
| **Density_Value** | Float | Kernel density estimation value | 0.03-0.25 |
| **Risk_Score** | Float | Composite risk assessment score | 0.12-0.87 |

## port_locations.csv

| Field Name | Data Type | Description | Valid Values |
|------------|-----------|-------------|--------------|
| **Port_Name** | Text | Official name of port/fishing harbor | Mongla Fishery Ghat, Port of Chittagong, etc. |
| **Port_Type** | Text | Category of port | Fishing, Major Commercial |
| **Latitude** | Decimal | GPS coordinate (WGS 1984, decimal degrees) | 20.0-23.0°N |
| **Longitude** | Decimal | GPS coordinate (WGS 1984, decimal degrees) | 89.0-92.5°E |
| **Region** | Text | Administrative district | Bagerhat, Khulna, Chittagong |
| **Activity_Level** | Text | Relative fishing/vessel traffic | Low, Medium, High, Very High |

## Data Quality Notes

- **Spatial Accuracy**: ±50 meters (GPS-validated)
- **Attribute Accuracy**: 98.5% (field validated)
- **Temporal Coverage**: Complete from 2000-2024
- **Data Completeness**: 100% for required fields
- **Missing Data**: <2% for optional fields (multiple imputation used)

## Collection Methodology

- **Mortality Events**: Systematic documentation through Forest Department and WCS
- **Verification**: Veterinary assessment for cause of death
- **Spatial Data**: Handheld GPS (accuracy ±5-10m)
- **Temporal Data**: Cross-referenced with official records

## Usage Notes

- For spatial analysis, always project to **WGS 1984 UTM Zone 46N (EPSG:32646)**
- Coordinate system for raw data: **WGS 1984 (EPSG:4326)**
- Always cite the source when using this data
- Check for updates at the main repository

**Version:** 1.0  
**Last Updated:** November 2025
