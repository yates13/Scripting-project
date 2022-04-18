#! /usr/bin/env python3

import sys
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt  

df = pd.read_csv(sys.argv[1])
print(df)



#df_name = pd.DataFrame([1,2,3])
#df_name[0].plot(kind='bar')

#plt.show()
#Virus = df.iloc[0:50, 0]
#print(Virus)

#hour = df.iloc[0:50, 2]
#print(hour)

#log_pfu = df.iloc[0:50,1]
#print(log_pfu)

#plt.plot(hour)
#plt.plot(log_pfu)
#plt.plot(Virus, color = 'green')
df.plot.line()
plt.title('Viral Growth Curve')
plt.xlabel('Hours')
plt.ylabel('Log_PFU')
plt.legend(loc='upper left')
plt.show()




# need to make a dictonary that time all the time point and values related to the different
# types of viruses ( can probably have that be an input like the other scripts 

#count = 0
#iter = 0
#virus = {}
#for i in sample_range:
#    j = re.match('\w', str(i))
#    iter = iter + 1
 #   if j != None:
  #      count = count + 1
   #     virus.update({df.iloc[iter, 0]:df.iloc[iter,1]})
   # else:
    #    quit()
#print(virus)

#counts = []
#frequencies = []

#for d in csv.DictReader(open('yourfile.csv'), delimiter='\t'):
 #   counts.append(int(d['Counts']))
  #  frequencies.append(int(d['frequency']))


#raw_val = input("Which samples need to be normalized? Separate by a comma (eg. SPL2, SPL3, SPL4): \n")



#def needle(infile, line_iterator,pos):
#    print('room1.txt')
#    with open('room1.txt', 'r') as in_stream:
#        print('Opening output.txt')
#        with open('needles.txt', 'w') as out_stream:
