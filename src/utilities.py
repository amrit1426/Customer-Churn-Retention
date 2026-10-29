"""Utility functions for Telco Customer Churn analysis."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

plt.style.use('seaborn-v0_8-whitegrid')

def load_data(path='data/processed/telco_churn_clean.csv'):
    return pd.read_csv(path)

def churn_rate_by_group(df, group_col):
    return df.groupby(group_col)['ChurnBinary'].agg(['count', 'sum', 'mean']).round(3)

def retention_roi(df, save_rate=0.15, campaign_cost_per_customer=500):
    churned = df[df['Churn'] == 'Yes']
    avg_monthly = churned['MonthlyCharges'].mean()
    potential_savers = len(churned) * save_rate
    revenue_saved = potential_savers * avg_monthly * 12
    campaign_cost = potential_savers * campaign_cost_per_customer
    roi = revenue_saved / campaign_cost if campaign_cost > 0 else 0
    return {
        'potential_savers': potential_savers,
        'revenue_saved': revenue_saved,
        'campaign_cost': campaign_cost,
        'roi': roi
    }

def statistical_tests(df):
    # T-test: tenure between churned and retained
    tenure_churned = df[df['Churn'] == 'Yes']['tenure']
    tenure_retained = df[df['Churn'] == 'No']['tenure']
    t_stat, t_p = stats.ttest_ind(tenure_churned, tenure_retained)
    
    # Chi-square: contract vs churn
    contingency = pd.crosstab(df['Contract'], df['Churn'])
    chi2, chi2_p, dof, expected = stats.chi2_contingency(contingency)
    
    return {
        'tenure_t_stat': t_stat,
        'tenure_p_value': t_p,
        'chi2_stat': chi2,
        'chi2_p_value': chi2_p,
        'tenure_churned_mean': tenure_churned.mean(),
        'tenure_retained_mean': tenure_retained.mean()
    }
