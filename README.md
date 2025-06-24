# EV Market Intelligence Suite

## Overview
This project is a comprehensive analytics suite designed to decode the competitive electric vehicle (EV) market using Python and Power BI. It combines clustering algorithms, custom KPIs, strategic risk assessment, and machine learning-based feature evaluation to support data-driven marketing, infrastructure, and product decisions.

---

## Business Objective
The EV market is rapidly expanding, but raw specifications alone don't reflect customer fit, efficiency, or infrastructure needs. This project transforms complex EV specs into actionable business insights to assist:

- **Marketing Teams** in identifying product-market fit through buyer personas
- **Energy and Infrastructure Providers** in pinpointing high-risk charging demand zones
- **Product and Strategy Units** in benchmarking efficiency and feature importance

---

## Data Source
Electric vehicle specifications (2025 projected models) including:

- Performance: top speed, acceleration, torque
- Battery: capacity, charging power, efficiency
- Design: drivetrain, dimensions, cargo volume, seating
- Range and utility metrics

---

## Tools Used
- **Python** (Pandas, Scikit-learn, Matplotlib, Seaborn)
- **Power BI** (for visual storytelling and dashboards)
- **Jupyter / PyCharm** (for ETL, modeling)
- **openpyxl** (to export processed data to Excel)

---

## Workflow Summary

### 1. **Data Cleaning & ETL**
- Removed unneeded columns (e.g., URLs)
- Handled units, missing values, and non-numeric entries
- Derived new metrics (e.g., km/kWh, range per charge power)

### 2. **Buyer Persona Clustering**
- **Goal:** Segment EVs by use-case (Urban, Performance, Family, Utility)
- **Method:** KMeans clustering on behavioral and design metrics
- **Result:** EVs grouped based on lifestyle fit, not just specs

### 3. **Range-per-kWh Benchmarking**
- **Goal:** Identify EVs offering the best range per battery unit
- **Insight:** Highlights value-focused models and engineering efficiency

### 4. **Charging Infrastructure Risk Mapping**
- **Goal:** Flag vehicles that are range-limited and charge slowly
- **Metric:** `range_km / fast_charging_power_kw_dc`
- **Outcome:** Strategic guidance for cities and charging networks

### 5. **Feature Importance Modeling**
- **Goal:** Understand which vehicle specs most strongly influence driving range
- **Model:** Random Forest Regression with One-Hot Encoding for categorical data
- **Insight:** Ranked impact of features like battery size, efficiency, drivetrain, cargo volume, and acceleration on EV range

---

## Power BI Dashboard Highlights

### **Page 1: EV Buyer Personas**
- Cluster comparison visuals (e.g., range, seats, acceleration)
- Drivetrain breakdown by persona
- Efficiency cards per segment

### **Page 2: EV Value & Efficiency Index**
- Top 10 EVs by range-per-kWh
- Drivetrain and segment filtering
- Value-based visual storytelling

### **Page 3: Charging Risk Strategy**
- Charging Power vs Range scatterplot
- High-risk model table (lowest range-per-charge power)
- KPI cards and filters for body type, brand, and drivetrain

---

## What Makes This Unique
- Combines technical data modeling with **real-world business framing**
- Every model serves a specific **stakeholder decision use-case**
- Balances exploratory analytics with storytelling and visual insights

---

## How to Use
1. Run `etl.py` to clean and prepare the dataset
2. Use individual scripts (`clustering.py`, `efficiency_ranking.py`, etc.) to generate insights
3. Load the `.xlsx` outputs into Power BI
4. Explore dashboards to identify strategic recommendations

---

## Author
Rakibul Hasan Shovon  
Graduate Student | Business Analytics | Marketing Strategy  
University of Wisconsin-Milwaukee

---

## License
This project is for educational and demonstration purposes.
