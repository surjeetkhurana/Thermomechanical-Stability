Here are the details of the files in this repository
1.- "1_Data" folder that contains the data needed top reproduce the work:

1.a.- "TrainingData.csv" - This file contains collected materials for Thermal Expansion Coeeficient (TEC) from the aflow Database. 
1.b.- "Predictions.csv" - This file contains Thermal Expansion coefficient predictions and generated features for ~25k materials found in the ICSD library.
1.c.- "PredictedCombinations" - Contains the list of 756 combinations of Cathode and Electrolyte maaterials with average and difference in TEC values for thermomechanical compatibility.
1.d.- "ValData.csv" - contains the experimental TEC values for the validation dataset with the references to previous works from which we collected the data.

2.- "2_Codes" contains the codes needed to recreate the work in two folders:
2.a.- "1_Python" contains the following:
2.a.1.-"ValidationCode.py" - This file contains the code used for experimental validation using the experimental dataset collected from previous works.  
2.a.2.- "PredictThermal.py" - This file contains the code for predicting TEC for new materials. 
2.a.3.- "Extra Trees.py" - This file contains the code employed in this work to predict Thermal Expansion Coefficients.
2.b.- "2_Pickle" contains the following:
2.b.1.- "ExtraTrees.sav" - This is a pickle file for the Extra Trees based TEC prediction model.

