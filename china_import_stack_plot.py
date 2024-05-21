import pandas as pd
import matplotlib.pyplot as plt

# # Load the Excel file
# file_path = 'path_to_your_excel_file.xlsx'  # Update this to the path of your Excel file
# xls = pd.ExcelFile(file_path)

# # Load the summary sheet
# summary_sheet = pd.read_excel(xls, sheet_name='Summary_sheet', skiprows=1, nrows=10)

# Manually inputed the data for easy reproduction for others. 
# ideally one should read it from the associated excel sheet which i have commented out above
years = ['2023-24', '2022-23', '2021-22', '2020-21']
intermediate_hybrids_corrected = [68402.89 + 2343.47 + 1361.39,
                                  65013.74 + 2056.36 + 1400.23,
                                  61991.39 + 1884.25 + 1224.17,
                                  40143.23 + 1468.34 + 652.34]

capital_hybrids_corrected = [17299.97 + 5183.60 + 187.45,
                             16697.39 + 5414.16 + 151.12,
                             14974.58 + 6597.08 + 181.22,
                             11164.32 + 4478.53 + 188.86]

consumer_hybrids_corrected = [4421.62 + 1275.49 + 1227.17,
                              4884.85 + 1519.60 + 1323.63,
                              4170.15 + 1383.13 + 2159.34,
                              3879.42 + 792.21 + 2441.88]

# Create a new DataFrame for visualization
data_for_plotting_corrected = pd.DataFrame({
    'Year': years,
    'Intermediate Goods': intermediate_hybrids_corrected,
    'Capital Goods': capital_hybrids_corrected,
    'Consumer Goods': consumer_hybrids_corrected
})

# Reorder years
data_for_plotting_corrected.set_index('Year', inplace=True)
data_for_plotting_corrected = data_for_plotting_corrected.loc[['2020-21', '2021-22', '2022-23', '2023-24']]

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#4C72B0', '#55A868', '#C44E52']

data_for_plotting_corrected.plot(kind='bar', stacked=True, ax=ax, color=colors)

# Adding values and percentage labels inside each stack
for i, year in enumerate(data_for_plotting_corrected.index):
    cumulative = 0
    for category in data_for_plotting_corrected.columns:
        value = data_for_plotting_corrected.loc[year, category]
        percentage = (value / data_for_plotting_corrected.loc[year].sum()) * 100
        ax.text(i, cumulative + value / 2, f'{value/1000:.1f}B\n({percentage:.1f}%)', ha='center', va='center', fontsize=12, color='white', fontweight='bold')
        cumulative += value

# Adding total labels on top of each stack
totals = data_for_plotting_corrected.sum(axis=1)
for i, total in enumerate(totals):
    ax.text(i, total + 2000, f'{total/1000:.2f}B', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_title('Composition of Chinese Imports into India (in Billion USD)', fontsize=14)
ax.set_ylabel('Billion USD', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.legend(title='Categories', fontsize=12)

# Adjust y-axis to display in billions
ax.set_yticklabels([f'{int(x/1000)}' for x in ax.get_yticks()])

plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Save the figure in high resolution
plt.savefig('composition_of_chinese_imports_high_res.png', dpi=500)
plt.show()