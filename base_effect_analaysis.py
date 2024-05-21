import pandas as pd
import matplotlib.pyplot as plt

# Load the excel file
data = pd.read_excel('base_effect.xlsx')

# Calculate YoY change for 'Total Exports' and 'Total Exports minus POL'
data['YoY_Total_Exports'] = data['Total Exports'].pct_change(periods=12) * 100
data['YoY_Total_Exports_minus_POL'] = data[
    'Total Exports minus POL'].pct_change(periods=12) * 100

# Extract the relevant data for the analysis
analysis_data = data[[
    'Month ', 'YoY_Total_Exports', 'YoY_Total_Exports_minus_POL'
]].dropna()
analysis_data['Total Exports (Billion)'] = data['Total Exports'].loc[
    analysis_data.index] / 1000
analysis_data['Total Exports minus POL (Billion)'] = data[
    'Total Exports minus POL'].loc[analysis_data.index] / 1000

# Plotting
bar_width = 20
fig, ax1 = plt.subplots(figsize=(15, 8))

# Bar charts for 'Total Exports' and 'Total Exports minus POL' in billions
ax1.bar(analysis_data['Month '],
        analysis_data['Total Exports (Billion)'],
        width=bar_width,
        label="Total Exports",
        color='lightblue',
        alpha=0.6)
ax1.bar(analysis_data['Month '],
        analysis_data['Total Exports minus POL (Billion)'],
        width=bar_width,
        label="Total Exports minus POL",
        color='lightcoral',
        alpha=0.6)
ax1.set_xlabel("Month")
ax1.set_ylabel("Exports (in USD Billions)")
ax1.legend(loc="upper left")

# Overlay the YoY growth trends
ax2 = ax1.twinx()
ax2.plot(analysis_data['Month '],
         analysis_data['YoY_Total_Exports'],
         marker='o',
         label="Total Exports YoY Growth",
         color='b')
ax2.plot(analysis_data['Month '],
         analysis_data['YoY_Total_Exports_minus_POL'],
         marker='o',
         label="Total Exports minus POL YoY Growth",
         color='r')
ax2.axhline(0, color='grey', linestyle='--')
ax2.set_ylabel("YoY Growth (%)")
ax2.legend(loc="upper right")

plt.title("Exports and YoY Growth Trend for India")
plt.xticks(rotation=45)
plt.grid(True,
         which='both',
         linestyle='--',
         linewidth=0.5,
         axis='y',
         alpha=0.6)
plt.tight_layout()
plt.savefig('exports_growth_trend_billion.png', dpi=600)
plt.show()
