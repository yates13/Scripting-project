#set wkdir
setwd("C:/Users/fmx398/Desktop/grad school/spring 2022/scripting for biologists/project")
library(ggplot2)
Titer=read.csv(file="Titers.csv")
summary(Titer)
install.packages("stringr") 
library("stringr") 

#time point cleanup
Titer$hour_fix <- str_remove_all(Titer$Hour, " hour")
Titer$hour_fix=as.numeric(Titer$hour_fix)

#starting a empty plot
plot(Titer$Log_PFU~Titer$hour_fix, type="n")

#plotting virus in lines

###WT viruses

#WT
lines(Titer$hour_fix[Titer$VIRUS=="WT"],Titer$Log_PFU[Titer$VIRUS=="WT"],
      col="red", type="o")
#WTD611
lines(Titer$hour_fix[Titer$VIRUS=="WT RES"],Titer$Log_PFU[Titer$VIRUS=="WT RES"],
      col="orange", type="o")
#WTrescue
lines(Titer$hour_fix[Titer$VIRUS=="WT Delta 611"],Titer$Log_PFU[Titer$VIRUS=="WT Delta 611"],
      col="yellow", type="o")


####MutRHIM virus

#MT
lines(Titer$hour_fix[Titer$VIRUS=="MT"],Titer$Log_PFU[Titer$VIRUS=="MT"],
      col="green", type="o")
#MTD611
lines(Titer$hour_fix[Titer$VIRUS=="MT Delta 611"],Titer$Log_PFU[Titer$VIRUS=="MT Delta 611"],
      col="blue", type="o")
#MTrescue
lines(Titer$hour_fix[Titer$VIRUS=="MT RES"],Titer$Log_PFU[Titer$VIRUS=="MT RES"],
      col="purple", type="o")


legend("topleft",c("WT","WT Delta 611","WT RES","MT","MT Delta 611","MT RES"),lty=1,pch=19, col=c("red","orange","yellow","green","blue","purple"),bty="n")

