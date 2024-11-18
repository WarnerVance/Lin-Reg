# Inputs the data from a csv file named data.
# The csv must be 2 columns with column 0 being x and column y being 1

def predict(df):
    import math
    import pandas as pd
    x_mean = df.iloc[:, 0].mean()
    y_mean = df.iloc[:, 1].mean()
    
    column_names = df.columns.to_list()
    x_column = column_names[0]
    y_column = column_names[1]

    df['S_xx'] = (df[x_column] - x_mean) ** 2
    df['S_yy'] = (df[y_column] - y_mean) ** 2
    df['S_xy'] = (df[x_column] - x_mean) * (df[y_column] - y_mean)
    s_xx_sum = df['S_xx'].sum()
    s_yy_sum = df['S_yy'].sum()
    s_xy_sum = df['S_xy'].sum()

    r = s_xy_sum/(math.sqrt(s_xx_sum)*math.sqrt(s_yy_sum))
    r_squared = r ** 2

    slope = s_xy_sum/s_xx_sum
    intercept = y_mean-(slope*x_mean)

    df['Predicted Y'] = slope*df[x_column] + intercept
    df['Squared Error'] = (df[y_column] - df['Predicted Y']) ** 2
    SSE = df['Squared Error'].sum()
    MSE = df['Squared Error'].mean()
    RSME = math.sqrt(MSE)

    output_idx = ('X_Mean', 'Y_Mean', 'R', 'R Squared',
                  'Slope', 'Intercept', 'SSE', 'S_xx sum', 'S_yy sum', 'S_xy Sum', "N", "MSE", "RSME")
    output_data = (x_mean, y_mean, r, r_squared, slope, intercept, SSE, s_xx_sum, s_yy_sum, s_xy_sum, int(df.shape[0]), MSE, RSME)
    
    answers = pd.DataFrame(output_data, index=output_idx)
    
    return answers
