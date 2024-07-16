---
blap: ['foo', 123, 2024-06-21 18:36:45, ['bar', 456, ['blap': [ 1, 2, 3, ]]]]
math: true
foo: 1234
bar: 2024-03-25 18:15:12
blap: ['foo', 123, 2024-06-21 18:36:45, ['bar', 456, ['blap': [ 3, 2, 1, ]]]]
qux: [ 4, 3, 2, 1, ]
---

This is the [IPDC Python+data](https://sites.google.com/edc.org/ipdc/python-data) *Data-Science Algorithms* extension unit activity for the *Näive Bayes Classifier* algorithm.

## Mathematics behind Bayesian Gaussian statistics 

Bayes Theorem can be stated as:

- P(A&#9168;B) is the posterior probability of class (A, target) given predictor (B, attributes).
- P(A) is the prior probability of class.
- P(B&#9168;A) is the likelihood which is the probability of predictor given class.
- P(B) is the prior probability of predictor.

- The features are independent, so that $P\left(x_{i}\vert y, \dots, x_{i-1}, x_{i+1}, \dots x_{n}\right) = P\left(x_{i}\vert y\right)$ and the joint probability is their product.
- The feature values are normally distributed with mean $\mu = \frac{\sum_{i=1}^{N}x_{i}}{N}$ and variance $\sigma^{2} = \frac{\sum_{i=1}^{N}x_{i}^{2}}{N} -\mu^{2}$, so that the probability density of $v$ given a class $C_{k}$, can be computed by $p\left(x = v\vert C_{k}\right) = \frac{1}{\sqrt{2\pi\sigma_{k}^{2}}}e^{-\frac{\left(v - \mu_{k}\right)^{2}}{2\sigma_{k}^{2}}}$

$$C=\pi D$$

## Notes:

- [[https://colab.research.google.com/drive/1gdRqv9bqXlSuiby1dF2vP_-n99qZB6Ym]] A Google Colab Notebook that follows the 

#data #Python #IPDC