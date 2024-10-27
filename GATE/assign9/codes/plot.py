import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]
exports = [50, 60, 70, 60, 70, 70, 100, 110]
imports = [40, 50, 60, 70, 80, 90, 100, 120]

# Set the width of the bars
# Set the positions of the bars on the x-axis
x = np.arange(len(years))

# Create the bar chart
plt.bar(x-0.2, exports, width=0.4, color='red', label='Exports')
plt.bar(x+0.2, imports, width=0.4, color='blue', label='Imports')

plt.yticks(np.arange(10, 121, 10))
# Customize the plot


plt.xticks(x, years)
plt.legend()
plt.grid(axis='y')
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')

# Show the plot
plt.show()
