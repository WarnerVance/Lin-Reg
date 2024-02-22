import math

import pandas as pd
import seaborn as sns
from pandas import DataFrame

# Inputs the data from a csv file named data.
# The csv must be 2 columns with column 0 being x and column y being 1
# This  programs assumes that we change the x value to linearize the data and not the y value
df: DataFrame = pd.read_csv("Data.csv")

x_mean = df.iloc[:, 0].mean()
y_mean = df.iloc[:, 1].mean()
# TODO: Update the readme file with more instructions.
# This calculates the S_xx and S_yy. I
x_variance = []
y_variance = []
for i in range(len(df)):
    x_variance.append((df.iloc[i, 0] - x_mean)**2)
for i in range(len(df)):
    y_variance.append((df.iloc[i, 1] - y_mean)**2)


# Calculate the S_xy and make it a new column in the dataframe
covariance = []
for i in range(len(df)):
    covariance.append((df.iloc[i, 0] - x_mean)*(df.iloc[i, 1] - y_mean))
s_xx_sum = sum(x_variance)
s_yy_sum = sum(y_variance)
s_xy_sum = sum(covariance)

# This finds the r and r squared values
r = s_xy_sum/(math.sqrt(s_xx_sum)*math.sqrt(s_yy_sum))
r_squared = r ** 2

# Find the slope and intercept
slope = s_xy_sum/s_xx_sum
intercept = y_mean-(slope*x_mean)

'''
Find the squared error. THat is the squared difference between the actual y value 
and the y value that would be predicted using the x value, the slope, and the intercept
'''
# Calculate the predicted values
predicted_values = []
for i in range(len(df)):
    predicted_values.append(slope*df.iloc[i, 0] + intercept)
df['Predicted Y'] = predicted_values

squared_error = []
for i in range(len(df)):
    squared_error.append((df.iloc[i, 1]-(predicted_values[i])) ** 2)
df['Squared Error'] = squared_error

df['S_xx'] = x_variance
df['S_yy'] = y_variance
df['S_xy'] = covariance

# This is the sum of the squared error
SSE = sum(df['Squared Error'])

# This creates a plot with a line of best fit then exports it as graph.png
graph = sns.regplot(data=df, x=df.iloc[:, 0], y=df.iloc[:, 1], ci=None)
fig = graph.get_figure()
fig.savefig("graph.png")

# Export the dataframe as a csv
df.to_csv('Exported_Data.csv', index=False)

# Export the collected stats summaries as another csv
output_idx = ('X_Mean', 'Y_Mean', 'R', 'R Squared',
              'Slope', 'Intercept', 'SSE', 'S_xx sum', 'S_yy sum', 'S_xy Sum', "N")
output_data = (x_mean, y_mean, r, r_squared, slope, intercept, SSE, s_xx_sum, s_yy_sum, s_xy_sum, int(len(df)))
df_output_data = pd.Series(output_data, index=output_idx)
df_output_data.to_csv('Exported_Stats.csv')
# Exits the program
exit(0)
