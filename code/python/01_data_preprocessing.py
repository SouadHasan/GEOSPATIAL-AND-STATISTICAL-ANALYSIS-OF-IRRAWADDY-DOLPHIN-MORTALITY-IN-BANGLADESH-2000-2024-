"""
01_data_preprocessing.py
Data Preprocessing Script for Irrawaddy Dolphin Mortality Analysis
Author: Souad Hasan Ishan
Date: November 2025
"""

import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================
# CONFIGURATION
# ============================================
RAW_DATA_PATH = Path('../../data/raw/mortality_events_2000-2024.csv')
PORT_DATA_PATH = Path('../../data/raw/port_locations.csv')
OUTPUT_PATH = Path('../../data/processed/analysis_ready_data.csv')

# ============================================
# FUNCTIONS
# ============================================

def load_data():
    """Load raw mortality and port data."""
    print("📂 Loading data...")
    
    mortality_df = pd.read_csv(RAW_DATA_PATH)
    ports_df = pd.read_csv(PORT_DATA_PATH)
    
    print(f"   ✅ Loaded {len(mortality_df)} mortality events")
    print(f"   ✅ Loaded {len(ports_df)} port locations")
    
    return mortality_df, ports_df

def clean_mortality_data(df):
    """Clean and validate mortality data."""
    print("\n🧹 Cleaning mortality data...")
    
    # Remove duplicates
    initial_len = len(df)
    df = df.drop_duplicates(subset=['Year', 'Latitude', 'Longitude'])
    print(f"   Removed {initial_len - len(df)} duplicates")
    
    # Validate coordinates
    df = df[(df['Latitude'].between(20.5, 23.5)) & 
            (df['Longitude'].between(89.0, 92.5))]
    print(f"   Validated coordinates: {len(df)} events remain")
    
    # Ensure positive death counts
    df['Total_Deaths'] = df['Total_Deaths'].clip(lower=1)
    
    # Fill missing values
    df['Entanglement_Bycatch'] = df['Entanglement_Bycatch'].fillna(0).astype(int)
    df['Boat_Strikes'] = df['Boat_Strikes'].fillna(0).astype(int)
    df['Other_Causes'] = df['Other_Causes'].fillna(0).astype(int)
    
    return df

def calculate_port_distance(df, ports_df):
    """
    Calculate distance from each mortality event to nearest port.
    Uses haversine formula for geographic distance.
    """
    print("\n📏 Calculating port distances...")
    
    def haversine(lat1, lon1, lat2, lon2):
        """Calculate great-circle distance between two points."""
        R = 6371  # Earth's radius in kilometers
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))
        return R * c
    
    distances = []
    
    for _, row in df.iterrows():
        min_dist = np.inf
        for _, port in ports_df.iterrows():
            dist = haversine(row['Latitude'], row['Longitude'],
                           port['Latitude'], port['Longitude'])
            min_dist = min(min_dist, dist)
        distances.append(min_dist)
    
    df['Port_Distance_km'] = distances
    print(f"   ✅ Port distances calculated (mean: {np.mean(distances):.2f} km)")
    
    return df

def create_summary_stats(df):
    """Create summary statistics table."""
    print("\n📊 Generating summary statistics...")
    
    stats = {
        'Total Events': len(df),
        'Total Deaths': df['Total_Deaths'].sum(),
        'Mean Deaths/Event': df['Total_Deaths'].mean(),
        'Median Deaths/Event': df['Total_Deaths'].median(),
        'Std Deviation': df['Total_Deaths'].std(),
        'Max Single Event': df['Total_Deaths'].max(),
        'Min Single Event': df['Total_Deaths'].min(),
        'Bycatch Total': df['Entanglement_Bycatch'].sum(),
        'Boat Strikes Total': df['Boat_Strikes'].sum(),
        'Other Causes Total': df['Other_Causes'].sum(),
        'Study Duration': f"{df['Year'].min()}-{df['Year'].max()}"
    }
    
    stats_df = pd.DataFrame([stats])
    print(f"   ✅ Summary statistics created")
    
    return stats_df

def save_data(df, stats_df, output_path):
    """Save processed data and summary statistics."""
    print(f"\n💾 Saving data to {output_path}...")
    
    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save main data
    df.to_csv(output_path, index=False)
    
    # Save summary stats
    stats_path = output_path.parent / 'summary_statistics.csv'
    stats_df.to_csv(stats_path, index=False)
    
    print(f"   ✅ Data saved successfully!")
    print(f"   📁 Main data: {output_path}")
    print(f"   📁 Statistics: {stats_path}")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    print("=" * 60)
    print("🐬 IRRAWADDY DOLPHIN MORTALITY ANALYSIS")
    print("   Data Preprocessing Pipeline")
    print("=" * 60)
    
    # Step 1: Load data
    mortality_df, ports_df = load_data()
    
    # Step 2: Clean data
    mortality_df = clean_mortality_data(mortality_df)
    
    # Step 3: Calculate port distances
    mortality_df = calculate_port_distance(mortality_df, ports_df)
    
    # Step 4: Create summary statistics
    stats_df = create_summary_stats(mortality_df)
    
    # Step 5: Save data
    save_data(mortality_df, stats_df, OUTPUT_PATH)
    
    print("\n" + "=" * 60)
    print("✅ DATA PREPROCESSING COMPLETE!")
    print("=" * 60)
    
    # Display summary
    print("\n📊 Quick Summary:")
    print(f"   • Total Events: {len(mortality_df)}")
    print(f"   • Total Deaths: {mortality_df['Total_Deaths'].sum()}")
    print(f"   • Mean Deaths/Event: {mortality_df['Total_Deaths'].mean():.2f}")
    print(f"   • Bycatch: {mortality_df['Entanglement_Bycatch'].sum()} deaths")
    print(f"   • Vessel Strikes: {mortality_df['Boat_Strikes'].sum()} deaths")
    print(f"   • Port Distance (mean): {mortality_df['Port_Distance_km'].mean():.2f} km")

if __name__ == "__main__":
    main()