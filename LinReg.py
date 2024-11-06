import math
import pandas as pd
import seaborn as sns

# Inputs the data from a csv file named data.
# The csv must be 2 columns with column 0 being x and column y being 1
# This  programs assumes that we change the x value to linearize the data and not the y value
df = pd.read_csv("Data.csv")

x_mean = df.iloc[:, 0].mean()
y_mean = df.iloc[:, 1].mean()
# TODO: Update the readme file with more instructions.
# This calculates the S_xx and S_yy.
column_names = df.columns.to_list()
x_column = column_names[0]
y_column = column_names[1]

# Calculate the S_xy and make it a new column in the dataframe
df['S_xx'] = (df[x_column] - x_mean) ** 2
df['S_yy'] = (df[y_column] - y_mean) ** 2
df['S_xy'] = (df[x_column] - x_mean) * (df[y_column] - y_mean)
s_xx_sum = df['S_xx'].sum()
s_yy_sum = df['S_yy'].sum()
s_xy_sum = df['S_xy'].sum()

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
df['Predicted Y'] = slope*df[x_column] + intercept
df['Squared Error'] = (df[y_column] - df['Predicted Y']) ** 2
# This is the sum of the squared error
SSE = df['Squared Error'].sum()
MSE = df['Squared Error'].mean()
RSME = math.sqrt(MSE)

# This creates a plot with a line of best fit then exports it as pzgraph.png
graph = sns.regplot(data=df, x=df.iloc[:, 0], y=df.iloc[:, 1], ci=None)
fig = graph.get_figure()
fig.savefig("graph.png")

# Export the dataframe as a csv
df.to_csv('Exported_Data.csv', index=False)

# Export the collected stats summaries as another csv
output_idx = ('X_Mean', 'Y_Mean', 'R', 'R Squared',
              'Slope', 'Intercept', 'SSE', 'S_xx sum', 'S_yy sum', 'S_xy Sum', "N", "MSE", "RSME")
output_data = (x_mean, y_mean, r, r_squared, slope, intercept, SSE, s_xx_sum, s_yy_sum, s_xy_sum, df.shape[0], MSE, RSME)
df_output_data = pd.Series(output_data, index=output_idx)
df_output_data.to_csv('Exported_Stats.csv')
# Exits the program
print(f"RSME: {RSME}, Slope: {slope}, Intercept: {intercept}")
exit(0) 
