
## Automating Routine Data Visualization - Python Scripting Project

### Shawn Yates and Rachel Haich
 
Our current lab practices use excel and graphpad for visualization of large amounts of data. This is sufficient for small experiments, but is time consuming, particularly for large
 experiments. Additionally, graphpad is not open source and requires an annual subscription. For this project, we created automated python and R scripts to process and visualize our results from excel datasheets into easily interpretted graphics.

The first main target for automation in our lab are cell death assays, which measure the rate of cell death in response to a treatment. The output of this test is a standardized excel template which can be used as the basis of our script. However, the excel sheet can change how the results should be interpreted depending on how th sample are loaded in the assay. to overcome this we wanted to make the script more interactive so the user could decide how to normalize the samples.

The second target is our viral growth curve assays. This requires manual input of viral titer counts into a formatted excel sheet. This assay has a varaiable sample size depending on how many viruses are measured.

We intend to write a python script for each case which quickly processes the data and presents it in an easy to read, publishable format while reducing the possiblity of user error during visualization. 

### Datasets
1   cell_death_data_final.xlsx

2   titer_data.csv


### Scripts
1   cell_death.py

2   titer.py

3   titer code.R 




### Tests to Visualize
-   Cell Death Assay (Bar Graph)
    ![viability](https://github.com/roh0002/Scripting-project/blob/main/viability.png)
-   Viral Growth Curve (Line Graph - multiple lines) 
    ![growth curve](https://github.com/roh0002/Scripting-project/blob/main/viral_growth_curve.jpg)
    


