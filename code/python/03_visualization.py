"""
03_visualization.py
Visualization Script for Irrawaddy Dolphin Mortality Study
Author: Souad Hasan Ishan
Date: November 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================
# CONFIGURATION
# ============================================
DATA_PATH = '../../data/processed/analysis_ready_data.csv'
OUTPUT_DIR = '../../docs/figures/'

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
COLORS = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E']

# ============================================
# FUNCTIONS
# ============================================

def load_data(path):
    """Load processed data."""
    print("📂 Loading data...")
    df = pd.read_csv(path)
    print(f"   ✅ Loaded {len(df)} records")
    return df

def plot_regional_comparison(df, output_path):
    """Create regional comparison bar chart."""
    print("\n📊 Creating regional comparison plot...")
    
    regional = df.groupby('Region_Type')['Total_Deaths'].sum().reset_index()
    regional = regional.sort_values('Total_Deaths', ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.barh(regional['Region_Type'], regional['Total_Deaths'], 
                   color=COLORS[:3], edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for bar, value in zip(bars, regional['Total_Deaths']):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{value} deaths', va='center', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('Total Deaths', fontsize=12, fontweight='bold')
    ax.set_ylabel('Region Type', fontsize=12, fontweight='bold')
    ax.set_title('Regional Comparison of Irrawaddy Dolphin Mortality\n(2000-2024)', 
                 fontsize=14, fontweight='bold')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/figure_4.2-1_regional_comparison.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"   ✅ Saved: figure_4.2-1_regional_comparison.png")

def plot_temporal_trends(df, output_path):
    """Create temporal trends plot."""
    print("\n📈 Creating temporal trends plot...")
    
    yearly = df.groupby('Year').agg({
        'Total_Deaths': ['sum', 'mean']
    }).reset_index()
    yearly.columns = ['Year', 'Total_Deaths', 'Mean_Deaths']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Subplot 1: Total Deaths
    ax1.bar(yearly['Year'], yearly['Total_Deaths'], 
            color=COLORS[0], alpha=0.7, edgecolor='black')
    ax1.plot(yearly['Year'], yearly['Total_Deaths'], 
             color='red', marker='o', linestyle='-', linewidth=2, 
             markersize=8, label='Trend')
    
    # Add trend line
    z = np.polyfit(yearly['Year'], yearly['Total_Deaths'], 1)
    p = np.poly1d(z)
    ax1.plot(yearly['Year'], p(yearly['Year']), 
             '--', color='darkred', linewidth=2, label='Linear Trend')
    
    ax1.set_xlabel('Year', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Total Deaths', fontsize=11, fontweight='bold')
    ax1.set_title('Annual Dolphin Deaths (2000-2024)', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Mean Deaths per Event
    ax2.bar(yearly['Year'], yearly['Mean_Deaths'], 
            color=COLORS[1], alpha=0.7, edgecolor='black')
    ax2.plot(yearly['Year'], yearly['Mean_Deaths'], 
             color='darkblue', marker='s', linestyle='-', linewidth=2, 
             markersize=8, label='Mean')
    
    ax2.set_xlabel('Year', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Mean Deaths per Event', fontsize=11, fontweight='bold')
    ax2.set_title('Event Severity Trend (2000-2024)', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/figure_4.5-1_temporal_trends.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"   ✅ Saved: figure_4.5-1_temporal_trends.png")

def plot_correlation_matrix(df, output_path):
    """Create correlation matrix heatmap."""
    print("\n📊 Creating correlation matrix plot...")
    
    variables = ['Total_Deaths', 'GiZScore', 'Port_Distance_km', 
                 'Density_Value', 'Risk_Score']
    
    corr = df[variables].corr()
    
    # Mask upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Custom heatmap
    cmap = sns.diverging_palette(250, 10, as_cmap=True)
    heatmap = sns.heatmap(corr, mask=mask, annot=True, fmt='.3f', 
                          cmap=cmap, square=True, linewidths=1,
                          cbar_kws={'shrink': 0.8, 'label': 'Correlation'})
    
    # Customize labels
    ax.set_xticklabels(['Total Deaths', 'GiZScore', 'Port Distance', 
                        'Density', 'Risk Score'], rotation=45, ha='right')
    ax.set_yticklabels(['Total Deaths', 'GiZScore', 'Port Distance', 
                        'Density', 'Risk Score'], rotation=0)
    
    ax.set_title('Dolphin Mortality - Risk Factor Correlation Matrix\n(Pearson)', 
                 fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/figure_4.7-1_correlation_matrix.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"   ✅ Saved: figure_4.7-1_correlation_matrix.png")

def plot_risk_mortality_relationship(df, output_path):
    """Create risk score vs mortality scatter plot."""
    print("\n📊 Creating risk-mortality relationship plot...")
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Scatter plot
    scatter = ax.scatter(df['Risk_Score'], df['Total_Deaths'], 
                         c=df['Total_Deaths'], cmap='Reds', 
                         s=df['Total_Deaths']*20 + 30, alpha=0.7, 
                         edgecolors='black', linewidth=1)
    
    # Add trend line
    z = np.polyfit(df['Risk_Score'], df['Total_Deaths'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(df['Risk_Score'].min(), df['Risk_Score'].max(), 100)
    ax.plot(x_line, p(x_line), '--', color='darkred', linewidth=2, 
            label=f'Trend (r²={z[0]**.2:.3f})')
    
    # Add reference lines
    ax.axvline(x=0.5, color='gray', linestyle=':', alpha=0.5, 
               label='Moderate Risk Threshold')
    ax.axvline(x=0.7, color='red', linestyle=':', alpha=0.5, 
               label='High Risk Threshold')
    
    ax.set_xlabel('Composite Risk Score', fontsize=12, fontweight='bold')
    ax.set_ylabel('Dolphin Mortality Count', fontsize=12, fontweight='bold')
    ax.set_title('Relationship Between Risk Score and Dolphin Mortality\n(2000-2024)', 
                 fontsize=14, fontweight='bold')
    
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    # Add colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label('Mortality Count', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/figure_4.8-1_risk_mortality_relationship.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"   ✅ Saved: figure_4.8-1_risk_mortality_relationship.png")

def plot_cause_of_death(df, output_path):
    """Create cause of death pie chart and bar chart."""
    print("\n📊 Creating cause of death plots...")
    
    causes = {
        'Entanglement/Bycatch': df['Entanglement_Bycatch'].sum(),
        'Boat Strikes': df['Boat_Strikes'].sum(),
        'Other Causes': df['Other_Causes'].sum()
    }
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Pie chart
    colors = ['#2E86AB', '#A23B72', '#F18F01']
    wedges, texts, autotexts = ax1.pie(causes.values(), 
                                        labels=causes.keys(),
                                        autopct='%1.1f%%',
                                        colors=colors,
                                        startangle=90,
                                        wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)
    
    ax1.set_title('Cause of Death Distribution\n(2000-2024)', fontsize=12, fontweight='bold')
    
    # Bar chart
    bars = ax2.bar(causes.keys(), causes.values(), 
                   color=colors, edgecolor='black', linewidth=1.5)
    
    for bar, value in zip(bars, causes.values()):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{value} deaths', ha='center', va='bottom', 
                fontsize=11, fontweight='bold')
    
    ax2.set_ylabel('Number of Deaths', fontsize=11, fontweight='bold')
    ax2.set_title('Cause of Death Counts\n(2000-2024)', fontsize=12, fontweight='bold')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/figure_4.6-1_cause_of_death.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"   ✅ Saved: figure_4.6-1_cause_of_death.png")

def plot_priority_zones(df, output_path):
    """Create conservation priority zones visualization."""
    print("\n📊 Creating priority zones plot...")
    
    # Define priority thresholds
    def classify_priority(row):
        if row['Risk_Score'] >= 0.7:
            return 'Critical'
        elif row['Risk_Score'] >= 0.5:
            return 'High'
        else:
            return 'Moderate'
    
    df['Priority'] = df.apply(classify_priority, axis=1)
    
    # Count by priority
    priority_counts = df.groupby('Priority').agg({
        'Total_Deaths': ['sum', 'count'],
        'Year': 'count'
    }).reset_index()
    priority_counts.columns = ['Priority', 'Total_Deaths', 'Event_Count', 'Events_Count']
    
    # Calculate area (simplified)
    priority_areas = {
        'Critical': 96,  # km²
        'High': 51,      # km²
        'Moderate': 57075 # km²
    }
    priority_counts['Area_km2'] = priority_counts['Priority'].map(priority_areas)
    priority_counts['Death_Density'] = priority_counts['Total_Deaths'] / priority_counts['Area_km2']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Bar chart: Deaths by priority
    colors = ['#C73E1D', '#F18F01', '#2E86AB']
    bars = ax1.bar(priority_counts['Priority'], priority_counts['Total_Deaths'], 
                   color=colors, edgecolor='black', linewidth=1.5)
    
    for bar, value in zip(bars, priority_counts['Total_Deaths']):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{value} deaths\n({value/df["Total_Deaths"].sum()*100:.1f}%)', 
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax1.set_ylabel('Total Deaths', fontsize=11, fontweight='bold')
    ax1.set_title('Mortality by Priority Zone', fontsize=12, fontweight='bold')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Bar chart: Death density
    bars2 = ax2.bar(priority_counts['Priority'], priority_counts['Death_Density'],
                    color=colors, edgecolor='black', linewidth=1.5)
    
    for bar, value in zip(bars2, priority_counts['Death_Density']):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{value:.3f}\ndeaths/km²', ha='center', va='bottom', 
                fontsize=10, fontweight='bold')
    
    ax2.set_ylabel('Death Density (deaths/km²)', fontsize=11, fontweight='bold')
    ax2.set_title('Conservation Efficiency by Zone', fontsize=12, fontweight='bold')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/figure_4.8-2_priority_zones.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"   ✅ Saved: figure_4.8-2_priority_zones.png")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    print("=" * 60)
    print("🐬 IRRAWADDY DOLPHIN MORTALITY ANALYSIS")
    print("   Visualization Pipeline")
    print("=" * 60)
    
    # Create output directory
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    # Load data
    df = load_data(DATA_PATH)
    
    # Generate plots
    plot_regional_comparison(df, OUTPUT_DIR)
    plot_temporal_trends(df, OUTPUT_DIR)
    plot_correlation_matrix(df, OUTPUT_DIR)
    plot_risk_mortality_relationship(df, OUTPUT_DIR)
    plot_cause_of_death(df, OUTPUT_DIR)
    plot_priority_zones(df, OUTPUT_DIR)
    
    print("\n" + "=" * 60)
    print("✅ VISUALIZATION COMPLETE!")
    print(f"   📁 All figures saved to: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()