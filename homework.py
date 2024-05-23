import matplotlib.pyplot as plt

# Import the pandas package to provide data manipulation tools
# Import matplotlib.pyplot to provide plotting (visualisation) tools

df = pd.read_csv('scotland-renewable-electricity.csv')
# Read the CSV file containing data and create a pandas DataFrame object to hold it.
# DataFrames are a powerful pandas datastructure;
# see: https://pandas.pydata.org/pandas-docs/stable/dsintro.html
test_df_1 = df.transpose()
print(test_df_1)
# See the contents of the DataFrame

df.plot(kind='bar', title='Scottish Electricity Generation - %age Renewable')
# Plot the data in the DataFrame as a basic bar chart

plt.show()
# Show the plot on the screen

