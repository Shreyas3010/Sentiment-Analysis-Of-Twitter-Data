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

### 2)	Downloading Trainind Data
* Download the training data of sentiment analysis for the link given below: http://help.sentiment140.com/for-students/.
* Save this file in the folder “…/trainingandtestdata/”.
* Training data for categorical classification is already given in the folder “…/Categorical Classification/Data/categorical_train_data.csv”.

### 3)	Downloading glove vector file
* Download the glove file from link given below: https://nlp.stanford.edu/projects/glove/.
* There are many option but we advise you to download the Twitter embedding for GloVe with 27B tokens and 100 dimensions. Here is the direct download link: http://nlp.stanford.edu/data/glove.twitter.27B.zip.
* Save this file in the folder “…/Sentiment Analysis/Data/glove”.
* This file will be used for both sentiment analysis and categorical classification.

### 4)	Preprocessing the training data
* Run the “Preprocessing Notebook” to pre-process all the training data.
* You need to run it twice. Once to preprocess data for “Sentiment Analysis” and another time to preprocess data for “Categorical Classification”.
* You need to save their respective preprocessed data in their respective “Data” folders (Optional).

### 5)	Machine Learning
* After giving specific paths for training dataset and the saving models, you can follow further instructions given in the 2 notebooks “Sentiment Analysis.ipynb” and “Categorical Classification.ipynb” to complete the training part.

### 6)	Gathering Twitter Data
* First Open the Neo4j Desktop app and start the graph DB.
* The file named “Twitter handles” contains all the usernames whose data will be collected. You can add or remove names in required.
* Now open “Twitter API.ipynb” notebook in Jupyter.
* Put the access tokens that you generated on the twitter developer site and change path for twitter handles file as required.
* Run the code. This will gather all the data in Neo4j DB.
* Now you can classify this data with the models you have trained and add the predicted labels to the DB.

### 7)	Using FrontEnd
* To start the Web-App for Analysis of the tweets, you need to have database running in Neo4j database.
* First enter the password of your Neo4j Database at the line 34 and 124 in "eg.py" and line 6 in "data_acquisition.py".
* Run the "data_acquisition.py" file with the help of command "python data_acquisition.py". It will find the cumulative sentiment of each user and store it in dictionary.txt file in the dictionary format (key:value pair).
* Install the necessary module (if required) with the help of "pip install X" command.
* Run the "eg.py" file with the help of command "python eg.py" or simply double click on the file.
* It will show the localhost IP and Port Number on which the Flask-App is running. Just navigate to that URL in the Web-browser and you will be able to see the home-page of the application.

Note: Internet connection is required to load the graph. You can use frontend only after you have stored the classified categories and sentiment values of tweets in Neo4j.
