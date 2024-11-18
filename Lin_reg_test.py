import math
import pandas as pd


# Inputs the data from a csv file named data.
# The csv must be 2 columns with column 0 being x and column y being 1
def calculate_r_squared(dataframe):
    column_names = dataframe.columns.to_list()
    x_column = column_names[0]
    y_column = column_names[1]
    x_mean = dataframe[x_column].mean()
    y_mean = dataframe[y_column].mean()

    # This calculates the S_xx and S_yy. I
    x_variance = pd.Series((dataframe[x_column] - x_mean) ** 2)
    y_variance = pd.Series((dataframe[y_column] - y_mean) ** 2)
    # Calculate the S_xy
    covariance = pd.Series((dataframe[x_column] - x_mean) * (dataframe[y_column] - y_mean))
    # This calculates the sums for the S_xx, S_yy and S_xy columns
    s_xx_sum = x_variance.sum()
    s_yy_sum = y_variance.sum()
    s_xy_sum = covariance.sum()

    # This finds the r and r squared values
    r = s_xy_sum / (math.sqrt(s_xx_sum) * math.sqrt(s_yy_sum))
    r_squared = r ** 2
    return r_squared

def find_best_r2(df):
    column_names = df.columns.to_list()
    x_column = column_names[0]
    y_column = column_names[1]
    df_safe = df
    list_r2 = ["R Squared"]
    list_r2_index = ["Curves", "Linear", "Squared", "Inverse", "Square Root"]
    current_r_squared = calculate_r_squared(df)
    list_r2.append(current_r_squared)
    df = df_safe
    df[x_column] = df[x_column] ** 2
    current_r_squared = calculate_r_squared(df)
    list_r2.append(current_r_squared)
    df = df_safe
    df[x_column] = 1 / df[x_column]
    current_r_squared = calculate_r_squared(df)
    list_r2.append(current_r_squared)
    df = df_safe
    df[x_column] = df[x_column] ** (1 / 2)
    current_r_squared = calculate_r_squared(df)
    list_r2.append(current_r_squared)
    r2_list_index = pd.DataFrame(list_r2, index=list_r2_index)
    return r2_list_index
