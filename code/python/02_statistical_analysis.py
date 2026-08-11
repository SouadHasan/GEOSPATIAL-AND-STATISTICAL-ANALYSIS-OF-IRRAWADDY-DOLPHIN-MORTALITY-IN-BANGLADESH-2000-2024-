"""
02_statistical_analysis.py
Statistical Analysis for Irrawaddy Dolphin Mortality Study
Author: Souad Hasan Ishan
Date: November 2025
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import pearsonr, spearmanr, mann_kendall, linregress
import warnings
warnings.filterwarnings('ignore')

# ============================================
# CONFIGURATION
# ============================================
DATA_PATH = '../../data/processed/analysis_ready_data.csv'
OUTPUT_DIR = '../../results/statistical_outputs/'

# ============================================
# FUNCTIONS
# ============================================

def load_data(path):
    """Load processed data."""
    print("📂 Loading processed data...")
    df = pd.read_csv(path)
    print(f"   ✅ Loaded {len(df)} records")
    return df

def descriptive_statistics(df):
    """Calculate comprehensive descriptive statistics."""
    print("\n📊 Calculating descriptive statistics...")
    
    stats = {
        'Variable': [],
        'N': [],
        'Mean': [],
        'Median': [],
        'Std_Dev': [],
        'Min': [],
        'Max': [],
        'CV': []
    }
    
    variables = ['Total_Deaths', 'GiZScore', 'Port_Distance_km', 
                 'Density_Value', 'Risk_Score']
    
    for var in variables:
        if var in df.columns:
            data = df[var].dropna()
            stats['Variable'].append(var)
            stats['N'].append(len(data))
            stats['Mean'].append(data.mean())
            stats['Median'].append(data.median())
            stats['Std_Dev'].append(data.std())
            stats['Min'].append(data.min())
            stats['Max'].append(data.max())
            stats['CV'].append((data.std() / data.mean()) * 100 if data.mean() != 0 else np.nan)
    
    stats_df = pd.DataFrame(stats)
    print(f"   ✅ Descriptive statistics calculated")
    return stats_df

def correlation_analysis(df):
    """Calculate Pearson and Spearman correlation matrices."""
    print("\n📈 Performing correlation analysis...")
    
    variables = ['Total_Deaths', 'GiZScore', 'Port_Distance_km', 
                 'Density_Value', 'Risk_Score']
    
    # Pearson correlation
    pearson_corr = df[variables].corr(method='pearson')
    print(f"   ✅ Pearson correlation calculated")
    
    # Spearman correlation
    spearman_corr = df[variables].corr(method='spearman')
    print(f"   ✅ Spearman correlation calculated")
    
    # P-values for Pearson
    p_values = pd.DataFrame(np.ones_like(pearson_corr), 
                           index=variables, columns=variables)
    for i, var1 in enumerate(variables):
        for j, var2 in enumerate(variables):
            if i != j:
                result = pearsonr(df[var1].dropna(), df[var2].dropna())
                p_values.iloc[i, j] = result.pvalue
    
    return pearson_corr, spearman_corr, p_values

def temporal_trend_analysis(df):
    """Analyze temporal trends in mortality."""
    print("\n⏳ Performing temporal trend analysis...")
    
    # Aggregate by year
    yearly = df.groupby('Year').agg({
        'Total_Deaths': ['sum', 'count', 'mean']
    }).reset_index()
    yearly.columns = ['Year', 'Total_Deaths', 'Event_Count', 'Mean_Deaths']
    
    # Linear regression
    x = yearly['Year'].values
    y = yearly['Total_Deaths'].values
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Mann-Kendall test
    mk_result = mann_kendall(y)
    
    # Pettitt's test for change point detection
    def pettitt_test(data):
        n = len(data)
        U = np.zeros(n)
        for t in range(1, n):
            U[t] = U[t-1]
            for j in range(n):
                if data[j] < data[t]:
                    U[t] += 1
                elif data[j] > data[t]:
                    U[t] -= 1
        k = np.argmax(np.abs(U))
        p_value = 2 * np.exp(-6 * U[k]**2 / (n**3 + n**2))
        return k, p_value
    
    change_point, cp_pvalue = pettitt_test(y)
    
    print(f"   ✅ Temporal analysis complete")
    
    return {
        'yearly_data': yearly,
        'regression': {'slope': slope, 'r_squared': r_value**2, 'p_value': p_value},
        'mann_kendall': {'tau': mk_result.statistic, 'p_value': mk_result.pvalue},
        'change_point': {'year': yearly['Year'].iloc[change_point], 
                        'p_value': cp_pvalue}
    }

def cause_of_death_analysis(df):
    """Analyze cause of death distribution."""
    print("\n🔍 Analyzing cause of death...")
    
    causes = {
        'Entanglement/Bycatch': df['Entanglement_Bycatch'].sum(),
        'Boat Strikes': df['Boat_Strikes'].sum(),
        'Other Causes': df['Other_Causes'].sum()
    }
    
    total = sum(causes.values())
    cause_df = pd.DataFrame({
        'Cause': list(causes.keys()),
        'Deaths': list(causes.values()),
        'Percentage': [v/total*100 for v in causes.values()]
    })
    
    print(f"   ✅ Cause analysis complete")
    return cause_df

def hypothesis_tests(df):
    """Perform key hypothesis tests."""
    print("\n🧪 Performing hypothesis tests...")
    
    results = []
    
    # H1: Bycatch is the primary cause (>60%)
    bycatch_pct = df['Entanglement_Bycatch'].sum() / df['Total_Deaths'].sum()
    h1_result = {
        'Hypothesis': 'H1: Bycatch > 60%',
        'Statistic': bycatch_pct,
        'Result': 'Supported' if bycatch_pct > 0.60 else 'Not Supported'
    }
    results.append(h1_result)
    
    # H2: Negative correlation with port distance
    corr, pval = pearsonr(df['Total_Deaths'], df['Port_Distance_km'])
    h2_result = {
        'Hypothesis': 'H2: Total_Deaths vs Port_Distance (negative)',
        'Statistic': corr,
        'P-value': pval,
        'Result': 'Supported' if corr < -0.3 and pval < 0.05 else 'Not Supported'
    }
    results.append(h2_result)
    
    # H3: Positive temporal trend
    yearly = df.groupby('Year')['Total_Deaths'].sum()
    slope, _, _, pval, _ = linregress(yearly.index, yearly.values)
    h3_result = {
        'Hypothesis': 'H3: Positive temporal trend',
        'Statistic': slope,
        'P-value': pval,
        'Result': 'Supported' if slope > 0 and pval < 0.05 else 'Not Supported'
    }
    results.append(h3_result)
    
    # H4: Spatial clustering (Moran's I > 0.5)
    # Note: Moran's I is calculated in ArcGIS, we reference it here
    h4_result = {
        'Hypothesis': 'H4: Spatial clustering (Moran\'s I > 0.5)',
        'Statistic': 0.782,  # From ArcGIS output
        'Result': 'Supported'  # Already validated
    }
    results.append(h4_result)
    
    results_df = pd.DataFrame(results)
    print(f"   ✅ Hypothesis tests complete")
    return results_df

def save_results(results_dict):
    """Save all statistical results to CSV files."""
    print(f"\n💾 Saving results to {OUTPUT_DIR}...")
    
    import os
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for name, data in results_dict.items():
        if isinstance(data, pd.DataFrame):
            path = f"{OUTPUT_DIR}/{name}.csv"
            data.to_csv(path, index=False)
            print(f"   ✅ Saved: {name}.csv")
        elif isinstance(data, dict):
            # Handle nested dictionaries
            for key, value in data.items():
                if isinstance(value, pd.DataFrame):
                    path = f"{OUTPUT_DIR}/{name}_{key}.csv"
                    value.to_csv(path, index=False)
                    print(f"   ✅ Saved: {name}_{key}.csv")
    
    print(f"\n   📁 All results saved to: {OUTPUT_DIR}")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    print("=" * 60)
    print("🐬 IRRAWADDY DOLPHIN MORTALITY ANALYSIS")
    print("   Statistical Analysis Pipeline")
    print("=" * 60)
    
    # Load data
    df = load_data(DATA_PATH)
    
    # Run analyses
    desc_stats = descriptive_statistics(df)
    pearson_corr, spearman_corr, p_values = correlation_analysis(df)
    temporal_results = temporal_trend_analysis(df)
    cause_results = cause_of_death_analysis(df)
    hypothesis_results = hypothesis_tests(df)
    
    # Compile results
    results = {
        'descriptive_statistics': desc_stats,
        'pearson_correlation': pearson_corr,
        'spearman_correlation': spearman_corr,
        'correlation_pvalues': p_values,
        'cause_of_death': cause_results,
        'hypothesis_tests': hypothesis_results
    }
    
    # Save results
    save_results(results)
    
    print("\n" + "=" * 60)
    print("✅ STATISTICAL ANALYSIS COMPLETE!")
    print("=" * 60)
    
    # Display key findings
    print("\n📊 Key Findings:")
    print(f"   • Total Events: {len(df)}")
    print(f"   • Total Deaths: {df['Total_Deaths'].sum()}")
    print(f"   • Bycatch: {cause_results['Deaths'].iloc[0]} ({cause_results['Percentage'].iloc[0]:.1f}%)")
    print(f"   • Spatial Clustering (Moran's I): 0.782")
    print(f"   • Temporal Trend: {temporal_results['regression']['slope']:.3f} deaths/year")
    print(f"   • Port Distance Correlation: {pearson_corr.loc['Total_Deaths', 'Port_Distance_km']:.3f}")

if __name__ == "__main__":
    main()