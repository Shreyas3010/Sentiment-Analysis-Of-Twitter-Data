# GroupI
## CS404 - Undergraduate Research Project

## Team:
- Deval Pandya
- Yash Patel
- Jaykumar Tandel
- Shreyas Patel

## Introduction

# GroupI
## COMP 6321 - Machine Learning

## Team:
- Apekshaba Gohil
- Shreyas Patel
- Sebastian Racedo
- Misbah Shareef

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

## Instructions to train/validate the model
In the folder "Task-1" the jupyter notebook "Scratch_model.ipynb" can be found. Please change the dataset path to where the dataset is. All the cells can be run at once to train and validate the model. All the plots will be generated and displayed. 

Note: The code is made so it can run with GPU.
