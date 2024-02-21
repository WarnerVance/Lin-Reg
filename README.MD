# Readme
This is my linear regression program written in python using pandas, math, and seaborn.

The data input csv must be two columns with the column 0 being the x data and column 1 being the y data. This program 
has only been tested with changing the x values (column 0) to linearize the data. The top row of the csv will be the two
variable names. I don't know if it would work if you choose to linearize by changing the y data. If you want to mess with that 
please let me know how it works

To use:
1. Place a file called Data.csv in the same directory as LinReg.py (follow the directions above regarding the csv file)
2. Run LinReg.py
3. This will create 3 files. Exported_data.csv contains the input data with added calculations performed on each row. Exported_stats.csv contains summary statistics
like of the slope of the line of best fit, r value, r squared value, and sum of squared error among others. 
The third file is graph.png which will contain a scatterplot of the inputted data with the line of best fit. 
4. Done!