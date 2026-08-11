# Processed Data Documentation

## Overview
This folder contains cleaned and analysis-ready data with derived variables for statistical and spatial analysis.

## File: analysis_ready_data.csv

### Variables
| Column | Type | Description |
|--------|------|-------------|
| Year | Integer | Calendar year (2000-2024) |
| Latitude | Decimal | GPS coordinate (WGS 1984) |
| Longitude | Decimal | GPS coordinate (WGS 1984) |
| Region_Type | Text | Sundarbans Core, Coastal Area, Chittagong Coast |
| Area_Name | Text | Specific location name |
| Entanglement_Bycatch | Integer | Deaths from fishing gear |
| Boat_Strikes | Integer | Deaths from vessel collisions |
| Other_Causes | Integer | Deaths from other causes |
| Total_Deaths | Integer | Total deaths per event |
| **GiZScore** | Float | Getis-Ord Gi z-score (hotspot analysis) |
| **Port_Distance_km** | Float | Distance to nearest fishing port (km) |
| **Density_Value** | Float | Kernel density estimation value |
| **Risk_Score** | Float | Composite risk assessment score (0-1) |

### Derived Variables Description

#### GiZScore
- Getis-Ord Gi* statistic for hotspot identification
- Positive values = hotspots, Negative = coldspots
- |Z| > 1.96 = statistically significant (p < 0.05)

#### Port_Distance_km
- Euclidean distance from event to nearest fishing port
- Calculated in WGS 1984 UTM Zone 46N (EPSG:32646)
- Units: kilometers

#### Density_Value
- Kernel density estimation (KDE) of mortality events
- Bandwidth: 15km
- Grid cell size: 1km

#### Risk_Score
- Composite risk score (0-1 scale)
- Higher values = higher risk
- Derived from: GiZScore, Port Distance, Density

### Data Processing Steps
1. Coordinate validation and transformation
2. Missing data imputation (<2%)
3. Spatial autocorrelation analysis
4. Hotspot detection
5. Risk score calculation

### Coordinate System
**Projected CRS:** WGS 1984 UTM Zone 46N (EPSG:32646)  
**Units:** Meters (for distance calculations)

### Version
**Version:** 1.0  
**Last Updated:** November 2025  
**Contact:** Souad Hasan Ishan (souadhasanishan@std.cu.ac.bd)