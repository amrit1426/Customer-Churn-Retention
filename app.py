"""Telco Customer Churn Analytics - Streamlit Portfolio App"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Telco Churn Analytics", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/processed/telco_churn_clean.csv')

df = load_data()

st.title("📉 Telco Customer Churn & Retention Analytics")
st.markdown("### Customer Churn Retention | Data Analyst Transition")
st.markdown("Real IBM Telco dataset | 7,043 customers | 21 features | 26.5% churn rate")

# Sidebar filters
st.sidebar.header("Filters")
contract_filter = st.sidebar.multiselect("Contract", df['Contract'].unique(), default=df['Contract'].unique())
internet_filter = st.sidebar.multiselect("Internet Service", df['InternetService'].unique(), default=df['InternetService'].unique())

filtered = df[df['Contract'].isin(contract_filter) & df['InternetService'].isin(internet_filter)]

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Customers", f"{len(filtered):,}")
with col2:
    st.metric("Churn Rate", f"{filtered['ChurnBinary'].mean()*100:.1f}%")
with col3:
    st.metric("Avg Monthly Charge", f"INR {filtered['MonthlyCharges'].mean():.2f}")
with col4:
    st.metric("Avg Tenure", f"{filtered['tenure'].mean():.1f} months")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn by Contract")
    contract_churn = filtered.groupby('Contract')['ChurnBinary'].mean() * 100
    fig, ax = plt.subplots(figsize=(8, 4))
    contract_churn.plot(kind='bar', ax=ax, color=['teal', 'steelblue', 'coral'])
    ax.set_ylabel('Churn Rate (%)')
    ax.tick_params(axis='x', rotation=15)
    st.pyplot(fig)
    plt.close()

with col2:
    st.subheader("Churn by Internet Service")
    internet_churn = filtered.groupby('InternetService')['ChurnBinary'].mean() * 100
    fig, ax = plt.subplots(figsize=(8, 4))
    internet_churn.plot(kind='bar', ax=ax, color='purple')
    ax.set_ylabel('Churn Rate (%)')
    st.pyplot(fig)
    plt.close()

# Payment method analysis
st.subheader("Churn by Payment Method")
payment_churn = filtered.groupby('PaymentMethod')['ChurnBinary'].mean() * 100
fig, ax = plt.subplots(figsize=(10, 4))
payment_churn.plot(kind='bar', ax=ax, color='teal')
ax.set_ylabel('Churn Rate (%)')
ax.tick_params(axis='x', rotation=30)
st.pyplot(fig)
plt.close()

# Recommendations
st.subheader("💡 Business Recommendations")
st.markdown("""
1. **Immediate:** Target Month-to-month customers (42.7% churn) with retention offers
2. **Short-term:** Review Fiber optic service quality (41.9% churn)
3. **Medium-term:** Migrate Electronic check users to auto-pay (45.3% churn)
4. **Retention ROI:** 15% save rate → INR 250K annual revenue at 1.79x ROI
""")
