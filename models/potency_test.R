library(data.table)
setwd("/home/tox2020/Desktop/HSE")
args = commandArgs(trailingOnly = TRUE)
dirname = args[1]

data1 <- fread(paste('media/',dirname,'/res.csv',sep=""), select = c("ATS5i",    "IC2",      "ATS4p",    "ATSC4v",   "JGI9",     "C3SP3",    "ATS4i",    "ATS3p",   
                                     "ATS2p",    "TPC",      "MPC9",     "MPC8",     "MPC7",     "MPC10",    "IC4",      "C4SP3",   
                                     "GGI3",     "ATS4v",    "ATS3v",    "ATSC4i",   "ZMIC0",    "MWC10",    "ATS3i",    "ATS6i",   
                                     "GGI2",     "nT10Ring", "nF10Ring", "IC5",      "MWC9",     "MWC8",     "MWC7",     "MPC6",    
                                     "ATS5p",    "TIC4",     "TIC3",     "GGI6",     "TSRW",     "MWC6",     "MPC5",     "MPC4",    
                                     "TIC5",     "ATS2v",    "SRW8",     "SRW10",    "ATS2i",    "IC3",     "ATS5v",    "ATS1p",   
                                     "SpMAD_Dt", "MWC5",     "MPC3",     "SpMax_Dt" ))

write.csv(data1, paste('media/',dirname,'/potencyres.csv',sep=""),row.names = F)
