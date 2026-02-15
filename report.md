# Crop Yield Prediction in Tanzania

## Machine Learning Project Report

---

### 1. Introduction

Agriculture is the backbone of Tanzania's economy, contributing to over 25% of the national GDP and employing the majority of the rural population. However, many farmers lack access to tools that can help them estimate their expected crop yield based on environmental and farming conditions.

This project aims to solve this problem by building a machine learning model that predicts **crop yield (kg per acre)** based on factors such as rainfall, temperature, fertilizer usage, soil type, farm size, and irrigation availability. Two models — **Linear Regression** and **Decision Tree** — were trained, evaluated, and compared. The best-performing model was then deployed as a web application using Streamlit, allowing users to input farming conditions and receive instant yield predictions.

---

### 2. Dataset Description

A synthetic dataset of **500 records** was created to simulate realistic Tanzanian farming conditions. The dataset contains the following 9 columns:

| Column             | Type        | Description                          |
|--------------------|-------------|--------------------------------------|
| region             | Categorical | Tanzanian region (Dodoma, Arusha, Mbeya, Morogoro, Iringa) |
| crop_type          | Categorical | Type of crop (Maize, Rice, Wheat, Cassava, Beans) |
| farm_size_acres    | Numeric     | Size of the farm in acres (0.5 – 20) |
| rainfall_mm        | Numeric     | Annual rainfall in millimeters (300 – 1800) |
| temperature_c      | Numeric     | Average temperature in °C (18 – 33)  |
| fertilizer_kg      | Numeric     | Amount of fertilizer used in kg (0 – 180) |
| soil_type          | Categorical | Type of soil (Clay, Loam, Sandy)     |
| irrigation         | Binary      | Whether irrigation is available (0 = No, 1 = Yes) |
| yield_kg_per_acre  | Numeric     | **Target variable** — crop yield in kg/acre |

The dataset contained **30 missing values** spread across rainfall, temperature, and fertilizer columns, which were handled during preprocessing.

---

### 3. Methodology

The project followed a standard machine learning pipeline:

**Step 1 — Data Preprocessing:**
- Missing values were filled using the **mean** of each respective column.
- Categorical columns (region, crop_type, soil_type) were encoded using **LabelEncoder**.
- The dataset was split into **80% training** and **20% testing** sets.

**Step 2 — Model Training:**
- **Linear Regression:** A simple model that finds the best linear relationship between features and yield.
- **Decision Tree Regressor:** A tree-based model that splits data based on feature thresholds to make predictions.

**Step 3 — Model Evaluation:**
Models were compared using two metrics:
- **R² Score** — measures how well the model explains variance (closer to 1 is better).
- **MAE (Mean Absolute Error)** — average prediction error in kg/acre (lower is better).

**Step 4 — Deployment:**
The best model was saved using `pickle` and integrated into a **Streamlit** web application.

---

### 4. Results

| Metric               | Linear Regression | Decision Tree |
|----------------------|-------------------|---------------|
| **R² Score**         | **0.6828**        | 0.4021        |
| **MAE (kg/acre)**    | **133.34**        | 174.13        |

**Linear Regression outperformed the Decision Tree** on both metrics. It achieved a higher R² score (0.6828 vs 0.4021) and lower MAE (133.34 vs 174.13), meaning its predictions are closer to actual yield values.

The **Feature Importance** analysis from the Decision Tree revealed that **rainfall** is the most influential factor affecting crop yield, followed by **fertilizer usage** and **crop type**.

Based on these results, the **Linear Regression model** was selected and saved for deployment.

---

### 5. Screenshots of the Application

**Screenshot 1: Application Input Interface**

*(Insert screenshot of the Streamlit app showing the input form with dropdowns and sliders)*

**Screenshot 2: Prediction Result**

*(Insert screenshot showing the predicted yield output after clicking the "Predict Yield" button)*

---

**Tools Used:** Python, Pandas, Scikit-learn, Matplotlib, Streamlit

**Deployed Application URL:** *(Insert Streamlit Cloud link here)*

---
