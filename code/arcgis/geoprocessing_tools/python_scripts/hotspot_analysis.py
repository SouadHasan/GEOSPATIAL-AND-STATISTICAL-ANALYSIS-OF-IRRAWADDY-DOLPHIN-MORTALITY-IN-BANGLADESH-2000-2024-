"""
hotspot_analysis.py
ArcGIS Pro Python Script for Hotspot Analysis (Getis-Ord Gi*)
For Irrawaddy Dolphin Mortality Study
Author: Souad Hasan Ishan
Date: November 2025
"""

import arcpy
from arcpy import env
from arcpy.sa import *

# ============================================
# CONFIGURATION
# ============================================

# Set workspace
arcpy.env.workspace = "path/to/your/geodatabase.gdb"
arcpy.env.overwriteOutput = True

# Input data
input_features = "mortality_events"
weight_field = "Total_Deaths"

# Output paths
output_gdb = "path/to/your/geodatabase.gdb"
hotspot_output = "hotspot_60km"
cluster_output = "local_moran_clusters"

# ============================================
# 1. HOT SPOT ANALYSIS (GETIS-ORD GI*)
# ============================================

def run_hotspot_analysis():
    """Run Getis-Ord Gi* hotspot analysis at multiple scales."""
    
    print("📍 Running Hot Spot Analysis...")
    
    # Fixed distance bands for analysis
    distance_bands = [30000, 60000, 90000]  # 30km, 60km, 90km
    
    for dist in distance_bands:
        output_name = f"hotspot_{dist//1000}km"
        
        try:
            print(f"   Analyzing at {dist//1000}km scale...")
            
            arcpy.stats.HotSpots(
                Input_Feature_Class=input_features,
                Input_Field=weight_field,
                Output_Feature_Class=output_name,
                Conceptualization_of_Spatial_Relationships="FIXED_DISTANCE_BAND",
                Distance_Method="EUCLIDEAN_DISTANCE",
                Standardization="NONE",
                Distance_Band=dist,
                Weights_Matrix_File=None,
                Self_Potential="INCLUDE",
                Gi_Field=None
            )
            
            print(f"   ✅ Completed: {output_name}")
            
        except arcpy.ExecuteError:
            print(f"   ❌ Error at {dist//1000}km: {arcpy.GetMessages(2)}")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")

# ============================================
# 2. LOCAL MORAN'S I ANALYSIS
# ============================================

def run_cluster_analysis():
    """Run Anselin Local Moran's I cluster analysis."""
    
    print("\n🔍 Running Cluster and Outlier Analysis...")
    
    try:
        arcpy.stats.ClusterOutlier(
            Input_Feature_Class=input_features,
            Input_Field=weight_field,
            Output_Feature_Class=cluster_output,
            Conceptualization_of_Spatial_Relationships="FIXED_DISTANCE_BAND",
            Distance_Method="EUCLIDEAN_DISTANCE",
            Standardization="NONE",
            Distance_Band=60000,
            Weights_Matrix_File=None,
            Self_Potential="INCLUDE",
            Permutations=999,
            Significance_Level=0.05
        )
        
        print(f"   ✅ Completed: {cluster_output}")
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")

# ============================================
# 3. KERNEL DENSITY ESTIMATION
# ============================================

def run_kde_analysis():
    """Run Kernel Density Estimation for mortality events."""
    
    print("\n🔄 Running Kernel Density Estimation...")
    
    try:
        kde_output = "kde_mortality"
        
        arcpy.stats.KernelDensity(
            in_features=input_features,
            population_field=weight_field,
            out_raster=kde_output,
            cell_size=1000,
            search_radius=15000,
            area_unit_scale="SQUARE_KILOMETERS",
            out_cell_values="DENSITIES",
            method="QUADRATIC_KERNEL"
        )
        
        print(f"   ✅ Completed: {kde_output}")
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")

# ============================================
# 4. RIPLEY'S K-FUNCTION
# ============================================

def run_ripley_k():
    """Run Multi-Distance Spatial Cluster Analysis (Ripley's K)."""
    
    print("\n📊 Running Ripley's K-Function...")
    
    try:
        arcpy.stats.MultiDistanceCluster(
            Input_Feature_Class=input_features,
            Output_Table="ripley_k_results",
            Weight_Field=weight_field,
            Number_of_Distance_Bands=10,
            Beginning_Distance=10000,
            Increment_Distance=10000,
            Study_Area_Method="MINIMUM_ENCLOSING_RECTANGLE",
            Boundary_Correction_Method="RIPLEYS_ISOTROPIC",
            Permutations=999
        )
        
        print(f"   ✅ Completed: ripley_k_results")
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    print("=" * 60)
    print("🐬 IRRAWADDY DOLPHIN MORTALITY ANALYSIS")
    print("   ArcGIS Pro Spatial Analysis Pipeline")
    print("=" * 60)
    
    # Run analyses
    run_hotspot_analysis()
    run_cluster_analysis()
    run_kde_analysis()
    run_ripley_k()
    
    print("\n" + "=" * 60)
    print("✅ SPATIAL ANALYSIS COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()