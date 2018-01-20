setwd("/home/tox2020/Desktop/HSE")
args = commandArgs(trailingOnly = TRUE)
dirname = args[1]
final <- read.csv(paste('media/',dirname,'/final.csv',sep=""))
f<- final[2]
active = 0
inactive = 0
for (i in f){
  if (i>0.6){
    active = active + 1
  }
  else{
    inactive = inactive + 1
  }
}
if (active > inactive){
  cat("Active")
}
if (active <inactive){
  cat("Inactive")
}
