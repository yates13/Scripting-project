#! /usr/bin/env python3


#importing necessary packages
import sys
import re
import pandas as pd
import openpyxl
from openpyxl.chart import BarChart,Reference
import matplotlib.pyplot as plt
import numpy as np
#read in excel document from command line argument
wb = pd.read_excel(sys.argv[1])

#set range to search for sample list
sample_range = wb.iloc[50:300, 1]

#initialize sample count (count), line iterator (iter), sample mean dictionary (sample_means), and sample names dictionary (sample_names)
count = 0
iter = 49
sample_means = {}
sample_names = {}
#Searching for samples in sample range using regex
for i in sample_range:
    j = re.match('SPL', str(i))
    iter = iter + 1
    #Adding sample name and mean to sample means dict if match found
    if j != None:
        count = count + 1
        sample_means.update({wb.iloc[iter, 1]:wb.iloc[iter,6]})
        sample_names.update({wb.iloc[iter, 1]:wb.iloc[iter,2]})

#Prompting user for normalization
raw_val = {}
raw_val = input("Which samples need to be normalized? Separate by a comma (eg. SPL2, SPL3, SPL4): \n")
raw_val_list = raw_val.split(", ")

#initialize adjusted mean list for vectors
norm_means = {}
#print(sample_names)
#Prompting user for control sample for each previous entry
for i in raw_val_list:
    norm = input("Which sample should be used to normalize " + i + "?\n")
    adj_mean = (sample_means[i]/sample_means[norm])*100
    tag = sample_names[i]
    print(tag)
    norm_means.update({tag:adj_mean})
    #print(name)

#    print(adj_mean)

print(norm_means)

#names = sample_names.values()
#index = np.arange(len(raw_val_list)) + 0.3
mean_values = norm_means.values()
sample = norm_means.keys()

#print(mean_values)
p1 = plt.bar(sample, mean_values)
#p1 = plt.bar(index, mean_values)
#p1.set_xticks(names)
plt.title('Cell Death Assay')
#plt.bar_label(p1, Labels=raw_val_list)
plt.ylabel('Mean Luminescence (Normalized)')
#p1.set_xticklabels(["A","B","C","D"])
plt.show()


