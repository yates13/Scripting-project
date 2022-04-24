
#! /usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt


def unique(Virus):
    """
    Generates a list containing all unique sample names within the dataset (df) 
    ---------
    Arguments:
        In:
            Virus = all the virus samples that are in the dataset cleaned to make them more uniform
        Out:
            unique_list = a list of the unique virus names found in the dataset
    --------
    Example:
    """
    # traverse for all elements
    for x in Virus:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return(unique_list)


def Data(virus_list, Virus, df):
    """
    Generates a dictionary that will pull each unique viral sample and match the
    corresponding  time point and viral titers for each sample
    ---------
    Arguments:
        In:
            virus_list = a list of the unique virus names found in the dataset
            Virus = all the virus samples that are in the dataset cleaned to make them more uniform
            df = the dataframe that the user inputs
        Out:
            A dictionary of each viral sample and corresponding time points (dict_sample)
    --------
    Example:
        dict_WT
        {'0 hour': 3.21, '12 hour ': 2.85, '24 hour': 2.98, '48 hour': 4.99, '72 hour': 5.75, '96 hour ': 6.44, '120 hour': 6.56}
    """

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
    """
    Generates a line plot of the viral samples to visualze growth over time
    ---------
    Arguments:
        In:
            virus_list = is a list of the unique virus found in the dataset
            hour = a list of all the time points in the dataset
            log_pfu = a list of all the log_pfu (viral titers) in the dataset
        Out:
            A line graph that takes all the viral samples and matches the corresponding time point and log_pfu to graph them as lines on the graph.
    """

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

