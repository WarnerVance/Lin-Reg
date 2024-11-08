# Readme
This is my linear regression program written in python using pandas, math, and seaborn.

The data input csv must be two columns with the column 0 being the x data and column 1 being the y data. This program 
has only been tested with changing the x values (column 0) to linearize the data. The top row of the csv will be the two
variable names. I don't know if it would work if you choose to linearize by changing the y data. If you want to mess with that 
please let me know how it works

## To use:
1. Place a file called Data.csv in the same directory as LinReg.py (follow the directions above regarding the csv file)
2. Run LinReg.py
3. This will create 3 files. Exported_data.csv contains the input data with added calculations performed on each row. Exported_stats.csv contains summary statistics
like of the slope of the line of best fit, r value, r squared value, and sum of squared error among others. 
The third file is graph.png which will contain a scatterplot of the inputted data with the line of best fit. 
4. Done!

# Lin_reg_test.py
This program tests various transformations that can be done on your dataset and compares their $`r^2`$ values to find which
one is lowest. You can then chose to transform your Data.csv file to fit which ever transformation you choose

# Explanation of Stats values
### r
r is the correlation coefficient which measured how correlated two datasets are. It goes from -1 to 1 with a higher absolute
value implying a stronger relationship. If r is negative it implies an inverse relationship between the two datasets (as 
one increases the other decreases). If r is positive it implies a direct relationship where as one value increases so does 
the other.

### r squared
r squared is just the r value from before squared. It is the proportion of the variation in the dependent variable that is 
predictable from the independent variable(s). Essentially it tells you how well your line of best fit explains the data. 
An r squared of 1 means that all the datapoints are on the line of best fit.

### SSE
SSE is the sum of the squared errors. In this case error means the distance between the recorded datapoint and the datapoint
predicted by the line of best fit. This value found for each data point, squared, then summed to find the SSE. 

### MSE
MSE is the mean square error. You get it be dividing SSE by the number of data points

#### RMSE

RMSE is the root mean square error. You get it by square rooting MSE. Unlike MSE it is not in square units. 

### s_xx and s_yy
These are the squared difference between the data points and the mean of that column (x for s_xx or y for s_yy).This is called the 
**variance**. The sum of the variances for x and y are found in exported_stats.csv. These sums are used to find the line of best fit,
and r values along with the covariance denoted s_xy

### s_xy
The covariance or s_xy is $`(x-x_{mean})*(y-y_{mean})`$. The sum of  s_xy is used along with s_xx and s_yy to find r and 
line of best fit.
