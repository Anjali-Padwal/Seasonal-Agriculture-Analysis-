# 1. IMPORT LIBRARIES

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import f_oneway

# 2. LOAD DATASET

FILE_PATH = "seasonal_agriculture_performance_dataset (1).csv"

df = pd.read_csv(FILE_PATH)

# 3. PROFESSIONAL VISUAL THEME

plt.rcParams["figure.facecolor"] = "#F7F8F5"
plt.rcParams["axes.facecolor"] = "#FFFFFF"
plt.rcParams["axes.edgecolor"] = "#26352C"
plt.rcParams["axes.labelcolor"] = "#26352C"
plt.rcParams["xtick.color"] = "#26352C"
plt.rcParams["ytick.color"] = "#26352C"
plt.rcParams["text.color"] = "#26352C"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlepad"] = 16

# High-contrast palette
DARK = "#173F2B"
GREEN = "#247A4D"
LIME = "#72A84A"
GOLD = "#D99A25"
ORANGE = "#D66A1F"
BLUE = "#246B8F"
TEAL = "#168C83"
PURPLE = "#68478C"
RED = "#B83B3B"
BROWN = "#82552F"
GREY = "#68736D"
LIGHT_GREY = "#D9E0DA"

PALETTE = [
    DARK,
    GREEN,
    GOLD,
    BLUE,
    TEAL,
    PURPLE,
    ORANGE,
    RED,
    BROWN
]

# 4. BASIC INFORMATION

print("\n" + "=" * 80)
print("SEASONAL AGRICULTURE PERFORMANCE ANALYSIS")
print("=" * 80)

print("\nDATASET INFORMATION")
print("-" * 80)
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

print("\nColumns:")
for column in df.columns:
    print("•", column)

# 5. DATA CLEANING

print("\n" + "=" * 80)
print("DATA CLEANING")
print("=" * 80)

# Remove duplicate records
duplicates = df.duplicated().sum()

print("\nDuplicate records:", duplicates)

df = df.drop_duplicates().copy()

# Clean column names
df.columns = df.columns.str.strip()

# Categorical columns
categorical_columns = [
    "State",
    "District",
    "Crop",
    "Season",
    "Irrigation_Method"
]

# Numerical columns
numerical_columns = [
    "Yield_Tonnes_Ha",
    "Production_Tonnes",
    "Rainfall_mm",
    "Avg_Temperature_C",
    "Humidity_pct",
    "Soil_Moisture_pct",
    "Water_Used_m3",
    "Revenue_INR",
    "Total_Cost_INR",
    "Profit_INR",
    "Sunlight_Hours_Day",
    "Soil_pH",
    "Nitrogen_kg_ha",
    "Phosphorus_kg_ha",
    "Potassium_kg_ha",
    "Fertilizer_kg_ha",
    "Pesticide_Litre_ha",
    "Seed_Quality_Score",
    "Water_Efficiency_t_per_1000m3",
    "Disease_Pest_Risk_pct"
]

# Strip categorical values
for col in categorical_columns:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
        )

# Convert numerical columns
for col in numerical_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# Fill numerical missing values
for col in numerical_columns:
    if col in df.columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(
                df[col].median()
            )

# Fill categorical missing values
for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].replace(
            ["nan", "None", ""],
            np.nan
        )

        df[col] = df[col].fillna("Unknown")

print(
    "\nTotal missing values after cleaning:",
    df.isnull().sum().sum()
)

print("Final dataset size:", df.shape)

# 6. AGRICULTURAL PERFORMANCE SCORE

def normalize(series):
    minimum = series.min()
    maximum = series.max()

    if maximum == minimum:
        return pd.Series(
            1.0,
            index=series.index
        )

    return (
        (series - minimum)
        / (maximum - minimum)
    )

df["Yield_Score"] = normalize(
    df["Yield_Tonnes_Ha"]
)

df["Profit_Score"] = normalize(
    df["Profit_INR"]
)

df["Water_Efficiency_Score"] = normalize(
    df["Water_Efficiency_t_per_1000m3"]
)

df["Agricultural_Performance_Score"] = (
    df["Yield_Score"] * 0.40 +
    df["Profit_Score"] * 0.40 +
    df["Water_Efficiency_Score"] * 0.20
) * 100

# 7. PROFIT MARGIN

df["Profit_Margin_pct"] = np.where(
    df["Revenue_INR"] != 0,
    (
        df["Profit_INR"]
        / df["Revenue_INR"]
    ) * 100,
    0
)

# 8. EXECUTIVE KPI PANEL

average_yield = df["Yield_Tonnes_Ha"].mean()
total_production = df["Production_Tonnes"].sum()
total_revenue = df["Revenue_INR"].sum()
total_profit = df["Profit_INR"].sum()
average_water_efficiency = (
    df["Water_Efficiency_t_per_1000m3"].mean()
)

overall_margin = (
    total_profit / total_revenue * 100
    if total_revenue != 0 else 0
)

fig, ax = plt.subplots(
    figsize=(15, 5)
)

ax.axis("off")

ax.text(
    0.02,
    0.88,
    "AGRICULTURAL PERFORMANCE",
    fontsize=22,
    fontweight="bold",
    color=DARK,
    transform=ax.transAxes
)

ax.text(
    0.02,
    0.76,
    "Executive overview of productivity, profitability and resource efficiency",
    fontsize=10,
    color=GREY,
    transform=ax.transAxes
)

kpis = [
    ("AVERAGE YIELD",
     f"{average_yield:.2f}\nTonnes/Ha"),

    ("TOTAL PRODUCTION",
     f"{total_production:,.0f}\nTonnes"),

    ("TOTAL REVENUE",
     f"₹{total_revenue/1e6:.2f}M"),

    ("TOTAL PROFIT",
     f"₹{total_profit/1e6:.2f}M"),

    ("PROFIT MARGIN",
     f"{overall_margin:.1f}%"),

    ("WATER EFFICIENCY",
     f"{average_water_efficiency:.2f}")
]

positions = np.linspace(
    0.08,
    0.92,
    len(kpis)
)

for position, (label, value) in zip(
    positions,
    kpis
):

    ax.text(
        position,
        0.47,
        value,
        ha="center",
        va="center",
        fontsize=17,
        fontweight="bold",
        color=GREEN,
        transform=ax.transAxes
    )

    ax.text(
        position,
        0.20,
        label,
        ha="center",
        fontsize=8,
        fontweight="bold",
        color=GREY,
        transform=ax.transAxes
    )

plt.tight_layout()
plt.show()

# 9. SEASON SUMMARY

season_summary = (
    df.groupby("Season")
    .agg(
        Yield=("Yield_Tonnes_Ha", "mean"),
        Production=("Production_Tonnes", "sum"),
        Revenue=("Revenue_INR", "sum"),
        Cost=("Total_Cost_INR", "sum"),
        Profit=("Profit_INR", "sum"),
        Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        ),
        Performance=(
            "Agricultural_Performance_Score",
            "mean"
        )
    )
    .sort_values(
        "Performance",
        ascending=False
    )
)

print("\n" + "=" * 80)
print("SEASONAL PERFORMANCE")
print("=" * 80)

print(
    season_summary.round(2)
)

# 10. VISUALIZATION 1
# SEASON PERFORMANCE — LOLLIPOP

plot_data = season_summary.sort_values(
    "Performance"
)

fig, ax = plt.subplots(
    figsize=(11, 6)
)

y = np.arange(
    len(plot_data)
)

ax.hlines(
    y,
    0,
    plot_data["Performance"],
    color=LIGHT_GREY,
    linewidth=5
)

ax.scatter(
    plot_data["Performance"],
    y,
    s=180,
    color=GREEN,
    edgecolor="white",
    linewidth=2,
    zorder=3
)

for i, value in enumerate(
    plot_data["Performance"]
):

    ax.text(
        value + 1,
        i,
        f"{value:.1f}",
        va="center",
        fontweight="bold"
    )

ax.set_yticks(y)
ax.set_yticklabels(plot_data.index)

ax.set_xlabel(
    "Agricultural Performance Score"
)

ax.set_title(
    "Season Performance Ranking",
    fontsize=17
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 11. VISUALIZATION 2
# SEASON FINANCIAL STRUCTURE

fig, ax = plt.subplots(
    figsize=(12, 7)
)

x = np.arange(
    len(season_summary)
)

width = 0.25

ax.bar(
    x - width,
    season_summary["Revenue"] / 1e6,
    width,
    label="Revenue",
    color=GREEN
)

ax.bar(
    x,
    season_summary["Cost"] / 1e6,
    width,
    label="Cost",
    color=ORANGE
)

ax.bar(
    x + width,
    season_summary["Profit"] / 1e6,
    width,
    label="Profit",
    color=GOLD
)

ax.set_xticks(x)
ax.set_xticklabels(
    season_summary.index
)

ax.set_ylabel(
    "Amount (₹ Million)"
)

ax.set_title(
    "Seasonal Financial Structure",
    fontsize=17
)

ax.legend(
    frameon=False
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 12. VISUALIZATION 3
# SEASON PRODUCTION DONUT

production = (
    season_summary["Production"]
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(
    figsize=(9, 8)
)

wedges, _, autotexts = ax.pie(
    production,
    labels=production.index,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.76,
    colors=[
        GREEN,
        GOLD,
        BLUE,
        TEAL,
        PURPLE
    ][:len(production)],
    wedgeprops={
        "width": 0.40,
        "edgecolor": "white",
        "linewidth": 2
    }
)

for text in autotexts:
    text.set_fontweight("bold")
    text.set_color("white")

ax.text(
    0,
    0,
    "TOTAL\nPRODUCTION",
    ha="center",
    va="center",
    fontsize=12,
    fontweight="bold",
    color=DARK
)

ax.set_title(
    "Contribution of Seasons to Total Production",
    fontsize=16
)

plt.tight_layout()
plt.show()

# 13. CROP SUMMARY

crop_summary = (
    df.groupby("Crop")
    .agg(
        Yield=("Yield_Tonnes_Ha", "mean"),
        Production=("Production_Tonnes", "sum"),
        Revenue=("Revenue_INR", "sum"),
        Profit=("Profit_INR", "sum"),
        Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        )
    )
    .sort_values(
        "Profit",
        ascending=False
    )
)

print("\n" + "=" * 80)
print("CROP PERFORMANCE")
print("=" * 80)

print(
    crop_summary.round(2)
)

# 14. VISUALIZATION 4
# CROP PROFIT RANKING

crop_plot = crop_summary.sort_values(
    "Profit"
)

fig, ax = plt.subplots(
    figsize=(12, 8)
)

y = np.arange(
    len(crop_plot)
)

ax.hlines(
    y,
    0,
    crop_plot["Profit"] / 1e6,
    color=LIGHT_GREY,
    linewidth=5
)

ax.scatter(
    crop_plot["Profit"] / 1e6,
    y,
    s=190,
    color=GREEN,
    edgecolor="white",
    linewidth=2
)

ax.set_yticks(y)
ax.set_yticklabels(
    crop_plot.index
)

ax.set_xlabel(
    "Total Profit (₹ Million)"
)

ax.set_title(
    "Crop Profitability Ranking",
    fontsize=17
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 15. VISUALIZATION 5
# CROP STRATEGY QUADRANT

fig, ax = plt.subplots(
    figsize=(12, 8)
)

scatter = ax.scatter(
    crop_summary["Yield"],
    crop_summary["Profit"] / 1e6,
    s=(
        crop_summary["Production"]
        / crop_summary["Production"].max()
    ) * 1800 + 150,
    c=crop_summary["Water_Efficiency"],
    cmap="viridis",
    alpha=0.85,
    edgecolor="white",
    linewidth=1.5
)

mean_yield = crop_summary["Yield"].mean()
mean_profit = (
    crop_summary["Profit"] / 1e6
).mean()

ax.axvline(
    mean_yield,
    color=GREY,
    linestyle="--",
    linewidth=1.5
)

ax.axhline(
    mean_profit,
    color=GREY,
    linestyle="--",
    linewidth=1.5
)

for crop, row in crop_summary.iterrows():

    ax.annotate(
        crop,
        (
            row["Yield"],
            row["Profit"] / 1e6
        ),
        xytext=(7, 7),
        textcoords="offset points",
        fontsize=9,
        fontweight="bold"
    )

# Quadrant labels
ax.text(
    0.03,
    0.93,
    "LOW YIELD\nHIGH PROFIT",
    transform=ax.transAxes,
    fontsize=8,
    fontweight="bold",
    color=BLUE
)

ax.text(
    0.72,
    0.93,
    "HIGH YIELD\nHIGH PROFIT",
    transform=ax.transAxes,
    fontsize=8,
    fontweight="bold",
    color=GREEN
)

ax.text(
    0.03,
    0.08,
    "LOW YIELD\nLOW PROFIT",
    transform=ax.transAxes,
    fontsize=8,
    fontweight="bold",
    color=RED
)

ax.text(
    0.72,
    0.08,
    "HIGH YIELD\nLOW PROFIT",
    transform=ax.transAxes,
    fontsize=8,
    fontweight="bold",
    color=ORANGE
)

ax.set_xlabel(
    "Average Yield (Tonnes/Ha)"
)

ax.set_ylabel(
    "Total Profit (₹ Million)"
)

ax.set_title(
    "Crop Strategy Matrix",
    fontsize=17
)

cbar = plt.colorbar(
    scatter
)

cbar.set_label(
    "Water Efficiency"
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 16. STATE SUMMARY

state_summary = (
    df.groupby("State")
    .agg(
        Yield=("Yield_Tonnes_Ha", "mean"),
        Production=("Production_Tonnes", "sum"),
        Profit=("Profit_INR", "sum"),
        Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        ),
        Performance=(
            "Agricultural_Performance_Score",
            "mean"
        )
    )
    .sort_values(
        "Performance",
        ascending=False
    )
)

print("\n" + "=" * 80)
print("STATE PERFORMANCE")
print("=" * 80)

print(
    state_summary.round(2)
)

# 17. VISUALIZATION 6
# STATE PERFORMANCE

state_plot = state_summary.sort_values(
    "Performance"
)

fig, ax = plt.subplots(
    figsize=(12, 9)
)

y = np.arange(
    len(state_plot)
)

bars = ax.barh(
    y,
    state_plot["Performance"],
    color=GREEN,
    height=0.58
)

for bar in bars:

    value = bar.get_width()

    ax.text(
        value + 1,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}",
        va="center",
        fontsize=8,
        fontweight="bold"
    )

ax.set_yticks(y)
ax.set_yticklabels(
    state_plot.index
)

ax.set_xlabel(
    "Agricultural Performance Score"
)

ax.set_title(
    "State-Level Performance Ranking",
    fontsize=17
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 18. VISUALIZATION 7
# STATE PRODUCTIVITY BUBBLE

fig, ax = plt.subplots(
    figsize=(12, 8)
)

sizes = (
    state_summary["Yield"]
    / state_summary["Yield"].max()
) * 1600 + 200

scatter = ax.scatter(
    state_summary["Production"],
    state_summary["Profit"] / 1e6,
    s=sizes,
    c=state_summary["Performance"],
    cmap="YlGn",
    alpha=0.85,
    edgecolor="white",
    linewidth=1.5
)

for state, row in state_summary.iterrows():

    ax.annotate(
        state,
        (
            row["Production"],
            row["Profit"] / 1e6
        ),
        xytext=(6, 6),
        textcoords="offset points",
        fontsize=8
    )

ax.set_xlabel(
    "Total Production (Tonnes)"
)

ax.set_ylabel(
    "Total Profit (₹ Million)"
)

ax.set_title(
    "State Productivity and Profitability Landscape",
    fontsize=17
)

cbar = plt.colorbar(
    scatter
)

cbar.set_label(
    "Performance Score"
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 19. IRRIGATION SUMMARY

irrigation_summary = (
    df.groupby("Irrigation_Method")
    .agg(
        Yield=("Yield_Tonnes_Ha", "mean"),
        Water_Used=("Water_Used_m3", "mean"),
        Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        ),
        Profit=("Profit_INR", "mean")
    )
    .sort_values(
        "Water_Efficiency",
        ascending=False
    )
)

print("\n" + "=" * 80)
print("IRRIGATION PERFORMANCE")
print("=" * 80)

print(
    irrigation_summary.round(2)
)

# 20. VISUALIZATION 8
# IRRIGATION EFFICIENCY

fig, ax = plt.subplots(
    figsize=(11, 7)
)

bars = ax.barh(
    irrigation_summary.index,
    irrigation_summary["Water_Efficiency"],
    color=BLUE,
    height=0.58
)

for bar in bars:

    value = bar.get_width()

    ax.text(
        value + 0.02,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}",
        va="center",
        fontsize=9,
        fontweight="bold"
    )

ax.set_xlabel(
    "Tonnes Produced per 1000 m³"
)

ax.set_title(
    "Irrigation Water-Efficiency Ranking",
    fontsize=17
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 21. VISUALIZATION 9
# IRRIGATION WATER VS YIELD

fig, ax = plt.subplots(
    figsize=(12, 8)
)

methods = df[
    "Irrigation_Method"
].unique()

for i, method in enumerate(methods):

    subset = df[
        df["Irrigation_Method"] == method
    ]

    ax.scatter(
        subset["Water_Used_m3"],
        subset["Yield_Tonnes_Ha"],
        s=65,
        alpha=0.70,
        color=PALETTE[
            i % len(PALETTE)
        ],
        label=method,
        edgecolor="white",
        linewidth=0.5
    )

ax.set_xlabel(
    "Water Used (m³)"
)

ax.set_ylabel(
    "Yield (Tonnes/Ha)"
)

ax.set_title(
    "Irrigation Resource Use vs Yield",
    fontsize=17
)

ax.legend(
    title="Irrigation Method",
    frameon=False
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 22. VISUALIZATION 10
# ENVIRONMENTAL CORRELATION HEATMAP

environment_columns = [
    "Rainfall_mm",
    "Avg_Temperature_C",
    "Humidity_pct",
    "Soil_Moisture_pct",
    "Sunlight_Hours_Day",
    "Soil_pH",
    "Nitrogen_kg_ha",
    "Phosphorus_kg_ha",
    "Potassium_kg_ha",
    "Fertilizer_kg_ha",
    "Pesticide_Litre_ha",
    "Seed_Quality_Score",
    "Disease_Pest_Risk_pct",
    "Yield_Tonnes_Ha",
    "Profit_INR"
]

environment_columns = [
    col
    for col in environment_columns
    if col in df.columns
]

corr = df[
    environment_columns
].corr()

fig, ax = plt.subplots(
    figsize=(15, 11)
)

image = ax.imshow(
    corr,
    cmap="RdYlGn",
    vmin=-1,
    vmax=1
)

ax.set_xticks(
    np.arange(len(corr.columns))
)

ax.set_yticks(
    np.arange(len(corr.columns))
)

ax.set_xticklabels(
    corr.columns,
    rotation=65,
    ha="right",
    fontsize=8
)

ax.set_yticklabels(
    corr.columns,
    fontsize=8
)

for i in range(
    len(corr.columns)
):

    for j in range(
        len(corr.columns)
    ):

        value = corr.iloc[i, j]

        ax.text(
            j,
            i,
            f"{value:.2f}",
            ha="center",
            va="center",
            fontsize=7,
            color=(
                "white"
                if abs(value) > 0.60
                else DARK
            )
        )

cbar = plt.colorbar(
    image
)

cbar.set_label(
    "Correlation Coefficient"
)

ax.set_title(
    "Agricultural Factor Relationship Matrix",
    fontsize=17
)

plt.tight_layout()
plt.show()

# 23. VISUALIZATION 11
# RAINFALL VS YIELD

fig, ax = plt.subplots(
    figsize=(12, 8)
)

scatter = ax.scatter(
    df["Rainfall_mm"],
    df["Yield_Tonnes_Ha"],
    c=df["Profit_Margin_pct"],
    cmap="viridis",
    s=65,
    alpha=0.78,
    edgecolor="white",
    linewidth=0.5
)

correlation = (
    df["Rainfall_mm"]
    .corr(
        df["Yield_Tonnes_Ha"]
    )
)

ax.text(
    0.03,
    0.94,
    f"Pearson correlation = {correlation:.2f}",
    transform=ax.transAxes,
    fontsize=10,
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.4",
        facecolor="white",
        edgecolor=LIGHT_GREY
    )
)

ax.set_xlabel(
    "Rainfall (mm)"
)

ax.set_ylabel(
    "Yield (Tonnes/Ha)"
)

ax.set_title(
    "Rainfall Influence on Agricultural Yield",
    fontsize=17
)

cbar = plt.colorbar(
    scatter
)

cbar.set_label(
    "Profit Margin (%)"
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 24. VISUALIZATION 12
# SOIL MOISTURE VS YIELD

fig, ax = plt.subplots(
    figsize=(12, 8)
)

scatter = ax.scatter(
    df["Soil_Moisture_pct"],
    df["Yield_Tonnes_Ha"],
    c=df["Agricultural_Performance_Score"],
    cmap="plasma",
    s=65,
    alpha=0.78,
    edgecolor="white",
    linewidth=0.5
)

ax.set_xlabel(
    "Soil Moisture (%)"
)

ax.set_ylabel(
    "Yield (Tonnes/Ha)"
)

ax.set_title(
    "Soil Moisture and Crop Productivity",
    fontsize=17
)

cbar = plt.colorbar(
    scatter
)

cbar.set_label(
    "Agricultural Performance Score"
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 25. VISUALIZATION 13
# SEED QUALITY VS YIELD

seed_bins = pd.cut(
    df["Seed_Quality_Score"],
    bins=5
)

seed_summary = (
    df.groupby(
        seed_bins,
        observed=True
    )["Yield_Tonnes_Ha"]
    .mean()
)

fig, ax = plt.subplots(
    figsize=(11, 6)
)

bars = ax.bar(
    range(len(seed_summary)),
    seed_summary.values,
    color=TEAL,
    width=0.62
)

for bar in bars:

    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontweight="bold"
    )

ax.set_xticks(
    range(len(seed_summary))
)

ax.set_xticklabels(
    seed_summary.index.astype(str),
    rotation=20,
    ha="right"
)

ax.set_xlabel(
    "Seed Quality Score Range"
)

ax.set_ylabel(
    "Average Yield (Tonnes/Ha)"
)

ax.set_title(
    "Seed Quality and Crop Productivity",
    fontsize=17
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 26. VISUALIZATION 14
# DISEASE / PEST RISK

risk_summary = (
    df.groupby("Season")
    ["Disease_Pest_Risk_pct"]
    .mean()
    .sort_values()
)

fig, ax = plt.subplots(
    figsize=(11, 6)
)

bars = ax.barh(
    risk_summary.index,
    risk_summary.values,
    color=RED,
    height=0.58
)

for bar in bars:

    value = bar.get_width()

    ax.text(
        value + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}%",
        va="center",
        fontweight="bold"
    )

ax.set_xlabel(
    "Average Disease / Pest Risk (%)"
)

ax.set_title(
    "Seasonal Disease and Pest Risk Exposure",
    fontsize=17
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 27. VISUALIZATION 15
# PROFIT MARGIN DISTRIBUTION

fig, ax = plt.subplots(
    figsize=(11, 6)
)

ax.hist(
    df["Profit_Margin_pct"],
    bins=25,
    color=PURPLE,
    edgecolor="white",
    alpha=0.88
)

median_margin = (
    df["Profit_Margin_pct"].median()
)

ax.axvline(
    median_margin,
    color=GOLD,
    linestyle="--",
    linewidth=2.5,
    label=f"Median = {median_margin:.1f}%"
)

ax.set_xlabel(
    "Profit Margin (%)"
)

ax.set_ylabel(
    "Number of Farms"
)

ax.set_title(
    "Distribution of Farm-Level Profit Margins",
    fontsize=17
)

ax.legend(
    frameon=False
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 28. VISUALIZATION 16
# SEASONAL YIELD DISTRIBUTION

seasons = list(
    df["Season"].unique()
)

yield_groups = [
    df.loc[
        df["Season"] == season,
        "Yield_Tonnes_Ha"
    ]
    for season in seasons
]

fig, ax = plt.subplots(
    figsize=(12, 7)
)

box = ax.boxplot(
    yield_groups,
    labels=seasons,
    patch_artist=True,
    showmeans=True
)

for i, patch in enumerate(
    box["boxes"]
):

    patch.set_facecolor(
        PALETTE[
            i % len(PALETTE)
        ]
    )

    patch.set_alpha(0.75)

for median in box["medians"]:

    median.set_color(
        "white"
    )

    median.set_linewidth(2)

for mean in box["means"]:

    mean.set_marker(
        "D"
    )

    mean.set_markerfacecolor(
        GOLD
    )

    mean.set_markeredgecolor(
        DARK
    )

ax.set_xlabel(
    "Season"
)

ax.set_ylabel(
    "Yield (Tonnes/Ha)"
)

ax.set_title(
    "Seasonal Yield Distribution and Variability",
    fontsize=17
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# 29. OUTLIER ANALYSIS

print("\n" + "=" * 80)
print("OUTLIER ANALYSIS")
print("=" * 80)

outlier_columns = [
    "Yield_Tonnes_Ha",
    "Production_Tonnes",
    "Revenue_INR",
    "Total_Cost_INR",
    "Profit_INR",
    "Water_Used_m3"
]

for column in outlier_columns:

    if column not in df.columns:
        continue

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = (
        (df[column] < lower)
        |
        (df[column] > upper)
    ).sum()

    print(
        f"{column:<35} : {outliers}"
    )

# 30. ANOVA

print("\n" + "=" * 80)
print("ANOVA — SEASONAL YIELD DIFFERENCE")
print("=" * 80)

groups = [
    group["Yield_Tonnes_Ha"].values
    for _, group in df.groupby("Season")
]

if len(groups) >= 2:

    f_statistic, p_value = f_oneway(
        *groups
    )

    print(
        f"F-statistic : {f_statistic:.4f}"
    )

    print(
        f"P-value     : {p_value:.6f}"
    )

    if p_value < 0.05:

        print(
            "Conclusion  : Seasonal yield differences "
            "are statistically significant."
        )

    else:

        print(
            "Conclusion  : Seasonal yield differences "
            "are not statistically significant."
        )

# 31. CORRELATION WITH YIELD

yield_correlations = (
    corr["Yield_Tonnes_Ha"]
    .drop("Yield_Tonnes_Ha")
    .sort_values(
        key=lambda x: abs(x),
        ascending=False
    )
)

print("\n" + "=" * 80)
print("STRONGEST FACTORS ASSOCIATED WITH YIELD")
print("=" * 80)

print(
    yield_correlations
    .head(10)
    .round(3)
)

# 32. BEST SEASON

best_season = season_summary[
    "Performance"
].idxmax()

best_season_score = season_summary.loc[
    best_season,
    "Performance"
]

# 33. BEST CROP

best_crop = crop_summary[
    "Profit"
].idxmax()

best_crop_profit = crop_summary.loc[
    best_crop,
    "Profit"
]

# 34. BEST STATE

best_state = state_summary[
    "Performance"
].idxmax()

best_state_score = state_summary.loc[
    best_state,
    "Performance"
]

# 35. BEST IRRIGATION METHOD

best_irrigation = irrigation_summary[
    "Water_Efficiency"
].idxmax()

best_irrigation_efficiency = (
    irrigation_summary.loc[
        best_irrigation,
        "Water_Efficiency"
    ]
)

# 36. STRONGEST YIELD FACTOR

strongest_factor = (
    yield_correlations.index[0]
)

strongest_correlation = (
    yield_correlations.iloc[0]
)

# 37. KEY FINDINGS

print("\n" + "=" * 80)
print("KEY FINDINGS")
print("=" * 80)

print(
    f"\n1. Highest-performing season: "
    f"{best_season} "
    f"(score: {best_season_score:.2f})."
)

print(
    f"\n2. Most profitable crop: "
    f"{best_crop} "
    f"(profit: ₹{best_crop_profit:,.2f})."
)

print(
    f"\n3. Highest-performing state: "
    f"{best_state} "
    f"(score: {best_state_score:.2f})."
)

print(
    f"\n4. Most water-efficient irrigation method: "
    f"{best_irrigation} "
    f"({best_irrigation_efficiency:.2f} tonnes/1000 m³)."
)

print(
    f"\n5. Strongest relationship with yield: "
    f"{strongest_factor} "
    f"(correlation: {strongest_correlation:.3f})."
)

print(
    f"\n6. Average yield: "
    f"{average_yield:.2f} tonnes/ha."
)

print(
    f"\n7. Overall profit margin: "
    f"{overall_margin:.2f}%."
)

# 38. DATA-DRIVEN RECOMMENDATIONS

print("\n" + "=" * 80)
print("DATA-DRIVEN RECOMMENDATIONS")
print("=" * 80)

recommendations = [

    (
        f"Prioritize practices associated with the "
        f"{best_season} season because it achieved "
        f"the highest performance score."
    ),

    (
        f"Evaluate expansion opportunities for "
        f"{best_crop} because it generated the highest "
        f"total profit in the dataset."
    ),

    (
        f"Study agricultural practices used in "
        f"{best_state} and identify methods that can "
        f"be applied to lower-performing states."
    ),

    (
        f"Promote efficient irrigation practices such as "
        f"{best_irrigation} where local conditions support "
        f"their adoption."
    ),

    (
        f"Monitor {strongest_factor} carefully because it "
        f"has the strongest observed relationship with yield."
    ),

    (
        "Combine yield, profitability and water efficiency "
        "when evaluating agricultural performance."
    ),

    (
        "Monitor disease and pest risk by season and "
        "prepare preventive crop-management strategies."
    ),

    (
        "Use environmental and soil indicators together "
        "with production data for better agricultural planning."
    )
]

for i, recommendation in enumerate(
    recommendations,
    1
):

    print(
        f"{i}. {recommendation}"
    )

# 39. FINAL SUMMARY

print("\n" + "=" * 80)
print("PROJECT SUMMARY")
print("=" * 80)

print(
    """
The Seasonal Agriculture Performance Analysis project
evaluates agricultural productivity across seasons,
crops, states, irrigation methods and environmental
conditions.

The project applies data cleaning, descriptive analysis,
correlation analysis, outlier detection and ANOVA to
identify meaningful patterns.

Multiple analytical visualizations are used to compare
productivity, profitability, water efficiency, crop
performance, environmental relationships and risk factors.

The resulting insights can support evidence-based
agricultural planning, efficient resource utilization,
improved productivity and sustainable water management.
"""
)

print("=" * 80)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 80)