# Code by tirumala, assisted by chatGPT
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from relative path
data = pd.read_excel("Master_monthly.xlsx")
data['Month'] = pd.to_datetime(data['Month'])

# Define the colors for plotting
colors = {
    'Korea': 'blue',
    'Japan': 'green',
    'India': 'red',
    'Germany': 'purple',
    'China': 'orange'
}


# Function to annotate lines at a specific year (2017 in this case)
def annotate_at_year(ax, x_data, y_data, text, color, year=2017):
    year_data = y_data[x_data.year == year].mean()
    ax.annotate(text, (pd.Timestamp(year=year, month=6, day=15), year_data),
                color=color,
                weight='bold',
                va='center',
                ha='right',
                fontsize=10,
                xytext=(-5, 0),
                textcoords='offset points')


# Plot the 3-month rolling average with annotations at 2017
rolling_avg_3 = data.set_index('Month').rolling(window=3).mean()
plt.figure(figsize=(14, 8))
for column in rolling_avg_3.columns:
    plt.plot(rolling_avg_3.index,
             rolling_avg_3[column],
             label=column,
             color=colors[column])
    annotate_at_year(plt.gca(), rolling_avg_3.index, rolling_avg_3[column],
                     column, colors[column])

plt.title('3-Month Rolling Average of Exports (in USD Billion)')
plt.xlabel('Month')
plt.ylabel('Exports (3-Month Average in USD Billion)')
#plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
# Saving for the first figure
plt.savefig('3_month_rolling_avg_exports_from_2014.png',
            dpi=600)  # Save the figure
plt.close()  # Close the current plot to free up memory


# Function to add label annotations on the lines
def annotate_line(ax,
                  x_data,
                  y_data,
                  text,
                  color,
                  position,
                  vertical_offset=0):
    y_pos = y_data.iloc[-1] + vertical_offset
    x_pos = x_data.iloc[-1]
    ax.annotate(text, (x_pos, y_pos),
                color=color,
                weight='bold',
                va=position,
                ha='right',
                fontsize=10,
                xytext=(-5, 0),
                textcoords='offset points')


# Plotting the actual exports for the last one year with average lines and annotations
last_year_data = data[data['Month'] >= (data['Month'].max() -
                                        pd.DateOffset(years=1))]
three_year_data = data[data['Month'] >= (data['Month'].max() -
                                         pd.DateOffset(years=3))]
average_exports_last_3_years = three_year_data.drop(columns=['Month']).mean()

fig, ax1 = plt.subplots(figsize=(14, 8))

# Left y-axis
for column, offset in [('Korea', 0), ('Japan', 0), ('India', 0)]:
    ax1.plot(last_year_data['Month'],
             last_year_data[column],
             label=column,
             color=colors[column],
             marker='o')
    ax1.axhline(y=average_exports_last_3_years[column],
                color=colors[column],
                linestyle='--')
    annotate_line(ax1, last_year_data['Month'], last_year_data[column], column,
                  colors[column], 'bottom', offset)

ax1.set_ylabel('Exports in USD Billion (Korea, Japan, India)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_xlabel('Month')
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Right y-axis
ax2 = ax1.twinx()
for column, offset in [('Germany', 5), ('China', 0)]:
    ax2.plot(last_year_data['Month'],
             last_year_data[column],
             label=column,
             color=colors[column],
             marker='o',
             linestyle='-')
    ax2.axhline(y=average_exports_last_3_years[column],
                color=colors[column],
                linestyle='-.')
    annotate_line(ax2, last_year_data['Month'], last_year_data[column], column,
                  colors[column], 'top', offset)

ax2.set_ylabel('Exports in USD Billion (Germany, China)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Title
plt.title(
    'Monthly Exports for the Last Year with 3-Year Average (in USD Billion)')
fig.tight_layout()
plt.savefig('monthly_exports_last_year_with_3_year_avg_line.png',
            dpi=600)  # Save the figure
plt.close()  # Close the current plot to free up memory
