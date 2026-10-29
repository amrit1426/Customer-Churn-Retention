"""Telco Customer Churn - Complete Analysis Pipeline"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utilities import churn_rate_by_group, retention_roi, statistical_tests

plt.style.use('seaborn-v0_8-whitegrid')
os.makedirs('reports/figures', exist_ok=True)

def main():
    df = pd.read_csv('data/processed/telco_churn_clean.csv')
    
    print("="*60)
    print("TELCO CUSTOMER CHURN - EXECUTIVE SUMMARY")
    print("="*60)
    print(f"Total Customers:       {len(df):,}")
    print(f"Churn Rate:            {df['ChurnBinary'].mean()*100:.2f}%")
    print(f"Churned Customers:     {df['ChurnBinary'].sum():,}")
    print(f"Retained Customers:    {(df['ChurnBinary']==0).sum():,}")
    print(f"Avg Monthly Charge:    INR {df['MonthlyCharges'].mean():.2f}")
    print(f"Avg Tenure:            {df['tenure'].mean():.1f} months")
    print("="*60)
    
    # Churn by contract
    contract_churn = churn_rate_by_group(df, 'Contract')
    print("\nChurn by Contract:")
    print(contract_churn)
    
    # Churn by internet service
    internet_churn = churn_rate_by_group(df, 'InternetService')
    print("\nChurn by Internet Service:")
    print(internet_churn)
    
    # Churn by payment method
    payment_churn = churn_rate_by_group(df, 'PaymentMethod')
    print("\nChurn by Payment Method:")
    print(payment_churn)
    
    # Statistical tests
    tests = statistical_tests(df)
    print(f"\nT-test (Tenure): t={tests['tenure_t_stat']:.3f}, p={tests['tenure_p_value']:.4f}")
    print(f"Chi-square (Contract vs Churn): chi2={tests['chi2_stat']:.3f}, p={tests['chi2_p_value']:.4f}")
    
    # ROI calculation
    roi = retention_roi(df)
    print(f"\nRetention Campaign ROI (15% save rate):")
    print(f"  Potential savers:     {roi['potential_savers']:.0f}")
    print(f"  Revenue saved:        INR {roi['revenue_saved']:,.0f}")
    print(f"  Campaign cost:        INR {roi['campaign_cost']:,.0f}")
    print(f"  ROI:                  {roi['roi']:.2f}x")
    
    # Generate visualizations
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Churn distribution
    churn_counts = df['Churn'].value_counts()
    churn_counts.plot(kind='pie', ax=axes[0,0], labels=['Retained', 'Churned'], 
                      autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
    axes[0,0].set_title('Customer Churn Distribution')
    
    # Churn by contract
    contract_churn['mean'].plot(kind='bar', ax=axes[0,1], color=['teal', 'steelblue', 'coral'])
    axes[0,1].set_title('Churn Rate by Contract Type')
    axes[0,1].set_ylabel('Churn Rate')
    axes[0,1].tick_params(axis='x', rotation=15)
    
    # Churn by internet service
    internet_churn['mean'].plot(kind='bar', ax=axes[1,0], color='purple')
    axes[1,0].set_title('Churn Rate by Internet Service')
    axes[1,0].set_ylabel('Churn Rate')
    axes[1,0].tick_params(axis='x', rotation=0)
    
    # Tenure distribution
    df[df['Churn']=='No']['tenure'].hist(ax=axes[1,1], bins=30, alpha=0.6, label='Retained', color='green')
    df[df['Churn']=='Yes']['tenure'].hist(ax=axes[1,1], bins=30, alpha=0.6, label='Churned', color='red')
    axes[1,1].set_title('Tenure Distribution')
    axes[1,1].set_xlabel('Tenure (months)')
    axes[1,1].set_ylabel('Count')
    axes[1,1].legend()
    
    plt.tight_layout()
    plt.savefig('reports/figures/churn_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("\nSaved: reports/figures/churn_analysis.png")
    
    # Revenue impact
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    revenue_impact = df[df['Churn']=='Yes'].groupby('Contract')['MonthlyCharges'].sum()
    revenue_impact.plot(kind='bar', ax=axes[0], color='darkred')
    axes[0].set_title('Monthly Revenue Lost by Contract')
    axes[0].set_ylabel('Monthly Charges')
    axes[0].tick_params(axis='x', rotation=15)
    
    avg_charges = pd.DataFrame({
        'Retained': [df[df['Churn']=='No']['MonthlyCharges'].mean()],
        'Churned': [df[df['Churn']=='Yes']['MonthlyCharges'].mean()]
    })
    avg_charges.plot(kind='bar', ax=axes[1], color=['green', 'red'])
    axes[1].set_title('Avg Monthly Charges')
    axes[1].set_ylabel('INR')
    axes[1].tick_params(axis='x', rotation=0)
    
    plt.tight_layout()
    plt.savefig('reports/figures/revenue_impact.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: reports/figures/revenue_impact.png")
    
    # Service analysis
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    df['tenure_bin'] = pd.cut(df['tenure'], bins=[0, 12, 24, 36, 48, 60, 72], labels=['0-12', '13-24', '25-36', '37-48', '49-60', '61-72'])
    tenure_churn = df.groupby('tenure_bin')['ChurnBinary'].mean() * 100
    tenure_churn.plot(kind='bar', ax=axes[0,0], color='orange')
    axes[0,0].set_title('Churn Rate by Tenure Group')
    axes[0,0].set_ylabel('Churn Rate (%)')
    
    payment_churn['mean'].plot(kind='bar', ax=axes[0,1], color='teal')
    axes[0,1].set_title('Churn Rate by Payment Method')
    axes[0,1].set_ylabel('Churn Rate (%)')
    axes[0,1].tick_params(axis='x', rotation=30)
    
    paperless_churn = churn_rate_by_group(df, 'PaperlessBilling')
    paperless_churn['mean'].plot(kind='bar', ax=axes[1,0], color=['blue', 'orange'])
    axes[1,0].set_title('Churn Rate by Paperless Billing')
    axes[1,0].set_ylabel('Churn Rate (%)')
    
    senior_churn = churn_rate_by_group(df, 'SeniorCitizen')
    senior_churn['mean'].plot(kind='bar', ax=axes[1,1], color=['green', 'red'])
    axes[1,1].set_title('Churn Rate by Senior Citizen')
    axes[1,1].set_ylabel('Churn Rate (%)')
    axes[1,1].set_xticklabels(['No', 'Yes'], rotation=0)
    
    plt.tight_layout()
    plt.savefig('reports/figures/service_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: reports/figures/service_analysis.png")
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
