## CS404 - Undergraduate Research Project

## Team:
- Deval Pandya
- Yash Patel
- Jaykumar Tandel
- Shreyas Patel

## Introduction

This report presents a comprehensive exploration of Convolutional Neural Networks (CNNs) in image classification, addressing real-world application challenges in the field.

In the project's first phase, we trained a ResNet-18 CNN on the Colorectal Cancer dataset (Dataset 1). Training the Pretrained ResNet-18 model achieved the highest accuracy at 98.39\%, and t-SNE reduced CNN encoder output dimensions, visually enhancing class feature distinctiveness and model performance understanding.
 
In the second phase, custom-trained (on Dataset 1) and ImageNet pre-trained CNN encoders were used for feature extraction on Prostate Cancer dataset (Dataset 2) and Animal Faces dataset (Dataset 3). t-SNE reduced dimensionality for visual clarity. Using the pretrained CNN encoder, we applied Random Forest (RF) and K-Nearest Neighbors (KNN), and evaluted the accuracy of these ML models on the feature maps.

## Requirements 
* [Python](http://www.python.org) version 3.8 or greater;
* [Numpy](http://www.numpy.org), the core numerical extensions for linear algebra and multidimensional arrays;
* [Matplotlib](http://matplotlib.sf.net), excellent plotting and graphing libraries;
* [Pandas](http://pandas.pydata.org/), library to read files has a dataframe;
* [Pytorch](https://pytorch.org/docs/stable/torch.html), library for Deep neural network models and Tenssor computation with strong GPU acceleration;
* [Sklearn](https://scikit-learn.org/stable/), library with different ML models.

## Instructions to run programs

### 1)	Setting up Environment
* Download and install the Anaconda environment for python 3.7+ from this link… https://www.anaconda.com/.
* To create and work with “.ipynb” files you will need Jupyter Notebook which can be opened once the Anaconda Package is installed.
* Download Neo4j Database from this link… https://neo4j.com/download/.
* Create a blank graph in Neo4j with password “123” and other things default. These settings are preferred because it will be used in many places in codes.
* You need to create an account in https://developer.twitter.com/en and generate an API key which will be used later for data acquisition.

