# Deployment Guide - Telco Customer Churn Analytics

## Local Setup
1. Clone repo
2. `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows)
4. Install deps: `pip install -r requirements.txt`
5. Launch: `streamlit run app.py`
6. Open browser at `http://localhost:8501`

## Streamlit Community Cloud
1. Push repo to GitHub
2. Go to https://streamlit.io/community-cloud
3. Click "New app" → select repo/branch
4. Set main file: `app.py`
5. Click "Deploy"

## Power BI Integration
- Import `data/processed/telco_churn_clean.csv`
- Use visuals: churn pie, contract bars, tenure histogram
- Add slicers for Contract, InternetService, PaymentMethod

## Notebook Execution
```bash
jupyter notebook notebooks/telco_churn_analysis.ipynb
```
Run all cells sequentially. Requires Python 3.8+.
