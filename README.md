# 🌾 Seasonal Agriculture Performance Analysis

> **A data-driven analysis of agricultural productivity, profitability, irrigation efficiency, and environmental factors across seasons, crops, and states.**

## 📌 Overview

**Seasonal Agriculture Performance Analysis** is a Python-based data analytics project designed to evaluate and compare agricultural performance across different **seasons, crops, states, irrigation methods, and environmental conditions**.

The project transforms raw agricultural data into meaningful insights using **data cleaning, statistical analysis, correlation analysis, outlier detection, performance scoring, and professional data visualizations**.

The analysis focuses on three major dimensions of agricultural performance:

* 🌱 **Productivity** — Yield and total production
* 💰 **Profitability** — Revenue, cost, profit, and profit margin
* 💧 **Resource Efficiency** — Water usage and water efficiency

The results help identify high-performing seasons, profitable crops, efficient irrigation methods, stronger-performing states, and environmental factors associated with crop yield.

---

## 🎯 Project Objectives

* Analyze agricultural performance across different seasons.
* Compare crop productivity and profitability.
* Evaluate state-level agricultural performance.
* Analyze irrigation methods and water efficiency.
* Study the relationship between environmental conditions and crop yield.
* Examine the impact of soil and agricultural inputs on productivity.
* Analyze seasonal disease and pest risk.
* Detect potential outliers in important agricultural variables.
* Determine whether seasonal yield differences are statistically significant.
* Identify the strongest observed factors associated with agricultural yield.
* Generate data-driven recommendations for agricultural planning.

---

## 🧠 Analytical Approach

The project follows a structured data analytics workflow:

```text
Raw Agricultural Dataset
          ↓
     Data Cleaning
          ↓
 Data Transformation
          ↓
 Performance Scoring
          ↓
 Descriptive Analysis
          ↓
 Statistical Analysis
          ↓
 Correlation Analysis
          ↓
 Data Visualization
          ↓
 Key Findings
          ↓
 Data-Driven Recommendations
```

---

## 🛠️ Technology Stack

| Technology     | Purpose                           |
| -------------- | --------------------------------- |
| **Python**     | Core programming and analysis     |
| **Pandas**     | Data manipulation and aggregation |
| **NumPy**      | Numerical computations            |
| **Matplotlib** | Data visualization                |
| **SciPy**      | Statistical analysis and ANOVA    |

---

## 📊 Dataset

The project analyzes an agricultural performance dataset containing information related to:

### 🌾 Agricultural Information

* State
* District
* Crop
* Season
* Irrigation Method
* Yield
* Production

### 🌦️ Environmental Factors

* Rainfall
* Average Temperature
* Humidity
* Soil Moisture
* Sunlight Hours
* Soil pH

### 🧪 Agricultural Inputs

* Nitrogen
* Phosphorus
* Potassium
* Fertilizer Usage
* Pesticide Usage
* Seed Quality

### 💧 Resource & Financial Metrics

* Water Used
* Water Efficiency
* Revenue
* Total Cost
* Profit
* Profit Margin

### ⚠️ Risk Indicator

* Disease / Pest Risk

---

## 🧹 Data Preparation

Before analysis, the dataset goes through several cleaning and preprocessing steps:

* Duplicate records are identified and removed.
* Column names are cleaned.
* Categorical values are stripped of unnecessary spaces.
* Numerical fields are converted to appropriate numeric types.
* Missing numerical values are handled using median imputation.
* Missing categorical values are replaced with `Unknown`.
* Required analytical columns are validated before processing.

This ensures that the dataset is suitable for reliable statistical and visual analysis.

---

## 📐 Agricultural Performance Score

A custom **Agricultural Performance Score** is calculated to provide a combined measure of agricultural performance.

The score uses three normalized indicators:

| Component              | Weight  |
| ---------------------- | ------- |
| Yield Score            | **40%** |
| Profit Score           | **40%** |
| Water Efficiency Score | **20%** |

### Formula

```text
Agricultural Performance Score
=
(Yield Score × 0.40
+ Profit Score × 0.40
+ Water Efficiency Score × 0.20)
× 100
```

This provides a balanced evaluation of **productivity, profitability, and resource efficiency**.

---

## 💰 Profitability Analysis

The project calculates farm-level profit margin using:

```text
Profit Margin (%) =
(Profit / Revenue) × 100
```

It also compares:

* Total Revenue
* Total Cost
* Total Profit
* Profit Margin
* Crop profitability
* Seasonal profitability
* State-level profitability

---

## 📈 Statistical Analysis

### 1. Outlier Detection

The **Interquartile Range (IQR)** method is used to detect potential outliers in:

* Yield
* Production
* Revenue
* Total Cost
* Profit
* Water Used

The analysis calculates:

```text
IQR = Q3 − Q1

Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

---

### 2. One-Way ANOVA

A one-way **ANOVA test** is performed to determine whether agricultural yield differs significantly across seasons.

The analysis reports:

* F-statistic
* P-value
* Statistical conclusion

A significance level of:

```text
α = 0.05
```

is used to interpret the result.

---

### 3. Correlation Analysis

Pearson correlation is used to identify the strongest observed relationships between agricultural and environmental variables and crop yield.

The analysis ranks factors according to the absolute strength of their correlation with:

```text
Yield_Tonnes_Ha
```

---

## 📊 Visual Analytics

The project generates a comprehensive set of analytical visualizations.

### Executive Overview

* Agricultural Performance KPI Panel
* Average Yield
* Total Production
* Total Revenue
* Total Profit
* Overall Profit Margin
* Average Water Efficiency

### Seasonal Analysis

* Season Performance Ranking
* Seasonal Financial Structure
* Seasonal Production Contribution
* Seasonal Yield Distribution
* Seasonal Disease and Pest Risk

### Crop Analysis

* Crop Profitability Ranking
* Crop Strategy Matrix
* Seed Quality vs. Crop Productivity

### State Analysis

* State Performance Ranking
* State Productivity and Profitability Landscape

### Irrigation Analysis

* Irrigation Water-Efficiency Ranking
* Water Usage vs. Yield

### Environmental Analysis

* Agricultural Factor Correlation Matrix
* Rainfall vs. Yield
* Soil Moisture vs. Yield

### Financial Analysis

* Farm-Level Profit Margin Distribution

---

## 🔍 Key Analytical Dimensions

### 🌱 Season Performance

Season-wise comparison of:

* Yield
* Production
* Revenue
* Cost
* Profit
* Water Efficiency
* Agricultural Performance Score

### 🌾 Crop Performance

Crop-wise evaluation of:

* Average Yield
* Total Production
* Revenue
* Profit
* Water Efficiency

### 🗺️ State Performance

State-level comparison based on:

* Yield
* Production
* Profit
* Water Efficiency
* Overall Performance Score

### 💧 Irrigation Performance

Irrigation methods are evaluated using:

* Average Yield
* Water Used
* Water Efficiency
* Average Profit

### 🌦️ Environmental Relationships

The project examines relationships between yield and:

* Rainfall
* Temperature
* Humidity
* Soil Moisture
* Sunlight
* Soil pH
* Nutrient levels
* Fertilizer usage
* Pesticide usage
* Seed quality
* Disease and pest risk

---

## 💡 Automated Insights

The analysis automatically identifies:

* 🏆 Highest-performing season
* 🌾 Most profitable crop
* 🗺️ Highest-performing state
* 💧 Most water-efficient irrigation method
* 📊 Strongest observed factor associated with yield
* 📈 Average agricultural yield
* 💰 Overall profit margin

The project also generates recommendations based on these analytical results.

---

## 🚜 Data-Driven Recommendations

The analysis produces recommendations around:

* Adopting practices associated with high-performing seasons.
* Evaluating profitable crop opportunities.
* Studying successful practices from high-performing states.
* Promoting efficient irrigation methods where appropriate.
* Monitoring factors strongly associated with yield.
* Managing seasonal disease and pest risks.
* Combining environmental, soil, productivity, and financial indicators.
* Improving resource utilization and sustainable water management.

---

## 📁 Project Structure

```text
Seasonal-Agriculture-Analysis-
│
├── code.py
├── seasonal_agriculture_performance_dataset (2).csv
└── README.md
```

> **Note:** If the dataset is not included in the repository, place the CSV file in the same directory as `code.py` before running the analysis.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Anjali-Padwal/Seasonal-Agriculture-Analysis-.git
```

### 2. Navigate to the Project Directory

```bash
cd Seasonal-Agriculture-Analysis-
```

### 3. Install Dependencies

```bash
pip install numpy pandas matplotlib scipy
```

### 4. Add the Dataset

Place the dataset in the project directory:

```text
seasonal_agriculture_performance_dataset (2).csv
```

### 5. Run the Analysis

```bash
python code.py
```

The program displays:

* Analytical results in the terminal
* KPI overview
* Statistical results
* Key findings
* Data-driven recommendations
* Analytical visualizations

---

## 📌 Important Notes

* The project reads the existing CSV dataset.
* Data preprocessing is performed in memory.
* No machine learning model is used in the current implementation.
* Statistical analysis is performed using SciPy.
* Visualizations are generated using Matplotlib.
* The analysis does not modify the original dataset.

---

## 🌱 Potential Applications

This project can support:

* Agricultural performance monitoring
* Seasonal crop planning
* Crop profitability comparison
* Irrigation efficiency assessment
* Resource utilization analysis
* Farm profitability analysis
* Environmental impact analysis
* Disease and pest risk monitoring
* Evidence-based agricultural decision-making

---

## 🔮 Future Scope

The project can be extended with:

* 🤖 Machine learning-based yield prediction
* 🌾 Crop recommendation systems
* 💧 Predictive irrigation management
* 🌦️ Real-time weather data integration
* 🗺️ Geospatial agricultural analysis
* 📊 Interactive Power BI dashboards
* 🌐 Streamlit-based analytical dashboards
* 📈 Time-series agricultural forecasting
* 🔬 Advanced statistical modeling
* ⚡ Automated agricultural reporting

---

## 👨‍💻 Author

**Anjali Padwal**

**Project:** Seasonal Agriculture Performance Analysis

---

## ⭐ Project Highlights

```text
✓ Data Cleaning & Preprocessing
✓ Agricultural Performance Scoring
✓ Seasonal Analysis
✓ Crop Analysis
✓ State-Level Analysis
✓ Irrigation Efficiency Analysis
✓ Environmental Correlation Analysis
✓ Profitability Analysis
✓ Outlier Detection
✓ ANOVA Statistical Testing
✓ Automated Key Findings
✓ Data-Driven Recommendations
✓ 17 Analytical Visualizations
```

---

## 📄 License

This project is developed for **educational and analytical purposes**.
