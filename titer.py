#! /usr/bin/env python3

import sys
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt  

dataset = pd.read_excel(sys.argv[1])
print(dataset)


def needle(infile, line_iterator,pos):
    print('room1.txt')
    with open('room1.txt', 'r') as in_stream:
        print('Opening output.txt')
        with open('needles.txt', 'w') as out_stream:
