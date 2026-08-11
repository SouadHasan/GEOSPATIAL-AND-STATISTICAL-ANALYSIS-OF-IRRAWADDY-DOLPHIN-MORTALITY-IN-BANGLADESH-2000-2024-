# Data Management Plan

## Overview
This document outlines the data management practices for the Irrawaddy dolphin mortality study (2000-2024).

## Data Collection

| Data Type | Collection Method | Frequency |
|-----------|-------------------|-----------|
| Mortality Events | Field monitoring (Forest Dept. + WCS) | Continuous |
| GPS Coordinates | Handheld GPS (accuracy ±5-10m) | Per event |
| Cause of Death | Veterinary assessment | Per event |
| Port Locations | Bangladesh Navy Hydrographic Dept. | Static |

## Data Storage

### Primary Storage
| Location | Purpose | Capacity |
|----------|---------|----------|
| GitHub Repository | Public access & version control | 100 MB (Git LFS for large files) |
| University Server | Backup & processing | 1 TB |
| Zenodo | Long-term preservation & DOI | 50 GB |

### File Formats
| File Type | Format | Reason |
|-----------|--------|--------|
| Tabular Data | CSV | Open format, widely supported |
| Spatial Data | Shapefile, GeoTIFF | Industry standard |
| Documentation | Markdown, PDF | Readable, reproducible |
| Code | Python, R | Open source |

## Data Quality Control

### Quality Metrics
| Metric | Target | Achieved |
|--------|--------|----------|
| Spatial Accuracy | ±100m | ±50m |
| Attribute Accuracy | 95% | 98.5% |
| Temporal Coverage | 100% | 100% |
| Data Completeness | 95% | 100% |

### Validation Methods
1. **Spatial**: Cross-reference with independent GPS
2. **Temporal**: Check against official records
3. **Attribute**: Field validation (20% of events)
4. **Logical**: Topological consistency checks

## Data Security

### Security Measures
- **Version Control**: Git with GitHub
- **Backups**: Daily automated backups
- **Access Control**: Public repository, private backup
- **Encryption**: HTTPS for transfer

## Data Sharing

### Repository: https://github.com/[username]/irrawaddy-dolphin-mortality-bangladesh

### License
| Component | License |
|-----------|---------|
| Data | CC BY 4.0 |
| Code | MIT |
| Documentation | CC BY 4.0 |

### Citation
Ishan, S.H., & Chowdhury, M.Z.R. (2026). Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024). SSRN. doi:10.2139/ssrn.7181758

## Long-term Preservation

### Platform: Zenodo
- **DOI**: 10.2139/ssrn.7181758
- **Format**: Complete repository snapshot
- **Frequency**: Annual updates

## Ethical Considerations
- No personally identifiable information
- Data collected under government permit
- No sensitive location data (coordinates generalized)