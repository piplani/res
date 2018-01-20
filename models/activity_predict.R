###############################################################
#                                                             #
#            Test the New dataset using saved Model           #
#                                                             #
###############################################################
#                                                             #
# Credit: Dr. Prashant Singh Rana                             #
# Email : psrana@gmail.com                                    #
# Web   : www.psrana.com                                      #
#                                                             #
###############################################################
#                                                             #
# This script do the following:                               #
# 1. Load the Model                                           #
# 2. Test the new Dataset                                     #
# 3. Finally Saving the results.                              #
#                                                             #
###############################################################


setwd("/home/tox2020/Desktop/HSE/models")
args = commandArgs(trailingOnly = TRUE)
dirname = args[1]

#--------------------------------------------------------------
# Step 1: Include Library
#--------------------------------------------------------------



#--------------------------------------------------------------
# Step 2: Variable Declaration
#--------------------------------------------------------------
#cat("\nStep 2: Variable Declaration")
modelFileName <- "activity_randomForest-Model.RData"
testFileName  <-"activityres.csv"


#--------------------------------------------------------------
# Step 3: Model Loading
#--------------------------------------------------------------
#cat("\nStep 3: Model Loading")
load(modelFileName)



#--------------------------------------------------------------
# Step 4: Data Loading
#--------------------------------------------------------------
#cat("\nStep 4: Data Loading")
newTestDataset <- read.csv(paste('../','media/',dirname,'/',testFileName,sep = ''))    # Read the datafile
#head(newTestDataset)


#--------------------------------------------------------------
# Step 5: Prediction (Testing)
#--------------------------------------------------------------
#cat("\nStep 5: Prediction using -> ", modelName)
library(randomForest)
NewPredicted <- predict(model, newTestDataset)
#head(NewPredicted)
#NewPredicted
#--------------------------------------------------------------
# Step 6: Saving Results
#--------------------------------------------------------------
#cat("\nStep 6: Saving Results")
write.csv(data.frame(newTestDataset,NewPredicted), file=paste('../media/',dirname,'/activity',modelName,"-Testing-Result.csv",sep=''), row.names=FALSE)
r <- read.csv(paste('../media/',dirname,'/activity',modelName,"-Testing-Result.csv",sep=''))
cat(r$NewPredicted)

#cat("\nDone")

#--------------------------------------------------------------
#                           END 
#--------------------------------------------------------------

