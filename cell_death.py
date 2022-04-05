#! /usr/bin/env python3

import sys
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt  


#import argument as dataset (.xlsx format)
dataset = pd.read_excel(sys.argv[1])
print(dataset)

#def cell_death():
#    print('Opening cell_death.xlsx ')
#    with open('cell_death.xlsx ', 'r') as in_stream:
#            print('Opening output.txt')
#    pass

#if __name__ == '__main__':
    #cell_death()
