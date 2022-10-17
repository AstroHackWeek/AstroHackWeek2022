# Day 2 afternoon session: Practical machine learning for astronomers 
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jwuphysics/AstroHackWeek2022)

This repository contains two machine learning tutorials. We will learn how to apply several machine learning algorithms, ranging from polynomial regression and random forests to deep convolutional neural networks, in order to answer a science qeustion (see e.g. [Wu 2020](https://ui.adsabs.harvard.edu/abs/2020ApJ...900..142W/abstract)). These notebooks will also help you gain familiarity with the `scikit-learn` and `pytorch`/`fastai` Python packages for machine learning.

Presented by John F. Wu ([@jwuphysics](https://github.com/jwuphysics)).

# Getting started

## Running on Google Colab (*recommended*)
Open the Colab notebooks for the [introductory machine learning (part 1)](https://colab.research.google.com/github/jwuphysics/AstroHackWeek2022/blob/main/day2/01-intro-machine-learning.ipynb) and the [deep learning (part 2)](https://colab.research.google.com/github/jwuphysics/AstroHackWeek2022/blob/main/day2/02-deep-learning.ipynb) sessions.

## Running locally (*not recommended*)
If you want to run these notebooks locally, then you should clone the repository and set up a conda environment with the necessary packages (`numpy`, `scipy`, `matplotlib`, `pandas`, `scikit-learn`, `pytorch`, `fastai`). The installation process might depend on (a) whether you have an NVIDIA graphics card, and (b) what version of CUDA your system is running. To avoid these complications, just use the Colab notebook!

# Part 1 - Introductory Machine learning 
[![Colab - Part 1](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jwuphysics/AstroHackWeek2022/blob/main/day2/01-intro-machine-learning.ipynb)

0. Before getting started
1. Can we predict a galaxy's neutral hydrogen (HI) content?
    - Examine data with pandas
    - A very simplified glossary for xGASS
    - Examine and clean features
    - Visualize correlations
2. Polynomial regression
    - Multivariate linear regression
    - Train-test split
    - Cross-validation
    - Quadratic and higher-order polynomial models
    - Overfitting
3. Decision trees
    - How scikit-learn does it
    - Random forests
    - Optimize hyperparameters
    - Feature importances

# Part 2 - Deep learning
[![Colab - Part 2](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jwuphysics/AstroHackWeek2022/blob/main/day2/02-deep-learning.ipynb)

1. Introducing the science problem (again)
2. Solving the task with a CNN
3. Understanding convolutions
4. Other neural network ingredients
5. A simple CNN model in action (forward)
6. Optimization
7. A simple CNN model in action (forward + backward)
8. Hyperparameters

# Other resources

- [Data analysis recipes: Fitting a model to data](https://arxiv.org/abs/1008.4686)
- [Scikit-learn - Machine learning with Python](https://scikit-learn.org/stable/)
- [Fast.ai - Practical Deep Learning for Coders](https://course.fast.ai/)
- [Training a deep neural network on astronomical data from scratch](https://jwuphysics.github.io/blog/galaxies/astrophysics/deep%20learning/computer%20vision/fastai/2020/05/26/training-a-deep-cnn.html)
