import time
start = time.process_time()
import numpy as np
import pandas as pd
import math


# Inputs the data from a csv file named data.
# The csv must be 2 columns with column 0 being x and column y being 1
df = pd.read_csv("Data.csv")

column_names = df.columns.to_list()
x_column = column_names[0]


def calculate_r_squared(dataframe):
    x_mean = dataframe.iloc[:, 0].mean()
    y_mean = dataframe.iloc[:, 1].mean()

    # This calculates the S_xx and S_yy. I
    x_variance = []
    y_variance = []
    for i in range(len(dataframe)):
        x_variance.append((dataframe.iloc[i, 0] - x_mean) ** 2)
    for i in range(len(dataframe)):
        y_variance.append((dataframe.iloc[i, 1] - y_mean) ** 2)

    # Calculate the S_xy
    covariance = []
    for i in range(len(dataframe)):
        covariance.append((dataframe.iloc[i, 0] - x_mean) * (dataframe.iloc[i, 1] - y_mean))

    # This calculates the sums for the S_xx, S_yy and S_xy columns
    s_xx_sum = sum(x_variance)
    s_yy_sum = sum(y_variance)
    s_xy_sum = sum(covariance)

    # This finds the r and r squared values
    r = s_xy_sum / (math.sqrt(s_xx_sum) * math.sqrt(s_yy_sum))
    r_squared = r ** 2
    return r_squared


list_r2 = []
list_r2_index = ["Linear", "Squared", "Inverse", "Square Root"]
# This outputs all the data.
print('Here is the r squared of various transformations that happen to the data')
current_r_squared = calculate_r_squared(df)
print(f'Linear model {current_r_squared}')
list_r2.append(current_r_squared)

df = pd.read_csv("Data.csv")
df[x_column] = df[x_column] ** 2
current_r_squared = calculate_r_squared(df)
print(f'Squared model {current_r_squared}')
list_r2.append(current_r_squared)

df = pd.read_csv("Data.csv")
df[x_column] = 1 / df[x_column]
current_r_squared = calculate_r_squared(df)
print(f'Inverse {current_r_squared}')
list_r2.append(current_r_squared)

df = pd.read_csv("Data.csv")
df[x_column] = df[x_column] ** (1 / 2)
current_r_squared = calculate_r_squared(df)
print(f'Square root {current_r_squared}')
list_r2.append(current_r_squared)


# This finds which model provides the lowest r squared value and then prints that out.
best_fit = np.argmax(list_r2)
print(list_r2_index[best_fit], "is the best model for fit.")

print(f'Elapsed time: {time.process_time()-start}')

print("0. Exit Program, 1.Square data, 2. Take the reciprocal (inverse), 3. Square root")
transform = int(input("How would you like to transform the data "))
df = pd.read_csv("Data1.csv")
if transform == 0:
    exit(0)
elif transform == 1:
    df[x_column] = df[x_column] ** 2
elif transform == 2:
    df[x_column] = 1 / df[x_column]
elif transform == 3:
    df[x_column] = df[x_column] ** 0.5
else:
    exit(1)

df.to_csv("Data1.csv", index=False)
exit(0)
