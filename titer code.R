#set wkdir
setwd("C:/Users/fmx398/Desktop/grad school/spring 2022/scripting for biologists/project")
library(ggplot2)
Titer=read.csv(file="Titers.csv")
summary(Titer)
install.packages("stringr") 
library("stringr") 

Titer$hour_fix <- str_remove_all(Titer$Hour, " hour")
Titer$hour_fix=as.numeric(Titer$hour_fix)

#ggplot(data=Titer, aes(x = hour_fix, y = Log_PFU, group = VIRUS))+
#  geom_line()

plot(Titer$Log_PFU~Titer$hour_fix, type="n")
#plot(Titer$hour_fix~Titer$Log_PFU, type="n")

###WT virus
lines(Titer$hour_fix[Titer$VIRUS=="WT"],Titer$Log_PFU[Titer$VIRUS=="WT"],
      col="red", type="o")

lines(Titer$hour_fix[Titer$VIRUS=="WT RES"],Titer$Log_PFU[Titer$VIRUS=="WT RES"],
      col="orange", type="o")

lines(Titer$hour_fix[Titer$VIRUS=="WT Delta 611"],Titer$Log_PFU[Titer$VIRUS=="WT Delta 611"],
      col="yellow", type="o")
####

####MutRHIM virus
lines(Titer$hour_fix[Titer$VIRUS=="MT"],Titer$Log_PFU[Titer$VIRUS=="MT"],
      col="green", type="o")

lines(Titer$hour_fix[Titer$VIRUS=="MT Delta 611"],Titer$Log_PFU[Titer$VIRUS=="MT Delta 611"],
      col="blue", type="o")

lines(Titer$hour_fix[Titer$VIRUS=="MT RES"],Titer$Log_PFU[Titer$VIRUS=="MT RES"],
      col="purple", type="o")
####

#legend(1.2, 0.7, c(paste0("Tree", seq(1,16))), cex=0.6, 
#       fill=colors, ncol = 2)

legend("topleft",c("WT","WT Delta 611","WT RES","MT","MT Delta 611","MT RES"),lty=1,pch=19, col=c("red","orange","yellow","green","blue","purple"),bty="n")



#plot.new()
#?plot

#?str_remove_all
#str_remove_all(DEI2, "%", "")

