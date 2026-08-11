"""
04_risk_modeling.py
Composite Risk Model for Irrawaddy Dolphin Conservation Prioritization
Author: Souad Hasan Ishan
Date: November 2025
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

# ============================================
# CONFIGURATION
# ============================================
DATA_PATH = '../../data/processed/analysis_ready_data.csv'
OUTPUT_DIR = '../../results/risk_scores/'

# ============================================
# FUNCTIONS
# ============================================

def load_data(path):
    """Load processed data."""
    print("📂 Loading data...")
    df = pd.read_csv(path)
    print(f"   ✅ Loaded {len(df)} records")
    return df

def calculate_risk_factors(df):
    """
    Calculate individual risk factor scores (0-1 scale).
    Higher values = higher risk.
    """
    print("\n📊 Calculating risk factors...")
    
    # GiZScore risk: Higher GiZScore = higher risk
    giz_min, giz_max = df['GiZScore'].min(), df['GiZScore'].max()
    df['Risk_GiZScore'] = (df['GiZScore'] - giz_min) / (giz_max - giz_min)
    
    # Port Distance risk: Lower distance = higher risk
    port_min, port_max = df['Port_Distance_km'].min(), df['Port_Distance_km'].max()
    df['Risk_PortDistance'] = 1 - ((df['Port_Distance_km'] - port_min) / (port_max - port_min))
    
    # Density risk: Higher density = higher risk
    dens_min, dens_max = df['Density_Value'].min(), df['Density_Value'].max()
    df['Risk_Density'] = (df['Density_Value'] - dens_min) / (dens_max - dens_min)
    
    print(f"   ✅ Risk factors calculated")
    return df

def calculate_composite_risk(df):
    """
    Calculate composite risk score using weighted sum.
    Weights based on correlation strengths.
    """
    print("\n📊 Calculating composite risk score...")
    
    # Weights based on correlation with mortality
    weights = {
        'Risk_GiZScore': 0.35,
        'Risk_PortDistance': 0.30,
        'Risk_Density': 0.35
    }
    
    df['Risk_Score'] = (
        weights['Risk_GiZScore'] * df['Risk_GiZScore'] +
        weights['Risk_PortDistance'] * df['Risk_PortDistance'] +
        weights['Risk_Density'] * df['Risk_Density']
    )
    
    # Ensure 0-1 range
    df['Risk_Score'] = df['Risk_Score'].clip(0, 1)
    
    print(f"   ✅ Composite risk scores calculated")
    return df, weights

def classify_risk_levels(df):
    """
    Classify risk levels based on composite score.
    Critical: >= 0.7, High: 0.5-0.7, Moderate: < 0.5
    """
    print("\n📊 Classifying risk levels...")
    
    def get_priority(row):
        if row['Risk_Score'] >= 0.7:
            return 'CRITICAL'
        elif row['Risk_Score'] >= 0.5:
            return 'HIGH'
        else:
            return 'MODERATE'
    
    df['Priority_Level'] = df.apply(get_priority, axis=1)
    df['Priority_Code'] = df['Priority_Level'].map({
        'CRITICAL': 3,
        'HIGH': 2,
        'MODERATE': 1
    })
    
    print(f"   ✅ Risk levels classified")
    return df

def create_priority_summary(df):
    """Create summary of priority zones."""
    print("\n📊 Creating priority summary...")
    
    summary = df.groupby('Priority_Level').agg({
        'Total_Deaths': ['sum', 'count', 'mean'],
        'Year': 'count'
    }).reset_index()
    summary.columns = ['Priority_Level', 'Total_Deaths', 'Event_Count', 'Events_Count']
    
    # Add area estimates
    area_mapping = {
        'CRITICAL': 96,
        'HIGH': 51,
        'MODERATE': 57075
    }
    summary['Area_km2'] = summary['Priority_Level'].map(area_mapping)
    summary['Death_Density'] = summary['Total_Deaths'] / summary['Area_km2']
    summary['Pct_Deaths'] = (summary['Total_Deaths'] / summary['Total_Deaths'].sum()) * 100
    summary['Pct_Area'] = (summary['Area_km2'] / summary['Area_km2'].sum()) * 100
    summary['Efficiency_Ratio'] = summary['Pct_Deaths'] / summary['Pct_Area']
    
    print(f"   ✅ Priority summary created")
    return summary

def identify_hotspots(df):
    """Identify top mortality hotspots."""
    print("\n📍 Identifying hotspots...")
    
    # Group by location
    hotspots = df.groupby(['Latitude', 'Longitude', 'Area_Name', 'Region_Type']).agg({
        'Total_Deaths': 'sum',
        'Year': 'count'
    }).reset_index()
    hotspots.columns = ['Latitude', 'Longitude', 'Area_Name', 'Region_Type', 
                       'Total_Deaths', 'Event_Count']
    
    # Sort by deaths
    hotspots = hotspots.sort_values('Total_Deaths', ascending=False)
    hotspots['Rank'] = range(1, len(hotspots) + 1)
    
    print(f"   ✅ {len(hotspots)} hotspots identified")
    return hotspots

def validate_risk_model(df):
    """Validate risk model by comparing predicted vs actual mortality."""
    print("\n📊 Validating risk model...")
    
    from scipy.stats import pearsonr
    
    correlation, p_value = pearsonr(df['Risk_Score'], df['Total_Deaths'])
    
    validation = {
        'Correlation': correlation,
        'P_Value': p_value,
        'R_Squared': correlation ** 2,
        'Significant': 'Yes' if p_value < 0.05 else 'No'
    }
    
    print(f"   ✅ Model validation complete")
    print(f"      • Correlation: {correlation:.3f}")
    print(f"      • R²: {correlation**2:.3f}")
    print(f"      • P-value: {p_value:.6f}")
    
    return validation

def save_results(df, summary, hotspots, validation, output_dir):
    """Save all results to CSV files."""
    print(f"\n💾 Saving results to {output_dir}...")
    
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Save full data with risk scores
    df.to_csv(f'{output_dir}/full_risk_scores.csv', index=False)
    
    # Save priority summary
    summary.to_csv(f'{output_dir}/priority_summary.csv', index=False)
    
    # Save hotspot list
    hotspots.to_csv(f'{output_dir}/hotspot_ranking.csv', index=False)
    
    # Save validation results
    validation_df = pd.DataFrame([validation])
    validation_df.to_csv(f'{output_dir}/model_validation.csv', index=False)
    
    print(f"   ✅ All results saved successfully!")
    print(f"   📁 Data: {output_dir}/full_risk_scores.csv")
    print(f"   📁 Summary: {output_dir}/priority_summary.csv")
    print(f"   📁 Hotspots: {output_dir}/hotspot_ranking.csv")
    print(f"   📁 Validation: {output_dir}/model_validation.csv")

def print_summary(summary):
    """Print formatted summary of priority zones."""
    print("\n" + "=" * 60)
    print("🏆 CONSERVATION PRIORITY ZONES")
    print("=" * 60)
    
    for _, row in summary.iterrows():
        print(f"\n🔴 {row['Priority_Level']} ZONE")
        print(f"   • Area: {row['Area_km2']:.0f} km² ({row['Pct_Area']:.1f}%)")
        print(f"   • Deaths: {row['Total_Deaths']:.0f} ({row['Pct_Deaths']:.1f}%)")
        print(f"   • Density: {row['Death_Density']:.3f} deaths/km²")
        print(f"   • Efficiency: {row['Efficiency_Ratio']:.1f}x")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    print("=" * 60)
    print("🐬 IRRAWADDY DOLPHIN MORTALITY ANALYSIS")
    print("   Composite Risk Modeling Pipeline")
    print("=" * 60)
    
    # Load data
    df = load_data(DATA_PATH)
    
    # Calculate risk factors
    df = calculate_risk_factors(df)
    
    # Calculate composite risk
    df, weights = calculate_composite_risk(df)
    
    # Classify risk levels
    df = classify_risk_levels(df)
    
    # Create summary
    summary = create_priority_summary(df)
    
    # Identify hotspots
    hotspots = identify_hotspots(df)
    
    # Validate model
    validation = validate_risk_model(df)
    
    # Save results
    save_results(df, summary, hotspots, validation, OUTPUT_DIR)
    
    # Print summary
    print_summary(summary)
    
    print("\n" + "=" * 60)
    print("✅ RISK MODELING COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()