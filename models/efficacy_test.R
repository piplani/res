setwd("/home/tox2020/Desktop/HSE")
args = commandArgs(trailingOnly = TRUE)
dirname = args[1]

library(data.table)
data1 <- fread(paste('media/',dirname,'/res.csv',sep=""), select = c("TIC2",           "ATS6i",          "TIC3",           "Sv",             "TIC5",          
                                     "TIC4",           "ATS7e",          "McGowan_Volume", "ATS7i",          "piPC2",         
                                     "ATS1p",          "TopoPSA",        "IC4",            "ATS5p",          "GGI3",          
                                     "nBondsS3",       "Si",             "ATS0i",          "ATS1i",          "GGI6",          
                                     "Sp",             "apol",           "ATS6p",          "ATS1v",          "nAtom",         
                                     "GGI4",           "ATS7v",          "R_TpiPCTPC",     "ATS0v",          "TWC",           
                                     "MWC9",           "TIC1",           "Zagreb",         "MWC2",           "GGI2",          
                                     "ATS8e",          "ATS4m",          "TSRW",           "SRW10",          "MWC8",          
                                     "piPC3",          "MWC10",          "ATS2v",          "ATS5i",          "piPC1",         
                                     "SRW8",           "MWC6",           "ATS6v",          "ATS4p",          "MWC4",          
                                     "MPC3",           "AMW",           "nO",             "ATSC5i",         "WPOL",          
                                     "ATSC5v",         "GGI5",           "AATS4v",         "IC3",            "AATS6v",        
                                     "MLFER_E",        "AATS5v",         "TIC0",           "IC5",            "GATS1m",        
                                     "GATS7v",         "AATS0m",         "SRW2",           "nBonds",         "AATS2m",        
                                     "AATS6m",         "GGI8",           "AATS3m",         "ATS5v",          "ATS4v",         
                                     "ATSC5p",         "nBondsM",        "nBondsD2",       "nBondsD",        "AATS4m",        
                                     "AATS6p",         "C2SP2",          "JGI3",         "nAtomP",         "AATS1m",        
                                     "GATS7p",         "AATS0v",         "IC2",            "ATS4i",          "ZMIC2",         
                                     "Mv",             "MWC7",           "ATS3m",          "ATS2m",          "ZMIC0",         
                                     "MWC5",           "JGI2",           "MATS7c",         "ATS5m",          "ATS1m",         
                                     "MPC6",           "AATS7p",         "ATS3v",          "GATS1i",         "SRW6",          
                                     "AATS5m",         "Mp",             "FMF",            "MPC5",           "MPC4",          
                                     "GATS1v",         "AATS7v",         "JGT",            "MWC3",           "AATSC7p",       
                                     "AATS6i",         "MATS5i",         "TPC",            "SpMax_Dt",       "SpAD_Dt",       
                                     "MPC9",           "MPC8",           "MPC7",           "EE_Dt", "AATS0p"))

write.csv(data1, paste('media/',dirname,'/efficacyres.csv',sep=""),row.names = F)



