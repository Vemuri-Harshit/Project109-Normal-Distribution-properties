import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff;
import plotly.graph_objects as go;

df = pd.read_csv("data.csv")
math_list = df["math"].to_list()

#Mean for math 
math_mean = statistics.mean(math_list)

#Median for math 
math_median = statistics.median(math_list)

#Mode for math 
math_mode = statistics.mode(math_list)

#Printing mean, median and mode to validate
print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_mean, math_median, math_mode))

#Standard deviation for math 
math_std_deviation = statistics.stdev(math_list)

#1, 2 and 3 Standard Deviations for math
math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

#Percentage of data within 1, 2 and 3 Standard Deviations for math
math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

#Printing data for math  (Standard Deviation)
print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))

fig = ff.create_distplot([math_list], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[math_mean, math_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[math_first_std_deviation_start, math_first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[math_first_std_deviation_end, math_first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[math_second_std_deviation_start, math_second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[math_second_std_deviation_end, math_second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[math_third_std_deviation_start, math_third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[math_third_std_deviation_end, math_third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()

