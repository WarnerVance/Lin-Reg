import pandas as pd
import math
import seaborn as sns

# Inputs the data from a csv file named data.
# The csv must be 2 columns with column 0 being x and column y being 1
# This  programs assumes that we change the x value to linearize the data and not the y value

df = pd.read_csv("Data.csv")
x_column = input("Enter the x column name: ")
def calculate_r_squared(df):
    x_mean = df.iloc[:, 0].mean()
    y_mean = df.iloc[:, 1].mean()

    # This calculates the S_xx and S_yy. I
    x_variance = []
    y_variance = []
    for i in range(len(df)):
        x_variance.append((df.iloc[i, 0] - x_mean) ** 2)
    for i in range(len(df)):
        y_variance.append((df.iloc[i, 1] - y_mean) ** 2)

    # Creates two columns in the dataframe with the x and y variances for each row
    df['S_xx'] = x_variance
    df['S_yy'] = y_variance

    # Calculate the S_xy and make it a new column in the dataframe
    covariance = []
    for i in range(len(df)):
        covariance.append((df.iloc[i, 0] - x_mean) * (df.iloc[i, 1] - y_mean))
    df['S_xy'] = covariance

    # This calculates the sums for the S_xx, S_yy and S_xy columns
    s_xx_sum = sum(df['S_xx'])
    s_yy_sum = sum(df['S_yy'])
    s_xy_sum = sum(df['S_xy'])

    # This finds the r and r squared values
    r = s_xy_sum / (math.sqrt(s_xx_sum) * math.sqrt(s_yy_sum))
    r_squared = r ** 2
    return r_squared
print('Here is the r squared of various transformations that happen to the data')
print(f'Linear model {calculate_r_squared(df)}')
df = pd.read_csv("Data.csv")
df[x_column] = df[x_column] **2
print(f'Squared model {calculate_r_squared(df)}')
df = pd.read_csv("Data.csv")
df[x_column] = 1/df[x_column]
print(f'Inverse {calculate_r_squared(df)}')
df = pd.read_csv("Data.csv")
df[x_column] = df[x_column] ** (1/2)
print(f'Square root {calculate_r_squared(df)}')

