markdown
# Analysis Workflow

## Research Workflow Diagram
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: DATA COLLECTION │
├─────────────────────────────────────────────────────────────────┤
│ • Field monitoring (Forest Dept. + WCS) │
│ • GPS coordinates for each event │
│ • Cause of death determination (veterinary) │
│ • Port location data (Bangladesh Navy) │
└────────────────────────────┬────────────────────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: DATA PREPROCESSING │
├─────────────────────────────────────────────────────────────────┤
│ • Coordinate transformation (WGS84 → UTM Zone 46N) │
│ • Duplicate removal │
│ • Missing data imputation │
│ • Port distance calculation │
│ • Data quality validation (98.5% accuracy) │
└────────────────────────────┬────────────────────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: SPATIAL STATISTICS │
├─────────────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ 3.1 Point Pattern Analysis │ │
│ │ • Mean/Median Center │ │
│ │ • Standard Distance │ │
│ │ • Directional Distribution (Ellipse) │ │
│ └──────────────────────────────────────────────────────────┘ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ 3.2 Spatial Autocorrelation │ │
│ │ • Global Moran's I (0.782, p<0.00001) │ │
│ │ • Local Moran's I (LISA) │ │
│ │ • Ripley's K-function (peak at 20km) │ │
│ └──────────────────────────────────────────────────────────┘ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ 3.3 Hot Spot Analysis │ │
│ │ • Getis-Ord Gi* (30/60/90km scales) │ │
│ │ • Statistical significance testing │ │
│ │ • Hotspot classification │ │
│ └──────────────────────────────────────────────────────────┘ │
└────────────────────────────┬────────────────────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 4: STATISTICAL ANALYSIS │
├─────────────────────────────────────────────────────────────────┤
│ • Descriptive statistics │
│ • Correlation analysis (Pearson, Spearman) │
│ • Multiple regression │
│ • Temporal trend analysis (Mann-Kendall, Pettitt's test) │
│ • Hypothesis testing │
└────────────────────────────┬────────────────────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 5: RISK MODELING & PRIORITIZATION │
├─────────────────────────────────────────────────────────────────┤
│ • Composite risk score calculation │
│ • Risk factor weighting (GiZScore 35%, Port 30%, Density 35%) │
│ • Priority zone classification │
│ • Conservation efficiency metrics │
└────────────────────────────┬────────────────────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 6: RESULTS & OUTPUTS │
├─────────────────────────────────────────────────────────────────┤
│ • Figures (8 main figures) │
│ • Statistical outputs (CSV files) │
│ • Spatial outputs (rasters, shapefiles) │
│ • Conservation recommendations │
└─────────────────────────────────────────────────────────────────┘

text

## Key Methods Used

### Spatial Statistics
| Method | Tool/Library | Purpose |
|--------|-------------|---------|
| Moran's I | ArcGIS Pro / PySAL | Measure spatial autocorrelation |
| Getis-Ord Gi* | ArcGIS Pro | Identify hotspots |
| Ripley's K | ArcGIS Pro | Multi-scale clustering |
| Kernel Density | ArcGIS Pro | Density surface creation |
| LISA | ArcGIS Pro | Local cluster detection |

### Statistical Tests
| Test | Python Library | Purpose |
|------|---------------|---------|
| Pearson Correlation | scipy.stats | Linear relationships |
| Mann-Kendall | scipy.stats | Temporal trends |
| Pettitt's Test | Custom | Change point detection |
| Multiple Regression | statsmodels | Multivariate analysis |

## Data Flow
Raw Data (CSV)
↓
Data Preprocessing (Python)
↓
Processed Data (CSV)
↓
├── Spatial Analysis (ArcGIS Pro) → Spatial Outputs (Rasters/Shapefiles)
│
└── Statistical Analysis (Python) → Statistical Outputs (CSV)
↓
Risk Modeling (Python)
↓
Final Results (CSV + Figures)

text

## Software Dependencies

| Software | Version | Purpose |
|----------|---------|---------|
| ArcGIS Pro | 3.4.2 | Spatial analysis |
| Python | 3.9+ | Data processing & statistics |
| R (Optional) | 4.2+ | Additional spatial stats |

## Expected Outputs

| Output | Format | Description |
|--------|--------|-------------|
| Figures | PNG (300 DPI) | 8 main figures |
| Statistical Outputs | CSV | Correlation, regression, trends |
| Spatial Outputs | Raster/Shapefile | Hotspots, clusters, density |
| Risk Scores | CSV | Composite risk model results |
| Priority Zones | Shapefile | Conservation prioritization map |