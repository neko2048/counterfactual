# Counterfactual Study
## Experimental Dataset: Case Study
- Case 1: Apparent Imbalanced
- Case 2: Apparent Imbalanced
- Case 3: Genuine Imbalanced

====================================

* adjustedRankTest.ipynb: Statistically verify the feasibility of detecting the interaction term.
* dataGeneration-T01.ipynb: generate data with treatment = 0/1.
* dataGeneration.ipynb: generate data with treatment = -1/1.
* SHAPinteraction-T01.ipynb: calculate SHAP values of the datasets with treatment = 0/1.
* SHAPinteraction_Case3.ipynb: no difference with SHAPinteraction-T01.ipynb?
* SHAPinteraction-T01-lightgbm.ipynb: change model from XGBOOST to lightgbm
* SHAPinteraction-T01-BiasAnalysis.ipynb: show why case 2 has wrong SHAP values.

* massiveDataGeneration.ipynb: generate data with treatment = 0/1 and interaction coefficients from 0.01 to 100.
* massiveSHAPinteraction.ipynb: calculate SHAP values of  the datasets with int. coef. from 0.01 to 100.

##  Semi-Synthesized dataset: IHDP
From Hills, 2011
