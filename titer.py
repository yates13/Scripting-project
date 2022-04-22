
#! /usr/bin/env python3

import sys
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt


def unique(Virus):

    # traverse for all elements
    for x in Virus:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return(unique_list)


def Data(virus_list, Virus, df):
    for x in virus_list:
        globals()[f"dict_{x}"] = {}
        iter = 0
        for i in Virus:
            if i == x:
                globals()[f"dict_{x}"].update({df.iloc[iter, 2]:df.iloc[iter, 1]})
            iter = iter + 1
        globals()[f"keys_{x}"] = list(globals()[f"dict_{x}"].keys())
        globals()[f"keys_{x}"] = [j.replace(' ', '') for j in globals()[f"keys_{x}"]]
        globals()[f"values_{x}"] = list(globals()[f"dict_{x}"].values())
        print(x)

def Plotting(virus_list, hour, log_pfu):
    for x in virus_list:
        plt.plot(globals()[f"keys_{x}"], globals()[f"values_{x}"])
    plt.title('Viral Growth Curve')
    plt.xlabel('Hours')
    plt.ylabel('Log_PFU')
    plt.legend(virus_list, loc='upper left')
    plt.savefig('titer.jpg', dpi = 100)
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv(sys.argv[1])
    Virus = df.iloc[0:50, 0]
    Virus = [w.replace(' ', '_') for w in Virus]
    unique_list = []
    unique(Virus)
    virus_list = unique(Virus)
    Data(virus_list, Virus, df)
    hour = df.iloc[0:50, 2]
    log_pfu = df.iloc[0:50,1]
    Plotting(virus_list, hour, log_pfu)

