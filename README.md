## CS404 - Undergraduate Research Project

## Team:
- Deval Pandya
- Yash Patel
- Jaykumar Tandel
- Shreyas Patel

## Introduction

This report outlines a comprehensive approach to leveraging Twitter API data for effective analysis of individuals' emotional and mental well-being through sentiment analysis and topic categorization. The acquired Twitter data is stored in a Neo4j graph database to facilitate efficient graph traversal and retrieval.

In the initial phase of the project, the code involves utilizing the Twitter API to gather tweets. Subsequently, the data is stored in a Neo4j graph database. The sentiment analysis is applied to calculate sentiment values for each tweet, providing insights into the emotional status of the individuals involved.

Moving on to the second phase, tweets are categorized into various topics such as Education, Business, Politics, Entertainment, and Sports. This categorization enables a detailed analysis of the mental health aspects related to different aspects of life. The Neo4j graph database proves to be instrumental in facilitating fast graph traversal and retrieval of relevant information for further analysis.

In summary, the integration of sentiment analysis, topic categorization, and storage in a Neo4j graph database allows for a comprehensive understanding of individuals' emotional states and mental well-being based on their Twitter activity.

## Requirements 
* [Python](http://www.python.org) version 3.8 or greater;
* [Numpy](http://www.numpy.org), the core numerical extensions for linear algebra and multidimensional arrays;
* [Ploty](https://plotly.com/python/), excellent plotting and graphing libraries;
* [Pandas](http://pandas.pydata.org/), library to read files has a dataframe;
* [Tensorflow](https://www.tensorflow.org/), library for Deep neural network models and Tensor computation with strong GPU acceleration;
* [Sklearn](https://scikit-learn.org/stable/), library with different ML models.
* [Flask](https://flask.palletsprojects.com/en/3.0.x/), library for creating web applications in Python.
* [Py2neo](https://neo4j-contrib.github.io/py2neo/), library for working with Neo4j from within Python applications.
* [NLTK](https://www.nltk.org/), library for building Python programs to work with human language data.
* [Tweepy](https://www.tweepy.org/), library for accessing Twitter API.
  
## Instructions to run programs

### 1)	Setting up Environment
* Download and install the Anaconda environment for python 3.7+ from this link… https://www.anaconda.com/.
* To create and work with “.ipynb” files you will need Jupyter Notebook which can be opened once the Anaconda Package is installed.
* Download Neo4j Database from this link… https://neo4j.com/download/.
* Create a blank graph in Neo4j with password “123” and other things default. These settings are preferred because it will be used in many places in codes.
* You need to create an account in https://developer.twitter.com/en and generate an API key which will be used later for data acquisition.

