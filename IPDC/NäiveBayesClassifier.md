This is the [IPDC Python+data](https://sites.google.com/edc.org/ipdc/python-data) *Data-Science Algorithms* extension unit activity for the *Näive Bayes Classifier* algorithm.

## Mathematics behind Bayesian Gaussian statistics 

[Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes'_theorem#Statement_of_theorem) can be stated as:

$$P(A\vert B) = \frac{P(A) P(B\vert A)}{P(B)}$$

or:

$$\text{posterior} = \frac{\text{prior}\times\text{likelihood}}{\text{evidence}}$$

where:

- $A$ and $B$ are events.
- $P(A\vert B)$ is the posterior probability of class (A, target) given predictor (B, attributes).
- $P(A)$ is the prior probability of class.
- $P(B\vert A)$ is the likelihood which is the probability of predictor given class.
- $P(B)$ is the prior probability of predictor, $P(B)\ne0$.

Bayesian Gaussian statistics further assumes (as described on [Kaggle](https://www.kaggle.com/code/dimitreoliveira/naive-bayes-probabilistic-ml-titanic-survival)):

- The features are independent, so that $P\left(x_{i}\vert y, \dots, x_{i-1}, x_{i+1}, \dots x_{n}\right) = P\left(x_{i}\vert y\right)$ and the joint probability is their product.
- The feature values are normally distributed with mean $\mu = \frac{\sum_{i=1}^{N}x_{i}}{N}$ and variance $\sigma^{2} = \frac{\sum_{i=1}^{N}x_{i}^{2}}{N} -\mu^{2}$, so that the probability density of $v$ given a class $C_{k}$, can be computed by $p\left(x = v\vert C_{k}\right) = \frac{1}{\sqrt{2\pi\sigma_{k}^{2}}}e^{-\frac{\left(v - \mu_{k}\right)^{2}}{2\sigma_{k}^{2}}}$

## Using data to build a classifier model

- The Titanic survivability data are available on [Kaggle](https://www.kaggle.com/c/titanic).
- Given .CSV headers `['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked', 'train']`, the relevant features are `Age`, `Embarked`, `Fare`, `Parch`, `Sex`, `SibSp`. The target is `Survived`. (The training data are labeled with `train`.)
- The features must be verified to meet the näive Gaussian criteria (as in [Dimitre Oliveira](https://www.kaggle.com/code/dimitreoliveira/naive-bayes-probabilistic-ml-titanic-survival#Distribution-study)'s solution).
- The data must be normalized with numerical values (not categorical) and cleaned of missing values or where missing values are set to the mean where appropriate.

Following the [Wikipedia](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gaussian_naive_Bayes) article and the [example](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Person_classification), yields the following approach:

- For each of the 6 features $f_{i}$ of each element in the training data, calculate the mean $\mu$ and variance $\sigma^{2}$ for each of two values of $C_k$: *survived* $S$ and *not survived* $\overline{S}$.
- The prior probability is $P(C_{k})$ and the likelihood is $\prod_{i}P({f_{i}\vert C_{k}})$, so the *joint probability* is: $$P\left(f_{i}\vert C_{k}, \dots, f_{i-1}, f_{i+1}, \dots f_{n}\right) = P\left(f_{i}\vert C_{k}\right) = P\left(C_{k}\right) \prod_{i}P\left({f_{i}\vert C_{k}}\right)$$
- The total evidence is $Z = P(S) \prod_{i}{P(f_{i}\vert S)} + P(\overline{S}) \prod_{i}{P(f_{i}\vert\overline{S})}$, so the *posterior probability* of each of two values of $C_k$ are: $$P(S\vert f_{1},\dots,f_{6}) = \frac{P\left(S\right) \prod_{i}P\left({f_{i}\vert S}\right)}{Z}$$ $$P(\overline{S}\vert f_{1},\dots,f_{6}) = \frac{P(\overline{S}) \prod_{i}P({f_{i}\vert \overline{S}})}{Z}$$
- If $P(\overline{S}\vert f_{1},\dots,f_{6}) \lt P(S\vert f_{1},\dots,f_{6})$ for any passenger, then that passenger **survived**.

## Sample code

- [[https://colab.research.google.com/drive/1gdRqv9bqXlSuiby1dF2vP_-n99qZB6Ym]] A [Google Colab Notebook](https://colab.research.google.com) that follows the above mathematics and [Dimitre Oliveira](https://www.kaggle.com/code/dimitreoliveira/naive-bayes-probabilistic-ml-titanic-survival#Distribution-study)'s solution with the use of [`numpy`](https://numpy.org/) and [`pandas`](https://pandas.pydata.org/).
- The Google Colab Notebook also includes [Oliveira](https://www.kaggle.com/code/dimitreoliveira/naive-bayes-probabilistic-ml-titanic-survival#Distribution-study)'s (updated) code using [`numpy`](https://numpy.org/), [`pandas`](https://pandas.pydata.org/), [`seaborn`](https://seaborn.pydata.org/index.html), [`matplotlib`](https://matplotlib.org/), [`scipy`](https://scipy.org/), [`scikit`](https://scikit-learn.org/stable/).

#data #Python #IPDC