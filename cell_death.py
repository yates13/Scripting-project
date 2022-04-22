#! /usr/bin/env python3


#importing necessary packages
import sys
import re
import pandas as pd
import openpyxl
from openpyxl.chart import BarChart,Reference
import matplotlib.pyplot as plt
import numpy as np



def sample(count, iter, sample_means, sample_names):
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
    raw_val = input("Which samples need to be normalized? Separate by a comma (eg. SPL2, SPL3, SPL4): \n")
    raw_val_list = raw_val.split(", ")


    for i in raw_val_list:
        norm = input("Which sample should be used to normalize " + i + "?\n")
        adj_mean = (sample_means[i]/sample_means[norm])*100
        tag = sample_names[i]
        print(tag)
        norm_means.update({tag:adj_mean})


def plotting(sample, mean_values):
    p1 = plt.bar(sample, mean_values)
    plt.title('Cell Death Assay')
    plt.ylabel('Mean Luminescence (Normalized)')
    plt.savefig('cell_death.jpg', dpi = 100)
    plt.show()

if __name__ == '__main__':
    #initialize sample count (count), line iterator (iter), sample mean dictionary (sample_means), and sample names dictionary (sample_names)
    count = 0
    iter = 49
    raw_val = {}
    norm_means = {}
    #read in excel document from command line argument
    wb = pd.read_excel(sys.argv[1])
    #set range to search for sample list
    sample_range = wb.iloc[50:300, 1]
    sample_means = {}
    sample_names = {}
    sample(count, iter, sample_means, sample_names)
    mean_values = norm_means.values()
    sample = norm_means.keys()
    plotting(sample, mean_values)
