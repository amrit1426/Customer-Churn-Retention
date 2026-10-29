# 📉 Telco Customer Churn & Retention Analytics

**Customer Churn Retention | Telecom Data Analytics**

---

## Business Problem

Customer churn is one of the most critical challenges in telecommunications. With high acquisition costs and intense competition, retaining existing customers is significantly more cost-effective than acquiring new ones. This project analyzes 7,043 customer records to identify churn drivers, quantify revenue at risk, segment customers by risk level, and design a data-backed retention strategy.

## Intended Stakeholder

- **Primary:** Head of Customer Retention / VP of Customer Experience
- **Secondary:** Marketing team, Account managers, Finance team

## Business Questions

1. What is the overall churn rate and annual revenue impact?
2. Which customer segments have the highest churn probability?
3. What contractual, service, and behavioral factors drive churn?
4. Can we identify at-risk customers before they churn?
5. What is the expected ROI of a targeted retention campaign?

## Key Performance Indicators (KPIs)

- Overall churn rate (%)
- Monthly/Annual revenue at risk (INR)
- Churn rate by contract type, internet service, payment method
- Average tenure: churned vs retained
- Retention campaign ROI
- Statistical significance of churn drivers

## Dataset Source

- **Source:** IBM Telco Customer Churn Dataset
- **URL:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- **License:** CC BY-NC-SA 4.0 (Educational use)
- **Size:** 7,043 rows × 21 columns
- **Raw file:** `data/raw/telco_churn_raw.csv`
- **Processed file:** `data/processed/telco_churn_clean.csv`

## Tools and Skills Demonstrated

- Python (pandas, numpy, matplotlib, seaborn, scipy)
- SQL (SQLite for analytical views)
- Statistical analysis (t-tests, Chi-square, correlation)
- Data visualization and storytelling
- Business impact quantification
- Streamlit app deployment
- Jupyter notebook development

## Project Structure

```
TelcoCustomerChurn_Retention/
├── data/
│   ├── raw/
│   │   └── telco_churn_raw.csv
│   └── processed/
│       └── telco_churn_clean.csv
├── notebooks/
│   └── telco_churn_analysis.ipynb
├── reports/
│   └── figures/
│       ├── churn_analysis.png
│       ├── revenue_impact.png
│       └── service_analysis.png
├── src/
│   └── utilities.py
├── scripts/
│   └── run_analysis.py
├── app.py
├── requirements.txt
├── .gitignore
├── deployment_guide.md
└── README.md
```

## Setup and Execution

### Local Setup
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Run Analysis Script
```bash
python scripts/run_analysis.py
```

### Launch Streamlit App
```bash
streamlit run app.py
```

### Open Jupyter Notebook
```bash
jupyter notebook notebooks/telco_churn_analysis.ipynb
```

## Key Findings

| Metric | Value |
|--------|-------|
| Overall Churn Rate | 26.54% |
| Churned Customers | 1,869 |
| Monthly Revenue Lost | INR 257,138 |
| Annual Revenue Lost | INR 3,085,661 |
| Avg Tenure (Churned) | 18.7 months |
| Avg Tenure (Retained) | 32.4 months |

### Critical Insights
1. **Month-to-month customers** churn at 42.7% vs 2.8% for Two-year contracts
2. **Fiber optic users** have 41.9% churn vs 19.0% for DSL
3. **Electronic check payment** users show 45.3% churn rate
4. **Tenure is significant**: churned customers average 18.7 months vs retained 32.4 months (t-test p<0.001)
5. **Contract type** is highly significant predictor (Chi-square p<0.001)

## Business Recommendations

### Immediate (0-30 days)
- Target Month-to-month customers with retention offers
- Review Fiber optic service quality issues
- Improve payment onboarding for Electronic check users

### Short-term (30-90 days)
- Launch retention campaign for high-risk customers
- Tech support expansion for excluded customers
- Loyalty program to drive annual contract migration

### Medium-term (90-180 days)
- Predictive churn model integration into CRM
- Customer health scoring dashboard
- Contract migration strategy with discounts

### Retention Campaign ROI
- Potential savers: 280 customers (15% save rate)
- Annual revenue saved: INR 250,436
- Campaign cost: INR 140,175
- Expected ROI: 1.79x

## Limitations

- Dataset is from a fictional California telco (IBM sample data)
- Does not represent actual operator data
- Limited to 21 features; real-world data may include more behavioral signals
- No actual campaign execution data; ROI is modeled

## Next Steps

- Add more recent/public telecom datasets (TRAI, T-Mobile, etc.)
- Build predictive model with scikit-learn/XGBoost
- Deploy on Streamlit Community Cloud
- Create Power BI dashboard version
