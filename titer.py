#! /usr/bin/env python3

import sys
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt  

df = pd.read_csv(sys.argv[1])
#print(df)


sample_range = df.iloc[0:150, 1]
#print(sample_range)

count = 0
iter = 49
virus = {}
for i in sample_range:
    j = re.match('12', str(i))
    iter = iter + 1
    if j != None:
        count = count + 1
        sample_means.update({wb.iloc[iter, 1]:wb.iloc[iter,6]})
print(sample_means)


raw_val = input("Which samples need to be normalized? Separate by a comma (eg. SPL2, SPL3, SPL4): \n")



#def needle(infile, line_iterator,pos):
#    print('room1.txt')
#    with open('room1.txt', 'r') as in_stream:
#        print('Opening output.txt')
#        with open('needles.txt', 'w') as out_stream:
