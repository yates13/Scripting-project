#! /usr/bin/env python3


#importing necessary packages
import sys
import re
import pandas as pd
import openpyxl
from openpyxl.chart import BarChart,Reference
import matplotlib.pyplot as plt  

#read in excel document from command line argument
wb = pd.read_excel(sys.argv[1])
#print(wb)

#set range to search for sample list 
sample_range = wb.iloc[50:300, 1]
print(sample_range)

#initialize sample count (count), line iterator (iter), and sample mean dictionary (sample_means)
count = 0
iter = 49
sample_means = {}

#Searching for samples in sample range using regex
for i in sample_range:
    j = re.match('SPL', str(i))
    iter = iter + 1
    #Adding sample name and mean to sample means dict if match found
    if j != None:
        count = count + 1
        sample_means.update({wb.iloc[iter, 1]:wb.iloc[iter,6]})
print(sample_means)
#print(wb.iloc[50:120, 6])

#Prompting user for normalization
raw_val = input("Which samples need to be normalized? Separate by a comma (eg. SPL2, SPL3, SPL4): \n")
raw_val_list = raw_val.split(", ")
print(raw_val_list)
adj_mean = []

#Prompting user for control sample for each previous entry
norm_pairs = {}
for i in raw_val_list:
    norm = input("Which sample should be used to normalize " + i + "?\n")
    adj_mean.append((sample_means[i]/sample_means[norm])*100)
  
print(adj_mean)



#    print(type(i)) 

#for i in range(10):

#            sheet.append([i])

# create data for plotting

#values = Reference(sheet, min_col = 1, min_row = 1,

                                                    #                    max_col = 1, max_row = 10)

# Create object of BarChart class

#chart = BarChart()

# adding data to the Bar chart object

#chart.add_data(values)

# set the title of the chart

#chart.title = " BAR-CHART "

# set the title of the x-axis

#chart.x_axis.title = " X_AXIS "

# set the title of the y-axis

#chart.y_axis.title = " Y_AXIS "

# add chart to the sheet

# the top-left corner of a chart

# is anchored to cell E2 .

#sheet.add_chart(chart, "E2")

# save the file

#wb.save("barChart.xlsx")
