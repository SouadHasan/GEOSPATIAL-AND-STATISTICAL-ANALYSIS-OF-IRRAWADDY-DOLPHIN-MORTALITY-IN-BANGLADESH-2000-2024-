# Raw Data Documentation

## Overview
This folder contains the original, unmodified data collected for the Irrawaddy dolphin mortality study (2000-2024).

## Files

### mortality_events_2000-2024.csv
Complete record of all dolphin mortality events documented during the study period.

**Variables:**
| Column | Type | Description |
|--------|------|-------------|
| Year | Integer | Calendar year of mortality event (2000-2024) |
| Latitude | Decimal | GPS coordinate (WGS 1984, decimal degrees) |
| Longitude | Decimal | GPS coordinate (WGS 1984, decimal degrees) |
| Region_Type | Text | Ecological region: Sundarbans Core, Coastal Area, Chittagong Coast |
| Area_Name | Text | Specific location/water body name |
| Entanglement_Bycatch | Integer | Deaths from fishing gear entanglement |
| Boat_Strikes | Integer | Deaths from vessel collisions |
| Other_Causes | Integer | Deaths from pollution, disease, unknown |
| Total_Deaths | Integer | Sum of all causes |

### port_locations.csv
Locations and characteristics of fishing and commercial ports in the study area.

**Variables:**
| Column | Type | Description |
|--------|------|-------------|
| Port_Name | Text | Official name of port/fishing harbor |
| Port_Type | Text | Category: Fishing, Major Commercial |
| Latitude | Decimal | GPS coordinate (WGS 1984, decimal degrees) |
| Longitude | Decimal | GPS coordinate (WGS 1984, decimal degrees) |
| Region | Text | Administrative district |
| Activity_Level | Text | Relative traffic: Low, Medium, High, Very High |

## Data Quality Notes
- **Spatial Accuracy**: ±50 meters (GPS-validated)
- **Attribute Accuracy**: 98.5% (field validated)
- **Temporal Coverage**: Complete from 2000-2024
- **Data Completeness**: 100% for required fields

## Coordinate System
- **Raw Format**: WGS 1984 (EPSG:4326) - Decimal Degrees
- **For Analysis**: Project to WGS 1984 UTM Zone 46N (EPSG:32646)

## Version
**Version:** 1.0  
**Last Updated:** November 2025  
**Contact:** Souad Hasan Ishan (souadhasanishan@std.cu.ac.bd)

## Citation
If using this data, please cite:
Ishan, S.H., & Chowdhury, M.Z.R. (2026). Geospatial and Statistical Analysis of Irrawaddy Dolphin Mortality in Bangladesh (2000-2024). SSRN. doi:10.2139/ssrn.7181758