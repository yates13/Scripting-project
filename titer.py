#! /usr/bin/env python3

import sys
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt  

dataset = pd.read_excel(sys.argv[1])
print(dataset)

