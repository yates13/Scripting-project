
#! /usr/bin/env python3

import sys
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])
#print(df)

Virus = df.iloc[0:50, 0]
Virus = [w.replace(' ', '_') for w in Virus]
#df = [w.replace(' ', '') for w in df]

#print(Virus)

def unique(list1):

    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return(unique_list)

virus_list = unique(Virus)
print(virus_list)


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
    print(globals()[f"keys_{x}"])
#    print(globals()[f"dict_{x}"])
#print("NEXT")
#print(dict_WT_Delta_611)
#print(values_WT_Delta_611)
#print(keys_WT_Delta_611)

hour = df.iloc[0:50, 2]
#hour = hour[::-1]
#print(hour)


log_pfu = df.iloc[0:50,1]
#print(log_pfu)

for x in virus_list:
    plt.plot(globals()[f"keys_{x}"], globals()[f"values_{x}"])


######this works
plt.title('Viral Growth Curve')
plt.xlabel('Hours')
plt.ylabel('Log_PFU')
plt.legend(virus_list, loc='upper left')
plt.show()



#plt.plot(log_pfu)
#plt.plot(Virus, color = 'green')


#for d in csv.DictReader(open('yourfile.csv'), delimiter='\t'):
 #   counts.append(int(d['Counts']))
  #  frequencies.append(int(d['frequency']))

