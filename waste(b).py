import pandas as pd
import matplotlib.pyplot as plt

# Read the main CSV file
waste_data = pd.read_csv('D:/homework/scotland-waste-data-2011-2013.csv')

# Read the region mapping CSV file
region_mapping = pd.read_csv('D:/homework/scottish-regions.csv')

# Merge the main data with the region mapping
waste_data = pd.merge(waste_data, region_mapping, on='GeographyCode')

# Group the data by region and year, and calculate the total generated waste and waste landfilled
grouped_data = waste_data.groupby(['Reference Area', 'DateCode']).sum()

# Calculate the recycling percentage
grouped_data['Recycling Percentage'] = grouped_data['Waste Generated(Tonnes)'] / grouped_data['Waste Landfilled (Tonnes)'] * 100

# Reset the index to make 'DateCode' and 'RegionName' columns
grouped_data.reset_index(inplace=True)

# Plot recycling percentage for each region over the years
for year in grouped_data['DateCode'].unique():
    year_data = grouped_data[grouped_data['DateCode'] == year]

    # Adjust figure size
    plt.figure(figsize=(8, 8))

    # Rotate labels
    plt.pie(year_data['Recycling Percentage'], labels=year_data['Reference Area'], autopct='%1.1f%%', startangle=90)
    plt.title(f'Recycling Percentage by Region in Scotland ({year})')

    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')
    plt.show()
