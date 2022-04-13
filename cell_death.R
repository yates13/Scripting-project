#set wkdir

setwd("C:/Users/fmx398/Desktop/grad school/spring 2022/scripting for biologists/project")

#installing libraries 
library(ggplot2)
library("stringr") 
library("openxlsx")

#uncomment for first run only 
#install.packages("stringr") 

cell_death <- read.xlsx(xlsxFile = "cell_death.xlsx", sheet = 1, skipEmptyRows = FALSE)
summary(cell_death)

sample_num = str_count(cell_death$`2.03.1`, regex((SPL)\d+))
#sample_num = COUNTIF(B52:B200, "SPL*")
print(sample_num)

