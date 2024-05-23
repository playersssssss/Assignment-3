# Import the pandas package to provide data manipulation tools
# Import matplotlib.pyplot to provide plotting (visualisation) tools
import pandas as pd
import matplotlib.pyplot as plt

waste_data = pd.read_csv('D:/homework/scotland-waste-data-2011-2013.csv')


waste_data.plot(kind='area',stacked= False, FIGSIZE=(10,6))
plt.title('the total waste produced and waste sent to landfill by each Scottish region in 2013')
plt.xlabel('regional area')
plt.ylabel('waste amount')

plt.show()