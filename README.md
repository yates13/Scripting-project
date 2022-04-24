
## Automating Routine Data Visualization - Python Scripting Project

### Shawn Yates and Rachel Haich
 
Our current lab practices use excel and graphpad for visualization of large amounts of data. This is sufficient for small experiments, but is time consuming, particularly for large
 experiments. Additionally, graphpad is not open source and requires an annual subscription. For this project, we created automated python and R scripts to process and visualize our results from excel datasheets into easily interpretted graphics.

The first main target for automation in our lab are cell death assays, which measure the rate of cell death in response to a treatment. The output of this test is a standardized excel template which can be used as the basis of our script. However, the excel sheet can change how the results should be interpreted depending on how the samples are loaded in the assay. To overcome this we wanted to make the script more interactive so the user could decide how to normalize the samples.

The second target is our viral growth curve assays. This requires manual input of viral titer counts into a formatted excel sheet. This assay has a variable sample size depending on how many viruses are measured.

We wrote a python script for each case which quickly processes the data and presents it in an easy to read, publishable format while reducing the possiblity of user error during visualization. We also wrote an R script which parallels the titer.py format to give users options depending on the language they feel more comfortable using. In total, this repository contains 3 fully commented and documented scripts, two written in python3, and one written in R 4.1.3

### Example Datasets
**1   cell_death_data_final.xlsx**

**2   titer_data.csv**


### Scripts
#### 1)   cell_death.py

External Packages
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
 

#### 2)   titer.py

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

#### 3)   titer code.R 

External Packages
 - stringr (search for a pattern within a string)
```
10 Titer$hour_fix <- str_remove_all(Titer$Hour, " hour")
```


### Tests to Visualize
-   Cell Death Assay (Bar Graph)
    ![viability](https://github.com/roh0002/Scripting-project/blob/main/viability.png)
-   Viral Growth Curve (Line Graph - multiple lines) 
    ![growth curve](https://github.com/roh0002/Scripting-project/blob/main/viral_growth_curve.jpg)
    


