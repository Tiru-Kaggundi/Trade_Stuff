import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable

# Load the data from the provided Excel file
file_path = 'Exports_States_AM23.xlsx'  # The path to your Excel file
sheet_name = 'Final'

# Read the data from the specified sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Adjust the bubble size to be 1/7th of the current size
data['Adjusted Bubble Size'] = data['Exports in USD million'] / 7

# Setting up the bubble chart with adjusted bubble size
fig, ax = plt.subplots(figsize=(20, 8))

# Scatter plot for the bubble chart with adjusted bubble size
# Use a colormap for the colors
cmap = plt.cm.Spectral
norm = plt.Normalize(vmin=data['Exports per capita in USD'].min(),
                     vmax=data['Exports per capita in USD'].max())
colors = cmap(norm(data['Exports per capita in USD']))

scatter = ax.scatter(data['Exports per capita in USD'],
                     data['SGDP per capita in USD'],
                     s=data['Adjusted Bubble Size'],
                     alpha=0.8,
                     c=colors,
                     edgecolors="w",
                     linewidth=2)

# Adding state short names inside the bubbles as legends
# Adjusting the annotation positions to avoid overlap
for i, txt in enumerate(data['Short name of State']):
    # Using a simple algorithm to adjust the position of the text to avoid overlap
    x_pos = data['Exports per capita in USD'].iloc[i]
    y_pos = data['SGDP per capita in USD'].iloc[i]

    # Adjusting positions for specific states
    if txt in ['NG', 'CG', 'TP']:  # Specific states to adjust
        x_pos += 1  # x-offset
        y_pos += 10  # y-offset

    ax.annotate(txt, (x_pos, y_pos),
                ha='center',
                va='center',
                fontsize=8,
                color='black')

# Adding a reference bubble for 1 billion USD of exports
reference_bubble_size = 1000 / 7  # 1 billion USD divided by 7 (adjusted bubble size scaling)
ax.scatter([], [],
           s=reference_bubble_size,
           color='green',
           alpha=0.6,
           label='1 Billion USD Exports')

# Creating a legend for the reference bubble
legend = ax.legend(loc='lower right',
                   frameon=True,
                   title='Reference Bubble Size')
legend.get_title().set_fontsize('10')

# Setting chart title and labels
ax.set_title('Relationship between Exports and State GDP Per Capita',
             fontsize=14)
ax.set_xlabel('Exports per Capita (USD)', fontsize=12)
ax.set_ylabel('SGDP per Capita (USD)', fontsize=12)

plt.tight_layout()

# Save the figure as 'bubble_states.png' with dpi=300
plt.savefig('bubble_states.png', dpi=300)

# Show the plot
plt.show()
