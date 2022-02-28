# AnimasCode
Code I've written to help visualize and analyze the data for the Animas using the APEX-MODFLOW-RT3D model
**CleanedCodeGraphs** is the code to pull in **one model** with visualization for
salt ion loadings for continuous and annual results as well as the observed loadings.
**PredictedSoilAndGeology** is the code to pull in **three models** with the same visualization.
It has the results of the three models and the observed data.
**AttemptatPullingSpecifiedDays** pulls in **one model** and observed data,
It selects days by subarea and year that are present in the observed data
**ObservedDaysandResiduals** uses the same code as AttemptatPullingSpecifiedDays and
adds in the calculation and plots for residuals.
