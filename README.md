# SITNovate

https://colab.research.google.com/drive/1uSwUoWbes46Ua8ZPC4FChxal_p9KDFfB?usp=sharing

📌 1️⃣ Project Overview
Superstore Sales Forecasting is a time-series analysis project that predicts future sales trends using SARIMA and Holt-Winters Exponential Smoothing.
This project helps businesses optimize inventory planning, forecast demand, and increase profitability.

📌 2️⃣ Dataset Details
Source: Retail Superstore Data (2015–2024)
Time Frame: Monthly Aggregated Sales Data
Columns Used:
Order Date → Transaction Date
Sales → Revenue Generated
Month, Year → Extracted from Order Date
Category, Sub-Category, Region → Sales Segmentation
📌 3️⃣ Models Used
We implemented and compared two forecasting techniques:
1️⃣ SARIMA (Seasonal ARIMA) → Captures seasonal patterns
2️⃣ Holt-Winters Exponential Smoothing → Best for trending & seasonal data

📌 4️⃣ Installation & Requirements
Run the following command to install dependencies:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn statsmodels pmdarima scikit-learn
Required Libraries

python
Copy
Edit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from pmdarima import auto_arima
from sklearn.metrics import mean_absolute_error, mean_squared_error
📌 5️⃣ How to Run the Code
Step 1: Load the Dataset
Modify FINAL_DATASET.csv in pd.read_csv():

python
Copy
Edit
df = pd.read_csv("FINAL_DATASET.csv", parse_dates=["Order Date"], dayfirst=True)
Step 2: Preprocess Data
Convert to monthly aggregated sales:

python
Copy
Edit
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
Step 3: Run SARIMA & Holt-Winters
Execute the script:

bash
Copy
Edit
python sales_forecasting.py
