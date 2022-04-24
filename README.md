
## Automating Routine Data Visualization - Python Scripting Project

### Shawn Yates and Rachel Haich
 
Our current lab practices use excel and graphpad for visualization of large amounts of data. This is sufficient for small experiments, but is time consuming, particularly for large
 experiments. Additionally, graphpad is not open source and requires an annual subscription. For this project, we created automated python and R scripts to process and visualize our results from excel datasheets into easily interpretted graphics.

The first main target for automation in our lab are cell death assays, which measure the rate of cell death in response to a treatment. The output of this test is a standardized excel template which can be used as the basis of our script. However, the excel sheet can change how the results should be interpreted depending on how the samples are loaded in the assay. To overcome this we wanted to make the script more interactive so the user could decide how to normalize the samples.

The second target is our viral growth curve assays. This requires manual input of viral titer counts into a formatted excel sheet. This assay has a variable sample size depending on how many viruses are measured.

We wrote a python script for each case which quickly processes the data and presents it in an easy to read, publishable format while reducing the possiblity of user error during visualization. We also wrote an R script which parallels the titer.py format to give users options depending on the language they feel more comfortable using. In total, this repository contains 3 fully commented and documented scripts, two written in python3, and one written in R 4.1.3

### Example Datasets


**titer_data.csv**

**cell_death_data_final.xlsx**

### Scripts

#### titer code.R 

**Purpose**

This script is a hard coded R script for viral samples commonly used in our lab. This script the viral sample names to extract the time points and viral titers for each sample to generate a line graph. This code is good for quick visualization, but produces a less polished and less reproducible product. In addition, the code must be altered directly in order to visualize different samples. For these reasons, we reccommend the python code for most visualization.  

External Packages
 - stringr (search for a pattern within a string)
```
10 Titer$hour_fix <- str_remove_all(Titer$Hour, " hour")
```
---

#### titer.py

**Purpose**

This script uses a lab generated csv template file in order to graph the growth curves of viral assays. The script will determine the number of viral samples in the dataset and will generate a line chart with corresponding time points and viral titer values. The generated graph includes a legend of the viral samples and can be used for comparison across viral growth curves. To use this script, datasets must be entered as a system argument: `python3 titer.py titer_data.csv`. The script will print the unique sample names, which will then be used in the legend of the final graph.  

External Packages
 - sys (import of user arguments)
 ```
 45     df = pd.read_csv(sys.argv[1])
 ```
 - pandas (read in csv files)
  ```
 45     df = pd.read_csv(sys.argv[1])
 ```
 - matplotlib
 ```
 35     plt.title('Viral Growth Curve')
36     plt.xlabel('Hours')
37     plt.ylabel('Log_PFU')
```

**Output**

![viral growth curve](https://github.com/yates13/Scripting-project/blob/main/Titers/titer.jpg)

---

#### cell_death.py

**Purpose**

This script provides an interactive interface to graph cell death data from a standardized excel output generated when using the Gen5 plate reading software (version 2.03.1) in combination with the synergy H1 Hybrid Plate Reader. The output file is added to the script as an argument. For example, `python3 cell_death.py cell_death_data_final.xlsx`. The script then prompts the user for samples to be normalized and graphed. Each entry is then normalized to another user input sample, which is confirmed through a print statement:

```
Which samples need to be normalized? Separate by a comma (eg. SPL2, SPL3, SPL4): 
SPL11, SPL12, SPL13
Which sample should be used to normalize SPL11?
SPL8
SVEC mRHIM
Which sample should be used to normalize SPL12?
SPL9
SVEC mRHIM d611
Which sample should be used to normalize SPL13?
SPL10
SVEC mRHIM rescue 
```
This will produce a python generated bar chart which is similar to the graphs generated using GraphPad and can be used for rapid (and free) data visualization. 

**External Packages**
 - sys (import of user arguments)
 ```
 53     wb = pd.read_excel(sys.argv[1])
```
 - re (regex arguments)
```
17     for i in sample_range:
18         j = re.match('SPL', str(i))
```
 - pandas (import .xlsx files)
 ```
 53     wb = pd.read_excel(sys.argv[1])
```
 - matplotlib (plotting)
 ```
37     plt.title('Cell Death Assay')
38     plt.ylabel('Mean Luminescence (Normalized)')
```

**Output**

![cell death - bar chart](https://github.com/yates13/Scripting-project/blob/main/Cell_death/cell_death.jpg)





