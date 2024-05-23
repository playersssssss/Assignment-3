# Import the pandas package to provide data manipulation tools
# Import matplotlib.pyplot to provide plotting (visualisation) tools
import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file
df = pd.read_csv('C:\\Users\\chen\\Downloads\\scotland-fire-incidents (1).csv')

# print the DataFrame to inspect the data
print(df)

# delete the entire column corresponding to the specific row index
df.drop('All', axis=1, inplace=True)

# Assign the dataFrame to a new variable
pd = df

# Plot a stacked bar chart
pd.plot(kind='bar', stacked=True, figsize=(10, 6))

# Set the x-axis tick labels with rotation
plt.xticks(range(len(df['Reference Area'])), df['Reference Area'], rotation=75)

# Add title and labels
plt.title('the number of fire incidents recorded in Scotland (by area)')
plt.xlabel('area')
plt.ylabel('Number of fires')

# Display the plot
plt.show()