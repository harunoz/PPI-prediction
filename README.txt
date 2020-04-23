Motivation: 

It has been emphasized in the literature that effects of mutation protein-protein interaction networks shed light on the molecular basis of diseases, which in turn can appraise methods for diagnosis and treatment. Hence, detecting effect of mutation PPIs is crucial. In this study, first, we analyze the recently proposed tools for predicting the effects of mutations on protein and protein-protein interactions and we process nearly 120.000 cancer patient’s mutation information on recently proposed tool by which named as ELASPIC. We get mainly predicted change in mutation’s Gibbs free energy (ΔΔG) of folding and/or binding for every domain interface affected by the mutation and we try to find a relationship between the effect of mutation and ΔΔG by matching the experimental results. Finally, we train a random forest classifier machine learning model with ELASPIC all results which includes 76 different features of mutations and proteins and we get mean 0.921 and our predictor importance results show that molecular features of PPIs effect most to our accuracy.

Files:

Data:

1-) ElaspicMutations.csv

--> Contains combination of Elaspic results of mutations.tsv file. 


2-) ClassificationData.cvs 

--> For the final classification.

Code:

1-) prepareToClassify.py

--> Data  file called "will_be_classified.csv" contains ELASPIC output of mutations.tsv file, prepareToClassify file combines the type of mutations.tsv file with their ELASPIC results.


2-) countTypeOfMut.ipynb

--> Contains helper function, not important.

3-) prepareToClassify2.ipynb

--> It preparess the our final file which called, "classificationData.csv": It can be adjustable by changing line 6, and It can create new classificationData files.


4-) classification.ipynb 

--> It's for the final classificaiton, 	I used yellowbrick framework for data visualization, It can be easily dowlandable by writing "pip install yellowbrick" to the terminal.  Note that, I just tried randomforestclassifier which gave a 0.93 accuracy score. 


5-) drawParamater.ipynb

--> for the adjusting the paramater of the random forest classifier I used that functions.


6-) predictor_importance.ipynb

--> It gives a very good predictor importance graph HOWEVER it takes long time to run.


