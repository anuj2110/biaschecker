DESCRIPTION 

In today's Artificial Intelligence and Machine Learning powered world the predictive models have become the ultimate decision makers in the industries such as banking, insurance, and employment for their respective purposes. 
But the major concerns here are, can we trust on the decision outputs attained by these models? Are they fair enough? Are they unbiased? Are inputs provided to the model are self-sufficient to train the model properly and predict correctly? And Imagine how harmful it could be to a person, company, industry and a society when the decisions made are incorrect. However, improper deployment of these models can lead to inadmissible consequences though it is unintentional discrimination.
Bias can creep into the model in one or the other way.A predictive model can be susceptible to discrimination if it was trained on inputs that exhibit discriminatory patterns. In such case, the predictive model can learn patterns of discrimination from data leading to high dependence on protected attributes like sexuality, race, gender, nationality etc. A predictive model that significantly weighs these protected attributes would tend to exhibit disparate outcomes for these group of individuals. 
Hence, the focus of this project is to determine whether the provided data is sample biased/biased on protected attributes and finding its relative significance so that, the user can know about the fairness in the data and hence, on confirming if it isn’t biased he/she can use the same for training predictive models to attain an unbiased/fair output. This is the first step towards bias mitigation which is bias checking hence, naming it as 'Bias Checker'.

The 2 modules developed here are 
1. To check the statistical distributions of the numerical and categorical data, where you can find on which protected attributes the data is biased.
2. To check the feature dependence in a particular dataset like how x varaiables are dependent on y predicted outcome.

Module 1 is developed using Python along with  Flask, HTML, CSS and is deployed on Heroku Cloud Application Platform.
This includes the files app.py, model.py, templates(index.html & result.html), procfile and requirements.txt.

This module is available to try on: https://bias-checker.herokuapp.com/

Module 2 is a feature importance i Python NoteBook(ipynb) file where you can input an dataset and check for relative feature dependence.


The Datasets used are:

1. A. Asuncion and D.J. Newman. 2007. UCI Machine Learning Repository. (2007). http://www.ics.uci.edu/$\sim$mlearn/
2. Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository. (2017). http://archive.ics.uci.edu/ml
3. J Larson, S Mattu, L Kirchner, and J Angwin. 2016. Compas analysis. GitHub, available at: https://github.
com/propublica/compas-analysis[Google Scholar] (2016)
4. M Redmond. 2011. Communities and crime unnormalized data set. UCI Machine Learning Repository. In website:
http://www. ics. uci. edu/mlearn/MLRepository. html (2011).

