# 🐬 Irrawaddy Dolphin Mortality Analysis: Bangladesh (2000-2024)

[![License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-3.4.2-green.svg)](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview)
[![DOI](https://img.shields.io/badge/DOI-10.2139%2Fssrn.7181758-blue.svg)](https://doi.org/10.2139/ssrn.7181758)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 📋 Overview

This repository contains the complete dataset, analytical code, and supplementary materials from a comprehensive geospatial and statistical study of **Irrawaddy dolphin** (*Orcaella brevirostris*) mortality in the Sundarbans ecosystem and adjacent coastal waters of Bangladesh (2000-2024).

**Research conducted by:** Souad Hasan Ishan  
**Co-author:** Mohammad Zahedur Rahman Chowdhury  
**Institution:** Institute of Marine Sciences, University of Chittagong  
**Degree:** B.Sc. (Hons') in Marine Science  
**Term Paper:** MS-499  
**Preprint:** [SSRN: 10.2139/ssrn.7181758](https://doi.org/10.2139/ssrn.7181758)

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
🐬 IRRAWADDY DOLPHIN MORTALITY ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 irrawaddy-dolphin-mortality-bangladesh/
│
├── 📄 README.md # Project overview & documentation
├── 📄 LICENSE # Licensing information
├── 📄 CITATION.cff # Academic citation metadata
├── 📄 .gitignore # Version control exclusions
├── 📄 .gitattributes # File handling specifications
│
├── 📊 data/
│ ├── 📁 raw/ # Original, unmodified data
│ │ ├── 📄 mortality_events_2000-2024.csv # 29 events, 135 deaths
│ │ ├── 📄 port_locations.csv # 10 fishing/commercial ports
│ │ └── 📄 README_raw_data.md # Raw data documentation
│ │
│ ├── 📁 processed/ # Cleaned, analysis-ready data
│ │ ├── 📄 analysis_ready_data.csv # Derived variables included
│ │ └── 📄 README_processed_data.md # Processing documentation
│ │
│ └── 📄 README_data.md # Main data directory guide
│
├── 💻 code/
│ ├── 📁 python/ # Python analysis scripts
│ │ ├── 📄 01_data_preprocessing.py # Data cleaning & validation
│ │ ├── 📄 02_statistical_analysis.py # Stats & correlations
│ │ ├── 📄 03_visualization.py # Figure generation
│ │ ├── 📄 04_risk_modeling.py # Composite risk model
│ │ └── 📄 requirements.txt # Python dependencies
│ │
│ └── 📁 arcgis/ # ArcGIS Pro spatial analysis
│ ├── 📁 geoprocessing_tools/
│ │ ├── 📄 spatial_analysis.atbx # ArcGIS toolbox
│ │ └── 📁 python_scripts/
│ │ ├── 📄 hotspot_analysis.py # Getis-Ord Gi*
│ │ ├── 📄 cluster_analysis.py # Local Moran's I
│ │ └── 📄 kde_analysis.py # Kernel Density
│ │
│ └── 📄 arcgis_project.aprx # ArcGIS Pro project
│
├── 📝 docs/
│ ├── 📁 manuscript/ # Research paper
│ │ └── 📄 ishan_mortality_analysis_2025.pdf # Complete term paper
│ │
│ ├── 📁 figures/ # High-resolution figures
│ │ ├── 🖼️ Cluster Map.jpg
│ │ ├── 🖼️ K function.jpg
│ │ ├── 🖼️ Cluster.jpg
│ │ ├── 🖼️ Geographic Distribution.jpg
│ │ ├── 🖼️ Trendline.png
│ │ ├── 🖼️ Pearson Correlation.png
│ │ ├── 🖼️ Risk Score.png
│ │ ├── 🖼️ Spatial Statistical Analysis.jpg
│ │ ├── 🖼️ workflow.png # Methodological workflow
│ │ └── 🖼️ Conservation Future and Policy.png # Conservation Future & Policy
│ │
│ └── 📁 supplementary/ # Supplementary materials
│ ├── 📄 appendix_a_statistical_outputs.md
│ ├── 📄 appendix_b_gis_methodology.md
│ ├── 📄 appendix_c_raw_data_sample.md
│ ├── 📄 appendix_d_spatial_analysis_parameters.md
│ ├── 📄 appendix_e_conservation_framework.md
│ ├── 🖼️ Postmortem Status.jpg # Postmortem condition
│ └── 📄 README.md # Supplementary index
│
├── 📊 results/
│ ├── 📁 spatial_outputs/ # GIS analysis outputs
│ │ ├── 📁 hotspot_rasters/ # Getis-Ord Gi* rasters
│ │ ├── 📁 density_surfaces/ # KDE surfaces
│ │ └── 📁 cluster_maps/ # LISA cluster maps
│ │
│ ├── 📁 statistical_outputs/ # Statistical analysis results
│ │ ├── 📄 correlation_results.csv
│ │ ├── 📄 regression_results.csv
│ │ └── 📄 temporal_analysis.csv
│ │
│ └── 📁 risk_scores/ # Risk modeling outputs
│ ├── 📄 composite_risk_model.csv
│ └── 📄 priority_zones.shp
│
├── 📓 notebooks/ # Interactive notebooks
│ ├── 📄 exploratory_analysis.ipynb
│ └── 📄 visualization_demo.ipynb
│
└── 📋 plan/ # Project documentation
├── 📄 analysis_workflow.md
└── 📄 data_management_plan.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KEY STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═══════════════════════════════════╦══════════════════════════════════════════╗
║ METRIC ║ VALUE ║
╠═══════════════════════════════════╬══════════════════════════════════════════╣
║ Total Deaths ║ 135 ║
║ Mortality Events ║ 29 ║
║ Study Period ║ 2000–2024 ║
║ Spatial Clustering (Moran's I) ║ 0.782 (p < 0.00001) ║
║ Bycatch Contribution ║ 68.1% ║
║ Critical Zone Area ║ 147 km² (0.9% of study area) ║
║ Mortality in Critical Zones ║ 68.1% ║
║ Temporal Trend ║ +0.342 deaths/year (p = 0.018) ║
╚═══════════════════════════════════╩══════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
```txt
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scipy>=1.9.0
scikit-learn>=1.1.0
statsmodels>=0.13.0
pysal>=23.0.0
arcpy>=3.4.0          # Requires ArcGIS Pro
ArcGIS Pro Extensions Required
Spatial Analyst

Geostatistical Analyst

3D Analyst (optional)

📥 Data Access
Included in Repository (Small Files)
data/raw/mortality_events_2000-2024.csv - Full mortality dataset

data/processed/analysis_ready_data.csv - Cleaned analysis data

Shapefiles for study area boundaries (if < 100MB)

Large Files (Available on Request / Zenodo)
Full ArcGIS Pro geodatabase (.gdb)

High-resolution raster outputs

Complete spatial analysis results

Access Request: Contact author (see below)

🔄 Reproduction Instructions
1. Clone the Repository
bash
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
Cluster Map.jpg	Local Moran's I Cluster Map
K function.jpg	Ripley's K-function Clustering Analysis
Cluster.jpg	Spatial Clustering Visualization
Geographic Distribution.jpg	Geographic Distribution of Mortality Events
Trendline.png	Temporal Trends (2000-2024)
Pearson Correlation.png	Risk Factor Correlation Matrix
Risk Score.png	Risk-Mortality Relationship
Spatial Statistical Analysis.jpg	Comprehensive Spatial Statistical Output
workflow.png	Methodological Workflow Diagram
Conservation Future and Policy.png	Conservation Future and Policy Framework
All figures available in docs/figures/

📝 Citation
If you use this data or code in your research, please cite:

APA Format:

Ishan, S. H., & Chowdhury, M. Z. R. (2026). Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024) [Data and Code]. Institute of Marine Sciences, University of Chittagong. SSRN Preprint. https://doi.org/10.2139/ssrn.7181758

BibTeX Format:

bibtex
@article{ishan2026irrawaddy,
  author = {Ishan, Souad Hasan and Chowdhury, Mohammad Zahedur Rahman},
  title = {Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024)},
  year = {2026},
  journal = {SSRN},
  publisher = {Elsevier},
  doi = {10.2139/ssrn.7181758},
  url = {https://doi.org/10.2139/ssrn.7181758}
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
Co-author: Mohammad Zahedur Rahman Chowdhury
Affiliation: Institute of Marine Sciences, University of Chittagong
Email: souadhasanishan@std.cu.ac.bd
ORCID: 0009-0006-8264-4492

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

## 📁 docs/supplementary/README.md

```markdown
# Supplementary Materials Index

## Overview
This folder contains all supplementary materials supporting the research paper "Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024)."

## Contents

### 📄 Appendices (Markdown)

| File | Description |
|------|-------------|
| **appendix_a_statistical_outputs.md** | Complete statistical outputs including descriptive statistics, correlation matrices, regression results, temporal analysis, and hypothesis tests |
| **appendix_b_gis_methodology.md** | Detailed GIS methodology including software configuration, coordinate systems, spatial analysis parameters, and quality control procedures |
| **appendix_c_raw_data_sample.md** | Raw data samples including mortality events (2000-2024), port locations, and complete data dictionary |
| **appendix_d_spatial_analysis_parameters.md** | Spatial analysis parameters for Ripley's K-function, Moran's I, Getis-Ord Gi*, Kernel Density, and processing configurations |
| **appendix_e_conservation_framework.md** | Conservation planning framework including priority criteria, management interventions, implementation timeline, monitoring indicators, and budget estimates |

### 🖼️ Figures

| File | Description |
|------|-------------|
| **Postmortem Status.jpg** | Photographic documentation of postmortem condition of Irrawaddy dolphins |

## How to Use

1. **Browse** the appendices for detailed methodology and results
2. **Reference** specific sections as needed for your research
3. **Cite** these materials using the main paper citation

## Citation

If using these supplementary materials, please cite:

Ishan, S.H., & Chowdhury, M.Z.R. (2026). Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024). SSRN. doi:10.2139/ssrn.7181758

## Version

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2025 | Initial release |

## Contact

**Author:** Souad Hasan Ishan  
**Email:** souadhasanishan@std.cu.ac.bd  
**ORCID:** [0009-0006-8264-4492](https://orcid.org/0009-0006-8264-4492)

---

*These supplementary materials are provided to support the reproducibility and transparency of the research.*
